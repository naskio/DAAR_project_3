from django.forms import ModelForm
from .models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        # fields = ['first_name', 'last_name', 'attached_file']
        fields = '__all__'
