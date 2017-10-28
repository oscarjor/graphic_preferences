from django.shortcuts import render
from django.http import JsonResponse
from quiz.models import Selection
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.db.models import Count

def index(request):
	context = {}
	return render(request, 'results/results.html', context)

@csrf_exempt
def getresults(request):
        
        stats = Selection.objects.values('image_category').annotate(dcount=Count('image_category'))
        
        statslist = []
        for stat in stats:
            statslist.append({'category':stat['image_category'], 'total':stat['dcount']})
            
        return JsonResponse({'code': 'success', 'stats': statslist}, safe=False)
