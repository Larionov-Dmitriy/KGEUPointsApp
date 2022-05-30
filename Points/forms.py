from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Student
from django import forms


class StudentCreationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }), error_messages={'unique': 'Студент с таким адресом электронной почты уже существует'})
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }), error_messages={'unique': 'Студент с таким именем пользователя уже существует'} )
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя'
    }))
    second_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фамилия'
    }))
    third_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Отчество'
    }))
    institute = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Институт'
    }))
    group = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Группа'
    }))
    hostel = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '№ Общежития'
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтверждение пароля'
    }))
    class Meta:
        model = Student
        fields = (
            'email',
            'username',
            'first_name',
            'second_name',
            'third_name',
            'institute',
            'group',
            'hostel',
            'photo'
        )


class StudentChangeForm(UserChangeForm):
    class Meta:
        model = Student
        fields = (
            'email',
            'username',
            'first_name',
            'second_name',
            'third_name',
            'institute',
            'group',
            'hostel',
            'photo'
        )


class StudentAuthenticationForm(forms.ModelForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={
        'class': 'form-control rounded-left',
        'placeholder': 'Email'
    }))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={
        'class': 'form-control rounded-left',
        'placeholder': 'Пароль'
    }))

    class Meta:
        model = Student
        fields = ('email', 'password')

    def clean(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']
        if not authenticate(email=email, password=password):
            raise forms.ValidationError("Неправильный логин или пароль. Попробуйте снова.")


class StudentUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='Адрес электронной почты', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Email'
    }), error_messages={'unique': 'Студент с таким адресом электронной почты уже существует'})
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя пользователя'
    }), error_messages={'unique': 'Студент с таким именем пользователя уже существует'})
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Имя'
    }))
    second_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Фамилия'
    }))
    third_name = forms.CharField(label='Отчество', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Отчество'
    }))
    institute = forms.CharField(label='Институт', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Институт'
    }))
    group = forms.CharField(label='Группа', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Группа'
    }))
    hostel = forms.CharField(label='Общежитие №', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': '№ Общежития'
    }))
    class Meta:
        model = Student
        fields = (
            'email',
            'username',
            'first_name',
            'second_name',
            'third_name',
            'institute',
            'group',
            'hostel',
            'photo',
        )

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                student = Student.objects.exclude(pk=self.instance.pk).get(email=email)
            except Student.DoesNotExist:
                return email
            raise forms.ValidationError("Пользователь с таким адресом электронной почты уже есть")

    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                student = Student.objects.exclude(pk=self.instance.pk).get(username=username)
            except Student.DoesNotExist:
                return username
            raise forms.ValidationError("Пользователь с таким именем уже есть")