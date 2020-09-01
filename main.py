from PyQt5.QtWidgets import QApplication
import sys
from view.view_main_window import ViewMainWindow
from model.game_model import GameModel


class Game:
    config = None

    def __init__(self):
        # our view
        self.main_view = None

        # our model
        self.model = None

        # our controller
        self.controller = None

    def run(self):
        # initializes the model
        self.model = GameModel()

        # initialize the view with the model
        self.main_view = ViewMainWindow()


if __name__ == "__main__":
    launch = Game()
    app = QApplication(sys.argv)
    launch.run()

    sys.exit(app.exec_())
