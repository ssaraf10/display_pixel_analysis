import cv2
import numpy as np
from pathlib import Path
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm, colors
import matplotlib.pyplot as plt


plot_folder = Path("./plot_functions/plots")
def plot_pixels_RGB(imgpath: Path) -> None:
    img = cv2.imread(imgpath.as_posix())
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(img)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))
    norm = colors.Normalize(vmin=-1, vmax=1)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()
    axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors)
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")

    output_name = imgpath.name[:-4] + "_rgb_plot.png"
    output_path = plot_folder / output_name
    plt.savefig(output_path)


def plot_pixels_hsv(imgpath: Path) -> None:
    img = cv2.imread(imgpath.as_posix())
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    pixel_colors = img.reshape((np.shape(img)[0]*np.shape(img)[1], 3))
    norm = colors.Normalize(vmin=-1, vmax=1)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()

    img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(img)

    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors)
    axis.set_xlabel("Hue")
    axis.set_ylabel("Saturation")
    axis.set_zlabel("Value")

    output_name = imgpath.name[:-4] + "_hsv_plot.png"
    output_path = plot_folder / output_name
    plt.savefig(output_path)
