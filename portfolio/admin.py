from django.contrib import admin

# Register your models here.
from .models import Represent,Detail, Fact, Skill, Resume, Portfolio

class RepresentAdminModel(admin.ModelAdmin):
    list_display=['represent_name']
    
    
    
admin.site.register(Represent, RepresentAdminModel), 
admin.site.register(Detail)
admin.site.register(Fact)
admin.site.register(Skill)
admin.site.register(Resume)
admin.site.register(Portfolio)
