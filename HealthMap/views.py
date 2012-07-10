from django.shortcuts import render_to_response
from django.template import RequestContext
from HealthMap.models import Dataset, Datarow, Region, Polyline

def HomePage(request):
    dataset = Dataset.objects.get(name='Empty')
    context = {'dataset': dataset}
    return render_to_response('index.html', context, context_instance=RequestContext(request))
    
