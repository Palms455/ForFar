from rest_framework.views import APIView
from django.http import JsonResponse
from checks.models import Printer, Check
#from checks.models import CheckSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
import json


# Create your views here.

class GetOrder(APIView):
	permission_classes = (AllowAny,)

	def post(self, request):
		order = json.loads(request.body.decode())
		all_printers = Printer.objects.filter(point_id=order['point_id'])
		if not all_printers:
			return JsonResponse({'error': "Для данной точки не настроено ни одного принтера"}, status=400)
		if Check.objects.filter(order__id=order['id']).exists():
			return JsonResponse({'error': "Для данного заказа уже созданы чеки"}, status=400)
		for printer in all_printers:
			new_check = Check.objects.create(printer_id=printer.id, check_type=printer.check_type, order=order)
		return JsonResponse({'ok' : "Чеки успешно созданы"}, status=201)


class NewCheck(APIView):
	permission_classes = (AllowAny,)

	def get(self, request, api_key):
		printer = Printer.objects.get(api_key=api_key)
		if not printer:
			return JsonResponse({'error': "Не существует принтера с таким api_key"}, status=401)
		checks = printer.checks_set.filter(status=Check.NEW).order_by('id')
		#list_check = CheckSerializer(checks, many=True).data
		return JsonResponse({'checks' : 'list_check'})

class PdfCheck(APIView):
	permission_classes = (AllowAny,)

	def get(self, request, api_key, check_id):
		if not Printer.objects.filter(api_key=api_key).exists():
			return JsonResponse({'error': "Не существует принтера с таким api_key"}, status=401)


	

