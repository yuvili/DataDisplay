from LogTable import logTable
from matplotlib import pyplot as plt
import pandas as pd

close = pd.read_excel(r"g.techAmp Data of A1_090851_LATENCY_2_close at (13;01;27).xlsx", index_col=1)
close_data = pd.DataFrame(close, columns=['GSR'])
far = pd.read_excel(r"g.techAmp Data of A1_090851_Slalom_1_far at (13;05;9).xlsx", index_col=1)
far_data = pd.DataFrame(far, columns=['GSR'])


def displays(json_file_name_far: str, json_file_name_close: str):
    # far
    plt.style.use('seaborn')
    plt.title("Slalom Simulation - Far")
    lt_far = logTable()
    lt_far.load_from_json(json_file_name_far)

    for lap in lt_far.log:
        simul_time = lap.simulation_time
        plt.plot(lap.latitude, lap.longitude, marker='o', linestyle='', markersize=10, label=far_data['GSR'].get(simul_time))

    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.show()

    # close
    plt.title("Slalom Simulation - Close")
    lt_close = logTable()
    lt_close.load_from_json(json_file_name_close)

    for lap in lt_close.log:
        simul_time = lap.simulation_time
        plt.plot(lap.latitude, lap.longitude, marker='o', linestyle='', markersize=10,
                 label=close_data['GSR'].get(simul_time))

    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.show()


if __name__ == '__main__':
    displays("CognataEngineLog_far.json", "CognataEngineLog_close.json")
