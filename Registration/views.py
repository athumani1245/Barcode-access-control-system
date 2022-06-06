from socket import timeout
from urllib import request
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from numpy import record
from Dashboard.models import People,Record,Custodian,Location
from Registration.models import Student,Staff,Visitor
from django.utils import timezone
import cv2,os
import subprocess
from pyzbar import pyzbar
from pyzbar.pyzbar import decode
import datetime,time
from django.db.models import Q





###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def string_to_id(string):
    info = Location.objects.get(venue_name = string)
    value = info.id
    return value
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def take_IP(var, direction):
    location_id = string_to_id(var)
    location = Location.objects.get(id = location_id)  
    if direction == "leave":
        IP = location.ip_leave
    elif direction == "enter":
        IP = location.ip_enter
    return IP

###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_registration_form(request):
    return render(request, 'registration.html', {})
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def log_in_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = Custodian.objects.get(username=username,password=password)
        if user is not None:
            return redirect("add")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request,'log_in_custodian.html')

###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def scan_view(url):
    #url = "http://192.168.43.38:8080/video"
    cap = cv2.VideoCapture(url)
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame,(0,0),fx=0.50,fy=0.50)
        cv2.putText(frame,"Press q to close camera",(10,10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,100),1)
        text = ''
        barcodes = pyzbar.decode(frame)
        for barcode in barcodes:
            (x,y,w,h) = barcode.rect
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),1)
            barcodeData = barcode.data.decode('utf-8')
            text = barcodeData
            cv2.putText(frame,text,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),1)
        cv2.imshow("BACS Scanner", frame)
        cv2.setWindowProperty("BACS Scanner", cv2.WND_PROP_TOPMOST,1)
        if cv2.waitKey(1)==ord('q') or text:
            cap.release()
            cv2.destroyAllWindows()
            break
    return text
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#this method checks for the person occupation
def occupation_view(x):
    checkstudent = Student.objects.filter(student_id = x).count()
    checkstaff = Staff.objects.filter(staff_id = x).count()
    checkvisitor = Visitor.objects.filter(visitor_id = x).count()
    #check if the person is a member of the institute
    if checkstudent == 1:
        chaguo = Student.objects.get(student_id=x)
        option= '1'
    elif checkstaff == 1:
        chaguo = Staff.objects.get(staff_id=x)
        option= '2'
    elif checkvisitor == 1:
        chaguo = Visitor.objects.get(visitor_id=x)
        option= '3'    
    return chaguo
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def view_scan_home(request):
    location = Location.objects.all()
    
    context={
    'actual':location,

    }
    return render(request, 'scan_home.html', context)
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#this view is responsible for scanning on the entry door of the premises
def entry_view(request):
    IP = take_IP("Pool","enter")
    info = scan_view(IP)
    checkwatu = Record.objects.filter(record_id = info,time_out = None).count()
    checkstudent = Student.objects.filter(student_id = info).count()
    checkstaff = Staff.objects.filter(staff_id = info).count()
    checkvisitor = Visitor.objects.filter(visitor_id = info).count()
    #check if the person is a member of the institute
    if checkwatu == 1:
        context={
        'heading': 'ACCESS DENIED',
        'message': "The person with ID number "+info+" is Already Inside"
        }
        return render(request,'information.html',context)
    else:
        if checkstudent == 1:
            chaguo = Student.objects.get(student_id=info)
            now_time=datetime.datetime.now().time()
            now_time=format(now_time,'%H:%M')
            now_date=datetime.datetime.now().date()
            poolrecord = Record.objects.create(record_id=chaguo.student_id,last_name=chaguo.last_name,occupation='student',venue_name='Pool',today_date=now_date,time_in=now_time)
            poolrecord.save()
            
            return render(request,'entry_detail.html',{'reg':chaguo, 'picha': chaguo.pic ,'message':'WELCOME',"occupation":'Student' })
        elif checkstaff == 1:
            chaguo = Staff.objects.get(staff_id=info)
            now_time=datetime.datetime.now().time()
            now_time=format(now_time,'%H:%M')
            now_date=datetime.datetime.now().date()
            poolrecord = Record.objects.create(record_id=chaguo.staff_id,last_name=chaguo.last_name,occupation='staff',venue_name='Pool',today_date=now_date,time_in=now_time)
            poolrecord.save()
            return render(request,'entry_detail.html',{'reg':chaguo, 'picha': chaguo.pic ,'message':'WELCOME',"occupation":'Staff' })
        elif checkvisitor == 1:
            chaguo = Visitor.objects.get(visitor_id=info)
            now_time=datetime.datetime.now().time()
            now_time=format(now_time,'%H:%M')
            now_date=datetime.datetime.now().date()
            poolrecord = Record.objects.create(record_id=chaguo.visitor_id,last_name=chaguo.last_name,occupation='visitor',venue_name='Pool',today_date=now_date,time_in=now_time)
            poolrecord.save()
            return render(request,'entry_detail.html',{'reg':chaguo,'message':'WELCOME',"occupation":'Visitor' })
        else:
            context={
            'heading':'SORRY YOUR DETAILS ARE NOT FOUND',
            'message':'Seems you are not a member of the institute',
            }
            return render(request,'information.html',context)

   
       # waturecord=People.objects.create(personal_id=info,occupation=option,last_name=chaguo.last_name,first_name=chaguo.first_name )
        #waturecord.save()
       

###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#this view is responsible for the people to scan when they are in the pool
def move_to_view(request):
    venue = request.GET['v']
    IP = take_IP(venue,"enter")
    info = scan_view(IP)
    checkpool = Record.objects.get(record_id = info,venue_name = "Pool",time_out=None)
    if checkpool:
        checkstudent = Student.objects.filter(student_id = info)
        checkstaff = Staff.objects.filter(staff_id = info)
        checkvisitor = Visitor.objects.filter(visitor_id = info)
        if checkstudent:
            chaguo = Student.objects.get(student_id=info)
            now_time=datetime.datetime.now().time()
            now_time=format(now_time,'%H:%M')
            now_date=datetime.datetime.now().date()
            mturecord = Record.objects.create(record_id=chaguo.student_id,last_name=chaguo.last_name,occupation='student',venue_name=venue,today_date=now_date,time_in=now_time)
            mturecord.save()
            depart= Record.objects.get(record_id = info,venue_name = "Pool",time_out=None)
            depart.time_out=now_time
            depart.save();
            context = {
            'reg' : info,
            'from': 'Pool',
            'to' : venue,
            'time':now_time,
            
            }
            return render(request, 'moving_detail.html',context)
        elif checkstaff:
            chaguo = Staff.objects.get(staff_id=info)
            now_time=datetime.datetime.now().time()
            now_time=format(now_time,'%H:%M')
            now_date=datetime.datetime.now().date()
            mturecord = Record.objects.create(record_id=chaguo.staff_id,last_name=chaguo.last_name,occupation='staff',venue_name=venue,today_date=now_date,time_in=now_time)
            mturecord.save()
            depart= Record.objects.get(record_id = info,venue_name = "Pool",time_out=None)
            depart.time_out=now_time
            depart.save();
            context = {
            'reg' : info,
            'from': 'Pool',
            'to' : venue,
            'time':now_time,
            
            }
            return render(request, 'moving_detail.html',context)
        elif checkvisitor:
            chaguo = Visitor.objects.get(visitor_id=info)
            now_time=datetime.datetime.now().time()
            now_time=format(now_time,'%H:%M')
            now_date=datetime.datetime.now().date()
            mturecord = Record.objects.create(record_id=chaguo.visitor_id,last_name=chaguo.last_name,occupation='visitor',venue_name=venue,today_date=now_date,time_in=now_time)
            mturecord.save()
            depart= Record.objects.get(record_id = info,venue_name = "Pool",time_out=None)
            depart.time_out=now_time
            depart.save();
            context = {
            'reg' : info,
            'from': 'Pool',
            'to' : venue,
            'time':now_time,
            
            }
            return render(request, 'moving_detail.html',context)

        else:
            context={
            'heading': 'ACCESS DENIED',
            'message': "Only Outside venue members are allowed in"
            }
            return render(request,'information.html',context)
    else :
        context={
        'heading': 'ACCESS DENIED',
        'message': "Only Outside members are allowed in"
        }
        return render(request,'information.html',context)
   
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def check_leave(venue):
    venue = request.GET['v']
    IP = take_IP(venue,"leave")
    #take = scan_view(IP)
    take = scan_view("http://192.168.43.1:8080/video")
    checkvenue = People.objects.filter(personal_id = take, venue_name = string_to_id(venue)).count()
    if checkvenue == 1 :
        mtu = People.objects.get(personal_id=take)
    else:
        not_allowed = "Not"
        return not_allowed
    context = {
    'mtu' : mtu,
    'venue':venue,
    'take':take
    }
    return context
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
def leave_from_view(request):
    venue = request.GET['v']
    IP = take_IP(venue,"leave")
    take = scan_view(IP)
    checkmtu = Record.objects.filter(record_id =take,venue_name = venue,time_out=None)
    
    #mturecord = People.objects.get(personal_id = take)
    
    if checkmtu!=0:
                
        now_time=datetime.datetime.now()
        now_date=datetime.datetime.now().date()
        depart= Record.objects.get(record_id = take,venue_name = venue,time_out=None)
        depart.time_out=now_time
        depart.save();
        vpool=Record.objects.create(record_id=take,venue_name="Pool",last_name=depart.last_name,occupation=depart.occupation,time_in=now_time,today_date=now_date)
        vpool.save()
        context = {
            'reg' : take,
            'from': venue,
            'to' : 'Pool',
            'time':now_time,
    
            }
        return render(request, 'moving_detail.html',context)
       
    else:
        context={
                'heading': 'ACCESS DENIED',
                'message': "You not inside of this venue"
                }
        return render(request,'information.html',context)

        
     
   
    
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def departure(request):
    
    IP = take_IP("Pool","leave")
    take = scan_view(IP)
    checkpool = Record.objects.filter(record_id = take,venue_name = "Pool",time_out=None)
    checkvenue = Record.objects.exclude(venue_name='Pool')
    if checkpool:
        now_time=datetime.datetime.now()
        depart= Record.objects.get(record_id = take,venue_name = "Pool",time_out=None)
        depart.time_out=now_time
        depart.save();
        context = {
        'reg' : depart, 
        'message' : 'GOODBYE', 
        'action':'leave'
        }
        return render(request, 'entry_detail.html',context)
       
    elif checkvenue:
        context={
            'heading': 'ACCESS DENIED',
            'message': "it seems like you are inside another vanue"
            }
        return render(request,'information.html',context)

    else:
         context={
            'heading': 'ACCESS DENIED',
            'message': "You are not inside the campus"
            }
         return render(request,'information.html',context)

    
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def register_student_view(request):
    return render(request, 'new-student.html',{})

def addst(request):
    firstname = request.POST['fname']
    lname =request.POST['lname']
    regno =request.POST['reg']
    gender=request.POST['gender']
    program =request.POST['program']
    yrs = request.POST['year']
    pic = request.FILES['pic']
    addstx=Student.objects.create(first_name=firstname,last_name=lname,student_id=regno,gender=gender,programme=program,year=yrs,pic=pic)
    addstx.save()
    return redirect('registerstudent')
###-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def register_staff_view(request):
    return render(request, 'new-staff.html',{})
    
def addstaff(request):
    firstname = request.POST['fname']
    lname =request.POST['lname']
    reg=request.POST['reg']
    gender=request.POST['gender']
    program =request.POST['program']
    pic = request.FILES['pic']
    addstx=Staff.objects.create(first_name=firstname,last_name=lname,staff_id=reg,gender=gender,department=program,pic=pic)
    addstx.save()
    return redirect('registerstaff')