from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def get_admin_context(context):
    location = None
    print context
    try:
        context['app_list']
        if len(context['app_list']) > 1:
            # we are at /admin/
            location = 'admin_index'
            return location
        elif len(context['app_list']) == 1:
            #We are at the app index
            location =  'app_index-%s' % context['app_list'][0]['name']
            return location
    except KeyError:
        pass

    try:
        # editing a model
        context['original']
        location = context['original'].__class__.__name__
        return location
    except KeyError:
        pass

    try:
        # we are in the list view of the model eg: admin/app/model/
        location = context['module_name']
        return location
    except KeyError:
        pass

    return location
