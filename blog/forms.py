from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    Имя = forms.CharField(max_length=25)
    Почта = forms.EmailField()
    Получатель = forms.EmailField()
    Комментарии = forms.CharField(required=False,
                               widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')

class SearchForm(forms.Form):
    Запрос = forms.CharField()