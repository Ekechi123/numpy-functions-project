def generate_and_index(shape):
    """
    Generate an array of integers and return indexes of even and odd numbers.
    
    Args:
        shape (tuple): Shape of the array (e.g., (3, 4)).
    
    Returns:
        tuple: (Generated array, indices of even numbers, indices of odd numbers)
    """
    array = np.random.randint(0, 100, size=shape)
    evens = np.argwhere(array % 2 == 0).tolist()
    odds = np.argwhere(array % 2 != 0).tolist()
    return array, evens, odds

