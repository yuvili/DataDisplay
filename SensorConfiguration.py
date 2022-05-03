from position import Position


class sensor_configuration:

    # SensorConfiguration
    # {"Type":"SensorConfiguration",
    # "WorldTime":"",
    # "SimulationTime":0,
    # "FrameID":0,
    # "SensorType":"RgbCamera",
    # "SensorName":"camera0001",
    # "Position":{"x":"0.340","y":"0.000","z":"1.650"},
    # "Rotation":{"x":"0.000","y":"13.500","z":"0.000"},
    # "ProjectionMatrix":{"x":"0.68728090, 0.00000000, 0.00000000, 0.00000000","y":"0.00000000, 3.77022700, 0.00000000, 0.00000000","z":"0.00000000, 0.00000000, -1.00060000, -0.60018000","w":"0.00000000, 0.00000000, -1.00000000, 0.00000000"},
    # "Near":"0.3",
    # "Far":"1000",
    # "FOV":"111",
    # "Width":"5760",
    # "Height":"1050",
    # "AspectRatio":"5.485714",
    # "OutputQuality":0},

    def __init__(self, typ: str, world_time: str, simulation_time: int, frame_id: int, sensor_type: str, sensor_name: str,
                 position: Position, rotation: Position,projection_matrix: dict, near: str, far: str, fov: str, width: str,
                 height: str, aspect_ratio: str,output_quality: int):
        self.typ = typ
        self.world_time = world_time
        self.simulation_time = simulation_time
        self.frame_id = frame_id
        self.sensor_type = sensor_type
        self.sensor_name = sensor_name
        self.position= position
        self.rotation = rotation
        self.projection_matrix = projection_matrix
        self.near = near
        self.far = far
        self.fov = fov
        self.width = width
        self.height = height
        self.aspect_ratio = aspect_ratio
        self.output_quality = output_quality
