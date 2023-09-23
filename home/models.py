from django.db import models
from django.core.validators import RegexValidator

class room(models.Model):
    room_id=models.AutoField
    room_number=models.IntegerField
    room_floor=models.IntegerField
    room_category=models.CharField(max_length=1)

    def __str__(self):
        return self.room_number
class book(models.Model):
    book_id=models.AutoField(primary_key=True)
    book_startdate = models.DateField()
    book_enddate = models.DateField()
    book_adults = models.IntegerField()
    book_childs = models.IntegerField()
    book_category=models.CharField(max_length=10)

    def __str__(self):
        return  f"{self.book_id} {self.book_category}"

class customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_fname=models.CharField(max_length=20)
    customer_lname = models.CharField(max_length=20)
    customer_phone = models.CharField(max_length=15, validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit phone number.')])
    customer_email=models.EmailField(max_length=30)

    def __str__(self):
        return  f"{self.customer_fname} {self.customer_lname}"



