import numpy as np


def minmax_scale(X, axis=0, eps=1e-12):
    """
    Scale X to [0,1]. If 2D and axis=0 (default), scale per column.
    Return np.ndarray (float).
    """
    X = np.asarray(X, dtype=float)
    
    # Compute min and max along axis
    X_min = np.min(X, axis=axis, keepdims=True)
    X_max = np.max(X, axis=axis, keepdims=True)
    
    # Avoid division by zero
    denom = X_max - X_min
    #np.where(condition, A, B)
    denom = np.where(denom < eps, eps, denom)
    #If denom is too small → replace it with eps
    #Otherwise → keep original value
    # Apply min-max scaling
    X_scaled = (X - X_min) / denom
    
    return X_scaled