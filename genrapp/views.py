# from rest_framework.response import Response 
from django.http import HttpResponse
import mimetypes
import os

from django.contrib.auth import authenticate, login, logout 
from django.conf import settings
from .models import *
# from rest_framework.decorators import APIView
# from rest_framework import status
from .models import JobApplication
from django.core.mail import EmailMessage

import requests
from .models import Count


from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *

from django.shortcuts import render, get_object_or_404, redirect

from django.views.decorators.cache import never_cache

from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *

def home(request):
    news = News.objects.all()
    counts = Count.objects.first()
    context ={
    'offer_data': Offer.objects.all(),
    'news':news,
    'counts': counts,
    'rating':CustomerReview.objects.all()
    }
    return render(request,'index.html',context)


def about(request):
    # Retrieve all news and workplace records from the database
    news = News.objects.all()
    work_place = WorkPlace.objects.all()
    
    # Variable to store the success message
    msg = ""
    
    # Check if the request method is POST (i.e., form submission)
    if request.method == 'POST':
        # Create a new instance of CustomerReview
        data1 = CustomerReview()
        
        # Retrieve form data from the POST request
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        company_name = request.POST.get('company_name', '')  # Default to empty string if not provided
        message = request.POST.get('message')
        customer_id = request.POST.get('customer_id')
        review = request.POST.get('rating')

        
        # Assign values to the CustomerReview instance
        data1.full_name = full_name
        data1.email = email
        data1.company_name = company_name
        data1.message = message
        data1.customer_id = customer_id
        data1.rating = review

        
        
        # Save the review to the database
        data1.save()
        
        # Set the success message to be displayed in the template
        msg = "Thanks for your review!"

    # Render the about page with the news, work_place, and msg context
    return render(request, 'about.html', {'news': news, 'work_place': work_place, 'msg': msg,'offer_data': Offer.objects.all()})


def Review_delete(request, id):
    review = CustomerReview.objects.get(id=id)
    review.delete()
    return redirect('dashboard')



def automation(request):
    return render(request,'automation.html',{'offer_data': Offer.objects.all()})

def cold_storage(request):
    return render(request,'cold_storage.html',{'offer_data': Offer.objects.all()})

def contact(request):
    return render(request,'contact.html',{'offer_data': Offer.objects.all()})

def gallery(request):
    return render(request,'gallery.html',{'offer_data': Offer.objects.all()})

def genrsmart(request):
    return render(request,'Genrsmart.html',{'offer_data': Offer.objects.all()})

def project(request):
    return render(request,'project.html',{'offer_data': Offer.objects.all()})



def solar(request):
    return render(request,'solar.html',{'offer_data': Offer.objects.all()})


def workdetails(request):
    return render(request,'workdetails.html',{'offer_data': Offer.objects.all()})



# def home(request):
#     counts = Count.objects.first() 
#     return render(request, 'index.html', {'counts': counts})


def Careers(request):
   careerdata = Career.objects.all()
   context = {
         'careerdata': careerdata,
         'offer_data': Offer.objects.all().distinct()
    }
   return render(request,'careers.html',context)


def job_application_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        job_position = request.POST.get("job_position")
        resume = request.FILES.get("resume")  

        if all([name, email, phone_number, job_position, resume]):  
            job = JobApplication.objects.create(
                name=name,
                email=email,
                phone_number=phone_number,
                job_position=job_position,
                cv=resume
            )

            # Email content
            subject = "New Job Application Received"
            message = f"""
            Name: {name}
            Email: {email}
            Phone: {phone_number}
            Position: {job_position}
            """

            mail = EmailMessage(
                subject,
                message,
                from_email="info@genr.in",
                to=["info@genr.in"],
                reply_to=[email]
            )

            # Attach the uploaded resume
            mail.attach(resume.name, resume.read(), resume.content_type)
            mail.send()

        return redirect("careers")  

    return render(request, "careers.html")

def admin_dashboard(request):
    applications = JobApplication.objects.all()  # Get all job applications
    return render(request, "admin.html", {"applications": applications})




def login(request):
    

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user with the username and password
        user = Login.objects.filter(username=username, password=password)
        
        
        if user:
            request.session["name"] = username
            # login(request,user)

            response = redirect('dashboard')  # Render the login page
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
            
    
            return response

            return redirect('dashboard')  # Redirect to the dashboard page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    else:
       
        if "name" in request.session:
            print("povulladaaa mandddaaaaaaaa",request.session['name'])
            # return HttpResponse('povullladaaaa mandddaaaaaaaa')  
            return redirect('dashboard')

        else:
            print("lloginnnnn")
            response = render(request, 'login.html')  # Render the login page
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
    
            return response
    

    
    

from django.contrib.auth import logout


def logout_view(request):
    if "name" in request.session:
        request.session.pop("name")

        return redirect('login')  # Redirect the user to the login page

    



# Admin Panel

def galleryadd(request):
    if request.method == "POST":
        image= request.FILES.get('galleryimage')
        category = request.POST.get('category')
        addinggalery = Gallery(gallery_image=image,category=category)
        addinggalery.save()
    return redirect('dashboard')  # Replace 'admin_page' with the actual name of your page's URL pattern




def offeradd(request):
    if request.method == "POST":
        banner_title = request.POST.get('bannertitle')
        banner_content = request.POST.get('bannercontent')
        image = request.FILES.get('image')  # Use request.FILES for file uploads

        # Save the data to the model
        addingoffer = Offer(banner_title=banner_title, banner_content=banner_content, image=image)
        addingoffer.save()
    return redirect('dashboard')  # Replace 'admin_page' with the actual name of your page's URL pattern

def careeradd(request):
    if request.method == "POST":
        jobtitle = request.POST.get('jobtitle')
        jobcontent = request.POST.get('jobcontent')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        work_time = request.POST.get('work_time')
        # Save the data to the model
        addingcareer = Career(job_title=jobtitle, job_description=jobcontent, email=email,phone_number=phone_number,work_time=work_time)
        addingcareer.save()
    return redirect('dashboard')  # Replace 'admin_page' with the actual name of your page's URL pattern


def delete_careersection(request, id):
    # Fetch the item using get_object_or_404 for better error handling
    career_item = Career.objects.get(id=id)
        # Delete the gallery item
    career_item.delete()
    # Redirect to a gallery list or success page
    return redirect('dashboard')

def update_careersection(request, id):
    if request.method == 'POST':
        title = request.POST.get('jobtitle')
        content = request.POST.get('jobcontent')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phone')
        worktime = request.POST.get('worktime')

        careerdata = get_object_or_404(Career, id=id)
        
        # Update fields if provided
        if title:
            careerdata.job_title = title
        if content:
            careerdata.job_description = content
        if email:
            careerdata.email = email
        if phonenumber:
            careerdata.phone_number = phonenumber
        if worktime:
            careerdata.work_time = worktime
        careerdata.save()
        
    return redirect('dashboard')  # Redirect after saving








def workadd(request):
    if request.method == "POST":
        # Get the primary work data from the form
        work_title = request.POST.get('title')
        work_category = request.POST.get('browsers')
        thumbnail_img = request.FILES.get('thumbnail_img')  # Use request.FILES for file uploads
        description = request.POST.get('description')

        # Save the primary work object
        addwork = Our_Works(title=work_title, work_category=work_category, thumbnail_img=thumbnail_img, description=description)
        addwork.save()

        # Handle multiple additional images
        additional_images = request.FILES.getlist('additional_images')  # Use `getlist` to handle multiple files
        for image in additional_images:
            Addiotional_work_images.objects.create(work=addwork, image=image)

        return redirect('dashboard')  # Replace 'showoffer' with the actual name of your page's URL pattern

    return redirect('dashboard')  # Redirect if method is not POST







def work_details(request,work_id):
    work_detail = Our_Works.objects.get(id=work_id)
    context = {
        'works':work_detail
    }
    return render(request, 'work_details.html',context)


def request_service(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('services')
        message = request.POST.get('message')

        enquiry = Enquiry(
            name = name,
            email = email,
            phone_number = phone,
            services = service,
            message = message,
        )
        enquiry.save()
        messages.success(request, 'Your message has been sent successfully')
        return redirect('request_service')
    
    return render(request, 'Requestserviceform.html')

def Enquiry_delete(request,id):
    enquiry = Enquiry.objects.get(id = id)
    print("the data:",enquiry)
    if enquiry:
        enquiry.delete()
    return redirect('dashboard')




def dashboard(request):
    if "name" in request.session:

        print(request.session["name"],"dashboard anada")
        powerenergy = 'Power & Energy'
        powerenergyworks = Our_Works.objects.filter(work_category=powerenergy).distinct()

        automation = 'Automation'
        automationworks = Our_Works.objects.filter(work_category=automation).distinct()

        coldstorage = 'Cold Storage'
        coldstorageworks = Our_Works.objects.filter(work_category=coldstorage).distinct()

        genrsmart = 'Genr Smart'
        genramartworks = Our_Works.objects.filter(work_category=genrsmart).distinct()

        solarplantadmin = 'solar plants'
        adminsolarplant = Gallery.objects.filter(category=solarplantadmin).distinct()

        galleryautomation = 'automation'
        automationgallery = Gallery.objects.filter(category=galleryautomation).distinct()

        gallerycoldstorage = 'cold storage'
        coldstoragegallery = Gallery.objects.filter(category=gallerycoldstorage).distinct()

        gallerygenrsmart = 'genr smart'
        genramartgallery = Gallery.objects.filter(category=gallerygenrsmart).distinct()

        admingenerator = 'generator'
        generatoradmin = Gallery.objects.filter(category=admingenerator).distinct()

        additional_work = Addiotional_work_images.objects.all()
        show_news = News.objects.all()
        rating = CustomerReview.objects.all()
        products = Package.objects.prefetch_related('products').all()
        Brands = Product.objects.prefetch_related('package').all()

        


        context={
                'offerdata': Offer.objects.all().distinct(),
                'enquirydata': Enquiry.objects.all(),
                'careerdata': Career.objects.all(),
                'gallery_images': Gallery.objects.all().distinct(),
                'work': Our_Works.objects.all().distinct(),
                'jobs': JobApplication.objects.all().distinct(),
                'contact': ContactForm.objects.all().distinct(),
                'count': Count.objects.all(),
                'brand': Solarpanel.objects.all().distinct(),
                'invertor': Invertor.objects.all().distinct(),
                'packages': Package.objects.all().distinct(),
                'powerenergy': powerenergyworks,
                'automation': automationworks,
                'cold': coldstorageworks,
                'genrsmart': genramartworks,
                'additional_work': additional_work,
                'adminsolarplant': adminsolarplant,
                'galleryautomation': automationgallery,
                'gallerycoldstorage': coldstoragegallery,
                'gallerygenrsmart': genramartgallery,
                'generatoradmin': generatoradmin,
                'news': show_news,
                'rating':rating,
                'invoice': Invoice.objects.all(),
                'products': products,
                'Brands': Brands


            }
        response = render(request, 'admin.html',context)  # Render the login page
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
    
        return response
    
    else:
        print("dashboard allada")
        return redirect('login') 
    


def gallery_page(request):
    galerysolarplant = 'solar plants'
    solarplant = Gallery.objects.filter(category=galerysolarplant).distinct()

    galleryautomation = 'automation'
    automationgallery = Gallery.objects.filter(category=galleryautomation).distinct()

    gallerycoldstorage = 'cold storage'
    coldstoragegallery = Gallery.objects.filter(category=gallerycoldstorage).distinct()

    gallerygenrsmart = 'genr smart'
    genramartgallery = Gallery.objects.filter(category=gallerygenrsmart).distinct()

    gallerygenerator = 'generator'
    generatorgallery = Gallery.objects.filter(category=gallerygenerator).distinct()

    context={
            'gallery_images': Gallery.objects.all().distinct(),
            'solarplant': solarplant,
            'galleryautomation': automationgallery,
            'gallerycoldstorage': coldstoragegallery,
            'gallerygenrsmart': genramartgallery,
            'generatorgallery':generatorgallery,
            'offer_data': Offer.objects.all()
        }
    return render(request, 'gallery.html', context)
    

       
def delete_gallery(request, id):
    # Fetch the item using get_object_or_404 for better error handling
    gallery_item = Gallery.objects.get(id=id)
        # Delete the gallery item
    gallery_item.delete()
    # Redirect to a gallery list or success page
    return redirect('dashboard')

# Function to display the update form with the current data
def update_gallery(request, id):
    gallery_item = get_object_or_404(Gallery, id=id)
    context = {
        'item': gallery_item
    }
    return render(request, 'admin.html', context)

# Function to handle the update operation


def updating_gallery(request, id):
    if request.method == 'POST':
        image = request.FILES.get('galleryimageupdate')  # Correct field name
        category = request.POST.get('categoryupdate')    # Correct field name
        gallery = get_object_or_404(Gallery, id=id)
        
        # Update fields if provided
        if image:
            gallery.gallery_image = image
        if category:
            gallery.category = category
        gallery.save()
        
    return redirect('dashboard')  # Redirect after saving



def delete_offer(request, id):
    offer_item = Offer.objects.get(id=id)
    offer_item.delete()
    return redirect('dashboard')

# Function to handle the update operation

def updating_offer(request, id):
    if request.method == 'POST':  
        offertitle = request.POST.get('offertitle')
        offercontent = request.POST.get('offercontent')
        offerimage = request.FILES.get('offerimage') 

        # Fetch the offer data or return a 404 error
        offerdata = get_object_or_404(Offer, id=id)

        # Update the fields if values are provided
        if offertitle:
            offerdata.banner_title = offertitle
        if offercontent:
            offerdata.banner_content = offercontent  
        if offerimage:
            offerdata.image = offerimage 

        # Save the updated offer object
        offerdata.save()

        # Add a success message (optional)
        messages.success(request, "Offer updated successfully!")

        # Redirect to the offers page
        return redirect('dashboard')

    return redirect('dashboard')  # In case of non-POST request





def delete_works(request, id):
    works_item = Our_Works.objects.get(id=id)
    works_item.delete()
    return redirect('dashboard')





def updating_works(request, id):
    if request.method == 'POST':
        work = get_object_or_404(Our_Works, id=id)

        # Update main work fields
        title = request.POST.get('worktitle')
        category = request.POST.get('workcategory')
        image = request.FILES.get('workimage')
        description = request.POST.get('workdescription')

        if title:
            work.title = title
        if category:
            work.work_category = category
        if image:
            work.thumbnail_img = image
        if description:
            work.description = description
        work.save()

        # Delete selected additional images
        delete_image_ids = request.POST.getlist('delete_images')
        if delete_image_ids:
            Addiotional_work_images.objects.filter(id__in=delete_image_ids).delete()

        # Save new additional images with a limit of 3
        work = get_object_or_404(Our_Works, id=id)
        existing_count = Addiotional_work_images.objects.filter(work=work).count()

        if request.method == 'POST':
            images = request.FILES.getlist('new_images')
            remaining_slots = max(0, 3 - existing_count)

        if remaining_slots == 0:
            messages.error(request, "You can only have up to 3 images for this work.")
            return redirect('dashboard')

        for image in images[:remaining_slots]:
            Addiotional_work_images.objects.create(work=work, image=image)

        messages.success(request, "Images added successfully.")
        return redirect('dashboard')
    return redirect('dashboard')


def addnews(request):
    if request.method == "POST":
        image= request.FILES.get('newsimage')
        desc = request.POST.get('newsdesc')
        name = request.POST.get('newsname')
        date= request.POST.get('newsdate')
        addingnews =News(image=image,description=desc,name=name,date=date)
        addingnews.save()
    return HttpResponseRedirect(reverse('dashboard') + '#news-section')




def delete_news(request, id):
    # Fetch the item using get_object_or_404 for better error handling
    news_item = News.objects.get(id=id)
        # Delete the gallery item
    news_item.delete()
    # Redirect to a gallery list or success page
    return HttpResponseRedirect(reverse('dashboard') + '#news-section')


# Function to display the update form with the current data

def update_news(request, id):
    news_item = get_object_or_404(News, id=id)
    context = {
        'item': news_item
    }
    return render(request, 'admin.html', context)



def update_count(request, id):
    if request.method == 'POST':  
        customers = request.POST.get('happy_customers')
        project =  request.POST.get('project_done')
        expert =  request.POST.get('expert_workers') 


        # Fetch the offer data or return a 404 error
        count_item = get_object_or_404(Count, id=id)

        # Update the fields if values are provided
        if customers:
            customers=int(customers)
            count_item.happy_customers=customers

        if project:
            project=int(project)
            count_item.projects_done=project  
        if expert:
            expert = int(expert)
            count_item.expert_workers=expert

        # Save the updated offer object
        count_item.save()

        # Add a success message (optional)
        messages.success(request, "Offer updated successfully!")

        # Redirect to the offers page
        return HttpResponseRedirect(reverse('dashboard') + '#count-section')


    return HttpResponseRedirect(reverse('dashboard') + '#count-section')





# def career_page(request):
#     careerdata = Career.objects.all()  
#     return render(request, 'your_template.html', {'careerdata': careerdata})


def contact_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        enquiry_type = request.POST.get('enquiry')
        message = request.POST.get('message')

        # Save form data to the database
        ContactForm.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            enquiry_type=enquiry_type,
            message=message
        )

        # Forward data to Web3Forms
        data = {
            "access_key": "7602f21f-477d-4668-8070-0b4e7ae9ae03",
            "name": name,
            "email": email,
            "mobile": mobile,
            "enquiry": enquiry_type,
            "message": message
        }
        response = requests.post("https://api.web3forms.com/submit", data=data)

        # Check if Web3Forms submission was successful
        if response.status_code == 200:
            return redirect('home')  # Redirect to a thank-you page
        else:
            return redirect('home')  # If Web3Forms fails, redirect to home

    return render(request, 'index.html')



def job_delete(request,id):
    job = JobApplication.objects.get(id = id)
    print("the data:",job)
    if job:
        job.delete()
    return HttpResponseRedirect(reverse('dashboard') + '#Career-section')




def contact_delete(request,id):
    contact = ContactForm.objects.get(id = id)
    print("the data:",contact)
    if contact:
        contact.delete()
    return HttpResponseRedirect(reverse('dashboard') + '#contact-section')


# def submit_review(request):
#     reviews = CustomerReview.objects.all()
#     context = {
#         'review': reviews
#     }
#     return render(request, 'about.html', context)



def solarpaneladd(request):
    if request.method == "POST":
        brand = request.POST.get('brand')
        adding = Solarpanel(brand_name = brand)
        adding.save()
    return HttpResponseRedirect(reverse('dashboard') + '#solarpanel-section')

def solarpanel_delete(request,id):
    solarpanel = Solarpanel.objects.get(id = id)
    if solarpanel:
        solarpanel.delete()
    return HttpResponseRedirect(reverse('dashboard') + '#solarpanel-section')


def invertoradd(request):
    if request.method == "POST":
        brand = request.POST.get('brand')
        adding = Invertor(brand_name = brand)
        adding.save()
    return HttpResponseRedirect(reverse('dashboard') + '#invertor-section')

def invertor_delete(request,id):
    invertor = Invertor.objects.get(id = id)
    if invertor:
        invertor.delete()
    return HttpResponseRedirect(reverse('dashboard') + '#invertor-section')

def add_package(request):
    if request.method == 'POST':
        package_name = request.POST.get('package_name')
        price = request.POST.get('price')
        if package_name:
            Package.objects.create(name=package_name,price = price)
    return HttpResponseRedirect(reverse('dashboard') + '#packages-section')

def add_product(request):
    if request.method == 'POST':
        package_id = request.POST.get('package_id')
        product_name = request.POST.get('product_name')

        if package_id and product_name:
            package = Package.objects.get(id=package_id)
            Product.objects.create(name=product_name, package=package)

        return redirect('dashboard')

def add_brand(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        brand_name = request.POST.get('brand_name')

        # Ensure the product exists
        product = get_object_or_404(Product, id=product_id)

        # Create the brand and associate it with the product
        Brand.objects.create(name=brand_name, product=product)

        # Redirect back to the dashboard or wherever you want to show the update
        return redirect('dashboard')


def LoadCalc(request):
    packages = Package.objects.prefetch_related('products__brands').all()
    context = {
        'offer_data': Offer.objects.all(),
        'packages': Package.objects.all().distinct(),
        'brand': Solarpanel.objects.all().distinct(),
        'invertor': Invertor.objects.all().distinct(),
        'packages': packages,
    
    }
    return render(request,'LoadCalc.html',context)

def create_invoice(request):
    if request.method == 'POST':
        solar = request.POST.get('selectedSolarPanel')
        inverter = request.POST.get('selectedInvertor')
        package_id = request.POST.get('selectedPackage')
        details = request.POST.get('packageDetails')

        # Save to DB
        Invoice.objects.create(
            solar_brands=solar,
            invertor_brands=inverter,
            packages=package_id,
            details=details
        )

        return redirect('LoadCalc')  # redirect to a thank you or success page

    return redirect('home') 


def invoice_delete(request, id):
    invoice = Invoice.objects.get(id=id)
    invoice.delete()
    return redirect('dashboard')
