# Import pyplot
import matplotlib.pyplot as plt

# Plot a line chart on each of the two y-axes
def line_line(x, y1, y2, y1_color='C0', y2_color='C1',
              title=None, x_label=None, y1_label=None, y2_label=None,
              y1_legend=None, y2_legend=None, y1_lim=None, y2_lim=None,
              y1_grid=False, y2_grid=False, export_as='fig.png'):
    '''
    Plot two series on a dual y-axis chart. Both series are plotted as line
    charts and must be of equal length.

    Parameters
    ----------
        x: array-like
            Values to plot along the x-axis.
        y1: array-like
            Values to plot along the y-axis on the left side.
        y2: array-like
            Values to plot along the y-axis on the right side.
        y1_color: str
            Color of `y1`.
        y2_color: str
            Color of `y2`.
        title: str
            Title of the chart.
        x_label: str
            Label for the x-axis.
        y1_label: str
            y-axis label for `y1`.
        y2_label: str
            y-axis label for `y2`.
        y1_legend: str
            Legend label for `y1`.
        y2_legend: str
            Legend label for `y2`.
        y1_lim: tuple
            Tuple of length 2. `y1_lim[0]` and `y1_lim[1]` are set as the
            minimum and maximum values for `y1` on the y-axis.
        y2_lim: tuple
            Tuple of length 2. `y2_lim[0]` and `y2_lim[1]` are set as the
            minimum and maximum values for `y2` on the y-axis.
        y1_grid: bool, default False
            If True, the chart will display horizontal lines on the major ticks
            of `y1`.
        y2_grid: bool, default False
            If True, the chart will display horizontal lines on the major ticks
            of `y2`.
        export_as: str
            Path and filename to export the chart.
    
    Returns
    -------
        Figure generated with `matplotlib.pyplot.subplots(nrows=1, ncols=1)`.
    
    GitHub
    ------
        https://github.com/ArturoSbr/
    '''
    fig, ax1 = plt.subplots()
    ax1.plot(y1, color=y1_color, lw=3, label=y1_legend)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y1_label)
    ax1.set_xticks(range(len(x)))
    ax1.set_xticklabels(labels=x, rotation=45)
    if type(y1_lim) is tuple:
        ax1.set_ylim(bottom=y1_lim[0], top=y1_lim[1])
    if y1_grid:
        ax1.grid(axis='y')
    ax2 = ax1.twinx()
    ax2.plot(y2, color=y2_color, lw=3, label=y2_legend)
    ax2.set_ylabel(y2_label, rotation=270, labelpad=13)
    if type(y2_lim) is tuple:
        ax2.set_ylim(bottom=y2_lim[0], top=y2_lim[1])
    if y2_grid:
        ax2.grid(axis='y')
    if (type(y1_legend) is str) or (type(y2_legend) is str):
        fig.legend(bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    plt.title(title)
    if type(export_as) == str:
        plt.savefig(export_as, dpi=300, bbox_inches='tight')
    plt.show()

# Plot a bar chart on the primary y-axis and a line chart on the secondary y-axis
def bar_line(x, y1, y2, y1_color='C0', y2_color='C1',
             title=None, x_label=None, y1_label=None, y2_label=None,
             y1_legend=None, y2_legend=None, y1_lim=None, y2_lim=None,
             y1_grid=False, y2_grid=False, export_as=None):
    '''
    Plot two series on a dual y-axis chart. The first series is plotted as a
    bar chart and the second one as a line chart. Both series must be of equal
    length.

    Parameters
    ----------
        x: array-like
            Values to plot along the x-axis.
        y1: array-like
            Values to plot along the y-axis on the left side.
        y2: array-like
            Values to plot along the y-axis on the right side.
        y1_color: str
            Color of `y1`.
        y2_color: str
            Color of `y2`.
        title: str
            Title of the chart.
        x_label: str
            Label for the x-axis.
        y1_label: str
            y-axis label for `y1`.
        y2_label: str
            y-axis label for `y2`.
        y1_legend: str
            Legend label for `y1`.
        y2_legend: str
            Legend label for `y2`.
        y1_lim: tuple
            Tuple of length 2. `y1_lim[0]` and `y1_lim[1]` are set as the
            minimum and maximum values for `y1` on the y-axis.
        y2_lim: tuple
            Tuple of length 2. `y2_lim[0]` and `y2_lim[1]` are set as the
            minimum and maximum values for `y2` on the y-axis.
        y1_grid: bool, default False
            If True, the chart will display horizontal lines on the major ticks
            of `y1`.
        y2_grid: bool, default False
            If True, the chart will display horizontal lines on the major ticks
            of `y2`.
        export_as: str
            Path and filename to export the chart.
    
    Returns
    -------
        Figure generated with `matplotlib.pyplot.subplots(nrows=1, ncols=1)`.
    
    GitHub
    ------
        https://github.com/ArturoSbr/
    '''
    fig, ax1 = plt.subplots()
    ax1.bar(range(len(x)), y1, color=y1_color, label=y1_legend)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y1_label)
    ax1.set_xticks(range(len(x)))
    ax1.set_xticklabels(labels=x, rotation=45)
    if type(y1_lim) is tuple:
        ax1.set_ylim(bottom=y1_lim[0], top=y1_lim[1])
    ax2 = ax1.twinx()
    ax2.plot(y2, color=y2_color, lw=3, label=y2_legend)
    ax2.set_ylabel(y2_label, rotation=270, labelpad=14)
    if type(y2_lim) is tuple:
        ax2.set_ylim(bottom=y2_lim[0], top=y2_lim[1])
    if y1_grid:
        ax1.grid(axis='y')
    if y2_grid:
        ax2.grid(axis='y')
    if (type(y1_legend) is str) or (type(y2_legend) is str):
        fig.legend(bbox_to_anchor=(1,1), bbox_transform=ax1.transAxes)
    plt.title(title)
    if type(export_as) == str:
        plt.savefig(export_as, dpi=300, bbox_inches='tight')
    plt.show()
