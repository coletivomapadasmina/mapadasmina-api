from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from candidates import views


router = routers.DefaultRouter()

router.register(r'parties', views.PartyViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'pictures', views.PictureViewSet)
router.register(r'candidates', views.CandidateViewSet)
router.register(r'causes', views.CauseViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]