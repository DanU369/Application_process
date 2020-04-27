from typing import List, Dict

from psycopg2 import sql
from psycopg2.extras import RealDictCursor

import database_common


@database_common.connection_handler
def get_mentors(cursor: RealDictCursor) -> list:
    query = """
        SELECT first_name, last_name, city
        FROM mentor
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()


@database_common.connection_handler
def get_mentors_by_last_name(cursor: RealDictCursor, last_name: str) -> list:

    query = f"""
        SELECT first_name, last_name, city
        FROM mentor
        WHERE last_name LIKE '{last_name}'
        """
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def get_mentors_by_city(cursor: RealDictCursor,city_name:str) ->list:
    query="""
        SELECT first_name, last_name, city
        FROM mentor
        WHERE city LIKE '{}'
        """.format(city_name)
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def get_applicants(cursor: RealDictCursor) -> list:
    query = """
        SELECT first_name, last_name, phone_number, email, application_code
        FROM applicant
        ORDER BY first_name"""
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def get_applicants_by_name(cursor: RealDictCursor,applicant_name:str) ->list:
    query="""
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE first_name LIKE '{}' OR last_name LIKE '{}'
        """.format(applicant_name,applicant_name)
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def get_applicants_by_email(cursor: RealDictCursor,email_ending:str) ->list:
    query="""
        SELECT first_name, last_name, phone_number
        FROM applicant
        WHERE email LIKE '%{}' 
        """.format(email_ending)
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def get_applicants_by_application_code(cursor: RealDictCursor,application_code:int) ->list:
    query = """
            SELECT *
            FROM applicant
            WHERE application_code = {}
            """.format(application_code)
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def delete_applicant_by_application_code(cursor: RealDictCursor,application_code:int) ->list:
    query="""
            DELETE FROM applicant
            WHERE application_code = {}
        """.format(application_code)
    cursor.execute(query)
    return "DONE"

@database_common.connection_handler
def delete_applicant_by_ending_email(cursor: RealDictCursor,ending_email:int) ->list:
    query="""
            DELETE FROM applicant
            WHERE email LIKE '%{}'
        """.format(ending_email)
    cursor.execute(query)
    return "DONE"

@database_common.connection_handler
def add_applicant(cursor: RealDictCursor,first_name:str,last_name:str,phone_number:str,email:str,application_id:int) ->list:
    query="""
        INSERT INTO applicant (first_name,last_name, phone_number,email,application_code)
        VALUES ('{}','{}','{}','{}',{});
        """.format(first_name,last_name,phone_number,email,application_id)
    cursor.execute(query)
    return "DONE"

@database_common.connection_handler
def get_id(cursor: RealDictCursor) ->int:
    query="""
        SELECT MAX(id)
        FROM applicant
    """
    cursor.execute(query)
    return cursor.fetchall()

@database_common.connection_handler
def update_phone_number(cursor: RealDictCursor,new_phone_number:str,application_code:int) ->list:
    query="""
            UPDATE applicant
            SET phone_number = '{}'
            WHERE application_code = {}
        """.format(new_phone_number,application_code)
    cursor.execute(query)
    query2 = """
                SELECT *
                FROM applicant
                WHERE application_code = {}
                """.format(application_code)
    cursor.execute(query2)
    return cursor.fetchall()