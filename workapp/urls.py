from django.urls import path
from .views import WorkerDetail

urlpatterns = [
    path('workers/<int:pk>',WorkerDetail.as_view(),name="worker-detail")
]