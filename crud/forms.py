
"""Forms for CRUD app models."""

from django import forms
from crud.models import Instructor, Learner, Enrollment


class EnrollmentForm(forms.ModelForm):
    """Form for Enrollment model."""
    class Meta:
        model = Enrollment
        fields = [
            'learner', 'course', 'date_enrolled', 'mode', 'grade', 'status',
            'progress', 'last_accessed', 'certificate_issued', 'feedback'
        ]
        widgets = {
            'date_enrolled': forms.DateInput(attrs={'type': 'date'}),
            'last_accessed': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'feedback': forms.Textarea(attrs={'rows': 2}),
        }

    def clean_progress(self):
        """Validate that progress is between 0 and 100."""
        progress = self.cleaned_data.get('progress')
        if progress is not None and (progress < 0 or progress > 100):
            raise forms.ValidationError('Progress must be between 0 and 100.')
        return progress


class InstructorForm(forms.ModelForm):
    """Form for Instructor model."""
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
        """Validate that total_learners is non-negative."""
        total_learners = self.cleaned_data.get('total_learners')
        if total_learners is not None and total_learners < 0:
            raise forms.ValidationError('Total learners must be non-negative.')
        return total_learners


class LearnerForm(forms.ModelForm):
    """Form for Learner model."""
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
        """Validate that social_link starts with http:// or https://."""
        link = self.cleaned_data.get('social_link')
        if link and not link.startswith(('http://', 'https://')):
            raise forms.ValidationError(
                'Social link must start with http:// or https://'
            )
        return link
