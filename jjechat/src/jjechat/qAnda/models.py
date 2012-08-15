from django.db import models

class QAndA(models.Model):
    question = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
        
    def __unicode__(self):
        return self.question

