import matplotlib.pyplot as plt

def view_chart():
    labels = ('A', 'B', 'C')
    values = (10, 20, 30)

    fig, ax = plt.subplots()

    ax.pie(values, labels=labels)

    plt.savefig('chart.png')

    plt.close()
