from django.shortcuts import render
from django.views import View
from serviceapp.models import ServiceCategory
from workapp.models import Workers,DirectionCategory,Direction

class MainView(View):
    def get(self, request):
        serviceCat = ServiceCategory.objects.all()
        workers = Workers.objects.all()
        directions = DirectionCategory.objects.all()
        data = {
            'serviceCat': serviceCat,
            'workers':workers,
            'directions':directions
        }
        return render(request,'hubapp/index.html',data)

class InovationView(View):
    def get(self, request):
        
        directions = Direction.objects.filter(category_id=2)

        data = {
            'directions': directions
        }
        return render(request,'hubapp/inovation.html',data)