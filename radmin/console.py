
# two dicts to hold all registed callbacks
REGISTERED_NAMED_ITEMS = {}
REGISTERED_TO_ALL = {}

def register_to_all(control_lbl, callback, display_result=False):
    """ Register an always avaliable command """
    REGISTERED_TO_ALL[control_lbl.lower()] = {'callback':callback, 'label':control_lbl, 'display_result':display_result}

def register_to_admin_index(control_lbl, callback, display_result=False):
    """ Register a callback that appears only at the admin index """
    REGISTERED_NAMED_ITEMS['admin_index'] = {'callback':callback, 'label':control_lbl, 'display_result':display_result}

def register_to_app(app_name, control_lbl, callback, display_result=False):
    """ Register a callback based on what app is present """
    REGISTERED_NAMED_ITEMS[app_name.lower()] = {'callback':callback, 'label':control_lbl, 'display_result':display_result}

def register_to_model_list(model, control_lbl, callback, display_result=False):
    """ Register a call back based on what model list is present """
    REGISTERED_NAMED_ITEMS[model.__name__.lower()+"s"] = {'callback':callback, 'label':control_lbl, 'display_result': display_result}

def register_to_model(model, control_lbl, callback, display_result=False):
    """ Register a call back based on what model is present """
    REGISTERED_NAMED_ITEMS[model.__name__.lower()] = {'callback':callback, 'label':control_lbl, 'display_result': display_result}

