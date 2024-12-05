# calculos/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def calcular_decimo_terceiro(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        salario = float(data.get('salario', 0))
        quantidade_meses = int(data.get('quantidade_meses', 0))
        percentual = float(data.get('percentual', 0))
        integral = data.get('integral', False)
        adiantamento = data.get('adiantamento', False)

        valorTemp = salario / 12

        if integral:
            valor = valorTemp * quantidade_meses
            valor_do_desconto = valor * percentual
            valorIntegral = valor - valor_do_desconto
            return JsonResponse({
                "valor_temporario": valor,
                "valor_do_desconto": valor_do_desconto,
                "valor_a_receber_integral": valorIntegral
            })

        if adiantamento:
            valor = valorTemp * quantidade_meses
            valor_do_desconto = valor * percentual
            parcela_1 = valor / 2
            parcela_2 = parcela_1 - valor_do_desconto
            return JsonResponse({
                "valor_da_primeira_parcela": parcela_1,
                "valor_da_segunda_parcela": parcela_2
            })

    return JsonResponse({"error": "Método não permitido"}, status=405)