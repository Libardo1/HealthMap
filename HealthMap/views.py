from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from HealthMap.models import Dataset, Datarow, Region, Polyline, Range
from HealthMap.forms import LookupForm
import json
import urllib
import sys

def HomePage(request):
    empty_dataset = Dataset.objects.get(name='Empty') 
    dataset_id = request.GET.get('id')    # Dataset passed as URL param
    dataset = empty_dataset     # use empty dataset as default

    if dataset_id!=None:
        data = Dataset.objects.filter(id=dataset_id)
        if data:
            dataset = data[0]

    dataset_range = Range.objects.filter(dataset=dataset)
    if not dataset_range:       # establish a default range from the Empty dataset
        # create a list of objects to mimic a dataset range using default range from Empty dataset
        class range_mimic(object):
            def __init__(self, name=None, low=None, high=None, color=None):
                self.name = name
                self.low = low
                self.high = high
                self.color = color

        row = dataset.datarow_set.all().order_by('value')
        dataset_range = []
        default_range = Range.objects.filter(dataset=empty_dataset)
        range_name = ['Low', 'Low-Mid', 'Mid', 'Mid-High', 'High', 'Very High']
        range_elements = 6
        for i in range(range_elements):      # assume legend of 6 elements
            if i==range_elements-1:
                dataset_range.append(range_mimic(name=range_name[i],
                                                                          low=row[row.count()/6*i], 
                                                                          high=row[row.count()-1],
                                                                          color=default_range[i].color))
            else:
                dataset_range.append(range_mimic(name=range_name[i], 
                                                                           low=row[row.count()/6*i],
                                                                           high=row[row.count()/6*(i+1)],
                                                                           color=default_range[i].color))

#    print("Dataset:%s" % dataset.name)
    form = LookupForm()
    context = ({'form': form, 'dataset': dataset, 'Datasets': Dataset.objects.all(), 'dataset_range': dataset_range})
    return render_to_response('index.html', context, context_instance=RequestContext(request))


def LookupRequest(request):
    form = LookupForm(request.POST)
    if form.is_valid():
        data = Dataset.objects.filter(name=form.cleaned_data['autocomplete'])
        if data:
            dataset_chosen = data[0].id
            return redirect('/?id=%s' % dataset_chosen)
        else:
            return redirect('/')
    else:
        print "Form is not valid"

    context = ({'form': form})
    return render_to_response('index.html', context, context_instance=RequestContext(request))
        

def dataset__lookup(request):
    print "In Dataset lookup"
    dataset = Dataset.objects.all()
    results = []
    for data in dataset:
        dataset_dict = {'id':data.id, 'label':data.name, 'value':data.name}
        results.append(dataset_dict)
    return HttpResponse(simplejson.dumps(results),mimetype='application/json')

def dataset_lookup(request):
    try:
        if request.is_ajax():
            q = request.GET.get('term', '')
            data = Dataset.objects.filter(name__icontains = q )[:20]
            print("q:%s  rows:%s" % (q, len(data)))
            results = []
            for d in data:
                data_json = {}
                data_json['id'] = d.id
                data_json['label'] = d.name
                data_json['value'] = d.name
                results.append(data_json)
            return_data = json.dumps(results)
            print("Results: %s" % len(results))
        else:
            return_data = 'fail'
        mimetype = 'application/json'
        return HttpResponse(return_data, mimetype)
    except Exception, e:
        print e












