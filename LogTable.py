import json

from GPS import gps


class logTable:

    def __init__(self):
        self.log = []
        self.latitudes = []
        self.longitudes = []
        self.simulation_time = []

    def load_from_json(self, file_name: str) -> bool:
        flag = True
        try:
            with open(file_name, "r") as f:
                logs = []
                longitudes = []
                latitudes = []
                simulation_times = []
                lst = json.load(f)

                for v in lst["Logs"]:
                    t = v["Type"]

                    match t:
                        case "GPS":
                            gpss = gps(t, v["WorldTime"], v["SimulationTime"], v["FrameID"],v["SimulationPosition"],
                                       v["NoisedSimulationPosition"], v["Latitude"], v["Longitude"], v["Altitude"],
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
                            simulation_times.append(v["SimulationTime"])
                            logs.append(gpss)

                self.log = logs
                self.latitudes = latitudes
                self.longitudes = longitudes
                self.simulation_time = simulation_times
        except FileNotFoundError:
            flag = False
            raise FileNotFoundError
        finally:
            return flag
