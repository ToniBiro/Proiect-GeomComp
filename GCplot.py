from tripy import earclip
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as pat  # Patches like pat.Polygon()
from matplotlib.collections import PolyCollection  # Collections of patches

def draw (firstFig,      secondFig,      interFig,
          firstFigColor, secondFigColor, interFigColor, 
          labels = ["first", "second", "inter", "combined"]):
    polyColors = [firstFigColor, secondFigColor, interFigColor]
    figures    = [[firstFig], [secondFig], interFig]

    ax  = plt.subplots(2, 2, True, True)[1]
    ax[1, 1].set_title(labels[3])

    polyNo = 0
    for polygons in figures:
        polyColor = polyColors[polyNo]
        ax[polyNo // 2, polyNo % 2].set_title(labels[polyNo])
        for polygon in polygons:
            assert (len(polygon) > 3), "Not a polygon"
            triangles = earclip(polygon)
            ax[1, 1].add_collection(PolyCollection(triangles, edgecolor=polyColor, facecolor=polyColor))  # Main Plot polygon collection
            ax[polyNo // 2, polyNo % 2].add_collection(PolyCollection(triangles, edgecolor=polyColor, facecolor=polyColor))  # Side Plot polygon collection
        polyNo += 1

    plt.autoscale()
    left, right = plt.xlim()
    down, up    = plt.ylim()
    plt.xlim(min(left, down), max(right, up))
    plt.ylim(min(left, down), max(right, up))
    plt.show()