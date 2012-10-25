from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import simplejson as json
from radmin.commands import REGISTERED_NAMED_ITEMS, REGISTERED_TO_ALL
from radmin.utils import *

@staff_member_required
def entry_point(request):
    """ This is the entry point for radmin console."""
    if request.is_ajax():
        # grab get params
        location = request.GET.get('location')
        additional = request.GET.get('additional')

        controls = []
        # first lets do the globally registered controls
        for key,value in REGISTERED_TO_ALL.items():
            controls.append({'label':value['label'],'target':key})

        if additional in REGISTERED_NAMED_ITEMS:
            value = REGISTERED_NAMED_ITEMS[additional]
            controls.append({'label':value['label'],'target':additional})

        return HttpResponse(json.dumps(controls), mimetype="application/json")

@staff_member_required
def runner(request):
    if request.is_ajax():
        target = request.GET.get('target')
        # now we have to do a look up and see if the target exists in commands dict
        if target in REGISTERED_NAMED_ITEMS:
            mod = radmin_import(REGISTERED_NAMED_ITEMS[target]['callback'])
            result = mod()
            return HttpResponse(json.dumps(result), mimetype="application/json")

        elif target in REGISTERED_TO_ALL:
            mod = radmin_import(REGISTERED_TO_ALL[target]['callback'])
            result = mod()
            return HttpResponse(json.dumps(result), mimetype="application/json")

        return HttpResponse(json.dumps(result), mimetype="application/json")


def sample():
    return "Hi there!"
