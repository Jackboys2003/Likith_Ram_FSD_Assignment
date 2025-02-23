from django.shortcuts import render, redirect
from .forms import FeedbackForm  # Ensure this form exists

def home(request):
    return render(request, 'feedback_app/home.html')  # Home template

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_success')  # Redirect to success page
    else:
        form = FeedbackForm()
    return render(request, 'feedback_app/feedback.html', {'form': form})

def feedback_success(request):
    return render(request, 'feedback_app/feedback_success.html')
