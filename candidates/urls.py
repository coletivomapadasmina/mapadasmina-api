"""mapadasminas_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from candidates import views

urlpatterns = [
    url(r'^candidates$', views.CandidateList.as_view()),
    #url(r'^roles$', views.role_list),
    #url(r'^pictures$', views.picture_list),
    #url(r'^parties$', views.party_list),
    url(r'^candidates/(?P<pk>[0-9]+)/$',  views.CandidateDetail.as_view()),
]