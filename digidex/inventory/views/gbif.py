from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from inventory.models import Species

def species_name_suggestion(request):
    query = request.GET.get('q', '')
    if query:
        results = Species.name_suggest(q=query, limit=20)
        suggestions = [
            {'id': result['taxonID'], 'text': result['vernacularName']} for result in results
        ]
    else:
        suggestions = []
    return JsonResponse({'results': suggestions})

def species_name_lookup(request):
    query = request.GET.get('term', '')
    if query:
        results = Species.name_lookup(q=query, limit=10)
        suggestions = [
            {'id': result.get('taxonID', ''), 'text': result.get('vernacularName', '')} for result in results.get('results', [])
        ]
    else:
        suggestions = []
    return JsonResponse({'results': suggestions})
