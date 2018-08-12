from django.contrib import admin
from .models import Party, Candidate, Role, Picture, Ethnicity, GenderIdentity, Cause

admin.site.register(Party)
admin.site.register(Candidate)
admin.site.register(Role)
admin.site.register(Picture)
admin.site.register(Ethnicity)
admin.site.register(GenderIdentity)
admin.site.register(Cause)