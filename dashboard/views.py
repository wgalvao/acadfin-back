# # dashboard/views.py

# from django.http import JsonResponse
# from clientes.models import Cliente
# from empresas.models import Empresa
# from funcionarios.models import Funcionario
# from fornecedores.models import Fornecedor

# def dashboard_stats(request):
#     total_clientes = Cliente.objects.count()
#     total_empresas = Empresa.objects.count()
#     total_funcionarios = Funcionario.objects.count()
#     total_fornecedores = Fornecedor.objects.count()

#     data = {
#         'total_clientes': total_clientes,
#         'total_empresas': total_empresas,
#         'total_funcionarios': total_funcionarios,
#         'total_fornecedores': total_fornecedores,
#     }

#     return JsonResponse(data)

# dashboard/views.py

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from clientes.models import Cliente
from empresas.models import Empresa
from funcionarios.models import Funcionario
from fornecedores.models import Fornecedor
from django.contrib.auth.models import User

def dashboard_stats(request, user_id):
    user = get_object_or_404(User, id=user_id)

    total_clientes = Cliente.objects.filter(user_id=user_id).count()
    total_empresas = Empresa.objects.filter(user_id=user_id).count()
    total_funcionarios = Funcionario.objects.filter(user_id=user_id).count()
    total_fornecedores = Fornecedor.objects.filter(user_id=user_id).count()

    data = {
        'total_clientes': total_clientes,
        'total_empresas': total_empresas,
        'total_funcionarios': total_funcionarios,
        'total_fornecedores': total_fornecedores,
    }

    return JsonResponse(data)