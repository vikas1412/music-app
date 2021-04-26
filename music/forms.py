from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from music.models import Music


class SignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=200, required=False, help_text="First Name")
    last_name = forms.CharField(max_length=200, required=False, help_text="Last Name")
    email = forms.CharField(max_length=200, required=False, help_text="Enter email")

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ("title", "audio_file")

    def clean(self):
        cleaned_data = super(MusicForm, self).clean()
        title = cleaned_data.get("title")
        audio_file = cleaned_data.get("audio_file")

        errors = {}
        if len(str(title)) < 7:
            raise ValidationError(_("Length of song name must be greater than 5 Characters"))

        if audio_file is None:
            raise ValidationError(_("You must also upload a music file."))

        if errors:
            raise ValidationError(errors)
        return cleaned_data
