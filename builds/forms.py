from django import forms
from .models import Build
from markdownx.fields import MarkdownxFormField
from django.core.validators import RegexValidator


class BuildForm(forms.ModelForm):

    build_usage = MarkdownxFormField()
    gw2skills_link = forms.URLField(validators=[RegexValidator(
                                                    r'gw2skills\.net/editor/\?[\w\+\-\/]+',
                                                    message="Link not from Gw2Skills.net editor"
                                                )])

    class Meta:
        model = Build
        fields = ('build_name', 'visible', 'build_description', 'build_usage', 'gw2skills_link')
        widgets = {
            'build_name': forms.TextInput(attrs={'class': 'form-control'}),
            'build_description': forms.TextInput(attrs={'class': 'form-control'}),
            'build_usage': forms.TextInput(attrs={'class': 'form-control'})
        }
