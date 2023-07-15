from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def index(request):
    return render(request, 'index.html')

def registration(request):
    error = ""
    if request.method == "POST":
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        pwd = request.POST['pwd']
        try:
            user = User.objects.create_user(first_name = fn, last_name = ln, username = em, password = pwd)
            Component.objects.create(user = user)
            error = "no"
        except:
            error = "yes"
        
    return render(request, 'registration.html', locals())

def emp_login(request):
    error = ""
    if request.method == "POST":
        em = request.POST['email']
        pwd = request.POST['pwd']
        user = authenticate(username = em, password = pwd)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'emp_login.html', locals())

def emp_home(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def admin_login(request):

    return render(request, 'admin_login.html')


def admin_login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['pwd']
        user = authenticate(username = u, password =p)
        if user.is_staff:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'admin_login',locals())

def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    return render(request, 'admin_home.html')

def addComponent(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user
    # component = Component.objects.get(user = user)
    if request.method == "POST":
        srNo = request.POST['srNo']
        work = request.POST['work']
        group = request.POST['group']
        nmc = request.POST['nmc']
        indate = request.POST['indate']
        outdate = request.POST['outdate']
        servicableber = request.POST['servicableber']
        fault = request.POST['fault']
        doc = request.POST['doc']
        doj = request.POST['doj']
        remarks = request.POST['remarks']
        info = request.POST['info']

        c = Component()
        c.user = user
        c.srNo = srNo
        c.work = work
        c.group = group
        c.nmc = nmc
        c.indate = indate
        c.outdate = outdate
        c.servicableber = servicableber
        c.fault = fault
        c.doc = doc
        c.doj = doj
        c.remarks = remarks
        c.info = info
        
        c.save()
        try:
            error = "no"
        except:
            error = "yes"
    

    return render(request, 'addComponent.html', locals())

def admin_addComponent(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    # component = Component.objects.get(user = user)
    if request.method == "POST":
        srNo = request.POST['srNo']
        work = request.POST['work']
        group = request.POST['group']
        nmc = request.POST['nmc']
        indate = request.POST['indate']
        outdate = request.POST['outdate']
        servicableber = request.POST['servicableber']
        fault = request.POST['fault']
        doc = request.POST['doc']
        doj = request.POST['doj']
        remarks = request.POST['remarks']
        info = request.POST['info']

        c = Component()
        c.user = user
        c.srNo = srNo
        c.work = work
        c.group = group
        c.nmc = nmc
        c.indate = indate
        c.outdate = outdate
        c.servicableber = servicableber
        c.fault = fault
        c.doc = doc
        c.doj = doj
        c.remarks = remarks
        c.info = info
        
        c.save()
        try:
            error = "no"
        except:
            error = "yes"
        
    return render(request, 'admin_addComponent.html', locals())

def viewComponent(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    
    components = Component.objects.all()
   
    return render(request, 'viewComponent.html', locals())

def all_components(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    components = Component.objects.all()
    return render(request, 'all_components.html',locals())


def edit_component(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    error = ""
    user = request.user
    if request.method == "POST":
        srNo = request.POST['srNo']
        work = request.POST['work']
        group = request.POST['group']
        nmc = request.POST['nmc']
        indate = request.POST['indate']
        outdate = request.POST['outdate']
        servicableber = request.POST['servicableber']
        fault = request.POST['fault']
        doc = request.POST['doc']
        doj = request.POST['doj']
        remarks = request.POST['remarks']
        info = request.POST['info']

        c = Component()
        c.user = user
        c.srNo = srNo
        c.work = work
        c.group = group
        c.nmc = nmc
        c.indate = indate
        c.outdate = outdate
        c.servicableber = servicableber
        c.fault = fault
        c.doc = doc
        c.doj = doj
        c.remarks = remarks
        c.info = info
        
        c.save()
        try:
            error = "no"
        except:
            error = "yes"
    
    return render(request, 'edit_component.html', locals())

def delete_component(request,pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    
    c = Component.objects.get(id=pid)
    c.delete() 

    return redirect('all_components')


