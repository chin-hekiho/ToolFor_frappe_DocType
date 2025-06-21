import pandas as pd
import json
import os

def dump_dt(excel_file):
    name = os.path.basename(excel_file).split(".")[0]
    print(f"File: {name}\n")
    
    # Read all sheets from the Excel file into a dictionary
    sheets_dict = pd.read_excel(excel_file, sheet_name=None)

    # Iterate over all sheets and convert them to JSON
    for sheet_name, df_sheet in sheets_dict.items():
        json_data = df_sheet.to_json(orient="records", force_ascii=False)
        print(f"Sheet: {sheet_name}\n")

        arr = []
        for item in json.loads(json_data):
            i = [v for v in item.values()]

            # If there are fewer than 4 elements, fill the missing ones with default values
            if len(i) < 4:
                i.extend([None] * (4 - len(i)))  # Add None for missing values

            field = {"label": i[0], "fieldname": i[1], "fieldtype": i[2]}
            if i[3] is not None and i[3] != 0:
                field["length"] = i[3]
            arr.append(field)

        print(arr)
        
        dt = [{
            "name": name,
            "module": "dev",
            "fields": arr
        }]
        
        # Format the output JSON with indentation
        pretty_json = json.dumps(dt, indent=4, ensure_ascii=False)
        print(pretty_json)
        
        # Create output file name
        output_file = name + "_" + sheet_name + ".json"
        
        # Write the JSON data to the output file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(pretty_json)

# Specify the file path
file = "ToDo.xlsx"
dump_dt(file)

