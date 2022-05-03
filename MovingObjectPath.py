from position import Position


class moving_object_path:

    # "Type":"MovingObject Path",
    # "WorldTime":"",
    # "SimulationTime":0,
    # "FrameID":0,
    # "VehicleName":"Moving object 0001",
    # "Waypoints":[{"x":"217.076","y":"0.000","z":"30.700"}]},

    def __init__(self, typ: str, world_time: str, simulation_time: int, frame_id: int, vehicle_name: str, waypoints: Position):
        self.typ = typ
        self.world_time = world_time
        self.simulation_time = simulation_time
        self.frame_id = frame_id
        self.vehicle_name = vehicle_name
        self.waypoints = waypoints