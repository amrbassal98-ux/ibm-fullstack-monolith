from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    path(route='', view=views.CourseListView.as_view(), name='popular_course_list'),
    path('course/<int:pk>/enroll/', views.EnrollView.as_view(), name= 'enroll'),
    path('logout/', views.logout_request, name='logout'),
    path('login/', views.login_request, name='login'),
    path('register/', views.registration_request, name='registration'),
    path('course/<int:pk>/', views.CourseDetailsView.as_view(), name='course_details'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)\
 + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

