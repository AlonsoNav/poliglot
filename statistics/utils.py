import numpy as np

def get_quartile_data(grades):
    """
    Returns the min and max values for each quartile and the list of data in each quartile.
    """
    # Sort the grades
    sorted_grades = sorted(grades)
    
    # Calculate quartiles
    q1 = np.percentile(sorted_grades, 25)
    q2 = np.percentile(sorted_grades, 50)  # Median
    q3 = np.percentile(sorted_grades, 75)
    
    # Split data into quartiles
    quartile_1 = [grade for grade in sorted_grades if grade <= q1]
    quartile_2 = [grade for grade in sorted_grades if q1 < grade <= q2]
    quartile_3 = [grade for grade in sorted_grades if q2 < grade <= q3]
    quartile_4 = [grade for grade in sorted_grades if grade > q3]
    
    # Prepare quartile data with min and max
    quartiles = [
        {"min": min(quartile_1), "max": max(quartile_1), "data": quartile_1},
        {"min": min(quartile_2), "max": max(quartile_2), "data": quartile_2},
        {"min": min(quartile_3), "max": max(quartile_3), "data": quartile_3},
        {"min": min(quartile_4), "max": max(quartile_4), "data": quartile_4}
    ]
    
    return quartiles

def get_statistics(grades):
    """
    Returns the mean, median, mode, and standard deviation of the grades.
    """
    mean = np.mean(grades)
    median = np.median(grades)
    std_dev = np.std(grades)
    
    # Manually calculate mode
    values, counts = np.unique(grades, return_counts=True)
    mode_index = np.argmax(counts)
    mode = values[mode_index]
    
    return {
        "mean": float(mean),
        "median": float(median),
        "mode": int(mode),
        "std_dev": float(std_dev)
    }
