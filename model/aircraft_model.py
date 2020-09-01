class AircraftModel:

    def __int__(self, name):
        self.name = name
        self.picture = None

    def add_picture(self):
        raise NotImplementedError()
