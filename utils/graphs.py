import matplotlib.pyplot as plt


def graphs(data: list):
    x = []
    y = []
    for d in data:
        x.append(d['seconds'])
        y.append(d['loss'])
    plt.figure()
    plt.plot(x, y)
    plt.show()