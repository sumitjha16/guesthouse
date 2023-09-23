from django.shortcuts import render,redirect
from .models import book,customer
from datetime import datetime


def index(request):
    return render(request,"home/index.html")
def htw(request):
    return render(request,"home/htw.html")

def contact(request):
    return render(request,"home/contact.html")
def room(request):
    return render(request,"home/room.html")

def book_view(request):
    return render(request,"home/book.html")

def calculateamount(start_date,end_date,room_category):
    duration=(end_date-start_date).days

    total_amount=duration*int(room_category)
    return total_amount
def book_room(request):
    if request.method == 'POST':
        start_date = datetime.strptime(request.POST['trip-start'], '%Y-%m-%d').date()
        end_date = datetime.strptime(request.POST['trip-end'], '%Y-%m-%d').date()
        room_category = request.POST['room-category']
        num_adults = int(request.POST['num-adults'])
        num_children = int(request.POST['num-child'])

        total_amount = calculateamount(start_date, end_date, room_category)
        print("Total Amount:", total_amount)
        booking = book(
            book_startdate=start_date,
            book_enddate=end_date,
            book_adults=num_adults,
            book_childs=num_children,
            book_category=room_category,

        )
        booking.save()
        return redirect('payment',total_amount=total_amount)
    return render(request, 'book.html')
def payment(request, total_amount=None):
    if request.method == 'POST':
        new_customer = customer(
            customer_fname=request.POST.get('first-name', ''),
            customer_lname=request.POST.get('last-name', ''),
            customer_phone=request.POST.get('mobile-number', ''),
            customer_email=request.POST.get('email', ''),
        )
        new_customer.save()
        payment_url = 'https://google.com/'  # Replace with your payment gateway URL
        return redirect(payment_url)

    return render(request, 'home/details.html',{'total_amount': total_amount})