from rest_framework.decorators import api_view
from django.http import JsonResponse
from checks.models import Printer, Check

# Create your views here.


@api_view(['POST'])
def get_order(request):
	order = json.loads(request.body.decode())
	all_printers = Printer.objects.filter(point_id=order['point_id'])
	if Check.objects.filter(order__id=order['id']).exists():
		return JsonResponse({'error': "Для данного заказа уже созданы чеки"}, status=400)
	if not all_printers:
		return JsonResponse({'error': "Для данной точки не настроено ни одного принтера"}, status=400)


	

