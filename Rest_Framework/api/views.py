import json
from django.views.generic import View
from django.http import HttpResponse
from rest_app.models import Update as UpdateModel
from rest_app.forms import UpdateModelForm
from .mixins import CSRFExemptMixin
from rest_app.mixins import HttpResponseMixin

class UpdateModelDetailAPIView(HttpResponseMixin, CSRFExemptMixin, View):
    is_json = True

    def get(self, request, id, *args, **kwargs):
        obj = UpdateModel.objects.get(id=id)
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
        qs = UpdateModel.objects.all()
        json_data = qs.serialize()
        return self.render_to_response(json_data)
    
    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = UpdateModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=True) 
            obj_data = obj.serialize()
            return self.render_to_response(obj_data, status=201)   
        if form.errors:    
            data = json.dumps(form.errors)
            return self.render_to_response(data, status=400)
        data = {"message": "Not Allowed"}
        return self.render_to_response(data, status=400)
     
    def delete(self, request, *args, **kwargs):
        data = json.dumps({"message": "you can't delete the whole list !!"})
        status_code = 403    # forbidden/not allowed
        return self.render_to_response(data, status=status_code)
        
