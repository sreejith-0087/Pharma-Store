from django.urls import path
from shop import views

app_name="shop"

urlpatterns=[
    path("",views.AllMedicines,name='all_medicines'),
    path("category/<slug:link>",views.AllMedicines,name='by_category'),
    path("shop-single/<int:med_id>",views.MedDetail,name='med_single'),
    path("contact",views.Contact,name='contact'),
    path("about",views.About,name='about'),
    path("search",views.Product_search,name='med_search'),
    path('retailer_profile',views.Retailer_profile,name='retailer_profile'),
    path('feedback/<int:med_id>',views.AddFeedback,name='feedback'),
    path('order_view',views.order_confirmation,name='order_view'),
]