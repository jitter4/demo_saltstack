
__outputter__ = {"run": "txt"}

def __virtual__():
    return 'chesse'

def run():
    return True

def __init__(opts):
    """
    Allow foreign imports if configured to do so
    """
    if opts.get("cheese.allow_foreign", False):
        _enable_foreign_products()