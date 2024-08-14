import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from .models import Update
from .mixins import JsonResponseMixin
from django.core.serializers import serialize 

# def detail_view(request):
#     # return HttpResponse(get_template().render({}))
#     return render(request, template.html, {})    -- return JSON DATA

def Json_example_view(request):
    data = {"count": 1000, "content": "Some new content"}
    # return JsonResponse(data)
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

class JsonCBV(View):
    def get(self, request, *args, **kwargs): 
        data = {"count": 1000, "content": "Some new content"}
        return JsonResponse(data)
    
class JsonCBV2(JsonResponseMixin, View):
    def get(self, request, *args, **kwargs):
        data = {"count": 1000, "content": "Some new content"}
        return self.render_to_json_response(data)

class SerializedDetailView(View):
    def get(self, request, *args, **kwargs):
        obj = Update.objects.get(id=1)
        json_data = obj.serialize() 
        # data = {"user": obj.user.username, "content": obj.content}
        # json_data = json.dumps(data)
        return HttpResponse(json_data, content_type='application/json')
    
class SerializedListView(View):
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        # data = serialize("json", qs, fields=('user', 'content'))
        # print(data)
        json_data = Update.objects.all().serialize()
        data = json_data
        return HttpResponse(data, content_type='application/json')
