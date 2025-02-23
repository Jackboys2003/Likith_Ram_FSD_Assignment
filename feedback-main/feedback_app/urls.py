from django.urls import path
from .views import feedback_view, feedback_success, home

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('feedback/', feedback_view, name='feedback'),  # Feedback form
    path('feedback/success/', feedback_success, name='feedback_success'),  # Success page
]
