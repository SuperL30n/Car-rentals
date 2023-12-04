from django.urls import path
from base import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.landing_page, name="landing_page"), 
    path('detail/<str:pk>',views.car_detail,name="detail_page"),
    path('cars/payment/<str:pk>', views.payment, name="make_payment"),
    path('verify/',views.verify_payments,name='verify-me'),
    path('cars/dashboard/',views.dashboard, name="dashboard"),
    path('cars/add/',views.add_car,name="add_car"),
    path('login/',views.login_user, name="login_user"),
    path('logout/',views.logout_user, name="logout"),
    path('cars/faqs',views.faq_page, name="faqs"),
    path('cars/feedback', views.feedback_page, name="cusomer_feedback"),
    path('cars/support/', views.customer_support, name="customer_support"),
    path('cars/feedback_success/',views.feedback_success, name="feedback_success")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)