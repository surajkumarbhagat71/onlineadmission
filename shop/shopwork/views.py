from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.db.models import Q

# Create your views here.
def home(r):

    return render(r,'product/home.html')

def contact(r):

    return render(r,'product/contact.html')
#---------------------------------------emplyee------------------------------------

def login(r):
    if r.method == "POST":
        username = r.POST.get("username")
        password = r.POST.get("password")

        cond = Q(emp_email = username) & Q (emp_password = password)
        check = Emplyee.objects.filter(cond).count()

        if (check > 0):
            r.session['login'] = username
            return redirect(product)
        else:
            return redirect(login)

    return render(r,'emplyee/login.html')


def product(r):
    if not r.session.has_key('login'):
        return redirect(login)

    data = {'pro':Product.objects.all()}

    return render(r,'product/product.html',data)

def emp_profile(r):
    if not r.session.has_key('login'):
        return redirect(login)

    log = r.session['login']

    data = {"profile":Emplyee.objects.filter(emp_email = log)}

    return render(r,'emplyee/emp_profile.html',data)


def search(r):
    if r.method=="GET":
        search = r.GET.get('search')
        data = Product.objects.filter(pro_code = search)
        return render(r,'product/product.html',{'pro':data})
    else:
        return redirect(home)


def logout(r):
    if r.session.has_key('login'):
        del r.session['login']
        return redirect(home)


#---------------------------------------------onner-----------------------------------
def login_dir(r):
    if r.method == "POST":
        email = r.POST.get('username')
        password = r.POST.get('password')

        cond = Q(email_id=email) & Q(password=password)

        check = DirSignup.objects.filter(cond).count()

        if (check > 0):
            r.session['login_dir']=email
            return redirect(pro_manage)
        else:
            return redirect(login_dir)

    return render(r,'director/login_dir.html')


def emp_manage(r):
    if not r.session.has_key('login_dir'):
        return redirect(login_dir)

    data = {"emp":Emplyee.objects.all()}

    return render(r,'director/emp_manage.html',data)

def pro_manage(r):
    if not r.session.has_key('login_dir'):
        return redirect(login_dir)

    data = {"pro":Product.objects.all()}
    return render(r,'director/pro_manage.html',data)


def insert_pro(r):
    if not r.session.has_key('login_dir'):
        return redirect('login_dir')

    form = ProductForm(r.POST or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(insert_pro)
    data = {"pro_form":form}
    return render(r,'director/insert_pro.html',data)


def insert_emp(r):
    if not r.session.has_key('login_dir'):
        return  redirect('login_dir')

    form = EmpForm(r.POST or None , r.FILES or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(insert_emp)
    data = {"emp_form":form}
    return render(r,'director/insert_emp.html',data)


def delete_pro(r,id):
    if not r.session.has_key('login_dir'):
        return redirect(login_dir)

    data = Product.objects.filter(id = id)
    data.delete()
    return redirect(pro_manage)


def update_pro(r,id):
    get_id = Product.objects.get(id = id )
    form = ProductForm(r.POST or None , instance=get_id)
    if r.method=="POST":
        if form.is_valid():
            form.save()
            return redirect(pro_manage)

    return render(r,'director/update_pro.html',{"pro":form})


def search_pro(r):

    if r.method == "GET":
        search_pro = r.GET.get('pro_code')
    data = Product.objects.filter(pro_code=search_pro)

    return render(r,'director/pro_manage.html',{"pro":data})


def emp_detail(r,id):
    data = {"profile":Emplyee.objects.filter(emp_id=id)}

    return render(r,'director/emp_detail.html',data)

def update_emp(r,id):
    get_id = Emplyee.objects.get(pk=id)
    form = EmpForm(r.POST or None , r.FILES or None ,instance=get_id)

    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(emp_manage)
    data = {"emp_form":form}
    return render(r,'director/update_emp.html',data)


def delete_emp(r,id):
    data = Emplyee.objects.filter(emp_id=id)
    data.delete()
    return redirect(emp_manage)


def logout_dir(r):
    if r.session.has_key('login_dir'):
        del r.session['login_dir']
        return redirect(home)



