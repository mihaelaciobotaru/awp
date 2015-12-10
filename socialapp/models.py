from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse


class UserPost(models.Model):
    text = models.TextField(max_length=500)
    date_added = models.DateTimeField(
        auto_now_add=True)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ['-date_added']

    def get_absolute_url(self):
        return reverse('index')

    def __unicode__(self):
        return u'{} @ {}'.format(self.author, self.date_added)


class UserPostComment(models.Model):
    text = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    post = models.ForeignKey(UserPost, related_name='comments')

    class Meta:
        ordering = ['date_added']

    def __unicode__(self):
        return u'{} @ {}'.format(self.author, self.date_added)
