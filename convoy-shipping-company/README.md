# Convoy Shipping Company Project
You're employed at "Convoy", a family transport company. Things are not going well financially, so your bosses want you to create a database to manage the company's assets in a better way and introduce scoring machines to automate some work. You will be dealing with different file formats to export data to various systems.

This project helps to learn how to: export data from an XLSX file to a CSV format, prepare the data to populate an SQLite database, how scoring machines are built, and how to select which data should be exported to other systems (in JSON and XML formats).

**Libraries/tools used**:
* Pandas
* Sqlite3
* csv
* json

## Project Stages
### Stage 1:
**About:** "Convoy" experiences financial problems. You suggested making a single database that contains every company's vehicle to plan the logistics, and your management agreed. You will take a closer look at different parameters: the engine capacity, the maximum load, the fuel consumption. The data has already been collected, all you need is to output it to a CSV file.

**Objectives:**
* Prompt the user to give a name for the input Excel file (complete with the .xlsx extension). For the prompt message, use `Input file name` followed by a newline.
* Import a sheet named Vehicles from the entered XLSX file to a CSV file.
* The CSV file should have the same name as the XLSX file but it should have the .csv extension (you can take the test table below).
* Program should import only the headers, omitting indexes.
* Count the number of entries imported to the CSV file and print them out to standard output; the headers should not be counted.
* Program should output the following message: `X lines were imported to *%file_name%.csv*` or `1 line was imported to *%file_name%.csv*` , where X is the number of imported lines.
* For example: `4 lines were imported to convoy.csv`

### Stage 2:
**About:** As usual, no one consulted the expert (you) on how to fill the table. Another employee mixed things up and just copy-pasted entries from various documents with different formats. Luckily, no data is missing! You definitely need to clear the data from the prefixes and suffixes so that you can calculate them later. Also, you are not sure that this is the final Excel version. So, your program must include previous functionality.

**Objectives:**
* Prompt the user to give a name for the input file (complete with the *.xlsx* or *.csv* extension).
* If your file is *.xlsx*, convert it to *.csv*.
* If your file is *.csv* correct the data right in the file (every cell of the output file, except headers, should contain only one integer number).
* Count the number of the cells corrected by your script.
* Write the corrected data to a CSV file, add the [CHECKED] suffix to your file. For example: *%file_name%[CHECKED].csv*.
* Program should output the following message for the converted CSV file: `X cells were corrected` or `1 cell was corrected`, where X is the number of corrected cells. Include the output file name.
For example: `4 cells were corrected in *%file_name%[CHECKED].csv*`.
* Display all the previous outputs for the conversions you have made earlier.

### Stage 3:
**About:** You are ready to create an SQLite3 database. Your bosses have some ideas on how to use the database for scoring in the future, so be ready for that! Unfortunately, it's an offer you can't refuse... The final Excel version is not ready yet. Write an algorithm that converts a corrected CSV file into an SQLite3 database.

**Objectives:**
* Prompt the user to give a name for the input file (complete with the *.xlsx*, *.csv*, or *[CHECKED].csv* extension).
* If your file is .xlsx or .csv, perform all the previous transformations in the correct order, until you get a file that ends with *%...%[CHECKED].csv*.
* If the file ends with *%...%[CHECKED].csv*, create an SQLite3 database with the CSV file name, change its extension to *.s3db*. Remove the *[CHECKED]* suffix. For example, *%file_name%[CHECKED].csv* should be changed to *%file_name%.s3db*.
* Use "convoy" as the name for your database table.
* Use headers from the CSV file as the names of the table columns.
* The vehicle_id column should have the INTEGER type; make sure it's PRIMARY KEY.
* Other columns should have the INTEGER type with NOT NULL attributes.
* Insert the entries from your *%...%[CHECKED].csv* file.
* Count the number of entries inserted into the database.
* Program should output the following message: `X records were inserted` or `1 record was inserted`, where X is a number of inserted records and the output file name.
For example: `4 records were inserted into *%file_name%.s3db*`.
* Display all the previous outputs for the conversions you have made.


### Stage 4:
**About:** Your database is ready. As you may have expected, you still don't have the final Excel version. Your boss told you that you will have to export part of the database to two different systems. You don't know which data goes where, but rumor has it you will need a scoring function for this. For now, your algorithm should export all the database entries. The first system needs the data in the JSON format.

**Objectives:**
* Prompt the user to give a name for the input file (complete with the *.xlsx*, *.csv*, *[CHECKED].csv* or *.s3db* extension).
* If your file is *.xlsx* or *.csv*, or it ends with the *%...%[CHECKED].csv*, perform all previous transformations in the correct order until you get an SQLite3 file.
* Once you have an SQLite3 file, generate a JSON file with the same name; use the *.json* extension.
* The JSON object should have the following structure:
```
{
    "convoy": [
        {
            "vehicle_id": 2,
            "engine_capacity": 200,
            "fuel_consumption": 25,
            "maximum_load": 70
        },
        {
            "vehicle_id": 1024,
            "engine_capacity": 500,
            "fuel_consumption": 80,
            "maximum_load": 150
        }
    ]
}
```
* Save the data to a file as a JSON object .
* Count the number of entries exported to the JSON file.
* Program should output the following message: `X vehicles were saved` or `1 vehicle was saved`, where X is a number of inserted entries. It should also include the output file name.
For example: `10 vehicles were saved into *%file_name%.json*`.
* Display all the previous outputs for the conversions you have made.

### Stage 5:
**About:** It's time to make the final transformation. You need to convert your SQLite3 database to XML. In this stage, your algorithm should export all the database entries. The final Excel file is expected next week: they promised.

**Objectives:**
* Prompt the user to give a name for the input file (complete with the *.xlsx*, *.csv*, *[CHECKED].csv* or *.s3db* extension).
* If your file is *.xlsx* or *.csv*, or it ends with *%...%[CHECKED].csv*, perform all the previous transformations in the correct order until you get an SQLite3 file.
* If your file is *.s3db*, generate a fresh JSON file, and XML with the same name, and the extensions *.json* and *.xml*. Both files should have all the entries from the SQLite3 file.
* An XML file with two entries should look like this:
```
<convoy>
    <vehicle>
        <vehicle_id>2</vehicle_id>
        <engine_capacity>200</engine_capacity>
        <fuel_consumption>25</fuel_consumption>
        <maximum_load>70</maximum_load>
    </vehicle>
    <vehicle>
        <vehicle_id>4</vehicle_id>
        <engine_capacity>220</engine_capacity>
        <fuel_consumption>55</fuel_consumption>
        <maximum_load>110</maximum_load>
    </vehicle>
</convoy>
```
* Save the data to the XML file. It can be either a single string or a formatted block of text as in the example above.
* Count the number of entries exported to the XML file.
* Your program should output the following message: `X vehicles were saved` or `1 vehicle was saved`, where X is the number of inserted entries. It should include the output file name.
For example: `10 vehicles were saved into *file_name.xml*`.
* Display all the previous outputs for the conversions you have made.

### Stage 6:
**About:** The requirements for scoring function have been defined. And it looks like you have the final version of the Excel file. It's time to prepare the scoring function and export the selected entries to JSON and XML files.

The idea of scoring function is to define under what conditions the scoring points are to be given. The next step is to determine how many points are enough to qualify or reject the testing object.

In our case, the management clarified some key issues:
1. Number of pitstops. If there are two or more gas stops on the way, the object has 0 points. One stop at the filling station means 1 point. No stops — 2 scoring points.
2. Fuel consumed over the entire trip. If a truck burned 230 liters or less, 2 points are given. If more — 1 point.
3. Truck capacity. If the capacity is 20 tones or more, it gets 2 points. If less — 0 points.

It was found that the average route length is 450 km. Do not include the return path: 450 kilometers is the whole route. Remember that the `engine_capacity` is in liters, the `fuel_consumption` is in liters/100 kilometers, and the `maximum_load` is in tonnes.

**Objectives:**
* Prompt the user to give a name for the input file (complete with the *.xlsx*, *.csv*, *[CHECKED].csv* or *.s3db* extension).
* If your file is *.xlsx* or *.csv*, or it ends with *%...%[CHECKED].csv*, perform all the previous transformations in the correct order.
* Add the score column to *.s3db* files. Populate the column with the scoring points, according to the algorithm described above. The score column should be added during the conversion from *%...%[CHECKED].csv* to *.s3db*.
* Generate JSON and XML files according to the scoring points. All entries with a score of greater than 3 should be exported to the JSON file, others to the XML file.
* The score column should not be exported to JSON and XML files.
* Count the number of entries imported to JSON and XML files.
* Your program should output the following message: `X vehicles were saved` or `1 vehicle was saved`, where X is the number of inserted entries. The program should include the output file name. For example:
`9 vehicles were saved into *%file_name%.json*`
`0 vehicles were saved into *%file_name%.xml*`
* Display all the previous outputs for the conversions you have made.

**Example:**
```
Input file name
> data_final_xlsx.xlsx
19 lines were added to data_final_xlsx.csv
3 cells were corrected in data_final_xlsx[CHECKED].csv
19 records were inserted into data_final_xlsx.s3db
12 vehicles were saved into data_final_xlsx.json
7 vehicles were saved into data_final_xlsx.xml
```
