from django.contrib import admin
from .models import *


admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Reviews)
admin.site.register(News)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Message)