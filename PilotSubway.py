
class Station:
    name = ""
    location = []
    id = 0

    def __init__(self,name,location):
            self.name = name
            self.location = location
    def __init__(self,name):
            self.name = name
            self.location = [0,0]
    def __init__(self):
            #self.name = name
            self.location = [0,0]
    def __str__(self):
            return f"Name: {self.name} Location: X[{self.location[1]}] Y[{self.location[2]}]"
       

class Subway:
    """
        in reality a subway has many stations 
        so there should be a list of Stations
        instead of just a single one , but...
        let's take this as an example    
    """
    Station = object()
    Stations = []
    def __init__(self,Station):
        self.Station = Station

class Passanger:
        id = 0
        valance = 0.00
        in_a_trip = False
    
    
        

def T():
    station = Station()
    station.name = "Jardines"
    station.location = [290123,192919]
    sub = Subway(station)

T()

      