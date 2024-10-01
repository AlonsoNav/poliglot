import numpy as np
import json
from collections import defaultdict
from datetime import datetime

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


def generate_report(group_data, exercise_details, exercise_aspects, exercise_grades):
    """
    Generates a report with statistics, quartile data, outliers and pass/fail rates.
    Receives a json type string.
    """
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Start the HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Poliglot Statistics Report</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <h1>Poliglot Statistics Report</h1>
        <p class="date-info">This page was generated using Python on {current_time}.</p>
        <h2 class="title">Statistics Per Group</h2>
        <div class="container">
    """
    # Generate the group report
    for course_name, proffesor_name, group_number, grades in group_data:
        # Turn grades into list
        grades_list = [int(num) for num in grades.split(',')]
        
        if grades_list:
            # Get statistics
            stats = get_statistics(grades_list)
            # Get quartile data
            quartiles = get_quartile_data(grades_list)
            # Get outliers
            outliers = get_outliers(grades_list)
            # Get pass/fail rate
            pass_fail_rate = get_pass_fail_rate(grades_list)
        else:
            # Handle the case where grades_list is empty
            stats = None
            quartiles = None
            outliers = None
            pass_fail_rate = None

        # Generate the HTML content for the group
        html_content += f"""
        <div class="info-frame">
            <h3>{course_name} - {proffesor_name} - Group {group_number}</h3>
            <div class="tables">
                <div class="table">
                    <h4>Statistics</h4>
                    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse;">
                        <tr>
                            <th>Measure</th>
                            <th>Value</th>
                        </tr>
                        <td>Mean</td>
                            <td>{'%.2f' % stats['mean'] if stats is not None and 'mean' in stats else 'N/A'}</td>
                        </tr>
                        <tr>
                            <td>Median</td>
                            <td>{'%.2f' % stats['median'] if stats is not None and 'median' in stats else 'N/A'}</td>
                        </tr>
                        <tr>
                            <td>Mode</td>
                            <td>{stats['mode'] if stats is not None and 'mode' in stats else 'N/A'}</td>
                        </tr>
                        <tr>
                            <td>Standard Deviation</td>
                            <td>{'%.2f' % stats['std_dev'] if stats is not None and 'std_dev' in stats else 'N/A'}</td>
                        </tr>
                        <tr>
                            <td>Coefficient of Variation</td>
                            <td>{'%.2f' % stats['cv'] if stats is not None and 'cv' in stats else 'N/A'}%</td>
                        </tr>
                    </table>
                </div>

                <div class="table">
                    <h4>Quartile Data</h4>
                    <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse;">
                        <tr>
                            <th>Quartile</th>
                            <th>Min</th>
                            <th>Max</th>
                        </tr>
                        <tr>
                            <td>Q1</td>
                            <td>{quartiles[0]['min'] if quartiles is not None else 'N/A'}</td>
                            <td>{quartiles[0]['max'] if quartiles is not None else 'N/A'}</td>
                        </tr>
                        <tr>
                            <td>Q2</td>
                            <td>{quartiles[1]['min'] if quartiles is not None else 'N/A'}</td>
                            <td>{quartiles[1]['max'] if quartiles is not None else 'N/A'}</td>
                        </tr>
                        <tr>
                            <td>Q3</td>
                            <td>{quartiles[2]['min'] if quartiles is not None else 'N/A'}</td>
                            <td>{quartiles[2]['max'] if quartiles is not None else 'N/A'}</td>
                        </tr>
                        <tr>
                            <td>Q4</td>
                            <td>{quartiles[3]['min'] if quartiles is not None and quartiles[3]['min'] is not None else 'N/A'}</td>
                            <td>{quartiles[3]['max'] if quartiles is not None and quartiles[3]['max'] is not None else 'N/A'}</td>
                        </tr>
                    </table>
                </div>
            </div>
            <h4>Outliers</h4>
            <p>{', '.join(map(str, sorted(set(outliers)))) if outliers else 'No outliers detected'}</p>

            <h4>Pass/Fail Rate</h4>
        """
        if pass_fail_rate is not None:
            html_content += f"""
                <div style="width: 50%; background-color: #f0f0f0; border-radius: 5px; overflow: hidden; margin: 0 auto;">
                    <div style="width: {pass_fail_rate['pass_rate']}%; height: 20px; background-color: #4CAF50; float: left;"></div>
                    <div style="width: {pass_fail_rate['fail_rate']}%; height: 20px; background-color: #F44336; float: left;"></div>
                </div>
                <p class="pass-rate">Pass Rate: {pass_fail_rate['pass_rate']:.2f}% | Fail Rate: {pass_fail_rate['fail_rate']:.2f}%</p>
            """
        else:
            html_content += "<p>No data available</p>"
        html_content += "</div>"

        
    # Generate the HTML content for the exercises
    html_content += """
        </div>
        <h2 class="title">Statistics Per Exercise</h2>
        <div class="container">
    """

    # Process each exercise
    exercise_amount = len(exercise_details)

    for i in range(exercise_amount):
        exercise_name = exercise_details[i][0]
        course_code = exercise_details[i][1]
        course_name = exercise_details[i][2]
        professor_name = exercise_details[i][3]

        # Get list of aspects
        aspects = exercise_aspects[i][1].split(',') if exercise_aspects[i][1] is not None else []

        # Turn grades into list
        grades_list = [int(num) for num in exercise_grades[i][1].split(',')] if exercise_grades[i][1] is not None else []
        if grades_list:
            # Get statistics
            stats = get_statistics(grades_list)
            # Get quartile data
            quartiles = get_quartile_data(grades_list)
            # Get outliers
            outliers = get_outliers(grades_list)
            # Get pass/fail rate
            pass_fail_rate = get_pass_fail_rate(grades_list)
        else:
            # Handle the case where grades_list is empty
            stats = None
            quartiles = None
            outliers = None
            pass_fail_rate = None
        
        # Generate the HTML content for the exercise
        html_content += f"""
        <div class="info-frame">
            <h3>{course_name} - {professor_name} - {exercise_name}</h3>
        """
        if aspects != []:
            html_content += "<ul class='aspects'>"

            for aspect in aspects:
                html_content += f"<li>{aspect}</li>"

            html_content += "</ul>"
        else:
            html_content += "<p>No aspects available</p>"
        html_content += f"""
        </ul>
        <div class="tables">
            <div class="table">
                <h4>Statistics</h4>
                <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse;">
                    <tr>
                        <th>Measure</th>
                        <th>Value</th>
                    </tr>
                    <tr>
                        <td>Mean</td>
                        <td>{'%.2f' % stats['mean'] if stats is not None and 'mean' in stats else 'N/A'}</td>
                    </tr>
                    <tr>
                        <td>Median</td>
                        <td>{'%.2f' % stats['median'] if stats is not None and 'median' in stats else 'N/A'}</td>
                    </tr>
                    <tr>
                        <td>Mode</td>
                        <td>{stats['mode'] if stats is not None and 'mode' in stats else 'N/A'}</td>
                    </tr>
                    <tr>
                        <td>Standard Deviation</td>
                        <td>{'%.2f' % stats['std_dev'] if stats is not None and 'std_dev' in stats else 'N/A'}</td>
                    </tr>
                    <tr>
                        <td>Coefficient of Variation</td>
                        <td>{'%.2f' % stats['cv'] if stats is not None and 'cv' in stats else 'N/A'}%</td>
                    </tr>
                </table>
            </div>

            <div class="table">
                <h4>Quartile Data</h4>
                <table border="1" cellpadding="5" cellspacing="0" style="border-collapse: collapse;">
                    <tr>
                        <th>Quartile</th>
                        <th>Min</th>
                        <th>Max</th>
                    </tr>
                    <tr>
                        <td>Q1</td>
                        <td>{quartiles[0]['min'] if quartiles is not None else 'N/A'}</td>
                        <td>{quartiles[0]['max'] if quartiles is not None else 'N/A'}</td>
                    </tr>
                    <tr>
                        <td>Q2</td>
                        <td>{quartiles[1]['min'] if quartiles is not None else 'N/A'}</td>
                        <td>{quartiles[1]['max'] if quartiles is not None else 'N/A'}</td>
                    </tr>
                    <tr>
                        <td>Q3</td>
                        <td>{quartiles[2]['min'] if quartiles is not None else 'N/A'}</td>
                        <td>{quartiles[2]['max'] if quartiles is not None else 'N/A'}</td>
                    </tr>
                    <tr>
                        <td>Q4</td>
                        <td>{quartiles[3]['min'] if quartiles is not None and quartiles[3]['min'] is not None else 'N/A'}</td>
                        <td>{quartiles[3]['max'] if quartiles is not None and quartiles[3]['max'] is not None else 'N/A'}</td>
                    </tr>
                </table>
            </div>
        </div>
        <h4>Outliers</h4>
        <p>{', '.join(map(str, sorted(set(outliers)))) if outliers else 'No outliers detected'}</p>

        <h4>Pass/Fail Rate</h4>
        """
        if pass_fail_rate is not None:
            html_content += f"""
            <div style="width: 50%; background-color: #f0f0f0; border-radius: 5px; overflow: hidden; margin: 0 auto;">
                <div style="width: {pass_fail_rate['pass_rate']}%; height: 20px; background-color: #4CAF50; float: left;"></div>
                <div style="width: {pass_fail_rate['fail_rate']}%; height: 20px; background-color: #F44336; float: left;"></div>
            </div>
            <p class="pass-rate">Pass Rate: {pass_fail_rate['pass_rate']:.2f}% | Fail Rate: {pass_fail_rate['fail_rate']:.2f}%</p>
            """
        else:
            html_content += "<p>No data available</p>"
        html_content += "</div>"
    # End the HTML content
    html_content += """
    </body>
    </html>
    """
    with open("report.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    
    