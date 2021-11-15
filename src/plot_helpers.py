import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns


PLOT_HEIGHT = 8
ASPECT_RATIO = 1.618
STANDARD_PLOT_SIZE = (PLOT_HEIGHT * ASPECT_RATIO, PLOT_HEIGHT)


def set_matplotlib_defaults():
    mpl.rcParams["figure.figsize"] = STANDARD_PLOT_SIZE
    plt.style.use("bmh")


def set_seaborn_defaults():
    """
    Set the default appearance for seaborn charts
    """
    sns.set_context('notebook')
    sns.set(
        font_scale=1.2,
        rc={
            'figure.figsize': STANDARD_PLOT_SIZE,
            "xtick.bottom": True,
            "ytick.left": True,
        }
    )
    sns.set_style()
