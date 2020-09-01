from view.i_view import IView

from window.main_window import MainWindow


class ViewMainWindow(IView):

    def __init__(self):
        super().__init__()
        self.q_main_window = MainWindow()

    def update_view(self, model):
        pass

    def add_controller(self, model):
        pass
