from django.contrib import admin
from django.urls import path
from customer360 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Core Application View Implementations
    path('', views.IndexView.as_view(), name='index'),
    path('create/', views.CustomerCreateView.as_view(), name='create_customer'),
    path('interact/<int:cid>/', views.InteractionCreateView.as_view(), name='interact'),
    path('summary/', views.SummaryView.as_view(), name='summary'),
    
    # Class-Based Authentication & Registration Handlers
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('signup/', views.AgentSignUpView.as_view(), name='signup'),
]