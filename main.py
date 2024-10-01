import argparse
import random 
from upload.drive import get_groups, get_exercises
from statistics.utils import get_statistics, get_quartile_data, generate_report
from db import get_grades, get_exercise_details, get_group_details, get_exercise_grades, get_exercise_aspects

def drive_group(path):
    get_groups(path + "grupos.xlsx") # Assume the standarized file name


def drive_exercises(path):
    get_exercises(path)


def main():
    parser = argparse.ArgumentParser(description='Welcome to Poliglot')
    
    # Options
    parser.add_argument('-dg', '--drive_group', type=str, 
                        help='Download groups from drive path and upload them to DB.\nThe path must be \"DATOS/year-semester/\".')
    parser.add_argument('-de', '--drive_exercises', type=str, 
                        help='Download exercises from drive path and upload them to DB.\nThe path must be \"DATOS/year-semester/professor full name\".')
    parser.add_argument('-s', '--statistics', action='store_true',
                        help='Get statistics of the exercises. The path must be \"DATOS/year-semester/professor full name\".')

    args = parser.parse_args()

    # Cases
    if args.drive_group:
        drive_group(args.drive_group) 
    if args.drive_exercises:
        drive_exercises(args.drive_exercises)
    if args.statistics:
        # grades = get_grades()
        # converted_grades = [int(grade[0]) for grade in grades]
        # print("\nStatistics of the exercises")
        # print(get_statistics(converted_grades))
        # print("Quartile data")
        # print(get_quartile_data(converted_grades))

        exercise_details = get_exercise_details()
        exercise_grades = get_exercise_grades()
        exercise_aspects = get_exercise_aspects()
        grades_groups = get_group_details()
        # print(grades_groups)
        # print(data)
        generate_report(grades_groups, exercise_details, exercise_aspects, exercise_grades)


if __name__ == '__main__':
    main()
