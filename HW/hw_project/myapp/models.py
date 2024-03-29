from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=25)
    adress = models.CharField(max_length=100)
    regist_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Name: {self.name} Email: {self.email} ' \
               f'Phone: {self.phone} Adress: {self.adress}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    regist_prod_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default=None)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Name: {self.name} Price: {self.price}'


class Status(models.Model):
    status = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.status}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(Status, default=1, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'\nCustomer: {self.customer} \nProducts: {self.products} \nTotal price: {self.total_price}'
