from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    reset_token = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
class HomePageBanner(models.Model):
    home_page_banner_image = models.ImageField(upload_to='HomePageBanner/Images')
    home_page_banner_text = models.CharField(max_length=200,blank=True, null=True)
    home_page_banner_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.home_page_banner_date
    
class HomePageSubscribeForm(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=120)
    
    def __str__(self):
        return self.name
    
class HomePageTicketsPrice(models.Model):
    price = models.IntegerField()
    def __str__(self):
        return self.price

# class HomePageMeetings(models.Model):
#     meetingsheading = models.CharField(max_length=150)
#     meetingsdescription = models.TextField()
#     meetingsImage = models.ImageField()
    
class CommitteePage(models.Model):
    committe_page_main_heading = models.CharField(max_length=150,blank=True,null=True)
    committe_card_heading = models.CharField(max_length=120,null=True,blank=True)
    committe_card_description = models.TextField()
    committe_card_email = models.EmailField()
    def __str__(self):
        return self.committe_card_heading
    
class SubmissionsPage_Abstracts(models.Model):
    abstracts_heading = models.CharField(max_length=150)
    abstracts_description = models.TextField()
    abstracts_text = models.CharField(max_length=120,blank=True,null=True)
    
    def __str__(self):
        return self.abstracts_heading

class SubmissionsPage_topics(models.Model):
    topic_name = models.CharField(max_length=150,blank=True,null=True)
    def __str__(self):
        return self.topic_name
        
class PresentationType(models.Model):
    presentation_name = models.CharField(max_length=120)
    def __str__(self):
        return self.presentation_name
    
class Topic_of_Interest(models.Model):
    topic_name = models.CharField(max_length=100)
    def __str__(self):
        return self.topic_name
    
class SubmissionsPage_Abstract_Form(models.Model):
    Title_choice = [
        ('Prof.','Prof.'),
        ('Dr.','Dr.'),
        ('Ms.','Ms.'),
        ('Mr.','Mr.'),
        ('Mrs.','Mrs.')
    ] 
    
    title = models.CharField(max_length=100,choices=Title_choice)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    university = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    email = models.EmailField()
    whatsapp_number = models.CharField(max_length=10)
    presentation_type = models.ForeignKey(PresentationType,on_delete=models.CASCADE)
    topic_of_interest =  models.ForeignKey(Topic_of_Interest, on_delete=models.CASCADE)
    title_of_abstract = models.CharField(max_length=200)
    file = models.FileField(upload_to='Submission/submitabstract/File')
    agree = models.BooleanField(default=True)
    def __str__(self):
        return self.first_name


class AgendaPageSpeakers(models.Model):
    speakerphoto = models.ImageField(upload_to='Agenda/Speakers')
    speakername = models.CharField(max_length=150)
    speaker_description = models.CharField(max_length=100)
    speaker_linked_in_link = models.URLField(max_length=200, blank=True, null=True)
    # speaker_qualification_location = models.CharField(max_length=200)
    # speaker_title = models.CharField(max_length=300)
    def __str__(self):
        return self.speakername
    
class Contactpage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    subject = models.CharField(max_length=200)
    message = models.TextField() 

class Country(models.Model):
    country_name = models.CharField(max_length=100)

class Register_Category(models.Model):
    category_name = models.CharField(max_length=100)
    
class Accommodation(models.Model):
    accommodation_name = models.CharField(max_length=200)
    
class No_of_Nights(models.Model):
    night = models.CharField(max_length=50)
      
class RegistrationForm(models.Model):
    Title_choice = [
        ('Prof.','Prof.'),
        ('Dr.','Dr.'),
        ('Ms.','Ms.'),
        ('Mr.','Mr.'),
        ('Mrs.','Mrs.')
    ] 
    title = models.CharField(max_length=50,choices=Title_choice)
    full_name = models.CharField(max_length=100)
    affiliation = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    postal_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    register_category = models.ForeignKey(Register_Category,on_delete=models.CASCADE) 
    accommodation = models.ForeignKey(Accommodation,on_delete=models.CASCADE)
    no_of_nights = models.ForeignKey(No_of_Nights,on_delete=models.CASCADE) 