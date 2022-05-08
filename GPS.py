from position import Position


class gps:

    # {"Type":"GPS",
    # "WorldTime":"12:58:50.9982520",
    # "SimulationTime":0.0666666701436043,
    # "FrameID":2,
    # "SimulationPosition":{"x":"132.907","y":"77.722","z":"1.817"},
    # "NoisedSimulationPosition":{"x":"132.907","y":"77.722","z":"1.817"},
    # "Latitude":41.740229749826,
    # "Longitude":-116.946502320116,
    # "Altitude":1.8171272277832,
    # "NoisedLatitude":41.740229749826,
    # "NoisedLongitude":-116.946502320116,
    # "NoisedAltitude":1.8171272277832,
    # "Orientation":{"x":"0.037","y":"0.100","z":"0.147"},
    # "Speed":-0.000369598652468994,
    # "Acceleration":{"x":"-0.001","y":"-0.006","z":"1.150"},
    # "PositionInLane":2.40606386796571E-05,
    # "LaneWidth":3.5,
    # "LaneNumber":-1,
    # "NavigationSegment":30,
    # "VelocityLocal3D":{"x":"0.000","y":"-0.002","z":"0.365"},
    # "AngularVelocityLocal3D":{"x":"0.014","y":"0.037","z":"0.000"},
    # "AngularAccelerationLocal3D":{"x":"0.052","y":"0.150","z":"0.000"},
    # "InstanceNumber":176,
    # "OnRoadDirection":true,
    # "RoadSpeedLimit":40.2336006164551,
    # "HeadedTrafficLightDistance":10000,
    # "TargetDistance":10000}

    def __init__(self, t: str, world_time: str, simulation_time: float, frame_id: int, simulation_pos: Position,
                 noised_simulation_position: Position, latitude: float, longitude: float, altitude: float,
                 noised_latitude: float, noised_longitude: float, noised_altitude: float, orientation: Position,
                 speed: float, acceleration: Position,
                 pos_in_lane: int, lane_width: float, lane_number: int, navi_segment: int, velocity_local3D: Position,
                 angular_velocity_local3D: Position, angular_acceleration_local3D: Position, instance_num: int,
                 on_road_direction: bool, road_speed_limit: float, headed_traffic_light_distance:int, target_distance: int):
        self.typ = t
        self.world_time = world_time
        self.simulation_time = simulation_time
        self.noised_simulation_position = noised_simulation_position
        self.frame_id = frame_id
        self.simulation_pos = simulation_pos
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.noised_latitude = noised_latitude
        self.noised_longitude = noised_longitude
        self.noised_altitude = noised_altitude
        self.orientation = orientation
        self.speed = speed
        self.acceleration = acceleration
        self.pos_in_lane = pos_in_lane
        self.lane_width = lane_width
        self.lane_number = lane_number
        self.navi_segment = navi_segment
        self.velocity_local3D = velocity_local3D
        self.angular_velocity_local3D = angular_velocity_local3D
        self.angular_acceleration_local3D = angular_acceleration_local3D
        self.instance_num = instance_num
        self.on_road_direction = on_road_direction
        self.road_speed_limit = road_speed_limit
        self.headed_traffic_light_distance = headed_traffic_light_distance
        self.target_distance = target_distance
