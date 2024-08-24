from django.db import models


class Products(models.Model):
    name = models.CharField("Название", max_length=100)
    price = models.IntegerField("Цена")
    description = models.TextField("Описание")
    
    def __str__(self):
        return self.name


