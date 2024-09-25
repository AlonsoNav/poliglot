import argparse
import random 
from upload.drive import get_groups, get_exercises
from statistics.utils import get_statistics, get_quartile_data

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
    
    # Create an option to get statistics of the exercises
    parser.add_argument('-s', '--statistics', type=str,
                        help='Get statistics of the exercises. The path must be \"DATOS/year-semester/professor full name\".')

    args = parser.parse_args()

    # Cases
    if args.drive_group:
        drive_group(args.drive_group) 
    if args.drive_exercises:
        drive_exercises(args.drive_exercises)
    if args.statistics:
        # Random list of 30 grades
        grades = [random.randint(0, 100) for _ in range(30)]
        print("Grades:", grades)
        print("\nStatistics of the exercises")
        print(get_statistics(grades))
        print("Quartile data")
        print(get_quartile_data(grades))

if __name__ == '__main__':
    main()
