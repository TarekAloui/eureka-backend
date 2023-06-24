from django.forms import ModelForm, ValidationError
from .models import researchPaper

class researchPaperForm(ModelForm):
    class Meta:
        model = researchPaper
        fields = ['title', 'author', 'description']
    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description)>300:
            raise ValidationError('This is too long')
        return description
    
