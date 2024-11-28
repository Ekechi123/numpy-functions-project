def solve_cramers_rule(coeff_matrix, constants):
    """
    Solve a system of linear equations using Cramer's Rule.
    
    Args:
        coeff_matrix (list[list[float]]): Coefficient matrix.
        constants (list[float]): Constant terms.
    
    Returns:
        list[float]: Solution for the variables.
    """
    coeff_matrix = np.array(coeff_matrix)
    constants = np.array(constants)
    det_main = np.linalg.det(coeff_matrix)
    
    if det_main == 0:
        raise ValueError("Determinant is zero, no unique solution.")
    
    solutions = []
    for i in range(coeff_matrix.shape[1]):
        temp_matrix = coeff_matrix.copy()
        temp_matrix[:, i] = constants
        solutions.append(np.linalg.det(temp_matrix) / det_main)
    
    return solutions

