from django.contrib.auth.models import User
from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


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


class UserProfile(models.Model):
    first_name = models.TextField(max_length=21)
    last_name = models.TextField(max_length=21)
    birthday = models.DateTimeField()
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    avatar = models.ImageField(upload_to='userprofile/', blank=True, null=True)
    user = models.OneToOneField(User)

    def __unicode__(self):
        return u'{} {} @ {}'.format(self.first_name, self.last_name, self.birthday)

    def admin_thumbnail(self):
        return u'<img src="/media/%s" />' % self.avatar
    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True

    def get_absolute_avatar_url(self):
        return settings.MEDIA_ROOT+"%s" % self.avatar.url
