
from utility.database_connection import get_database_connection

def fetch_query_executer(niche,query):
    db_connection, db_cursor = get_database_connection(niche= niche)
    db_cursor.execute(query)
    data = db_cursor.fetchall()
    db_cursor.close()
    return data

def is_table_is_exist(niche,country_code):
    query = f"SELECT count(*) FROM {country_code}_{niche}_business_data limit 1;"
    try:
        data = fetch_query_executer(niche,query)
        print('Table Is Exist')
        return True
    except:
        print('Table Is Not Exist')
        return False

def get_country_wise_data(args):

    country_code, niche = args
    if is_table_is_exist(niche= niche, country_code= country_code):

        print(f"fetching {niche} --> {country_code}")
        # (SELECT count(*) FROM {country_code}_{niche}_emails WHERE validation_status = 1) AS `Total Validated Emails`;
        query = f"""
                    SELECT
                        (SELECT count(*) FROM {country_code}_{niche}_business_data) AS `Total Business`,
                        (SELECT count(distinct gl_business_name) FROM {country_code}_{niche}_business_data) AS `Total Unique Business`,
                        (SELECT count(distinct gl_website) FROM {country_code}_{niche}_business_data WHERE gl_website != 'None' AND gl_website IS NOT NULL) AS `Total Unique Website`,
                        (SELECT count(*) FROM {country_code}_{niche}_business_data WHERE custom_website_flag = 1) AS `Total Custom Website`,
                        (SELECT count(*) FROM {country_code}_{niche}_business_data WHERE custom_website_flag IS NULL AND gl_website != 'None' AND gl_website IS NOT NULL) AS `Total Non-Custom Website`,
                        (SELECT count(distinct email) FROM {country_code}_{niche}_business_data WHERE email IS NOT NULL) AS `Total Unique Emails`;
                    """
        
        email_query = f"""SELECT count(*) FROM {country_code}_{niche}_emails WHERE validation_status = 1"""

        data = fetch_query_executer(niche= niche, query= query)
        
        data = [data_value for data_value in data[0]]
        try:
            email_count = fetch_query_executer(niche= niche,query=email_query)
           
        except Exception as e:
         
            email_count= [(0,)]
        
        email_count = email_count[0][0]
        
        data.append(email_count)
        data = [(data)]
    
        columns = ['Total Business', 'Total Unique Business', 'Total Unique Website',
                'Total Custom Website', 'Total Non-Custom Website', 'Total Unique Emails',
                'Total Validated Emails']
        result_dict = {country_code:{column: value for column, value in zip(columns, data[0])}}
        return result_dict
    else:
        return None
