from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.

class Our_Products(models.Model):
    name = models.CharField(max_length=25, blank=False)
    company_name = models.CharField(max_length=50,blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name
    

class Gallery(models.Model):
    gallery_image = models.ImageField(upload_to='gallery', null=True, blank=True)
    data = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=20)

class Offer(models.Model):
    banner_title = models.CharField(max_length=25, default="Our Offers")
    banner_content = models.TextField(blank=True)
    image = models.ImageField(upload_to='offer')

class Our_Works(models.Model):
    title = models.CharField(max_length=25)
    work_category = models.CharField(max_length=25)
    thumbnail_img = models.ImageField(upload_to='works')
    description = models.TextField()

    def __str__(self):
        return self.title

class Addiotional_work_images(models.Model):
    work = models.ForeignKey(Our_Works,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='works')



class Enquiry(models.Model):
        name = models.CharField(max_length=25, blank=False)
        email = models.EmailField()
        phone_number = models.CharField(max_length=10, blank=False)
        services = models.CharField(max_length=225,blank=False)
        message = models.TextField()

        @property
        def display_name(self):
            label = "Enquiry" 
            return f"{label}: {self.services}"
        
        def __str__(self):
            return self.display_name
        

class Career(models.Model):
    job_title = models.CharField(max_length=25, blank=False)
    job_description = models.CharField(max_length=225,blank=False)
    work_time = models.TextField()
    email = models.EmailField()
    phone_number = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.job_title
        

class JobApplication(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    job_position = models.CharField(max_length=255)
    cv = models.FileField(upload_to='resumes/')

    def __str__(self):
        return self.name


class ContactForm(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    enquiry_type = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class News(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=False, blank=False)
    date = models.CharField(max_length=50)
    image = models.ImageField(upload_to='news')


    def __str__(self):
        return self.name
    
class Login(models.Model):
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        # Only hash if not already hashed
        if not self.password.startswith('pbkdf2_'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class Count(models.Model):
    happy_customers = models.IntegerField(default=0)
    projects_done = models.IntegerField(default=0)
    expert_workers = models.IntegerField(default=0)

    def __str__(self):
        return "Counts Data"
    
class WorkPlace(models.Model):
    WorkPlace = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.WorkPlace


class CustomerReview(models.Model):
    full_name = models.CharField(max_length=25)
    email = models.EmailField()
    customer_id = models.CharField(max_length=15, blank=True, null=True)
    work = models.CharField(max_length=100, blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()

    # Star rating field
    rating = models.DecimalField(
        max_digits=2,  # Allow ratings up to 99 (e.g., 5.0, 4.5, etc.)
        decimal_places=1,  # For half-star ratings (e.g., 4.5)
        blank=True,  # Optional field (if you want to make it optional)
        null=True,  # Allow null values if the rating is not provided
    )

    def __str__(self):
        return f"{self.full_name} - {self.rating} stars"

   
class Solarpanel(models.Model):
    brand_name = models.CharField(max_length=50)


class Invertor(models.Model):
    brand_name = models.CharField(max_length=50)


    
class Invoice(models.Model):
    solar_brands = models.CharField(max_length=30)
    invertor_brands = models.CharField(max_length=30)
    total_power = models.CharField(max_length=30,blank=True)
    packages = models.TextField()
    details = models.TextField()


class Package(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=100,blank=True) 

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    package = models.ForeignKey('Package', on_delete=models.CASCADE, related_name='products')  


    def __str__(self):
        return f"{self.name} ({self.package.name})"

class Brand(models.Model):
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, related_name='brands', on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.name} - {self.product.name}"