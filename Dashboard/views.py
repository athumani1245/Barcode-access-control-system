from audioop import reverse
import datetime
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.shortcuts import render, redirect
import datetime,time
#this part imports from the project views
from Registration.models import Student, Staff, Visitor
from Dashboard.models import People, Record,Location


###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user:
            auth.login(request,user)
            return redirect("/Dashboard/dashboard")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/logindash')
    else:
        return render(request,'log_in_admin.html')
###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def logout(request):
    auth.logout(request)
    return redirect('logindash')

###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_home(request):
    if request.user.is_authenticated:    
        location = Location.objects.all()
        count_total = Record.objects.filter(time_out = None).count()
        stu_total = Record.objects.filter(occupation = "Student", time_out = None).count()
        sta_total = Record.objects.filter(occupation = "Staff", time_out = None).count()
        vis_total = Record.objects.filter(occupation = "Visitor", time_out = None).count()
        #the list below takes all the counts of the venues
        no_location = []
        no  = []
        stu = []
        sta = []
        vis = []
        cap=[]
        taker = 0
        for i in location:
            no_location.append(taker)
            taker = taker + 1
            no.append(Record.objects.filter(venue_name = i.id).count())
            stu.append(Record.objects.filter(venue_name = i.id, occupation = 1).count())
            sta.append(Record.objects.filter(venue_name = i.id, occupation = 2).count())
            vis.append(Record.objects.filter(venue_name = i.id, occupation = 3).count())
            cap.append(i.capacity)
        
        context = {
        'total_count':count_total,
        'total_student':stu_total,
        'total_staff':sta_total,
        'total_visitor':vis_total,
        'count': no,
        'limit':no_location,
        'location':location,
        'student':stu,
        'staff':sta,
        'visitor':vis,
        'cap':cap

         }
        return render(request, 'Dash.html', context)
    else:
        return redirect('logindash')

###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def open_list(request,obj_id):
    venue=Location.objects.get(id=obj_id)
    loc=location = Location.objects.all()
    members_student=[]
    members_staff=[]
    members_visitors=[]
    members_student=Record.objects.filter(venue_name=obj_id,occupation=1)
    members_staff=Record.objects.filter(venue_name=obj_id,occupation=2)
    members_visitors=Record.objects.filter(venue_name=obj_id,occupation=3)
    idadi = Record.objects.filter(venue_name=obj_id).count()

    context={
    'student':members_student,
    'staff':members_staff,
    'visitor':members_visitors,
    'idadi':idadi,
    'venue':venue,
    'location':loc,
    }
    return render(request, 'list_people.html',context)
###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_report(request):
    if request.user.is_authenticated:
        location=Location.objects.all()
        datetaker = Record.objects.values_list('today_date',flat=True).distinct()
        members = Record.objects.all()
        today = datetime.datetime.now().date()
        no= Record.objects.all().count()    
        
        context={
        'watu' : members,
        'idadi' : no,
        'tarehe': datetaker,
        'location':location
        }
        return render(request, 'report.html', context)
    else:
        return redirect('logindash')
###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_reportweekly(request):
    if request.user.is_authenticated:
        datetaker = Record.objects.values_list('today_date',flat=True).distinct()
        members = Record.objects.all()
        #before = datetaker[0]
        #after=datetaker[2]
        no= Record.objects.all().count()
        loc = Location.objects.all()

        ###this part is for the bar chart
        student = Student.objects.all().count()
        staff = Staff.objects.all().count()
        visitor = Visitor.objects.all().count()
        day=datetime.datetime.now()
        name_of_day=day.strftime("%A")
        
        context={
        'v':loc,
        'watu' : members,
        #'after_date': after,
        #'before_date':before,
        'idadi' : no,  
        'tarehe': datetaker,
        'stu':student,
        'sta':staff,
        'vis':visitor,
        'day':name_of_day
        }
        return render(request, 'reportweekly.html',context)
    else:
        return redirect('logindash')
def beforetaker():
    takebefore = request.POST['datefrom']
    return takebefore
def aftertaker():
    takeafter = request.POST['dateto']
    return takeafter
###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
def addvenue_view(request):
    name = request.POST['Vname']
    capacity=request.POST['Vcapacity']
    ipenter=request.POST['ip_enter']
    ipleave=request.POST['ip_leave']
    addv=Location.objects.create(venue_name=name,capacity=capacity,ip_enter=ipenter,ip_leave=ipleave)
    addv.save()
    return redirect('custodian')
###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
def updatevenue_view(request):
    idtaker = request.POST['id']
    updatevalue = Location.objects.get(pk=idtaker)
    updatevalue.venue_name = request.POST['Vname']
    updatevalue.capacity=request.POST['Vcapacity']
    updatevalue.ip_enter=request.POST['ip_enter']
    updatevalue.ip_leave=request.POST['ip_leave']
    updatevalue.save()
    return redirect('deletevenue')
###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def admin_custodian_view(request):
    if request.user.is_authenticated:
        return render(request,'CustodianPanel_addvenue.html')
    else:
        return redirect('logindash')

###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
def deletevenue_view(request):
    addv=Location.objects.create(venue_name=name,capacity=capacity,initial=initial)
    addv.save()
    return redirect('custodian')
###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def admin_Del_venue_view(request):
    if request.user.is_authenticated:
        location = Location.objects.all()
        context={
        'location':location,
        }
        return render(request,'CustodianPanel_deletevenue.html',context)
    else:
        return redirect('logindash')
###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def venue_edit(request,obj_id):
    object = Location.objects.get(id=obj_id)
    context={
    'id':obj_id,
    'name':object.venue_name,
    'capacity':object.capacity,
    'enter':object.ip_enter,
    'leave':object.ip_leave,
    }
    return render(request,'CustodianPanel_editvenue.html',context)

###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def admin_Del_student_view(request):
    if request.user.is_authenticated:
        student_list = Student.objects.all()
        context={
        'location':student_list,
        }
        return render(request,'CustodianPanel_deletestudent.html',context)
    else:
        return redirect('logindash')
###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def admin_Del_staff_view(request):
    if request.user.is_authenticated:
        student_list = Staff.objects.all()
        context={
        'location':student_list,
        }
        return render(request,'CustodianPanel_deletestaff.html',context)
    else:
        return redirect('logindash')
###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def object_delete(request,obj_id = None):
    object = Location.objects.get(id=obj_id)
    object.delete()
    return redirect('deletevenue')
###--------------------------------------------------------------------------------------------------------------------------------------------------------
def visitor_view(request):
    if request.user.is_authenticated:
        v = Location.objects.all()
        context = {
            'venue':v
        }
        return render(request,'new-visitor.html', context)
    else:
        return redirect('logindash')
###--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    
def addvisitor_view(request):
    fname = request.POST['fname']
    lname=request.POST['lname']
    mob=request.POST['contact']
    venue=request.POST['venue']
    reason=request.POST['reason']
    v_id=request.POST['reg']
    anchor=request.POST['reg2']

    addvisitor=Visitor.objects.create(first_name=fname,last_name=lname,visitor_id=v_id,contact=mob,reason=reason,go_to=venue,anchor_id=anchor)
    addvisitor.save()
    return redirect('visitoradd')
###------------------------------------------------------------------------------------------------------
def edit_student(request,id):
    std=Student.objects.get(id=id)
    context={'std':std}
    return render(request,'edit-student.html',context)