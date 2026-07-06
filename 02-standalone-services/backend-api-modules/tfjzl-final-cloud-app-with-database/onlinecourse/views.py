import logging

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django import forms

from .models import Choice, Course, Enrollment, Question, Submission

logger = logging.getLogger('onlinecourse')


# =============================================================================
# Input Validation Forms
# =============================================================================

class EnrollmentForm(forms.Form):
    course_id = forms.IntegerField(min_value=1)


class SubmissionForm(forms.Form):
    course_id = forms.IntegerField(min_value=1)
    choice_ids = forms.ListField(
        child=forms.IntegerField(min_value=1),
        min_length=1,
        max_length=50,
        error_messages={
            'min_length': 'At least one choice must be selected.',
            'max_length': 'Too many choices submitted.',
        },
    )


class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=150,
        strip=True,
        error_messages={'required': 'Username is required.'},
    )
    password = forms.CharField(
        min_length=4,
        widget=forms.PasswordInput,
        error_messages={'required': 'Password is required.'},
    )


class RegistrationForm(forms.Form):
    username = forms.CharField(
        min_length=3,
        max_length=150,
        strip=True,
        error_messages={'required': 'Username is required.'},
    )
    password = forms.CharField(
        min_length=8,
        widget=forms.PasswordInput,
        error_messages={'required': 'Password is required.'},
    )
    first_name = forms.CharField(
        min_length=1,
        max_length=150,
        strip=True,
        error_messages={'required': 'First name is required.'},
    )
    last_name = forms.CharField(
        min_length=1,
        max_length=150,
        strip=True,
        error_messages={'required': 'Last name is required.'},
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already exists.')
        return username


# =============================================================================
# Views
# =============================================================================

class CourseListView(generic.ListView):
    template_name = 'onlinecourse/course_list_bootstrap.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-pub_date')[:5]


class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'onlinecourse/course_detail_bootstrap.html'


def enroll(request, course_id):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('onlinecourse:index'))

    form = EnrollmentForm({'course_id': course_id})
    if not form.is_valid():
        logger.warning('Invalid enrollment request: form validation failed')
        return HttpResponseRedirect(reverse('onlinecourse:index'))

    course = get_object_or_404(Course, pk=course_id)
    enrollment, created = Enrollment.objects.get_or_create(
        user=request.user, course=course
    )
    logger.info(
        'User %s enrolled in course %s (created=%s)',
        request.user.username,
        course.name,
        created,
    )
    return HttpResponseRedirect(
        reverse('onlinecourse:course_details', args=(course.id,))
    )


def submit(request, course_id):
    if request.method != 'POST':
        return HttpResponseRedirect(reverse('onlinecourse:index'))

    raw_choices = []
    for key, value in request.POST.items():
        if key.startswith('choice'):
            try:
                raw_choices.append(int(value))
            except (ValueError, TypeError):
                logger.warning('Invalid choice value in submission: %s', value)
                continue

    form = SubmissionForm({'course_id': course_id, 'choice_ids': raw_choices})
    if not form.is_valid():
        logger.warning(
            'Invalid submission from user %s: %s',
            request.user.username,
            form.errors,
        )
        return HttpResponseRedirect(reverse('onlinecourse:index'))

    course = get_object_or_404(Course, pk=course_id)
    user = request.user

    try:
        enrollment = Enrollment.objects.get(user=user, course=course)
    except Enrollment.DoesNotExist:
        logger.error(
            'No enrollment found for user %s in course %s',
            user.username,
            course.name,
        )
        return HttpResponseRedirect(reverse('onlinecourse:index'))

    submission = Submission.objects.create(enrollment=enrollment)
    submission.choices.set(form.cleaned_data['choice_ids'])
    submission.save()

    logger.info(
        'Submission %d created by user %s for course %s',
        submission.id,
        user.username,
        course.name,
    )
    return HttpResponseRedirect(
        reverse(
            'onlinecourse:exam_result',
            args=(course.id, submission.id),
        )
    )


def show_exam_result(request, course_id, submission_id):
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)

    selected_choices = submission.choices.all()
    total_questions = course.question_set.count()
    correct_answers = 0

    for question in course.question_set.all():
        correct_choices = set(
            question.choice_set.filter(is_correct=True)
        )
        selected_for_question = set(selected_choices.filter(question=question))
        if correct_choices == selected_for_question:
            correct_answers += 1

    grade = (
        int((correct_answers / total_questions) * 100)
        if total_questions > 0
        else 0
    )

    context = {
        'course': course,
        'grade': grade,
        'choices': selected_choices,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)


def login_request(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render(
                request,
                'onlinecourse/user_login_bootstrap.html',
                {'error_message': 'Please provide valid credentials.'},
            )

        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        if user is not None:
            login(request, user)
            logger.info('User %s logged in successfully', user.username)
            return HttpResponseRedirect(reverse('onlinecourse:index'))
        else:
            logger.warning('Failed login attempt for username: %s', form.cleaned_data['username'])
            return render(
                request,
                'onlinecourse/user_login_bootstrap.html',
                {'error_message': 'Invalid username or password'},
            )

    return render(request, 'onlinecourse/user_login_bootstrap.html')


def logout_request(request):
    logger.info('User %s logged out', request.user.username)
    logout(request)
    return HttpResponseRedirect(reverse('onlinecourse:index'))


def registration_request(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if not form.is_valid():
            error_msg = (
                form.errors.get('username', ['Validation failed'])[0]
                if form.errors
                else 'Invalid registration data.'
            )
            return render(
                request,
                'onlinecourse/user_registration_bootstrap.html',
                {'error_message': error_msg},
            )

        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
        )
        login(request, user)
        logger.info('New user registered: %s', user.username)
        return HttpResponseRedirect(reverse('onlinecourse:index'))

    return render(request, 'onlinecourse/user_registration_bootstrap.html')
