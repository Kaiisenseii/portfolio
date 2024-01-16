from django.db import models

class Represent(models.Model):
    represent_name = models.CharField(max_length = 100)
    
    def __str__(self):
        return str(self.represent_name)
    
    
class Detail(models.Model):
    name = models.CharField(max_length=254)
    dob = models.DateField()
    website = models.CharField(max_length=254)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length = 254)
    phone = models.IntegerField()
    email = models.EmailField()
    city = models.CharField(max_length=254)
    freelance = models.CharField(max_length=254)

    
    def __str__(self):
        return str(self.name)
    
class Fact(models.Model):
    fact_detail = models.TextField()
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.fact_detail)
    
    
class Skill(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.CASCADE, null = True)
    skill_name = models.CharField(max_length=100, null = True)
    
    def __str__(self):
        return str(self.details)

class Resume(models.Model):
    name_course = models.CharField(max_length = 254)
    year = models.IntegerField()
    name_org = models.CharField(max_length = 254)
    desc = models.CharField(max_length = 254)
    
    def __str__(self):
        return str(self.name_course)

class Portfolio(models.Model):
    port_desc = models.CharField(max_length = 254)
    image = models.ImageField(upload_to="portfolio/")
    
    def __str__(self):
        return str(self.port_desc)
    

    
        
