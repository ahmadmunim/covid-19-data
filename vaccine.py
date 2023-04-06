import matplotlib.pyplot as plt
import pyodbc as db
import mpld3 as mp
import numpy as np

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
    
    sample_query = '''
    SELECT UnVaxRate100k, PartialVaxRate100k, FullVaxRate100k 
    FROM Vaccine 
    WHERE Date = '2021-10-06'
    '''
    
    get_age_category = '''
    SELECT AgeCategory 
    FROM AgeCategories
    WHERE AgeCategoryID >= 8 AND AgeCategoryID <= 14 
    '''
    
    cursor.execute(sample_query)
    VACCINE_DATA = cursor.fetchall()
    print(VACCINE_DATA)
    
    cursor.execute(get_age_category)
    AGE_CATEGORIES = cursor.fetchall()
    
    del AGE_CATEGORIES[5]
    del AGE_CATEGORIES[1]
    del AGE_CATEGORIES[3]
    
    x = [AGE_CATEGORIES[i][0].strip() for i in range(len(AGE_CATEGORIES))]
    unvax_rate = [VACCINE_DATA[i][0] for i in range(len(VACCINE_DATA))]
    partial_vax_rate = [VACCINE_DATA[i][1] for i in range(len(VACCINE_DATA))]
    full_vax_rate = [VACCINE_DATA[i][2] for i in range(len(VACCINE_DATA))]
    
    bar_width = 0.25
    x_pos = np.arange(len(x))
    
    fig = plt.figure()
    plot = fig.add_subplot(1,1,1)
    
    plot.bar(x_pos - bar_width, unvax_rate, label='Unvaccination Rate', width=0.25)
    plot.bar(x_pos, partial_vax_rate, label='Partial Vaccination Rate', width=0.25)
    plot.bar(x_pos + bar_width, full_vax_rate, label='Full Vaccionation Rate', width=0.25)
    
    plot.set_xticks(x_pos, x)
    
    plot.legend()
    plot.set_xlabel('Age Categories')
    plot.set_ylabel('Vaccination Rate')
    plot.set_title('Average Vaccination Rates Based on Age Group on 2021-10-06')
    
    to_html = mp.fig_to_html(fig)
    html_file = open('vaccine.html', 'w')
    html_file.write(to_html)
    html_file.close

    
    plt.show()   
        
if __name__ == "__main__":
    main()