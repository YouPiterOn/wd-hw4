from django.db import models


class Tree(models.Model):
    id = models.AutoField(primary_key=True)
    height = models.IntegerField()
    age = models.IntegerField()
    typeOf = models.CharField(max_length=100)

    class Meta:
        app_label = 'hw6app'
