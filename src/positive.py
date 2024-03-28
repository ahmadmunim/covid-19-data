import matplotlib.pyplot as plt
import pyodbc as db
import mpld3 as mp

def main():
    DRIVER_NAME = 'SQL SERVER'
    SERVER_NAME = 'DESKTOP-6KMHFF2'
    DATABASE_NAME = 'COVID19'

    # Defines the connection string
    connection = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
    """
    #Connects to COVID19 database
    db_connection = db.connect(connection)
    cursor = db_connection.cursor();
    
    xaxis_query = '''
    SELECT AgeCategory 
    FROM AgeCategories
    WHERE AgeCategoryID = 3 OR AgeCategoryID = 6 OR AgeCategoryID = 7 OR AgeCategoryID = 9 OR AgeCategoryID = 13    
    '''
    
    x = [cursor.execute(xaxis_query).fetchall()[i][0].strip() for i in range(5)]
    
if __name__ == "__main__":
    main()