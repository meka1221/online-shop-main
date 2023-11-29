from django.urls import path
from . views import (
    cart,
    checkout,
    store,
    updateItem,
    processOrder,
    login,
    register,
)

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('', store, name='store'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),
]