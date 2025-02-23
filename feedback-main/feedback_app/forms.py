from django import forms
from .models import Feedback
import re

class FeedbackForm(forms.ModelForm):
    """Feedback Form with validation for email and message length."""
    
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'subject', 'message']
    
    def clean_email(self):
        """Validate email to ensure it ends with @example.com."""
        email = self.cleaned_data.get('email')
        allowed_domain = "@example.com"

        if not email.endswith(allowed_domain):
            raise forms.ValidationError(f'Only emails ending with {allowed_domain} are allowed.')
        
        return email
    
    def clean_message(self):
        """Ensure message length is at least 50 characters and not just whitespace."""
        message = self.cleaned_data.get('message')
        
        if len(message.strip()) < 50:
            raise forms.ValidationError('Message must be at least 50 meaningful characters long.')
        
        return message
