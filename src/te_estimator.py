import numpy as np
from pyinform import transfer_entropy

def compute_te(x, y, k=3, delay=1):
    """
    计算 T_{y → x}(delay) using Kraskov estimator
    x, y: 1D arrays (price returns)
    k: number of nearest neighbors
    delay: time lag τ
    """
    # 构造嵌入向量：X_t = [x_t, x_{t-1}, ..., x_{t-k+1}]
    #               Y_t = [y_{t-delay}, y_{t-delay-1}, ..., y_{t-delay-k+1}]
    X = np.column_stack([x[k-i-1:-i] for i in range(k)])
    Y = np.column_stack([y[k+i-1+delay:-i-delay] for i in range(k)])
    
    # 确保长度一致
    min_len = min(len(X), len(Y))
    X, Y = X[:min_len], Y[:min_len]
    
    te = transfer_entropy(Y, X, k=k, local=False)
    return te  # in bits
