# calculos/views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def calcular_decimo_terceiro(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        salario = float(data.get('salario', 0))
        mesesTrabalhados = int(data.get('mesesTrabalhados', 0))
        taxaPercentual = float(data.get('taxaPercentual', 0))
        taxaPercentual = taxaPercentual / 100.0
        isIntegral = data.get('isIntegral', False)

        valorTemp = salario / 12

        if isIntegral:
            valor = valorTemp * mesesTrabalhados
            valor_do_desconto = valor * taxaPercentual
            valorIntegral = valor - valor_do_desconto
            return JsonResponse({
                "valor_temporario": valor.__round__(2),
                "valor_do_desconto": valor_do_desconto.__round__(2),
                "valor_a_receber_integral": valorIntegral.__round__(2)
            })

        else:
            valor = valorTemp * mesesTrabalhados
            valor_do_desconto = valor * taxaPercentual
            parcela_1 = valor / 2
            parcela_2 = parcela_1 - valor_do_desconto
            return JsonResponse({
                "valor_da_primeira_parcela": parcela_1.__round__(2),
                "valor_da_segunda_parcela": parcela_2.__round__(2)
            })

    return JsonResponse({"error": "Método não permitido"}, status=405)
