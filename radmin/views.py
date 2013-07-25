from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import simplejson as json
from django.views.decorators.cache import never_cache
from radmin.console import REGISTERED_NAMED_ITEMS, REGISTERED_TO_ALL
from radmin.utils import *

@never_cache
@staff_member_required
def entry_point(request):
    """ This is the entry point for radmin console."""
    if request.is_ajax():
        # grab get params
        location = request.GET.get('location', None) # where we are in the admin site
        param1 = request.GET.get('param1', None) # usually specifics about location, app_name or model_name etc
        param2 = request.GET.get('param2', None) # and additional field, can carry model id

        controls = []
        # first lets do the globally registered controls
        for key,value in REGISTERED_TO_ALL.items():
            controls.append({'label':value['label'],'target':key})

        # check for admin_index stuff
        if location in REGISTERED_NAMED_ITEMS:
            value = REGISTERED_NAMED_ITEMS[location]
            controls.append({'label':value['label'],'target':location, 'data':param2})

        if param1 in REGISTERED_NAMED_ITEMS:
            value = REGISTERED_NAMED_ITEMS[param1]
            controls.append({'label':value['label'],'target':param1, 'data':param2})

        return HttpResponse(json.dumps(controls), mimetype="application/json")

@never_cache
@staff_member_required
def runner(request):
    if request.is_ajax():
        target = request.GET.get('target')
        data = request.GET.get('data', None)
        # now we have to do a look up and see if the target exists in commands dict
        if target in REGISTERED_NAMED_ITEMS:
            console_item = REGISTERED_NAMED_ITEMS[target]
            mod = radmin_import(console_item['callback'])
            if mod:
                try:
                    if data:
                        output = mod(data)
                    else:
                        output = mod()
                    result = {'result':'success', 'output':output, 'display_result':console_item['display_result']}
                except Exception as e:
                    result = {'result':'error', 'output':e, 'display_result':console_item['display_result']}

                return HttpResponse(json.dumps(result), mimetype="application/json")
            else:
                result = {'result':'error', 'output':'No Module Found', 'display_result':console_item['display_result']}
                return HttpResponse(json.dumps(result), mimetype="application/json")

        elif target in REGISTERED_TO_ALL:
            console_item = REGISTERED_TO_ALL[target]
            mod = radmin_import(console_item['callback'])
            if mod:
                try:
                    result = {'result':'success', 'output':mod(),'display_result':console_item['display_result']}
                except Exception as e:
                    result = {'result':'error', 'output':e, 'display_result':console_item['display_result']}
                return HttpResponse(json.dumps(result), mimetype="application/json")
            else:
                result = {'result':'error', 'output':'No Module Found', 'display_result':console_item['display_result']}
                return HttpResponse(json.dumps(result), mimetype="application/json")

        return HttpResponse(json.dumps({'result':'not_found_error'}), mimetype="application/json")


def sample():
    return "Hi there!"
