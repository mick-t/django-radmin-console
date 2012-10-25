from django.http import HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.utils import simplejson as json
from radmin.commands import REGISTERED_NAMED_ITEMS, REGISTERED_TO_ALL
from radmin.utils import *

@staff_member_required
def entry_point(request):
    """ This is the entry point for radmin console."""
    if request.is_ajax():
        controls = []
        # first lets do the globally registered controls
        for key,value in REGISTERED_TO_ALL.items():
            controls.append({'label':value['label'],'target':key})

        # we need to make sure we are in the right context before we display these
        # methods
        for key,value in REGISTERED_NAMED_ITEMS.items():
            controls.append({'label':value['label'],'target':key})

        return HttpResponse(json.dumps(controls), mimetype="application/json")
