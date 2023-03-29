from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('adminlogin', views.adminlogin, name='adminlogin'),
    #path('edit', views.edit, name='edit'),
    path('signup', views.signup, name='signup'),
    path('signout',views.signout,name='signout'),
    path('detail',views.detail, name='detail'),
    path('rdetail',views.rdetail, name='rdetail'),
    path('odetail',views.odetail, name='odetail'),
    path('hdetail',views.hdetail, name='hdetail'),
    path('quick',views.quick, name='quick'),
    path('detail2',views.detail2, name='detail2'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('rdashboard',views.rdashboard,name='rdashboard'),
    path('hdashboard',views.hdashboard,name='hdashboard'),
    path('odashboard',views.odashboard,name='odashboard'),
    path('qdashboard',views.qdashboard,name='qdashboard'),
    path('profile',views.profile, name='profile'),
    path('admindash',views.admindash, name='admindash'),
    path('admdonar',views.admdonar, name='admdonar'),
    path('admdonreq',views.admdonreq, name='admdonreq'),
    path('admrecreq',views.admrecreq, name='admrecreq'),
    path('admrec',views.admrec, name='admrec'),
    path('admorg',views.admorg, name='admorg'),
    path('admorgreq',views.admorgreq, name='admorgreq'),
    path('admhos',views.admhos, name='admhos'),
    path('admhosreq',views.admhosreq, name='admhosreq'),
    path('qrec',views.qrec, name='qrec'),
    path('qorg',views.qorg, name='qorg'),
    path('qhos',views.qhos, name='qhos'),
    path('dsearch',views.dsearch, name='dsearch'),
    path('admin_home/',views.admin_home,name="admin_home"),
    ] 