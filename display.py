from LogTable import logTable
from matplotlib import pyplot as plt


def displays(file_name: str):
    plt.style.use('seaborn')
    lt = logTable()
    lt.load_from_json(file_name)

    x = lt.lat
    y = lt.lon

    plt.scatter(x, y)
    plt.xlabel('Latitude')
    plt.ylabel('Longitude')
    plt.show()


if __name__ == '__main__':
    displays("7500(12_25_55)-VehicleGPSLog.json")
    displays("7500(12_25_55)-CognataEngineLog.json")
