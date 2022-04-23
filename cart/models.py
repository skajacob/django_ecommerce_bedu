"""Cart app Models"""
from email.policy import default
from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
# Create your models here.

User = get_user_model()

class Address(models.Model):
    ADDRESS_CHOICES=(
        ('B','Billing'),
        ('S','Shipping'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1,choices=ADDRESS_CHOICES)
    default = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.address_line_1}, {self.address_line_2}, {self.city}, {self.zip_code}"
    class Meta:
        verbose_name_plural = 'Addresses'

class Product(models.Model):
    """Product model for cart app"""
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    descritption = models.TextField()
    image = models.ImageField(null = True, upload_to='product_image')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("cart:product_detail", kwargs={'slug': self.slug})


class OrderItem(models.Model):
    """Order item models por cart app"""
    order = models.ForeignKey("order", related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return f"{self.quantity} x {self.product.title}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    orderd_date = models.DateTimeField(auto_now=True)
    billing_address = models.ForeignKey(Address, related_name='billing_address', blank=True, null=True, on_delete=models.SET_NULL)
    shipping_address = models.ForeignKey(Address, related_name='shipping_address', blank=True, null=True, on_delete=models.SET_NULL)
    

    def __str__(self):
        return self.referemce_number
    
    @property
    def referemce_number(self):
        return f"ORDER- {self.pk}"

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20, choices=(
        ('Paypal','Paypal'),
    ))
    timestamp = models.DateTimeField(auto_now_add=True)
    succesful = models.BooleanField(default=False)
    amount = models.FloatField()
    raw_response = models.TextField()

    def __str__(self):
        return self.order
    
    @property
    def referemce_number(self):
        return f"PAYMENT- {self.order}-{self.pk}"
