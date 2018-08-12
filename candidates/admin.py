from django.contrib import admin
from .models import Party, Candidate, Role, Picture

admin.site.register(Party)
admin.site.register(Candidate)
admin.site.register(Role)
admin.site.register(Picture)
