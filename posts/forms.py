from django import forms
from .models import Post, Comments

class PostForm(forms.ModelForm):
    post_body = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'autocomplete':'off', 'placeholder': 'What do you think today?'}))
    video = forms.FileField(required=False, widget=forms.FileInput(attrs={'accept':'video/*', 'required':False}))
    class Meta:
        model = Post
        fields = ('post_body', 'image', 'video')

class CommentForm(forms.ModelForm):
    comment_body = forms.CharField(label='', 
                            widget=forms.TextInput(attrs={'placeholder': 'Add a comment...', 'autocomplete':'off', 'class':'id_comment_body_class', 'id': ''}))
    class Meta:
        model = Comments
        fields = ('comment_body',)