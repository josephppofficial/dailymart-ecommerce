from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Contact),
admin.site.register(Registration),
admin.site.register(Cart),
admin.site.register(Checkout)