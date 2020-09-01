from abc import abstractmethod


class IView:
    @abstractmethod
    def __init__(self):  # create view
        pass

    @abstractmethod
    def update_view(self, model):
        pass

    @abstractmethod
    def add_controller(self, model):
        pass
