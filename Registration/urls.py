from django.urls import path
from .views import view_registration_form,view_scan_home,entry_view,leave_from_view,\
scan_view, register_student_view,addst,departure,move_to_view,log_in_view,register_staff_view,addstaff
from Dashboard.views import visitor_view, addvisitor_view


urlpatterns=[
    path('add',view_registration_form,name='add'),
    path('scanner',view_scan_home,name='home'),
    path('entry',entry_view,name='entry'),
    path('departure_view',departure,name='departure'),
    path('enter', move_to_view, name = 'move_to'),
    path('leave', leave_from_view, name = 'move_from'),
    path('scan_view', scan_view, name="scan"),
    path('registerstudent', register_student_view, name="registerstudent"),
    path('form-saver',addst,name="form-saver"),
    path('registerstaff', register_staff_view, name="registerstaff"),
    path('staffsaver',addstaff,name="staffsaver"), 
    path('login',log_in_view, name = 'login'),
    path('visitoradd',visitor_view,name = 'visitoradd'),
    path('addvisitor',addvisitor_view,name='addvisitor'),
    
]