def dashboard_mode(app_mode : str | None=None):
    pass

def toogle_mode(parent, destroy: bool, geometry : tuple , name : str, widgets,app_mode : str):
    if app_mode != name:
        app_mode = name
    
    parent.title(f'{app_mode}')
    
    widgets(parent, app_mode, geometry, destroy)
    