from django.db import models

# Create your models here.
class Suser(models.Model):
    id = models.AutoField(primary_key=True, max_length=30)
    email = models.TextField(120)
    nickname = models.TextField(20)
    password = models.TextField(255)
    point = models.IntegerField()


    class Meta:
        db_table = 'suser'

    def __str__(self):
        return f'{self.pk} {self.email} {self.nickname} {self.password} {self.point} '