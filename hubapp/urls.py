from django.urls import path,include
from .views import MainView,InovationView

urlpatterns = [
    path('',MainView.as_view(),name="mainView"),
    path('inovation/',InovationView.as_view(),name="inovationView"),
    path('news/',include(('newsapp.urls','news'))),
    path('service/',include(('serviceapp.urls','service'))),
    # path('shop/',include(('shopapp.urls','shop'))),
    path('work/',include(('workapp.urls','work')))
]