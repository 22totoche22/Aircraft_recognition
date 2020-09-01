class GameModel:

    def __init__(self):
        self.points = 0
        self.aircraft = None

    def change_aircraft(self, aircraft):
        self.aircraft = aircraft
