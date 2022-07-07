from django.db import models

# Create your models here.
class question(models.Model):
    question_text = models.CharField(max_length = 2000)
    pub_date