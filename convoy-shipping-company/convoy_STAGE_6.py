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
            "insert or replace into convoy (vehicle_id, engine_capacity, "
            "fuel_consumption, maximum_load) VALUES (?, ?, ?, ?);", contents)
    cur.execute("""ALTER TABLE convoy
            ADD COLUMN score INT NOT NULL
            DEFAULT 3""")
    conn.commit()
    changes = conn.total_changes
    conn.close()

    if changes == 1:
        print(f'1 record was inserted into {file_name_raw}.s3db')
    else:
        print(f'{changes} records were inserted into {file_name_raw}.s3db')


def get_score(engine_cap, fuel_consump, max_load):
    score = 0
    crit_1 = (fuel_consump * 4.5) / engine_cap
    crit_2 = fuel_consump * 4.5

    if crit_1 <= 1:
        score += 2
    elif crit_1 <= 2:
        score += 1

    if crit_2 <= 230:
        score += 2
    else:
        score += 1

    if max_load >= 20:
        score += 2

    return score


conn = sqlite3.connect(f'{file_name_raw}.s3db')
cur = conn.cursor()

sql_df = pd.read_sql_query('SELECT * FROM convoy;', conn)

sql_df['score'] = sql_df.apply(lambda x: get_score(x['engine_capacity'], x['fuel_consumption'], x['maximum_load']), axis=1)
sql_df.to_csv('testcsv.csv', index=False, header=True)


with open('testcsv.csv', 'r') as fin:
    dr = csv.DictReader(fin)
    contents = [(i['vehicle_id'], i['engine_capacity'], i['fuel_consumption'], i['maximum_load'], i['score']) for i in dr]
    cur.executemany(
            "insert or replace into convoy (vehicle_id, engine_capacity, "
            "fuel_consumption, maximum_load, score) VALUES (?, ?, ?, ?, ?);", contents)
    conn.commit()
conn.close()

json_df = sql_df[sql_df['score'] > 3]
json_df = json_df.drop(['score'], axis=1)
json_rows = json_df.shape[0]

xml_df = sql_df[sql_df['score'] <= 3]
xml_df = xml_df.drop(['score'], axis=1)
xml_rows = xml_df.shape[0]

js = json_df.to_json(orient='records')
json_dict = {'convoy': json.loads(js)}

with open(f'{file_name_raw}.json', 'w') as json_file:
    json.dump(json_dict, json_file)

if json_rows == 1:
    print(f'1 vehicle was saved into {file_name_raw}.json')
else:
    print(f'{json_rows} vehicles were saved into {file_name_raw}.json')

if xml_rows == 0:
    xml_string = "<convoy></convoy>"
    xml_file = open(f'{file_name_raw}.xml', "w")
    xml_file.write(xml_string)
    xml_file.close()
else:
    xml_df.to_xml(path_or_buffer=f'{file_name_raw}.xml', index=False, root_name='convoy', row_name='vehicle', xml_declaration=False)

if xml_rows == 1:
    print(f'1 vehicle was saved into {file_name_raw}.xml')
else:
    print(f'{xml_rows} vehicles were saved into {file_name_raw}.xml')
