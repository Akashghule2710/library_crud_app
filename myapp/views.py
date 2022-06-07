
import email
from pkgutil import get_data
from re import U
from urllib import request
from urllib.request import Request
from django.shortcuts import render,redirect
from .models import *
from rest_framework import viewsets
from .serializers import BookDetailsSerializer
from rest_framework.response import Response
from django.http import HttpResponseRedirect


def IndexPage(request):
    return render(request,"myapp/index.html")

def LoginPage(request):
    return render(request,"myapp/login.html")

def InsertPageView(request):
    return render(request,"myapp/insert.html")


'''
def RegisterAdmin(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        mobile = request.POST['mobile']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        role = request.POST['role']
        #validating user is already exist or not
        vuser = UserMaster.objects.filter(email=email)
        if vuser:
            message = "Admin already exist go to login"
            return render(request,"myapp/signup.html",{'msg':message})
        else:
            if password == cpassword:
                newuser = UserMaster.objects.create(firstname=firstname,lastname=lastname,mobile=mobile,password=password)
                message ="admin registration success"
                return render(request,"myapp/login.html",{'msg':message})
            else:
                message = "your password and confirm password not matched"
                return render(request,"myapp/signup.html",{'msg':message})
'''
            
#login page authentication view
def LoginAdmin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        #checking email with database
        luser = UserMaster.objects.get(email=email)
        if luser:
            if luser.password == password:
                #we are getting our mail in session
                request.session['email'] = luser.email
                return render(request,"myapp/insert.html")
            else:
                
                print('password does not match')
                return render(request,"myapp/login.html")
        else:
            
            print('user does not exists')
            return HttpResponseRedirect("/")
 #insert data view       
def InsertData(request):
    bno=request.POST['bno']
    name=request.POST['name']
    auther=request.POST['auther']
    status=request.POST['status']

    newuser=BookDetails.objects.create(bno=bno,name=name,auther=auther,status=status)

#after insert render on show.html
    return redirect('showtable')
#show table view
def ShowTable(request):
    all_data = BookDetails.objects.all()
    return render (request,"myapp/show.html",{'key1':all_data})            
  
#edit page view
def EditPage(request,pk):
    get_data=BookDetails.objects.get(id=pk)
    return render(request,"myapp/edit.html",{'key2':get_data})

#update data view
def UpdateData(request,pk):
    udata=BookDetails.objects.get(id=pk)
    udata.bno=request.POST['bno']
    udata.name=request.POST['name']
    udata.auther=request.POST['auther']
    udata.status=request.POST['status']
    #query for update
    udata.save()
    return redirect('showtable')

#delete data view

def DeleteData(request,pk):
    ddata=BookDetails.objects.get(id=pk)
    #query for delete
    ddata.delete()

    return redirect("showtable")          

#book list view

def BookListView(request):
    all_data = BookDetails.objects.all()
    return render (request,"myapp/booklist.html",{'key1':all_data})
    
class BookDetailsViewSet(viewsets.ViewSet):
    
    def list(self,request):
        data=BookDetails.objects.all()
        ser = BookDetailsSerializer(data,many=True)
        return Response(ser.data)

      
     
    def retrieve(self,request,pk=None):
        book=BookDetails.objects.get(id=pk)
        ser=BookDetailsSerializer(book)
        return Response(ser.data)
    

    def create(self,request):
        ser=BookDetailsSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'book details updated in db'})
        return Response(ser.errors)


    def partial_update(self,request,pk=None):
        book=BookDetails.objects.get(id=pk)
        ser=BookDetailsSerializer(book,request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'book details updated in db'})
        return Response(ser.errors)

    def update(self,request,pk=None):
        book=BookDetails.objects.get(id=pk)
        ser=BookDetailsSerializer(book,request.data)
        if ser.is_valid():
            ser.save()
            return Response({'msg':'book details updated in db'})
        return Response(ser.errors)

    def delete(self,request,pk=None):
        book=BookDetails.objects.get(id=pk)
        book.delete()
        return Response({'msg':'book deleted from db'})