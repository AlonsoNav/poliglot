import pyodbc
from dotenv import load_dotenv
import os

load_dotenv()
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
conn_string = f'DRIVER={{MySQL ODBC 9.0 Unicode Driver}};SERVER={db_host};PORT={db_port};DATABASE={db_name};UID={db_user};PWD={db_password};'


def execute_query_without_return(query, params):
    try:
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
    except pyodbc.Error as e:
        print(f"Database error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        try:
            cursor.close() 
            conn.close()
        except: 
            pass
    

def execute_query_with_return(query, params):
    try:
        conn = pyodbc.connect(conn_string)
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
        return results
    except pyodbc.Error as e:
        print(f"Database error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


def set_groups(group):
    query = "CALL SP_Insert_Group(?, ?, ?, ?, ?, ?, ?)"
    params = (  
        group['Año'], 
        group['Semestre'], 
        group['Código'], 
        group['Curso'], 
        group['Grupo'], 
        group['Docente'], 
        group['Sede']
    )
    execute_query_without_return(query, params)


def set_student(group):
    query = "CALL SP_Insert_Student(?, ?, ?, ?, ?)"
    params = (
        group['Carné'], 
        group['Nombre'],
        1, 
        group['Género'],
        group['Correo electrónico']
    )
    execute_query_without_return(query, params)


def get_grades():
    query = "SELECT grade FROM StudentSolution"
    return execute_query_with_return(query, ())

def get_exercise_details():
    query = """
        SELECT 
            e.name,
            GROUP_CONCAT(DISTINCT g.course_code) AS course_code,
            GROUP_CONCAT(DISTINCT c.course_name) AS course_name,
            GROUP_CONCAT(DISTINCT p.professor_name) AS professor_name
        FROM 
            Exercise e
        LEFT JOIN 
            `Group` g ON e.group_id = g.group_id
        LEFT JOIN 
            Course c ON g.course_code = c.course_code
        LEFT JOIN 
            Professor p ON g.professor_id = p.professor_id
        GROUP BY 
            e.exercise_id
        ORDER BY 
            e.name;
    """
    return execute_query_with_return(query, ())

def get_exercise_grades():
    query = """
        SELECT 
            e.name,
            GROUP_CONCAT(s.grade ORDER BY s.grade DESC) AS grade
        FROM 
            Exercise e
        LEFT JOIN 
            StudentSolution s ON e.exercise_id = s.exercise_id
        GROUP BY 
            e.exercise_id
        ORDER BY 
            e.name;
    """
    return execute_query_with_return(query, ())


def get_exercise_aspects():
    query = """
        SELECT 
            e.name AS exercise_name, 
            GROUP_CONCAT(a.aspect_name ORDER BY a.aspect_name ASC) AS aspects
        FROM 
            Exercise e
        LEFT JOIN 
            ExerciseAspect ea ON e.exercise_id = ea.exercise_id
        LEFT JOIN 
            Aspect a ON ea.aspect_id = a.aspect_id
        GROUP BY 
            e.exercise_id
        ORDER BY 
            e.name;
    """
    return execute_query_with_return(query, ())

def get_exercise_with_aspects():
    # Get the exercise details and aspects
    exercise_details = get_exercise_details()
    exercise_aspects = get_exercise_aspects()

    # Create a dictionary to hold aspects by exercise name
    aspects_by_exercise = {}
    
    # Populate the dictionary with aspects
    for exercise_name, aspect_name in exercise_aspects:
        if exercise_name not in aspects_by_exercise:
            aspects_by_exercise[exercise_name] = []
        aspects_by_exercise[exercise_name].append(aspect_name)

    # Create a list to hold the final results
    result = []
    
    # Combine exercise details with their aspects
    for detail in exercise_details:
        grade, group_number, course_code, course_name, professor_name, exercise_name = detail
        aspects = aspects_by_exercise.get(exercise_name, [])
        result.append((grade, group_number, course_code, course_name, professor_name, exercise_name, aspects))

    return result

def get_group_details():
    query = """
        SELECT 
            c.course_name,
            p.professor_name,
            g.group_number,
            GROUP_CONCAT(s.grade ORDER BY s.grade DESC) AS grades
        FROM 
            StudentSolution s
        JOIN 
            Exercise e ON s.exercise_id = e.exercise_id
        JOIN 
            `Group` g ON e.group_id = g.group_id
        JOIN 
            Course c ON g.course_code = c.course_code
        JOIN 
            Professor p ON g.professor_id = p.professor_id
        GROUP BY 
            c.course_code, g.group_id, p.professor_name
        ORDER BY 
            c.course_name, g.group_number;
    """
    return execute_query_with_return(query, ())


def get_grades_exercise():
    # Call the functions to retrieve the data
    grades_data = get_exercise_details()
    aspects_data = get_exercise_aspects()

    # Initialize a dictionary to hold the final structure
    result = {}

    # Populate the result with grades and exercise details
    for row in grades_data:
        grade, group_number, course_code, course_name, professor_name, exercise_id = row
        
        if exercise_id not in result:
            result[exercise_id] = {
                "grades": [],
                "course_code": course_code,
                "course_name": course_name,
                "group": group_number,
                "professor_name": professor_name,
                "aspects": []
            }
        
        result[exercise_id]["grades"].append(int(grade))

    # Populate the aspects
    for row in aspects_data:
        exercise_id, aspect_name = row
        
        if exercise_id in result:
            result[exercise_id]["aspects"].append(str(aspect_name))

    # Build the JSON-like string manually
    json_string = "{\n"
    
    for exercise_id, data in sorted(result.items()):
        json_string += f'  "{exercise_id}": {{\n'
        json_string += f'    "grades": {sorted(data["grades"])},\n'
        json_string += f'    "course_code": "{data["course_code"]}",\n'
        json_string += f'    "course_name": "{data["course_name"]}",\n'
        json_string += f'    "group": {data["group"]},\n'
        json_string += f'    "professor_name": "{data["professor_name"]}",\n'
        json_string += '    "aspects": [{0}]\n'.format(", ".join(f'"{aspect}"' for aspect in data["aspects"]))
        json_string += "  },\n"

    # Remove the last comma and close the JSON object
    json_string = json_string.rstrip(",\n") + "\n}"    
    
    return json_string
