from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.db.models import Q

# Create your views here.

def home(r):

    return render(r,'home.html')

###############################################   Director     ###############################################

def login(r):
    if r.method == "POST":
        username = r.POST.get('username')
        password = r.POST.get('password')

        cond = Q(dir_email = username) & Q(dir_password = password)

        cheak = Director.objects.filter(cond).count()

        if (cheak > 0 ):
            r.session['login']=username
            return redirect(dashabord)
        else:
            return redirect(login)

    return render(r, 'director/login.html')

def dashabord(r):
    if not r.session.has_key('login'):
        return redirect(login)

    data = {
        "admission":Admission.objects.all().count(),
        "college":College.objects.all().count(),
        "registation":Registation.objects.all().count(),
        "cat":Category.objects.all().count(),
        "course":Course.objects.all().count(),
    }
    return render(r, 'director/dashabord.html',data)


def addcollege(r):
    if not r.session.has_key('login'):
        return redirect(login)

    form = CollegeForm(r.POST or None , r.FILES or None )
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(dashabord)

    return render(r,'director/add college.html',{"colform":form})



def addcourse(r):
    if not r.session.has_key('login'):
        return redirect(login)

    form = CourseForm(r.POST or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(dashabord)

    return render(r, 'director/add_course.html', {"courseform":form})


def addcategory(r):
    if not r.session.has_key('login'):
        return redirect(login)

    f = CatForm(r.POST or None)
    if r.method == "POST":
        if f.is_valid():
            f.save()
            return redirect(dashabord)
    return render(r, 'director/add_cat.html', {"catform":f})

def all_category(r):
    if not r.session.has_key('login'):
        return redirect(login)

    data = {"cat":Category.objects.all()}

    return render(r,'director/all_category.html',data)

def all_course(r):
    if not r.session.has_key('login'):
        return redirect(login)

    data = {"course":Course.objects.all()}

    return render(r,'director/all_course.html',data)


def all_college(r):
    if not r.session.has_key('login'):
        return redirect(login)

    data = {"college":College.objects.all()}

    return render(r,'director/all_college.html',data)


def dcourse(r,co_id):
    if not r.session.has_key('login'):
        return redirect(login)

    data = Course.objects.filter(course_id=co_id)
    data.delete()
    return redirect(all_course)


def dcategory(r,ca_id):
    if not r.session.has_key('login'):
        return redirect(login)

    data = Category.objects.filter(cat_id=ca_id)
    data.delete()
    return redirect(all_category)

def dcollege(r,id):
    if not r.session.has_key('login'):
        return redirect(login)

    data = College.objects.filter(col_id=id)
    data.delete()
    return redirect(all_college)



def logout(r):
    if r.session.has_key('login'):
        del r.session['login']
        return redirect(home)


##############################################  student ############################

def registation(r):
    form = RegForm(r.POST or None)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(slogin)

    data = {"regform":form}

    return render(r,'student/regitation.html',data)


def profile(r):
    if not r.session.has_key('slogin'):
        return redirect(slogin)

    r_id = Registation.objects.get(student_email=r.session['slogin']).r_id

    data = {
        "profile":Registation.objects.get(student_email = r.session['slogin']),
        "all_detail":Admission.objects.get(registation_no = r_id)
    }

    return render(r,'student/profile.html',data)


def slogin(r):
    if r.method == "POST":
        username = r.POST.get('username')
        password = r.POST.get('password')

        cond = Q(student_email=username) & Q(student_password = password)
        cheak = Registation.objects.filter(cond).count()

        if (cheak > 0):
            r.session['slogin']=username
            return redirect(admission)
        else:
            return redirect(slogin)

    return render(r,'home.html')



def admission(r):
    if not r.session.has_key('slogin'):
        return redirect(slogin)

    reg = Registation.objects.get(student_email= r.session['slogin']).r_id
    col = Registation.objects.get(student_email=r.session['slogin']).student_college_id

    admission = Admission.objects.filter(registation_no=reg).count()

    if (admission == 1):
        return redirect(profile)
    else:
        form = Admissionform(r.POST or None , r.FILES or None)
        if r.method == "POST":
            if form.is_valid():
                a = form.save(commit=False)
                a.registation_no = Registation(reg)
                a.admision_in_col = col
                a.save()
                return redirect(profile)

    return render(r,'student/addmition.html',{"adform":form})


def documtnt(r):
    if not r.session.has_key('slogin'):
        return redirect(slogin)

    r_id = Registation.objects.get(student_email = r.session['slogin']).r_id
    data = Admission.objects.filter(registation_no= r_id).count()

    doc = Document.objects.filter(student_id=r_id).count()



    if (data == 1):
        if (doc == 1):
            return redirect(profile)

        form = DocForm(r.POST or None ,r.FILES or None)
        if r.method == "POST":
            if form.is_valid():
                a = form.save(commit=False)
                a.student_id = Registation(r_id)
                a.save()
                return redirect(documtnt)
    else:
        return redirect(admission)

    return render(r,'student/document.html',{"docform":form})


def slogout(r):
    if r.session.has_key('slogin'):
        del r.session['slogin']
        return redirect(slogin)




