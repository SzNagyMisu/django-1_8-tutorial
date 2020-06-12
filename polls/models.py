import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    author = models.CharField(max_length=50, null=True)
    color = models.CharField(max_length=10, default='black', null=True)

    def __unicode__(self):
        return self.question_text
        # return "#%d - %s" % (self.id, self.question_text)

    def was_published_recently(self):
        """
        Returns True if the question was published in less than a day,
        False otherwise
        :return: Boolean
        """
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
        # return "#%d - %s (question#%d)" % (self.id, self.choice_text, self.question.id)
