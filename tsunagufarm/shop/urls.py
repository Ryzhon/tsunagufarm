from django.urls import path
from .views import shop_view,recipe_view
from .views import purchase_view

urlpatterns = [

    path('map', shop_view.map, name='map'),

    path('shops', shop_view.show_shops, name='shops'),
    path('shop/<int:shop_id>/', shop_view.show_shop, name='single_shop'),
    path('user/shop/', shop_view.show_user_with_shop, name="user_with_shop"),
    path('add_farm/', shop_view.create_shop, name="add_farm"),

    path("recipe/<int:id>/", recipe_view.recipe_detail, name="recipe_detail"),

    path('purchase/', purchase_view.purchase, name='purchase'),
    path('purchase/after/', purchase_view.purchase_after, name='purchase_after'),

    # path('qr/upload/', purchase_view.upload_qrcode, name='upload_qr'),

    path('others/', shop_view.other, name='others')


]


