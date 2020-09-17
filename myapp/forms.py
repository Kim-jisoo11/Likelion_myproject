from django import forms
from .models import Blog, Comment

class BlogForm(forms.ModelForm):

    class Meta : 
        model = Blog
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].label = "제목"
        self.fields['content'].label = "글 내용"
        
        self.fields['title'].widget.attrs.update({
            'class' : 'blog_title', 
            'placeholder' : '제목',

        })
        self.fields['content'].widget.attrs.update({
            'class':'blog_content_form',
        })


class CommentForm(forms.ModelForm):
    class Meta :
        model = Comment 
        fields = ('content', )