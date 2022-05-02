from position import Position


class vehicle_info:

    # {"Type":"VehicleInfo",
    # "WorldTime":"",
    # "SimulationTime":0,
    # "FrameID":0,
    # "Name":"Ego",
    # "Dimensions":{"x":"2.199","y":"1.728","z":"4.534"}}

    def __init__(self, typ: str, world_time: str, simulation_time: int, frame_id: int, name: str, dimensions: Position):
        self.typ = typ
        self.world_time = world_time
        self.simulation_time = simulation_time
        self.frame_id = frame_id
        self.name = name
        self.dimensions = dimensions
