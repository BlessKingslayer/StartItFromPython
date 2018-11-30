from django import forms
from rangoapp.models import Category, Page


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
