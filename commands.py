
REGISTERED_NAMED_ITEMS = {}
REGISTERED_TO_ALL = {}


def register_to_all(control_lbl, callback):
    """ Register an always avaliable command """
    REGISTERED_TO_ALL[control_lbl.lower()] = {'callback':callback, 'label':control_lbl}

def register_to_app(app_name, control_lbl, callback):
    """ Register a callback based on what app is present """
    REGISTERED_NAMED_ITEMS[app_name.lower()] = {'callback':callback, 'label':control_lbl}

def register_to_model(model, control_lbl, callback):
    """ Register a call back based on what model is present """
    REGISTERED_NAMED_ITEMS[model.__name__.lower()] = {'callback':callback, 'label':control_lbl}

