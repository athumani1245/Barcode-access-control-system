from django.urls import path
from .views import view_home,view_report,view_reportweekly,\
            login,logout,admin_custodian_view,addvenue_view,admin_Del_venue_view,deletevenue_view,\
            admin_Del_student_view,admin_Del_staff_view,object_delete,venue_edit,updatevenue_view,visitor_view,\
            addvisitor_view,edit_student,open_list
            

urlpatterns=[
    path('', login, name='frontlogin'),
    path('logindash',login,name='logindash'),
    path('logoutdash',logout,name='logoutdash'),
    path('dashboard', view_home,name='dash'),
    path('report',view_report,name='report'),
    path('reportweekly',view_reportweekly,name='weekly'),
    path('intocustodian',admin_custodian_view,name='custodian'),
    path('venuesaver',addvenue_view,name='venue'),
    path('update_venue',updatevenue_view,name='update_venue'),
    path('venueedit',venue_edit,name = 'object_edit'),
    path('intocustodiandeletion',admin_Del_venue_view,name='deletevenue'),
    path('venuedeleter',deletevenue_view,name='venuedeleter'),
    path('deletestudent',admin_Del_student_view,name='deletestudent'),
    path('deletestaff',admin_Del_staff_view,name='deletestaff'),
    path('delete/(?P<obj_id>[0-9]+)/$',object_delete,name='object_delete'),
    path('edit/(?P<obj_id>[0-9]+)/$',venue_edit,name='object_edit'),
    path('open_link/(?P<obj_id>[0-9]+)/$',open_list,name='open_list'),
    path('visitoradd',visitor_view,name = 'visitoradd'),
    path('addvisitor',addvisitor_view,name='addvisitor'),
    path('edit-student/<str:id>',edit_student,name='edit student data'),
    



]