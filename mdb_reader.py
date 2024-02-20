import pandas as pd
import subprocess
from IPython.display import display

def show_tables(path='./data_exports/315107-Bay-View-Road.mdb'):
    tables = subprocess.check_output(["mdb-tables", path])
    print (tables.decode().split())
    return tables.decode().split()
 
def show_data(path='./data_exports/315107-Bay-View-Road.mdb', table='WENNER_PROBE'):
    tables = subprocess.check_output(["mdb-export", path, table])
    print (tables.decode().split('\n'))
    return tables.decode().split('\n')
 
def convert_df(path, table):
    d = show_data(path, table)
    columns = d[0].split(',')
    data = [i.split(',') for i in d[1:]]
    print(data)
    # df = pd.DataFrame(columns=columns, data=data)
    # display(df)
    # return df 

# show_tables()
# show_data()
convert_df('./data_exports/315107-Bay-View-Road.mdb', 'WENNER_PROBE')