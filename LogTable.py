import json
from types.Anchor import cognataEngine


class logTable:

    def __init__(self, logs):
        self.log = logs

    def load_from_json(self, file_name: str) -> bool:
        flag = True
        try:
            with open(file_name, "r") as f:
                logs = []
                lst = json.load(f)
                logs = lst["Logs"]

                for v in logs:
                    t = v["Type"]
                    word_time = v["WorldTime"]
                    simulation_time = v["SimulationTime"]
                    frame_id = v["FrameID"]
                    anchors = v["Anchors"]

                    ce = cognataEngine(t, word_time, simulation_time, frame_id, anchors)
                    logs.append(ce)

                self.__init__(logs)
        except FileNotFoundError:
            flag = False
            raise FileNotFoundError
        finally:
            return flag
