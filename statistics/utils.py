import numpy as np

def get_quartile_data(grades):
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
        {"min": min(quartile_1) if quartile_1 else None, "max": max(quartile_1) if quartile_1 else None},
        {"min": min(quartile_2) if quartile_2 else None, "max": max(quartile_2) if quartile_2 else None},
        {"min": min(quartile_3) if quartile_3 else None, "max": max(quartile_3) if quartile_3 else None},
        {"min": min(quartile_4) if quartile_4 else None, "max": max(quartile_4) if quartile_4 else None},
    ]
    
    return quartiles

def get_statistics(grades):
    """
    Returns the mean, median, mode, coefficient of deviation and standard deviation of the grades.
    """
    mean = np.mean(grades)
    median = np.median(grades)
    std_dev = np.std(grades)
    
    # Manually calculate mode
    values, counts = np.unique(grades, return_counts=True)
    mode_index = np.argmax(counts)
    mode = values[mode_index]

    cv = (std_dev / mean) * 100 if mean != 0 else 0
    
    return {
        "mean": float(mean),
        "median": float(median),
        "mode": int(mode),
        "std_dev": float(std_dev),
        "cv": float(cv)
    }

def get_outliers(grades):
    """
    Returns the list of outliers in the grades.
    """
    q1, q3 = np.percentile(grades, [25, 75])
    iqr = q3 - q1
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    return [grade for grade in grades if grade < lower_bound or grade > upper_bound]

def get_pass_fail_rate(grades, passing_grade=67.5):
    """
    Returns the pass and fail rates for the grades.
    """
    total = len(grades)
    passed = sum(1 for grade in grades if grade >= passing_grade)
    pass_rate = (passed / total) * 100 if total > 0 else 0
    fail_rate = 100 - pass_rate
    return {"pass_rate": pass_rate, "fail_rate": fail_rate}
