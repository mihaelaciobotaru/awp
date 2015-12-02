from django.db import models


class UserPost(models.Model):
    text = models.TextField(max_length=500)
    date_added = models.DateTimeField(
        auto_now_add=True)
    author = models.CharField(default='Eau de Web', max_length=20)

    class Meta:
        ordering = ['-date_added']

    def __unicode__(self):
        return u'{} @ {}'.format(self.author, self.date_added)


class UserPostComment(models.Model):
    text = models.TextField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    author = models.CharField(default='Eau De Web', max_length=20)
    post = models.ForeignKey(UserPost, related_name='comments')

    class Meta:
        ordering = ['date_added']

    def __unicode__(self):
        return u'{} @ {}'.format(self.author, self.date_added)
