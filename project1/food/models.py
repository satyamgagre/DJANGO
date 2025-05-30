from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name
    
    item_name = models.CharField(max_length=200)
    item_des = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500,default='https://cdn.dribbble.com/userupload/22570626/file/original-379b4978ee41eeb352e0ddacbaa6df96.jpg?resize=752x564&vertical=center')

