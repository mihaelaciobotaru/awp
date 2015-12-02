from django.forms import Form, CharField, Textarea


class UserPostForm(Form):
    text = CharField(widget=Textarea(
        attrs={'cols': 100, 'rows': 5, 'placeholder': "What's on your mind?"}),
        label='')


class UserPostCommentForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 4, 'cols': 50, 'placeholder': 'Write a comment...'}),
        label='')
