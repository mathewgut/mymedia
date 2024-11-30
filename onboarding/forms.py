from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, likedMovie



class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','password1','password2']



class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    movieGenre = forms.ChoiceField(
        choices=Profile.VIDEO_GENRE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    showGenre = forms.ChoiceField(
        choices=Profile.VIDEO_GENRE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    musicGenre = forms.ChoiceField(
        choices=Profile.MUSIC_GENRE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Profile
        fields = ['photo', 'bio', 'movieGenre', 'showGenre', 'musicGenre']
