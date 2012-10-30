# Radmin utils

def radmin_import(name):
    nspl = name.split(".")
    try:
        m = __import__(name)
    except ImportError:
        try:
            m = __import__(nspl[0])
            for n in name.split(".")[1:]:
                m = getattr(m, n)
        except AttributeError:
            return None
    return m

