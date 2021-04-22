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


class NewMusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ("title", "audio_file")

    def clean(self):
        cleaned_data = super(NewMusicForm, self).clean()
        print(cleaned_data['audio_file'])

        errors = {}
        if len(cleaned_data["title"]) < 7:
            errors['title'] = _("Length of song name must be greater than 5 Characters")
        if cleaned_data["audio_file"] is None:
            errors["audio_file"] = _("You must also upload a music file.")

        if errors:
            raise ValidationError(errors)
        return cleaned_data
