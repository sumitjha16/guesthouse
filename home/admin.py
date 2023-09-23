from django.contrib import admin

# Register your models here.
from .models import room, customer, book
admin.site.register(room)
admin.site.register(customer)
admin.site.register(book)

