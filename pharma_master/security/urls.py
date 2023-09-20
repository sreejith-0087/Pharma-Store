from django.urls import path
from security import views

app_name="security"

urlpatterns=[
  path("",views.Home,name="index"),
  path('staff-login',views.StaffLogin,name="staff_login"),
  path('staff-register',views.StaffRegister,name="staff_register"),
  path('staff-logout',views.Logout,name="staff_logout"),

  #path('staff_reg_finish',views.reg_finish,name="staff_reg_finish"),

  path("retailer-reg",views.RetailerRegister,name='retailer_reg'),
  path("retailer-login",views.RetailerLogin,name='retailer_login'),

]
