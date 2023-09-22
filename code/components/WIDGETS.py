from code.components.Card.FRAME import Creation_of_Cards
from code.components.MENU import Menu_Widgets
from customtkinter import CTkScrollableFrame
from code.config.settings_widgets import *
from code.components.FOOTER import Footer_Widgets
from code.other.modes_app.delete.delete_sell import delete_sell
from code.other.modes_app.delete.delete_prod import delete_prod
from code.other.modes_app.delete.delete_client import delete_client

def widgets(parent, app_mode: str, geometry: tuple, destroy=False):
    if destroy:
        for widget in parent.winfo_children():
            widget.destroy()
            
    Menu_Widgets(parent=parent, destroy=True, geometry=geometry, name='', widgets=widgets, app_mode=app_mode, master=parent).pack(padx=10, pady=10)
    Frame_Card = CTkScrollableFrame(parent, width=geometry[0], height=(geometry[1] - 130))
    Frame_Card.pack(padx=3)
    Footer_Widgets(master=parent, app_mode=app_mode).pack()

    if 'dashboard' in app_mode and '_exp' not in app_mode:
        dashboard_number = Dashboard_Number(0, True)
        Creation_of_Cards(dashboard_number, Frame_Card, app_mode)
        
        dashboard_total = Dashboard_Total(0, True)
        Creation_of_Cards(dashboard_total, Frame_Card, app_mode)
        
        dashboard_lucro = Dashboard_Lucro(0, True)
        Creation_of_Cards(dashboard_lucro, Frame_Card, app_mode)
        
    elif 'dashboard' in app_mode and '_exp' in app_mode:
        dashboard_number = Dashboard_Number(0, False)
        Creation_of_Cards(dashboard_number, Frame_Card, app_mode)
        
        dashboard_total = Dashboard_Total(0, False)
        Creation_of_Cards(dashboard_total, Frame_Card, app_mode)

        dashboard_lucro = Dashboard_Lucro(0, False)
        Creation_of_Cards(dashboard_lucro, Frame_Card, app_mode)
        
    if '_exp' not in app_mode and app_mode != 'dashboard':
        db_data, db_class = app_mode_to_db.get(app_mode, (None, None))
        if db_data and db_class:
            for key, item in db_data.items():
                db_card = db_class(item, True)
                btn_del = Creation_of_Cards(db_card, Frame_Card, app_mode)

    elif '_exp' in app_mode and app_mode != 'dashboard':
        db_data, db_class = app_mode_to_db.get(app_mode, (None, None))
        if db_data and db_class:
            for key, item in db_data.items():
                db_card = db_class(item)
                btn_del = Creation_of_Cards(db_card, Frame_Card, app_mode)
                if 'vendas' in app_mode:
                    btn_del.bind('<Button>', lambda _, key=key: delete_sell(key, widgets, parent, app_mode, geometry, destroy))
                if 'produtos' in app_mode:
                    btn_del.bind('<Button>', lambda _, db_data=item['id'] : delete_prod(db_data, widgets, parent, app_mode, geometry, destroy))
                if 'clientes' in app_mode:
                    btn_del.bind('<Button>', lambda _, key=key: delete_client(key, widgets, parent, app_mode, geometry, destroy))
