from django import forms

from .models import Todos

class TodosForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = [
            'user',
            'title',
            'completed'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if len(title) == 240:
            raise forms.ValidationError('Content is to long')
        return content

