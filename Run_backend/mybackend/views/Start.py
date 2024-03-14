from django.views.decorators.csrf import csrf_exempt
from ..models import Account
from . import account
from django.http import JsonResponse

@csrf_exempt
def get_rank(request):
    if request.method == 'GET':
        user = account.get_user_cache()
        username = user.username
        rank = Account.objects.order_by('score')
        current_rank = rank.filter(username=username).count() + 1
        top_10 = list(rank.values()[:10])  # 转换为列表
        data = {
            "top_10": top_10,
            "current_rank": current_rank
        }
        return JsonResponse(data, status=200)
    return JsonResponse({'error': 'get rank failed'}, status=400)
