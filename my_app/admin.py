from django.contrib import admin

from my_app.models import Fact,SavedFact

# Register your models here.

admin.site.register(Fact)
admin.site.register(SavedFact)