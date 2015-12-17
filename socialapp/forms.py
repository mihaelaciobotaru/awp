from django.forms import Form, CharField, Textarea, PasswordInput, DateTimeInput, ImageField


class UserPostForm(Form):
    text = CharField(widget=Textarea(
        attrs={'cols': 100, 'rows': 5, 'placeholder': "What's on your mind?"}),
        label='')


class UserPostCommentForm(Form):
    text = CharField(widget=Textarea(
        attrs={'rows': 4, 'cols': 50, 'placeholder': 'Write a comment...'}),
        label='')


class UserLoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(widget=PasswordInput)


class UserProfileForm(Form):
    first_name = CharField(max_length=21)
    last_name = CharField(max_length=21)
    birthday = DateTimeInput()
    gender = CharField(max_length=1)
    avatar = ImageField()

