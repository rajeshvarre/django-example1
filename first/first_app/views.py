from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from first_app.models import Topic,Webpage,AccessRecord
def index(request):
    webpages_list=AccessRecord.objects.order_by('date')
    date_dict={'access_records':webpages_list}
    return render(request, 'first_app/index.html',context=date_dict)
def help(request):
    return render(request,'first_app/help.html')