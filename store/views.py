from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models.product import product
from .models.category import category
from .models.customer import customer
from django.contrib.auth.hashers import make_password, check_password
#from django.contrib.auth.models import User, auth
from django.views import View
from django.http.request import QueryDict

class index(View):
    def post(self,request):
        product=request.POST.get('product')
        remove=request.POST.get('remove')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]=quantity-1
                else:
                    cart[product]=quantity+1

            else:
                cart[product]=1


        else:
            cart={}
            cart[product]=1
        request.session['cart']=cart
        #print(request.session['cart'])
        print(product)
        return redirect('homepage')
    def get(self,request):

        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        products = None
        categorys = category.get_all_categorys()
        categoryid = request.GET.get('category')
        type(categoryid)
        print(categoryid,'this is the category id')
        if categoryid:
            products = product.get_all_product_by_id(categoryid)
            print(products,'this is product')
        else:
            products = product.get_all_product()
            print('it is else part')

        data = {}

        data['products'] = products
        data['categorys'] = categorys
        # print(products)
        print(data)
        print("you are: ", request.session.get('email'))
        return render(request, 'file1.html', data)


# Create your views here.


class signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        postData = request.POST
        first_name = postData.get('firstname')

        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validations
        values = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = None
        customer1 = customer(first_name=first_name,
                             last_name=last_name,
                             phone=phone,
                             email=email,
                             )

        if (not first_name):
            error_message = "First Enter Your First Name"
        elif len(first_name) < 4:
            error_message = "first name must be 4 char long"
        if (not last_name):
            error_message = "First Enter Your Last Name"
        elif len(last_name) < 4:
            error_message = "Last name must be 4 char long"
        if (not phone):
            error_message = "First Enter Your First Name"
        elif len(phone) == 10:
            error_message = "Phone Number must be 10 digit long"
        elif len(email) < 5:
            error_message = "email must be 4 char long"
        elif customer1.isexist():
            error_message = "EMAIL ADDRESS ALREADY "

        # saving
        if (not error_message):
            print(first_name, last_name, phone, email, password)
            customer1.password = make_password(password)
            customer1.register()
            return redirect("homepage")
        else:
            data = {
                'error': error_message,
                'value': values
            }

            return render(request, 'signup.html', data)


class login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer2 = customer.get_customer_by_email(email)

        if customer2:
            error_message = None
            print(password)
            print(customer2.password)
            flag = check_password(password, customer2.password)
            print(flag)
            if flag:
                request.session['customer']=customer2.id
                request.session['email']=customer2.email
               #as print('the logined person is ',request.session.get('email'))
                return redirect("homepage")
            else:
                error_message = "invalid ! password"
                return render(request, 'login.html',{'error':error_message})


        else:
            error_message = "invalid ! email"

        return render(request, 'login.html', {'error': error_message})


def logout(request):
        request.session.clear()
        return redirect('login')

def cart(request):
    ids=list(request.session.get('cart').keys())
    products=product.get_product_by_id_cart(ids)
    print(products)
    return render(request,'cart.html',{'products':products})


