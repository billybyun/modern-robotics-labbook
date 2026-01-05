import numpy as np

def hat(w: np.ndarray) -> np.ndarray:
    """Skew-symmetric matrix (so(3)) from 3-vector."""
    wx, wy, wz = w
    return np.array([[0, -wz, wy],
                     [wz, 0, -wx],
                     [-wy, wx, 0]], dtype=float)

def normalize(v: np.ndarray, eps: float = 1e-12) -> np.ndarray:
    n = np.linalg.norm(v)
    if n < eps:
        raise ValueError("Cannot normalize near-zero vector.")
    return v / n

def exp_so3(w: np.ndarray, theta: float) -> np.ndarray:
    """Rodrigues formula: exp([w] theta) in SO(3). w can be non-unit."""
    w = np.asarray(w, dtype=float)
    wn = np.linalg.norm(w)
    if wn < 1e-12:
        return np.eye(3)
    w_unit = w / wn
    th = theta * wn
    W = hat(w_unit)
    I = np.eye(3)
    return I + np.sin(th) * W + (1 - np.cos(th)) * (W @ W)
