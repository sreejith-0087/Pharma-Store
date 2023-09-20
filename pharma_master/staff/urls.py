from django.urls import path
from . import views

app_name="staff"

urlpatterns=[
    path("",views.StaffDashboard,name="staffdash"),
    path("add-cat",views.AddCategory,name="add_category"),
    path('add-medicine',views.AddMedicine,name="add_medicine"),
    path('all-medicines',views.AllMedicines,name="all_medicines"),
    path('update-medicine/<int:mid>',views.UpdateMedicine,name="update_medicine"),
    path('medicine-detail/<int:mid>',views.MedicineDetail,name="medicine_detail"),
    path('delete-medicine/<int:mid>',views.DeleteMedicine,name="delete_medicine"),
    path('view_profile',views.view_profile,name="view_profile"),
    path('staff_search_results',views.product_search,name='staff_search_results'),
    path('add-wishlist/<int:mid>/<int:count>',views.AddWishlist,name="add_wishlist"),
    path('view-orders',views.ViewOrders,name="view_orders"),
    path('order/<int:id>',views.OrderDetail,name="order_detail"),
]
