from django.db import models


class Buser(models.Model):
    id = models.AutoField(int, primary_key=True, max_length=30)
    email = models.TextField(120)
    nickname = models.TextField(20)
    password = models.TextField(255)


    class Meta:
        db_table = 'busers'

    def __str__(self):
        return f'{self.pk} {self.email} {self.nickname} {self.password} '