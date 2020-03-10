from django.db import models

# Create your models here.

class Professor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    uid = models.CharField(max_length = 5)

    def __str__(self):
        return '%s %s ' % (self.first_name, self.last_name)

class Module(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    code = models.CharField(max_length = 10, unique = True)
    year = models.IntegerField()
    semester = models.IntegerField()
    professors = models.ManyToManyField(Professor)

    def __str__(self):
        return '%s %s %i %i' % (self.name, self.code, self.year, self.semester)


class Rating(models.Model):
    professor_uid = models.ForeignKey(Professor, on_delete = models.CASCADE)
    module_code = models.ForeignKey(Module, on_delete = models.CASCADE)
    module_rating = models.IntegerField()

class User(models.Model):
    username = models.CharField(max_length = 30, unique = True)
    password = models.CharField(max_length = 30)
    #email = models.CharField(max_length = 50, unique = True)
