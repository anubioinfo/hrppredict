# howdy/urls.py
from django.conf.urls import url
from hrp import views

urlpatterns = [
    url(r'^$', views.add_anc_data, name='add_anc_data'),
    url(r'^hrp/', views.HrpPredict.as_view()),
    #url(r'^add_anc/', views.add_anc_data.as_view()),
    url(r'^add_anc/$', views.add_anc_data, name='add_anc_data'),
]