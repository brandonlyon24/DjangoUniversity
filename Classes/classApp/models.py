from django.db import models

#model class, register in admin.py
class djangoClasses(models.Model):
    title = models.CharField(max_length=100, default="", blank=True, null=False)
    courseNumber = models.IntegerField(default="", blank=True, null=False)
    instructorName = models.CharField(max_length=30, default="", blank=True, null=False)
    duration = models.FloatField(default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.title
