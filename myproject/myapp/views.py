from django.http import JsonResponse
from .models import Item
from .serializers import ItemSerializer


def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return JsonResponse({'items': serializer.data})
