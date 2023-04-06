import matplotlib.pyplot as plt
import pyodbc as db
import mpld3 as mp

def generate_query(PHUNum):
    return '''
    SELECT *
    FROM (
    SELECT *, ROW_NUMBER() OVER (ORDER BY Date) as row_num
    FROM Testing
    WHERE PHUNum = ''' + str(PHUNum) + ''') as t
    WHERE t.row_num % 180 = 0
    '''
    
def generate_graph(plot, cursor, query, ICUName):
    cursor.execute(query)    
    DATA = cursor.fetchall()
    x = [DATA[i][1] for i in range(len(DATA))]
    y = [DATA[i][4]/DATA[i][5] for i in range(len(DATA))]
    plot.plot(x, y, label=ICUName)

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
    
    windsor_query = generate_query(2268)
    ontario_query = generate_query(35)
    toronto_query = generate_query(3895)  
    
    fig = plt.figure()
    plot = fig.add_subplot(1,1,1)
    
    generate_graph(plot, cursor, windsor_query, 'Windsor')
    generate_graph(plot, cursor, ontario_query, 'Ontario')
    generate_graph(plot, cursor, toronto_query, 'Toronto')
    
    plot.legend()
    plot.set_title('Percentage of COVID Postive from Patients Tested Every Six Months')
    plot.set_xlabel('Date')
    plot.set_ylabel('Percentage')
    
    to_html = mp.fig_to_html(fig)
    html_file = open('../views/testing.html', 'w')
    html_file.write(to_html)
    html_file.close
    
    plt.show()
    
if __name__ == "__main__":
    main()