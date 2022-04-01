# **** run python manage.py runserver on mysite dir
from django.shortcuts import render

from django.http import HttpResponse
import datetime
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def index( request):
    currentDay = datetime.datetime.now()
    #return HttpResponse("Hellooo world. At home")
    return render(request , "index.html", {"today": currentDay})
# Create your views here.
