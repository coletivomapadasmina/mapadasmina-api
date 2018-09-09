from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from candidates import views

router = routers.DefaultRouter()

router.register(r'parties', views.PartyViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'pictures', views.PictureViewSet)
router.register(r'candidates', views.CandidateViewSet)
router.register(r'causes', views.CauseViewSet)
router.register(r'gender-identity', views.GenderIdentityViewSet)
router.register(r'ethnicity', views.EthnicityViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
