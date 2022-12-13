from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from shop.iris_model import IrisModel


@api_view(['POST'])
@parser_classes([JSONParser])
def iris(request):
    user_info = request.data
    SepalLengthCm = user_info['SepalLengthCm']
    SepalWidthCm = user_info['SepalWidthCm']
    PetalLengthCm = user_info['PetalLengthCm']
    PetalWidthCm = user_info['PetalWidthCm']
    print(f'넘어온 데이터 {user_info}')
    print(f'SepalLengthCm : {SepalLengthCm}')
    print(f'SepalWidthCm : {SepalWidthCm}')
    print(f'PetalLengthCm : {PetalLengthCm}')
    print(f'PetalWidthCm : {PetalWidthCm}')
    return JsonResponse({'Response Test' : 'SUCCESS'})