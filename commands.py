
REGISTERED_NAMED_ITEMS = {}
REGISTERED_TO_ALL = {}

def register_to_app(app_name, control_lbl, view):
    """ Register a callback based on what app is present """
    REGISTERED_NAMED_ITEMS[app_name] = {'view':view, 'label':control_lbl}

def register_to_model(model, control_lbl, view):
    """ Register a call back based on what model is present """
    REGISTERED_NAMED_ITEMS[model.__name__] = {'view':view, 'label':control_lbl}

def register_to_all(control_lbl, view):
    """ Register an always avaliable command """
    REGISTERED_TO_ALL[control_lbl] = {'view':view, 'label':control_lbl}
