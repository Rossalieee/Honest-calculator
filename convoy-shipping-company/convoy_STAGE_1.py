import pandas as pd

user_df = input('Input file name\n')
file_name = user_df.split('.')[0]
my_df = pd.read_excel(user_df, sheet_name='Vehicles', dtype=str, engine='openpyxl')
my_df.to_csv(f'{file_name}.csv', index=False, header=True)
new_lines = my_df.shape[0]
if new_lines == 1:
    print(f'{new_lines} line was added to {file_name}.csv')
else:
    print(f'{new_lines} lines were added to {file_name}.csv')
