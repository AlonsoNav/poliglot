import pandas as pd
import json
from ..utils.db import set_groups, set_student, set_aspects
from ..utils.genderize import predict_gender

def analyze_group(file):
    df = pd.read_excel(file, skiprows=6)
    df.columns = df.columns.str.strip()
    course_data = df[['Año', 'Semestre', 'Código', 'Curso', 'Grupo', 'Docente', 'Sede']]
    course_data = course_data.dropna() # Remove empty rows
    
    for index, row in course_data.iterrows():
        set_groups(row)
    
    print("Groups inserted successfully.")


def analyze_student(file):
    df = pd.read_excel(file, skiprows=8)
    df.columns = df.columns.str.strip()
    course_data = df[['Carné', 'Nombre', 'Correo electrónico']]
    course_data = course_data.dropna() # Remove empty rows
    
    for index, row in course_data.iterrows():
        row['Género'] = predict_gender(row['Nombre'])
        set_student(row)
    
    print("Student inserted successfully.")


def analyze_aspects(file, exercise):
    df = pd.read_csv(file)
    df.columns = df.columns.str.strip()
    keywords = df['keywords'].dropna().tolist()
    set_aspects(int(exercise), json.dumps(keywords))


def analyze_grade(file, case):
    df = pd.read_excel(file)
    df.columns = df.columns.str.strip()
    if case == 1:
        grade_date = df[['ejercicio', 'nota']]
        grade_date.set_index('ejercicio', inplace=True)
    else:
        grade_date = df[['id', 'nota']]
        grade_date.set_index('id', inplace=True)
    grade_date = grade_date.dropna() # Remove empty rows
    return grade_date['nota'].to_dict()
