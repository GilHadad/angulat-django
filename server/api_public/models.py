from django.db import models
from django.urls import reverse

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):

        return reverse('%s - %s' % (self.id, self.title))

    def __str__(self):

        return self.title

class List(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()

    def get_absolute_url(self):

        return reverse('%s - %s' % (self.id, self.title))

    def __str__(self):

        return self.title

class ListProducts(models.Model):
    id = models.AutoField(primary_key=True)
    List = models.ForeignKey('List', on_delete=models.PROTECT)
    Product = models.ForeignKey('Product', on_delete=models.PROTECT)

    class Meta:
        ordering = ["List", "Product"]

    def get_absolute_url(self):

        return self.id

    def __str__(self):

        return '%s - %s' % (self.List, self.id)