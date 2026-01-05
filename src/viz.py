import numpy as np

def draw_frame(ax, R=np.eye(3), p=np.zeros(3), L=1.0, label=""):
    """Draw a coordinate frame (RGB axes) on a matplotlib 3D axis."""
    colors = ['r', 'g', 'b']
    for i in range(3):
        v = R[:, i] * L
        ax.quiver(p[0], p[1], p[2], v[0], v[1], v[2],
                  color=colors[i], linewidth=2)
    if label:
        ax.text(p[0], p[1], p[2], label, fontsize=12)
