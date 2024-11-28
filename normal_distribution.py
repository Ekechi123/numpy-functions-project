import numpy as np

def normal_distribution_array(shape, mean, std_dev):
    """
    Generate a NumPy array of normally distributed numbers.
    
    Args:
        shape (tuple): Shape of the array (e.g., (2, 3)).
        mean (float): Mean of the distribution.
        std_dev (float): Standard deviation of the distribution.
    
    Returns:
        np.ndarray: Generated array.
    """
    return np.random.normal(loc=mean, scale=std_dev, size=shape)

