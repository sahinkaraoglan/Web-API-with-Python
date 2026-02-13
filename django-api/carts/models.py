from django.db import models
from django.conf import settings
from products.models import Product

class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cart')
    #cart oluştuğunda...
    created = models.DateTimeField(auto_now_add=True)
    #cart güncellendiğinde...
    updated = models.DateTimeField(auto_now=True)
    
    #sahin's cart
    def __str__(self):
        return f"{self.user}'s cart"
    
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items') #yukardaki carta ait özellikleri items diyerek ulaşabileceğiz.
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    #iphone(6)
    def __str__(self):
        return f"{self.product.name}({self.quantity})"
    
    def get_total_price(self):
        return self.product.price * self.quantity