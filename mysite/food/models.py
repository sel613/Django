from django.db import models

# Create your models here.

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length = 200)
    item_desc = models.CharField(max_length = 200)
    item_price = models.IntegerField()
    item_img = models.CharField(max_length=1000,default ="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRftcWMZycPdTp4H5yYhp9SroBMfuVYJLLPDIQ4JvLRpSSHhnwIwPKmeNXeBlKRY88p8C8&usqp=CAU")
