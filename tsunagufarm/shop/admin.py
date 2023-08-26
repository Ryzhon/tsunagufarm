from django.contrib import admin
from .models import Shop, Product, Tag, Recipe, Comment

# ShopのAdmin定義
@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'longitude','latitude', 'owner')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("recipe","created_at")

# ProductのAdmin定義
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)

# TagのAdmin定義
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

# RecipeのAdmin定義
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'shop')
    filter_horizontal = ('tags',)  # ManyToMany関係のため

# ReviewのAdmin定義

