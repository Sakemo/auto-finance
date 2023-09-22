from code.config.settings import *

class App(ctk.CTk):
    def __init__(self, geometry : tuple):
        super().__init__()
        self.iconbitmap('empty.ico')
        self.geometry(f'{geometry[0]}x{geometry[1]}')
        self.resizable(False, False)
        
        # Define initial mode of app
        self.app_mode = 'dashboard'
        
        # Widgets
        toogle_mode(self, True, geometry, self.app_mode, widgets, self.app_mode)

        # Run app
        self.mainloop()

if __name__ == '__main__':
    App((478,888))