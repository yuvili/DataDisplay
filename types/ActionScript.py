class action_script:
    # {"Type":"ActionScript",
    # "WorldTime":"",
    # "SimulationTime":0,
    # "FrameID":0,
    # "ActorName":"EgoCar",
    # "Trigger":{"Script":"SimulationTimeTrigger","SimulationTime":"0"},
    # "Action":{
    #     "Script":"SetXYLocation",
    #     "Position":{"X":"133.8484","Y":"77.71294"},
    #     "RoadSegment":{"RoadID":"16","LaneID":"-1","FirstSectionID":"0","LastSectionID":"0"},
    #     "Orientation":"0"}},

    def __init__(self, typ: str, world_time: str, simulation_time: int, frame_id: int, actor_name: str, trigger: dict,
                 actions: dict):
        self.typ = typ
        self.world_time = world_time
        self.simulation_time = simulation_time
        self.frame_id = frame_id
        self.actor_name = actor_name
        self.trigger = trigger
        self.actions = actions
