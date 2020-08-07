from django.contrib import admin

from . models import Position, Contestant, User

admin.site.register(Position)
admin.site.register(Contestant)
admin.site.register(User)

# Register your models here.
