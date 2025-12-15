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
            "message": f"{request.user.username} has successfully hired {hire.talent_name}",
            "data" :{
                "id" : hire.id,
                "talent_name": hire.talent_name,
                "talent_location": hire.talent_location,
                "talent_contact": hire.talent_contact,
                "talent_email": hire.talent_email,
                "status": hire.status,
                "hired_at": hire.hired_at,
            }
        },status=201)
        
class UpdateHireStatusView(View):
    def post (self,request,hire_id):
        if not request.user.is_authenticated:
            return JsonResponse({"error":"User is not logged in"},status=401)
        
        new_status = request.GET.get("status")
        if not new_status:
            return JsonResponse({"error":"status query parameter is required"},status=400)
        
        if new_status not in dict(HireModel.STATUS_CHOICES):
            return JsonResponse({"error":"Invalid status value"},status=400)
        
        try:
            hire = HireModel.objects.get(id=hire_id)
        except HireModel.DoesNotExist:
            return JsonResponse({"error":"hire not found"},status=404)
        
        if request.user not in [hire.client,hire.talent]:
            return JsonResponse({"error":"User does not have the permission to update this hire"},status=403)

        if new_status == HireModel.STATUS_COMPLETED and request.user != hire.client:
            return JsonResponse({"error":"Only the client can mark a hire as completed"},status=403)
        
        if not hire.can_transition_to(new_status):
            return JsonResponse({"error":f"hires cannot be updated from {hire.status} to {new_status}"},status=400)
        
        hire.status = new_status
        hire.save()
        
        return JsonResponse({
            "message":f"hire successfully updated to {new_status}",
            "data":{
                "id":hire.id,
                "status":hire.status
            }
        },status = 200)