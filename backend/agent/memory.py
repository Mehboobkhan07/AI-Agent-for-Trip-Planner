class TripMemory():
    def __init__(self):
        self.messages=[]
        self.trip_data={}
    
    def add_message(self,role,content):
        self.messages.append({"role":role,"content":content})

    def update_trip(self, data: dict):
        for key, value in data.items():
            if value:
                self.trip_data[key] = value

    def get_context(self):
        return self.messages