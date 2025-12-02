from django.http import HttpResponse
from django.template import loader

import food_diary

# Create your views here.

def food_diary_view(request):
    template = loader.get_template("food_diary.html")
    return HttpResponse(template.render({}, request))