from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from blog.models import Incident

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(
    )
    first_name = forms.CharField(
        max_length=50,
    )
    last_name = forms.CharField(
        max_length=50,
    )
    username = forms.CharField(
        max_length=150,
        help_text="Maximum of 150 characters.",
    )

    class Meta:
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
        
    def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("An account is already associated with this email.")
            return email
    
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'location', 'pictures']

class IncidentUpdateForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'description', 'location', 'pictures']

    def __init__(self, *args, **kwargs):
        # Pop the 'initial_picture' argument from kwargs before calling super().__init__()
        initial_picture = kwargs.pop('initial_picture', None)
        super().__init__(*args, **kwargs)
        self.initial_picture = initial_picture

    def clean_pictures(self):
        # If the 'pictures' field has changed, do any processing needed
        # For example, you can use a custom method in your model to handle this
        if self.cleaned_data['pictures'] != self.initial_picture:
            self.instance.custom_picture_update_method(self.initial_picture)
        return self.cleaned_data['pictures']