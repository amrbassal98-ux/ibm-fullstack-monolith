from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner


class CourseInstructorInline(admin.StackedInline):
    model = Course.instructors.through
    extra = 1

class CourseLearnerInline(admin.StackedInline):
    model = Course.learners.through
    extra = 1

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

class InstructorAdmin(admin.ModelAdmin):
    inlines = [CourseInstructorInline]

class LearnerAdmin(admin.ModelAdmin):
    inlines = [CourseLearnerInline]


class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor, InstructorAdmin)
admin.site.register(Learner, LearnerAdmin)
