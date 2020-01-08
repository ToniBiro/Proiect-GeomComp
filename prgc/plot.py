from tripy import earclip
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as pat  # Patches like pat.Polygon()
from matplotlib.collections import PolyCollection  # Collections of patches


def draw(firstFig, secondFig, interFigs,
         firstFigColor="blue", secondFigColor="red", interFigColor="yellow",
         labels=["first", "second", "inter", "combined"]):
    polyColors = [firstFigColor, secondFigColor, interFigColor]
    figures = [[firstFig], [secondFig], interFigs]

    ax = plt.subplots(2, 2, True, True)[1]
    ax[1, 1].set_title(labels[3])

    polyNo = 0
    for polygons in figures:
        polyColor = polyColors[polyNo]
        ax[polyNo // 2, polyNo % 2].set_title(labels[polyNo])
        for polygon in polygons:
            if len(polygon) == 0:
                continue
            if len(polygon) == 1:
                ax[1, 1].plot([polygon[0][0]], [polygon[0][0]], 'yo')
                ax[polyNo // 2, polyNo %
                    2].plot([polygon[0][0]], [polygon[0][0]], 'yo')
            elif len(polygon) == 2:
                ax[1, 1].plot([polygon[0][0], polygon[1][0]], [
                              polygon[0][1]-0.1, polygon[1][1]-0.1], 'yo--')
                ax[polyNo // 2, polyNo % 2].plot([polygon[0][0], polygon[1][0]], [
                                                 polygon[0][1]-0.1, polygon[1][1]-0.1], 'yo--')
            else:
                triangles = earclip(polygon)
                ax[1, 1].add_collection(PolyCollection(
                    triangles, edgecolor=polyColor, facecolor=polyColor))  # Main Plot polygon collection
                ax[polyNo // 2, polyNo % 2].add_collection(PolyCollection(
                    triangles, edgecolor=polyColor, facecolor=polyColor))  # Side Plot polygon collection
        polyNo += 1

    plt.autoscale()
    left, right = plt.xlim()
    down, up = plt.ylim()
    plt.xlim(min(left, down), max(right, up))
    plt.ylim(min(left, down), max(right, up))
    plt.show()


def drawPolygonLines(polygon):

    ax = plt.subplots()[1]
    x = []
    y = []

    for dot in polygon:
        x.append(dot[0])
        y.append(dot[1])
    x.append(polygon[0][0])
    y.append(polygon[0][1])

    ax.plot(x, y)
    plt.show()
