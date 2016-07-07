from django import template
import json
from django.conf import settings
register = template.Library()

@register.simple_tag(takes_context=True)
def get_admin_context(context):

    ctx = {'location':None, 'param1':None, 'param2':None, 'static':settings.STATIC_URL}
    try:
        context['app_list']
        if len(context['app_list']) > 1:
            # we are at /admin/
            ctx['location'] = 'admin_index'
            return json.dumps(ctx)
        elif len(context['app_list']) == 1:
            #We are at the app index eg: /admin/app/
            ctx['location'] = 'app_index'
            ctx['param1'] = context['app_list'][0]['name'].lower()

            return json.dumps(ctx)

    except KeyError:
        pass

    try:
        # we are in the list view of the model eg: admin/app/model/
        ctx['location']= 'model_list'
        module_name = context['module_name'].lower()
        # django adds an 's' to every model name in this view, so we are gonna
        ctx['param1'] = module_name

        return json.dumps(ctx)

    except KeyError:
        pass

    try:
        # editing a model
        ctx['location']= 'model_edit'
        ctx['param1'] = context['original'].__class__.__name__.lower()
        ctx['param2'] = context['original'].pk
        return json.dumps(ctx)
    except KeyError:
        pass

    return json.dumps(ctx)
