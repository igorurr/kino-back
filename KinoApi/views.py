from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import JsonResponse

import json

class MeApiView(CreateView):
    template_name = 'me.html'

    def get(self, request, *args, **kwargs):
        return JsonResponse({"key": "value"})

    def post(self, request, *args, **kwargs):
        return JsonResponse({"key": "value"})