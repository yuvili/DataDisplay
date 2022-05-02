from position import Position


class vehicleGPS:
    def __init__(self, t: str, worldTime: str, simulTime: float, frameID: int, simulPos: Position,
                 latitude: float, longitude: float, orientation: Position, speed: float, acceleration: Position,
                 posInLane: int, laneWidth: float, laneNumber: int, naviSegment: int, velocityLocal3D: Position,
                 angularVelocityLocal3D: Position, angularAccelerationLocal3D: Position, instanceNum: int, name: str):
        self.type = t
        self.wordTime = worldTime
        self.simulTime = simulTime
        self.frameID = frameID
        self.simulPos = simulPos
        self.latitude = latitude
        self.longitude = longitude
        self.orientation = orientation
        self.speed = speed
        self.acceleration = acceleration
        self.posInLane = posInLane
        self.laneWidth = laneWidth
        self.laneNumber = laneNumber
        self.naviSegment = naviSegment
        self.velocityLocal3D = velocityLocal3D
        self.angularVelocityLocal3D = angularVelocityLocal3D
        self.angularAccelerationLocal3D = angularAccelerationLocal3D
        self.instanceNum = instanceNum
        self.name = name
