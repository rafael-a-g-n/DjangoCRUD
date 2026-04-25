from django import forms
from .models import Instructor, Learner

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = [
            'first_name', 'last_name', 'email', 'location', 'dob',
            'full_time', 'total_learners'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_total_learners(self):
        total_learners = self.cleaned_data.get('total_learners')
        if total_learners is not None and total_learners < 0:
            raise forms.ValidationError('Total learners must be non-negative.')
        return total_learners

class LearnerForm(forms.ModelForm):
    class Meta:
        model = Learner
        fields = [
            'first_name', 'last_name', 'email', 'location', 'dob',
            'occupation', 'social_link'
        ]
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'social_link': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }

    def clean_social_link(self):
        link = self.cleaned_data.get('social_link')
        if link and not link.startswith(('http://', 'https://')):
            raise forms.ValidationError('Social link must start with http:// or https://')
        return link
