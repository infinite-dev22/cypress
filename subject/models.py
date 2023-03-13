from django.db import models

from echelon.models import Class, Term


class Subject(models.Model):
    name = models.CharField(max_length=50)
    abbreviated_name = models.CharField(max_length=20)
    is_optional = models.BooleanField(default=False)
    classes = models.ManyToManyField(Class, blank=True)
    is_active = models.BooleanField(default=True)

    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, )
    # created_on = models.DateTimeField(auto_now=datetime.now())

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    class_of_Topic = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    term = models.ForeignKey(Term, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    # competency = models.TextField()
    # maximum_mark = models.FloatField(null=True, blank=True)
    # created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, )
    # created_on = models.DateTimeField(auto_now=datetime.now())

    def __str__(self):
        return self.name
