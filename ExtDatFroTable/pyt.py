import tabula

file_path = "PASSWORDS.pdf"
'''
# Predefined IDs and passwords
initial_ids = list(range(1, 301))  # Given your list goes from 1 to 300
initial_passwords = [
    # ... Your list of Passwords, truncated here for brevity...
    "IVYKX", "KKUXR", ... , "USNED", "AIWKL"
]
'''
all_ids = []
all_passwords = []

# Read the PDF into a list of DataFrames (tables)
tables = tabula.read_pdf(file_path, pages='all', multiple_tables=True)

# Loop through each table and extract IDs and PASSWORDs
for df in tables:
    id_columns = [col for col in df.columns if 'ID' in col]
    password_columns = [col for col in df.columns if 'PASSWORD' in col]

    for id_col, pass_col in zip(id_columns, password_columns):
        try:
            ids_in_current_col = [int(val) for val in df[id_col].dropna().tolist() if (1 <= int(val) <= 1000 or int(val) > 2000)]
            passwords_in_current_col = [df[pass_col].iloc[i] for i, val in enumerate(df[id_col].dropna().tolist()) if (1 <= int(val) <= 1000 or int(val) > 2000)]

            all_ids.extend(ids_in_current_col)
            all_passwords.extend(passwords_in_current_col)
        except:
            # If any error occurs in conversion to int or extraction, we skip to the next column.
            continue


# Subtract 1000 from IDs that are greater than or equal to 2000
all_ids = [id_val - 1000 if id_val >= 2000 else id_val for id_val in all_ids]

# Convert IDs to string format
formatted_ids = [
    "R20000" + str(id_val) if 1 <= id_val <= 9 else 
    "R2000" + str(id_val) if 10 <= id_val <= 99 else 
    "R200" + str(id_val) if 100 <= id_val <= 999 else 
    "R20" + str(id_val) 
    for id_val in all_ids
]

print(len(formatted_ids))
print(len(all_passwords))
# Print the combined values
print("Combined IDs:", formatted_ids)
print("Corresponding PASSWORDs:", all_passwords)

