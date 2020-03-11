from django.db import models

# Create your models here.

class Professor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 40)
    uid = models.CharField(max_length = 5,unique = True)

    def __str__(self):
        return '%s %s ' % (self.first_name, self.last_name)


class Module(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    code = models.CharField(max_length = 10, unique = True)

    def __str__(self):
        return '%s %s ' % (self.name, self.code)

class ModuleInstance(models.Model):
    code = models.ForeignKey(Module, on_delete = models.CASCADE)
    year = models.IntegerField()
    semester = models.IntegerField()
    professors = models.ManyToManyField(Professor)

    def __str__(self):
        # if self.professors.size() == 2:
        #     pass
        return '%s %i %i ' % (self.code, self.year, self.semester)+'-'.join([str(professor) for professor in self.professors.all()])

class Rating(models.Model):
    professor_uid = models.ForeignKey(Professor, on_delete = models.CASCADE)
    module_instance = models.ForeignKey(ModuleInstance, on_delete = models.CASCADE)
    rating = models.IntegerField()

    def __str__(self):
        return '%s %s %i' % (self.professor_uid, self.module_instance, self.rating)
