import pandas as pd
import sqlite3
import csv
import json

user_df = input('Input file name\n')
file_name = user_df.split('.')[0]
file_extension = user_df.split('.')[1]

if file_extension == "xlsx":
    excel_file = pd.read_excel(user_df, sheet_name='Vehicles', dtype=str, engine='openpyxl')
    excel_file.to_csv(f'{file_name}.csv', index=False, header=True)
    new_lines = excel_file.shape[0]
    if new_lines == 1:
        print(f'1 line was added to {file_name}.csv')
    else:
        print(f'{new_lines} lines were added to {file_name}.csv')

if '[CHECKED]' not in file_name and file_extension != 's3db':
    my_df = pd.read_csv(f'{file_name}.csv')
    df2 = my_df.replace(regex=[r'\D'], value='')
    df2.to_csv(f'{file_name}[CHECKED].csv', index=False, header=True)
    differences_df = my_df.eq(df2)
    dif_cells = differences_df.values.tolist()
    dif_cells = [x for y in dif_cells for x in y]
    counter = dif_cells.count(False)
    if counter == 1:
        print(f'1 cell was corrected in {file_name}[CHECKED].csv')
    else:
        print(f'{counter} cells were corrected in {file_name}[CHECKED].csv')

    file_name_raw = file_name
elif '[CHECKED]' in file_name:
    file_name_raw = file_name.removesuffix('[CHECKED]')
else:
    file_name_raw = file_name

if file_extension != 's3db':
    conn = sqlite3.connect(f'{file_name_raw}.s3db')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS convoy
            (vehicle_id INT PRIMARY KEY,
            engine_capacity INT NOT NULL,
            fuel_consumption INT NOT NULL,
            maximum_load INT NOT NULL);""")

    with open(f'{file_name_raw}[CHECKED].csv', 'r') as fin:
            dr = csv.DictReader(fin)
            contents = [(i['vehicle_id'], i['engine_capacity'], i['fuel_consumption'], i['maximum_load']) for i in dr]

    cur.executemany(
            "insert or replace into convoy (vehicle_id, engine_capacity, fuel_consumption, maximum_load) VALUES (?, ?, ?, ?);", contents)
    conn.commit()
    changes = conn.total_changes
    conn.close()

    if changes == 1:
        print(f'1 record was inserted into {file_name_raw}.s3db')
    else:
        print(f'{changes} records were inserted into {file_name_raw}.s3db')

conn = sqlite3.connect(f'{file_name_raw}.s3db')
cur = conn.cursor()

cur.execute('SELECT * FROM convoy;')
row_headers = [x[0] for x in cur.description]
results = cur.fetchall()
conn.close()
json_data = []
count = 0
for result in results:
    json_data.append(dict(zip(row_headers, result)))
    count += 1
json_dict = {'convoy': json_data}

with open(f'{file_name_raw}.json', 'w') as json_file:
    json.dump(json_dict, json_file)

if count == 1:
    print(f'1 vehicle was saved into {file_name_raw}.json')
else:
    print(f'{count} vehicles were saved into {file_name_raw}.json')
