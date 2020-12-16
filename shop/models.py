from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255, null=True)
    amount = models.CharField(max_length=255, null=True)
    status = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to = 'imagesFolder/', null=True)
    description = models.CharField(max_length=255, null=True)
    posted_date = models.DateTimeField(auto_now_add=True, null=True)
    product_category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE) 

    def __str__(self):
      return self.product_name

class Category(models.Model):
    categories = (("Men","Men"),("Women","Women"),("Kids","Kids"),("Others","Others")) 
    category = models.CharField(max_length = 255, choices = categories, null=True)

    def save_category(self):
        self.save()

    @classmethod
    def get_category_id(cls,id):
        categories = cls.objects.get(id = id)
        return categories

    def __str__(self):
      return self.category


class Customer(models.Model):
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True) 
    # posted_date = models.DateTimeField(auto_now_add=True, null=True)
    # product_category = models.ForeignKey('Category', null=True, on_delete=models.CASCADE) 

    def __str__(self):
      return self.first_name      