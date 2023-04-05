import matplotlib.pyplot as plt
import pyodbc as db
import numpy as np
import mpld3 as mp

def generate_query(region):
    return '''
        SELECT *
        FROM (
        SELECT *, ROW_NUMBER() OVER (ORDER BY Date) as row_num
        FROM Hospital
        WHERE Region = ''' + region + ''') as t
        WHERE t.row_num % 70 = 0
        '''
        
def generate_html(figure):
    to_html = mp.fig_to_html(figure)
    html_file = open('index.html', 'w')
    html_file.write(to_html)
    html_file.close

def render_graph(data, region, row, figure):
    #Defining variables
    x = [data[i][1] for i in range(len(data))]
    hos_y = [data[i][5] for i in range(len(data))]
    icu_y = [data[i][3] for i in range(len(data))]
    vent_y = [data[i][4] for i in range(len(data))]

    #Plotting the points
    ax1 = figure.add_subplot(5, 1, row)
    ax1.plot(x, hos_y, label='hospitalization')
    ax1.plot(x, icu_y, label='on icu')
    ax1.plot(x, vent_y, label='on ventilator')
    ax1.legend()
    ax1.set_title(region + ' Region')

def main():
    DRIVER_NAME = 'SQL SERVER'
    SERVER_NAME = 'DESKTOP-6KMHFF2'
    DATABASE_NAME = 'COVID19'

    #    uid=<username>
    #    pwd=<password>

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

    central_query = generate_query('\'CENTRAL\'')
    cursor.execute(central_query);
    CENTRAL_DATA = cursor.fetchall();

    # Create the GUI window
    fig1 = plt.figure(figsize=(20,10))

    render_graph(CENTRAL_DATA, 'CENTRAL', 1, fig1)

    east_query = generate_query('\'EAST\'')
    cursor.execute(east_query);
    EAST_DATA = cursor.fetchall();

    render_graph(EAST_DATA, 'EAST', 2, fig1)

    west_query = generate_query('\'WEST\'')
    cursor.execute(west_query);
    WEST_DATA = cursor.fetchall();

    render_graph(WEST_DATA, 'WEST', 3, fig1)

    north_query = generate_query('\'NORTH\'')
    cursor.execute(north_query);
    NORTH_DATA = cursor.fetchall();

    render_graph(NORTH_DATA, 'NORTH', 4, fig1)

    toronto_query = generate_query('\'TORONTO\'')
    cursor.execute(toronto_query);
    TORONTO_DATA = cursor.fetchall();

    render_graph(TORONTO_DATA, 'TORONTO', 5, fig1)

    generate_html(fig1)

    # # Show the GUI
    plt.show()
    
if __name__ == "__main__":
    main()