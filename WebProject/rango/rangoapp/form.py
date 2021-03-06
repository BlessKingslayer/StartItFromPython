from django import forms
from rangoapp.models import Category, Page, UserProfile
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text='请输入种类名称')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = "__all__"


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text='请输入页面标题')
    url = forms.URLField(max_length=128, help_text='请输入URL')
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startwith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data


class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(
        widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    website = forms.URLField(
        help_text="Please enter your website.", required=False)
    picture = forms.ImageField(
        help_text="Select a profile image to upload.", required=False)

    class Meta:
        model = UserProfile
        fields = ('website', 'picture')