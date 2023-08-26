from django.db import models
import uuid


class Shop(models.Model):
    name = models.CharField(max_length=255)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    owner = models.ForeignKey('user.User', related_name="shops", on_delete=models.CASCADE)
    img = models.ImageField(upload_to="images/shop/")
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=255)
    shop = models.ForeignKey(Shop, related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)

class Recipe(models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    #slug  = models.SlugField() #投稿固有の情報
    content = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True) #blank=Trueを追加
    created_by = models.ForeignKey('user.User', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name="recipes", on_delete=models.CASCADE)
    #posted_data = models.DateTimeField(auto_now_add=True) #投稿日時

class Comment(models.Model):

    recipe = models.ForeignKey(Recipe, related_name="comments", on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to="images")
    user = models.ForeignKey('user.User', related_name="comments", on_delete=models.CASCADE)