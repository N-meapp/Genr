from django.urls import path
from . import views
from .views import *
from .views import contact_form



urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('automation',views.automation, name='automation'),
    path('cold_storage',views.cold_storage, name='cold_storage'),
    path('contact/',views.contact, name='contact'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('gallery/',views.gallery_page,name='gallery'),
    path('genrsmart',views.genrsmart, name='genrsmart'),
    path('project',views.project, name='project'),
    path('request_service',views.request_service, name='request_service'),
    path('solar',views.solar, name='solar'),
    path('workdetails',views.workdetails, name='workdetails'),
    path('LoadCalc',views.LoadCalc, name='LoadCalc'),
    path('Careers',views.Careers, name='careers'),
    path('apply/', job_application_view, name='job_application'),
    path('contact_form/', contact_form, name='contact_form'),
    path('addgallery',views.galleryadd,name='addgallery'),
    path('work_deatil/<int:work_id>',views.work_details,name='work_deatil'),
    path('workadd',views.workadd,name='workadd'),
    path('contact',views.contact,name='contact'),
    path('offeradd',views.offeradd,name='offeradd'),
    path('careeradd',views.careeradd,name='careeradd'),

    # Admin Panel
    path('delete_careersection/<int:id>',views.delete_careersection,name='delete_careersection'),
    path('update_careersection/<int:id>/', views.update_careersection, name='update_careersection'),
    path('gallery_delete/<int:id>',views.delete_gallery,name='gallery_delete'),
    path('gallery_delete/<int:id>',views.delete_gallery,name='gallery_delete'),
    path('job_delete/<int:id>/', views.job_delete, name='job_delete'),
    path('contact_delete/<int:id>/', views.contact_delete, name='contact_delete'),

    path('update_gallery/<int:id>/', views.update_gallery, name='update_gallery'),
    path('Enquiry_delete/<int:id>/', views.Enquiry_delete, name='Enquiry_delete'),
    path('offer_delete/<int:id>',views.delete_offer,name='offer_delete'),
    path('updating_offer/<int:id>/', views.updating_offer, name='updating_offer'),
    path('delete_works/<int:id>',views.delete_works,name='delete_works'),
    path('updating_works/<int:id>/', views.updating_works, name='updating_works'),
    path('updating_count/<int:id>/', views.update_count, name='updating_count'),
    path('addnews',views.addnews, name="addnews"),
    path('addsolarpanel',views.solarpaneladd, name="addsolarpanel"),
    path('solarpanel_delete/<int:id>/', views.solarpanel_delete, name='solarpanel_delete'),
    path('invertoradd',views.invertoradd, name="invertoradd"),
    path('invertor_delete/<int:id>/', views.invertor_delete, name='invertor_delete'),
    path('add-package', views.add_package, name='add_package'),
    path('add_product', views.add_product, name='add_product'),
    # path('updating_package/<int:id>/', views.updating_package, name='updating_package'),

    path('Review_delete/<int:id>/', views.Review_delete, name='Review_delete'),
    path('delete_news/<int:id>/', views.delete_news, name='delete_news'),
    path('login/', views.login, name='login'),
    # path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout'),
    # path('submit-review/', views.submit_review, name='submit_review'),

    path('create-invoice/', views.create_invoice, name='create_invoice'),
    path('invoice_delete/<int:id>/', views.invoice_delete, name='invoice_delete'),
    path('add_brand', views.add_brand, name='add_brand'),
    # path('generate_pdf/', views.generate_pdf, name='generate_pdf'),







]
 