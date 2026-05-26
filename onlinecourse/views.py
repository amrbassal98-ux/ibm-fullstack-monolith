from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.views import generic
from .models import Course, Enrollment, Question, Choice, Submission

class CourseListView(generic.ListView):
    template_name = 'onlinecourse/course_list_bootstrap.html'
    context_object_name = 'course_list'

    def get_queryset(self):
        return Course.objects.order_by('-pub_date')[:5]

class CourseDetailView(generic.DetailView):
    model = Course
    template_name = 'onlinecourse/course_detail_bootstrap.html'

def enroll(request, course_id):
    if request.method == 'POST':
        course = get_object_or_404(Course, pk=course_id)
        enrollment, created = Enrollment.objects.get_or_create(user=request.user, course=course)
        return HttpResponseRedirect(reverse('onlinecourse:course_details', args=(course.id,)))

def submit(request, course_id):
    """
    Creates an exam submission record for a course enrollment.
    Extracts choice IDs from POST request and associates them with the submission.
    """
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    
    # Retrieve active enrollment
    enrollment = Enrollment.objects.get(user=user, course=course)
    
    # Initialize a new submission instance
    submission = Submission.objects.create(enrollment=enrollment)
    
    # Extract submitted choice IDs
    submitted_choices = []
    for key, value in request.POST.items():
        if key.startswith('choice'):
            submitted_choices.append(int(value))
            
    # Map extracted choices to the submission instance
    submission.choices.set(submitted_choices)
    submission.save()
    
    return HttpResponseRedirect(reverse('onlinecourse:exam_result', args=(course.id, submission.id,)))

def show_exam_result(request, course_id, submission_id):
    """
    Evaluates the submission, calculates the final grade percentage, 
    and renders the exam result template with precise context variables.
    """
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    
    # Retrieve all choices selected by the user for this specific submission
    selected_choices = submission.choices.all()
    
    total_questions = course.question_set.count()
    correct_answers = 0
    
    # Evaluate accuracy against boolean flags
    for question in course.question_set.all():
        correct_choices = question.choice_set.filter(is_correct=True)
        selected_for_question = selected_choices.filter(question=question)
        
        # A question is marked correct exclusively if selected choices perfectly match the true parameters
        if set(correct_choices) == set(selected_for_question):
            correct_answers += 1
            
    # Calculate percentage-based grade parameter
    grade = int((correct_answers / total_questions) * 100) if total_questions > 0 else 0
    
    # Construct context matching template variable requirements
    context = {
        'course': course,
        'grade': grade,
        'choices': selected_choices
    }
    
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)

def login_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('onlinecourse:index'))
        else:
            return render(request, 'onlinecourse/user_login_bootstrap.html', {'error_message': 'Invalid username or password'})
    return render(request, 'onlinecourse/user_login_bootstrap.html')

def logout_request(request):
    logout(request)
    return HttpResponseRedirect(reverse('onlinecourse:index'))

def registration_request(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        if User.objects.filter(username=username).exists():
            return render(request, 'onlinecourse/user_registration_bootstrap.html', {'error_message': 'Username already exists'})
        else:
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
            login(request, user)
            return HttpResponseRedirect(reverse('onlinecourse:index'))
    return render(request, 'onlinecourse/user_registration_bootstrap.html')