from position import Position


class anchor:

    def __init__(self, t: str, world_time: str, simulation_time: float, frame_id: int, anchors: list):
        self.typ = t
        self.world_time = world_time
        self.simulation_time = simulation_time
        self.frame_id = frame_id
        self.anchors = anchors
