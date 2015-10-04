from django import forms
from mymap.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'lnglat', 'photo',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
