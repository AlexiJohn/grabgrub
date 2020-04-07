from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    city = models.CharField(max_length=300)
    objects = models.Manager()
    created_at = models.DateTimeField(auto_now=True)

    def getName(self):
        return self.name
    def getAddress(self):
        return self.address
    def getCity(self):
        return self.city
    def __str__(self):
        return "{}: {} - {},{}".format(
            self.pk,self.getName(),self.getAddress(),
            self.getCity()
        )
class Food(models.Model):
    food_name = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def getName(self):
        return self.food_name
    def getDesc(self):
        return self.description
    def getPrice(self):
        return self.price
    def __str__(self):
        return "{}:{} - {}, {} created at:{}".format(
            self.pk,self.food_name,self.price,self.description,
            self.created_at
        )

class Order(models.Model):
    Payment_choices = [
        ('Card','Card'),
        ('Cash','Cash'),
    ]

    cust_order = models.ForeignKey(Customer,on_delete=models.CASCADE)
    mode_payment = models.CharField(max_length=300,choices=Payment_choices,default='Cash')
    ordered_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    
    def getMode(self):
        return self.mode_payment
    
    def __str__(self):
        return "{}: {}, {}, {}, {}, ordered at {}".format(
            self.pk, self.cust_order.getName(), 
            self.cust_order.getAddress(), self.cust_order.getCity(),
            self.getMode(),self.ordered_at
        )

class OrderLine(models.Model):
    ord = models.ForeignKey(Order, on_delete=models.CASCADE)
    food = models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity = models.FloatField()
    objects = models.Manager()
    total = 0

    def getTotal(self): 
        self.total = self.quantity * self.food.price
        return self.total
    def getQuantity(self):
        return self.quantity
    def __str__(self):
        return "{}: Order {} - {}, {}".format(
            self.pk,self.pk,self.food.getName(),self.getQuantity()
        )
