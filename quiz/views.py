from django.http import JsonResponse
from .models import Ranking

def salvar_ranking(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        pontos = int(request.POST.get('pontos'))

        ranking = Ranking(nome=nome, pontos=pontos)
        ranking.save()

        return JsonResponse({'status': 'sucesso'})
