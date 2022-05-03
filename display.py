from LogTable import logTable
from matplotlib import pyplot as plt


def displays(file_name: str):
    plt.style.use('seaborn')
    lt = logTable()
    if not lt.load_from_json(file_name):
        print("hi")

    x = lt.latitudes
    y = lt.longitudes

    plt.scatter(x, y)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.show()


if __name__ == '__main__':
    displays("CognataEngineLog_close.json")
    displays("CognataEngineLog_far.json")
