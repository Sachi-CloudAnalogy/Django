import json
from django.views.generic import View
from django.http import HttpResponse
from rest_app.models import Update
from .mixins import CSRFExemptMixin
from rest_app.mixins import HttpResponseMixin

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get(self, request, id, *args, **kwargs):
        obj = Update.objects.get(id=id)
        json_data = obj.serialize()
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data)
    def put(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data)
    def delete(self, request, *args, **kwargs):
        json_data = {}
        return self.render_to_response(json_data, status = 403)
    
class UpdateModelListAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True
    
    def get(self, request, *args, **kwargs):
        qs = Update.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        data = json.dumps({"message": "Unknown data"})
        return self.render_to_response(data, status=400)
    
    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "you can't delete the whole list !!"})
        status_code = 403    # forbidden/not allowed
        return self.render_to_response(data, status=status_code)
        
