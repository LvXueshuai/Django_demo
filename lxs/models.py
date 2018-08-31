from django.db import models

# Create your models here.
class Classes(models.Model):
    '''
    学生表
    '''
    titile = models.CharField(max_length=32)
    m = models.ManyToManyField('Teachers')

class Teachers(models.Model):
    '''
    教师表
    '''
    name = models.CharField(max_length=32)

# class C2T(models.Model):
#     cid = models.ForeignKey(Classes)
#     tid = models.ForeignKey(Teachers)

class Student(models.Model):
    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.BooleanField()
    cs = models.ForeignKey(Classes,on_delete='cascade',related_name='relate')
    '''
    #related_name是关联名称，
    用于从Class表进行反向查找：Class.objects.all().values('titile','relate__username')，
    若不加related_name，
    则可用  小写类名_set：Class.objects.all().values('titile','student_set('username')')
    
    正向查找：（从有主键的表开始）尽量用正向查找
    Student.objects.all().values('username','cs__titile')
    
        
    '''







