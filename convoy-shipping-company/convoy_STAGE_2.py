import pandas as pd

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
