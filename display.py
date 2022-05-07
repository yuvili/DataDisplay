from LogTable import logTable
from matplotlib import pyplot as plt
import pandas as pd


def displays(json_file_name: str, xl_file_name: str):
    plt.style.use('seaborn')
    lt = logTable()
    lt.load_from_json(json_file_name)

    x = lt.latitudes
    y = lt.longitudes
    colors = []
    df = pd.read_excel(xl_file_name, index_col=0, dtype={"simulation time": float, 'GSR': float})
    df_simulation_time = df.get("simulation time")

    for lap in lt.log:
        simul_time = lap.simulation_time
        colors.append(df_simulation_time.get(simul_time))

    plt.scatter(x, y, c=colors)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.show()


if __name__ == '__main__':
    displays("CognataEngineLog_close.json", 'g.techAmpDataofA1_090851_LATENCY_2_closeat(13;01;27).xlsx')
    displays("CognataEngineLog_far.json", "g.techAmpDataofA1_090851_LATENCY_2_closeat(13;01;27).xlsx")
