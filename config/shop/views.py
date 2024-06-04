from django.shortcuts import render, redirect
from .models import Product, Banner, User
from .forms import Reg, Auth

def index(request):
    products = Product.objects.all()
    banners = Banner.objects.all()
    return render(request, 'index.html', {'products':products,'banners': banners})

def catalog(request):
    products = Product.objects.all()
    return render(request, 'catalog.html', {'products':products})

def panel(request):
    current_user = False
    if 'user' in request.session:
        current_user = User.objects.filter(login=request.session['user']).first()
    suc = False
    if 'suc' in request.GET and request.GET['suc'] == '1':
        suc = True
    form_auth = Auth()
    form_reg = Reg()
    return render(request, 'panel.html', {'form_auth':form_auth, 'form_reg':form_reg,'suc': suc, 'current_user': current_user})

def reg_post(request):
    suc = '0'
    if request.method == 'POST':
        login = request.POST['login']
        password = request.POST['password']
        phone = request.POST['phone']
        email = request.POST['email']

        if User.objects.filter(login=login).exists():
            suc = 0
        else:
            user = User()
            user.login = login
            user.password = password
            user.phone = phone
            user.email = email
            user.save()
            suc = '1'
    return redirect('/panel?suc='+suc)


def auth_post(request):
    login = request.POST['login']
    password = request.POST['password']

    if User.objects.filter(login=login,password=password).exists():
        request.session['user'] = login

    return redirect('/panel')


def logout(request):
    if 'user' in request.session:
        del request.session['user']
    return redirect('/panel')

def addcart(request):
    if request.method == 'POST':
        id_product = request.POST['product']
        if 'cart' in request.session:
            request.session['cart'] += (',' + id_product)
        else:
            request.session['cart'] = id_product
    return redirect('/catalog')


def cart(request):
    if 'cart' in request.session:
        carts_id = request.session['cart'].split(',')
        products_new = []
        for i in carts_id:
            product = Product.objects.filter(id=int(i))
            products_new.append(product)


    return render(request, 'cart.html', {'products_new': products_new})