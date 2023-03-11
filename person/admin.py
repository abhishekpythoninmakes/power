from django.contrib import admin

# Register your models here.
from person.models import City, District, Person

admin.site.register(City)
admin.site.register(District)
admin.site.register(Person)