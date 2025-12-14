import json
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.utils import timezone
from django.views import View
from .models import HireModel



class CreateHireView(View):
    def post(self,request,talent_id):
        if not request.user.is_authenticated:
            return JsonResponse({"error":"User is not logged in"},status=401)
        
        try:
            talent = User.objects.get(id=talent_id)
        except User.DoesNotExist:
             return JsonResponse({"error":"Talent not found"},status = 404)

        existing_hire = HireModel.objects.filter(client=request.user,talent=talent,status=HireModel.STATUS_PENDING).exists()

        if existing_hire:
            return JsonResponse({"error": "You already have a pending hire with this talent"}, status=400)
         
        if request.user.id == talent.id:
            return JsonResponse({"error": "You cannot hire yourself"},status=400)
        
        hire = HireModel.objects.create(
            client = request.user,
            talent = talent,
            talent_name = talent.username,
            talent_location = "",
            talent_contact = "",
            talent_email = talent.email,
            status = HireModel.STATUS_PENDING
        )
        
        return JsonResponse({
            "id" : hire.id,
            "talent_name": hire.talent_name,
            "talent_location": hire.talent_location,
            "talent_contact": hire.talent_contact,
            "talent_email": hire.talent_email,
            "status": hire.status,
            "hired_at": hire.hired_at,
        },status=201)