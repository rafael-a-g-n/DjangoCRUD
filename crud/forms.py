from django import forms
from .models import Instructor

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
