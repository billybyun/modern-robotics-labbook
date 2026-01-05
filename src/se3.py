import numpy as np
from .so3 import hat, exp_so3, normalize

def hat6(xi: np.ndarray) -> np.ndarray:
    """se(3) matrix from 6-vector twist xi = [w, v]."""
    xi = np.asarray(xi, dtype=float).reshape(6,)
    w = xi[:3]
    v = xi[3:]
    W = hat(w)
    return np.block([[W, v.reshape(3,1)],
                     [np.zeros((1,3)), np.zeros((1,1))]])

def make_T(R: np.ndarray, p: np.ndarray) -> np.ndarray:
    """Homogeneous transform from R, p."""
    T = np.eye(4)
    T[:3,:3] = R
    T[:3, 3] = p.reshape(3,)
    return T

def exp_se3(xi: np.ndarray, theta: float) -> np.ndarray:
    """
    Basic exponential map for se(3) -> SE(3) using matrix exponential approximation.
    For learning/visualization. (You can upgrade to closed-form later.)
    """
    xi = np.asarray(xi, dtype=float).reshape(6,)
    w = xi[:3]
    v = xi[3:]
    wn = np.linalg.norm(w)
    if wn < 1e-12:
        # pure translation
        R = np.eye(3)
        p = v * theta
        return make_T(R, p)

    w_unit = w / wn
    th = theta * wn
    R = exp_so3(w_unit, th)

    # Simple closed-form V matrix for unit w (Modern Robotics)
    W = hat(w_unit)
    I = np.eye(3)
    V = I*th + (1 - np.cos(th))*W + (th - np.sin(th))*(W@W)
    p = V @ (v / wn)  # scale consistent with th = theta*||w||
    return make_T(R, p)
