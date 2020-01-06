from django.contrib import admin

from .models import Owner, Social_account, About_me, Experience, Skills, Percentage

admin.site.register(Owner)
admin.site.register(Social_account)
admin.site.register(About_me)
admin.site.register(Experience)
admin.site.register(Skills)
admin.site.register(Percentage)
