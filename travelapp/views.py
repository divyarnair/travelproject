from django.shortcuts import render
from . models import Place
from . models import Team
# Create your views here.
def demo(request):
     obj=Place.objects.all()
     var=Team.objects.all()
     return render(request,"index.html",{'results':obj,'charge':var})
