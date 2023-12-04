import re
from django.shortcuts import redirect, render
from django.urls import is_valid_path
from base.models import Car, Payments, Feedback
from rest_framework.parsers import JSONParser
from base.forms import AddCarForm, PaymentForm
from base.paystack import make_payment, verify_payment
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from base.emails import send_email
from cloudinary.uploader import upload

# Create your views here.
def landing_page(request):
    """This Will Return All Cars Both Booked and UnAvailable"""
    # all_cars = Car.objects.all()
    """This Will Return All Cars that are only available to be booked """
    all_cars = Car.objects.filter(car_availability=True)
    context = {'all_cars':all_cars}
    return render(request, 'base/main.html', context)


def car_detail(request,pk):
    car_data = Car.objects.get(id=pk)
    context = {'car_data':car_data}
    
    return render(request, 'base/detail.html', context)

def payment(request,pk):
    car_data = Car.objects.get(id=pk)

    form = PaymentForm()
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone_number = request.POST['phone_number']
        email_address = request.POST['email-address']
        address= request.POST['address']
        town_city = request.POST['town_city']
        pickup_location = request.POST['pick_location']
        pickup_date = request.POST['pick_date']
        drop_location = request.POST['drop_location']
        number_of_days = request.POST['drop_date']

        # Option one
        _num = int(float(number_of_days))
        _amount_payable = _num * car_data.amount_per_day
        _data = make_payment(int(_amount_payable),email_address)

        payment = Payments.objects.create(name=full_name,email_address=email_address,phone_number=phone_number,town_city=town_city,address=address,
                                           pickup_location=pickup_location, pickup_date=pickup_date,
                                            dropoff_location=drop_location,number_of_days=number_of_days, payment_amount= int(_amount_payable),
                                            payment_ref=_data['reference'],car_details=car_data) 
        payment.save()
        # print(request.POST)
        car_data.car_availability = False
        car_data.save()
        send_email(email=email_address,car_name=car_data.car_name,_amount_payable=_amount_payable, number_of_days=number_of_days)

        return render(request,'base/verify_payment.html',{'url':_data['auth_url']})     
    context = {'car_data':car_data,'form':form}
    return render(request,'base/payment.html', context)

def verify_payments(request):
    
    context = {}
    return render(request,'base/verify_payment.html', context)

@login_required(login_url='/login/')
def dashboard(request):
    transactions = Payments.objects.all()
    cars_value = Car.objects.all().count()
    cars = Car.objects.filter(car_availability=True).count()
    cars_out = Car.objects.filter(car_availability=False).count()

    amount = 0
    for transaction in transactions:
        amount +=transaction.payment_amount
    
    context = {'transactions':transactions,'amount':amount,'cars_value':cars_value,'cars':cars,'cars_out':cars_out }
    return render(request,'base/dashboard.html', context)

@login_required(login_url='/login/')
def add_car(request):
    form = AddCarForm()
    if request.method == 'POST':
        form = AddCarForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get("car_image")
            print(request.FILES)
            record = form.save(commit=False)
            record.car_image = image
            # Upload image to cloudinary
            _url = upload(image)
            pub_id = _url['public_id']
            url = f"https://res.cloudinary.com/dxrxrd21n/image/upload/f_auto,q_auto/{pub_id}"
            print(url)
            record.car_image_urls = url
            record.save()
            return redirect(dashboard)
    context = {'form':form}
    return render(request,'base/add_car.html', context)

def login_user(request):    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password= password)
        if user is not None:
            login(request, user)
            return redirect(dashboard)

    return render(request,'base/login.html')

def logout_user(request):
    logout(request)
    return redirect(landing_page)

def faq_page(request):
    context = {}
    return render(request, 'base/faq-page.html',context)


def customer_support(request):
    context = {}
    return render(request,'base/support.html',context)

def feedback_page(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        phone_number= request.POST['phone_number']
        email_address= request.POST['email-address']
        car_category= request.POST['car-category']
        cleanliness = request.POST['vehicle-cleanliness']
        pickup_and_dropoff = request.POST['pickup_and_dropoff']
        staff_professionalism = request.POST['staff-professionalism']

        feedback = Feedback.objects.create(full_name=full_name, phone_number=phone_number,email_address=email_address
                                           ,car_category=car_category,vehicle_cleanliness=cleanliness,
                                           pickup_and_dropoff= pickup_and_dropoff,
                                           staff_professionalism=staff_professionalism)
        feedback.save()
        """SEND EMAIL NOTIFYING THEM ABOUT THEIR FEEDBACK BEING RECORDED"""
        return redirect(feedback_success)


    context = {}
    return render(request,'base/feedback.html', context)

def feedback_success(request):
    return render(request,'confirm.html')