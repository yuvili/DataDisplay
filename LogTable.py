import json

from types.ActionScript import action_script
from types.Anchor import anchor
from types.GPS import gps
from types.MovingObjectPath import moving_object_path
from types.SensorConfiguration import sensor_configuration
from types.VehicleInfo import vehicle_info


class logTable:

    def __init__(self, logs, latitudes, longitudes):
        self.log = logs
        self.latitudes = latitudes
        self.longitudes = longitudes

    def load_from_json(self, file_name: str) -> bool:
        flag = True
        try:
            with open(file_name, "r") as f:
                logs = []
                longitudes = []
                latitudes = []
                lst = json.load(f)
                logs = lst["Logs"]

                for v in logs:
                    t = v["Type"]

                    match t:
                        case "GPS":
                            gpss = gps(t, v["WorldTime"], v["SimulationTime"], v["FrameID"], v["SimulationPosition"],
                                       v["NoisedSimulationPosition"],v["Latitude"], v["Longitude"], v["Altitude"],
                                       v["NoisedLatitude"], v["NoisedLongitude"],
                                       v["NoisedAltitude"], v["Orientation"], v["Speed"], v["Acceleration"],
                                       v["PositionInLane"],
                                       v["LaneWidth"], v["LaneNumber"], v["NavigationSegment"], v["VelocityLocal3D"],
                                       v["AngularVelocityLocal3D"], v["AngularAccelerationLocal3D"],
                                       v["InstanceNumber"],
                                       v["OnRoadDirection"], v["RoadSpeedLimit"], v["HeadedTrafficLightDistance"],
                                       v["TargetDistance"])
                            longitudes.append(v["Longitude"])
                            latitudes.append(v["Latitude"])
                            logs.append(gpss)

                        case "Anchor":
                            word_time = v["WorldTime"]
                            simulation_time = v["SimulationTime"]
                            frame_id = v["FrameID"]
                            anchors = v["Anchors"]
                            an = anchor(t, word_time, simulation_time, frame_id, anchors)
                            logs.append(an)

                        case "ActionScript":
                            word_time = v["WorldTime"]
                            simulation_time = v["SimulationTime"]
                            frame_id = v["FrameID"]
                            actor_name = v["ActorName"]
                            trigger = v["Trigger"]
                            actions = v["Actions"]
                            asc = action_script(t, word_time, simulation_time, frame_id, actor_name, trigger, actions)
                            logs.append(asc)

                        case "SensorConfiguration":
                            word_time = v["WorldTime"]
                            simulation_time = v["SimulationTime"]
                            frame_id = v["FrameID"]
                            sensor_type = v["SensorType"]
                            sensor_name = v["SensorName"]
                            pos = v["Position"]
                            rotation = v["Rotation"]
                            projection_matrix = v["ProjectionMatrix"]
                            near = v["Near"]
                            far = v["Far"]
                            fov = v["FOV"]
                            width = v["Width"]
                            height = v["Height"]
                            aspect_ratio = v["AspectRatio"]
                            output_quality = v["OutputQualit"]
                            sc = sensor_configuration(t, word_time, simulation_time, frame_id, sensor_type, sensor_name,
                                                      pos, rotation, projection_matrix, near, far, fov, width, height,
                                                      aspect_ratio, output_quality)
                            logs.append(sc)

                        case "VehicleInfo":
                            word_time = v["WorldTime"]
                            simulation_time = v["SimulationTime"]
                            frame_id = v["FrameID"]
                            name = v["Name"]
                            dimensions = v["Dimensions"]
                            vi = vehicle_info(t, word_time, simulation_time, frame_id, name, dimensions)
                            logs.append(vi)

                        case "MovingObject Path":
                            word_time = v["WorldTime"]
                            simulation_time = v["SimulationTime"]
                            frame_id = v["FrameID"]
                            vehicle_name = v["VehicleName"]
                            waypoints = v["Waypoints"]
                            mop = moving_object_path(t, word_time, simulation_time, frame_id, vehicle_name, waypoints)
                            logs.append(mop)

                self.__init__(logs, latitudes, longitudes)
        except FileNotFoundError:
            flag = False
            raise FileNotFoundError
        finally:
            return flag
