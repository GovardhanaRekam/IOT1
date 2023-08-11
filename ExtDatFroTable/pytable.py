import tabula

file_path = "PASSWORDS.pdf"
'''
# Read the PDF into a list of DataFrames (tables)
tables = tabula.read_pdf(file_path, pages='all', multiple_tables=True)

# Assuming the table you want is the first one
df = tables[0]

# Filter for columns 'ID' and 'PASSWORD'
ids = df['ID'].tolist()
passwords = df['PASSWORD'].tolist()

# Print the values
print("IDs:", ids)
print("PASSWORDs:", passwords)
'''
'''
# Read the PDF into a list of DataFrames (tables)
tables = tabula.read_pdf(file_path, pages='all', multiple_tables=True)

all_ids = []
all_passwords = []

# Loop through each table and extract IDs and PASSWORDs
for df in tables:
    if 'ID' in df.columns and 'PASSWORD' in df.columns:
        all_ids.extend(df['ID'].tolist())
        all_passwords.extend(df['PASSWORD'].tolist())

# Print the values
print("All IDs:", all_ids)
print("All PASSWORDs:", all_passwords)
'''
'''
# Read the PDF into a list of DataFrames (tables)
tables = tabula.read_pdf(file_path, pages='all', multiple_tables=True)

all_ids = []
all_passwords = []

# Loop through each table and extract IDs and PASSWORDs
for df in tables:
    if 'ID' in df.columns and 'PASSWORD' in df.columns:
        for index, row in df.iterrows():
            try:
                # Convert the ID value to integer for comparison
                id_value = int(row['ID'])
                
                if 1 <= id_value <= 1000 or id_value > 2000:
                    all_ids.append(id_value)
                    all_passwords.append(row['PASSWORD'])
            except ValueError:
                # This handles the case if the ID value is not an integer, e.g. a header or some other text.
                pass

# Print the filtered values
print("Filtered IDs:", all_ids)
print("Corresponding PASSWORDs:", all_passwords)
'''

# Predefined IDs and passwords
initial_ids = [
    951, 952, 953, 954, 955, 956, 957, 958, 959, 960,
    961, 962, 963, 964, 965, 966, 967, 968, 969, 970,
    971, 972, 973, 974, 975, 976, 977, 978, 979, 980,
    981, 982, 983, 984, 985, 986, 987, 988, 989, 990,
    991, 992, 993, 994, 995, 996, 997, 998, 999, 1000
]

initial_passwords = [
    "ASWHI", "FMGLO", "FMRUP", "LNAVJ", "XVSVU", "AAKOF", "VLCBM", "ECQCA",
    "QUUGJ", "NQVKA", "TEKVE", "IDHXO", "MTVPQ", "MEGFQ", "TMCOD", "FEJGE",
    "GXLSG", "HCGKO", "MSDGM", "GOTEV", "VPDIH", "ANQRW", "SUWSL", "OBVWL",
    "LNKJE", "YMDNA", "KJLFJ", "JBYDM", "FTWCI", "SGVLB", "MURKC", "AQECH",
    "ECFLY", "BCYHS", "YYJLT", "MBGKC", "FKKIM", "WQACS", "SAAWW", "DPLNJ",
    "WDYCV", "UKRIB", "NRPIL", "UIAEY", "EEQNC", "TOKWW", "GPWAE", "GXPPW",
    "UBYOC", "HDAYQ"
]

# Initialize the all_ids and all_passwords lists with the predefined values
all_ids = initial_ids[:]
all_passwords = initial_passwords[:]

# Read the PDF into a list of DataFrames (tables)
tables = tabula.read_pdf(file_path, pages='all', multiple_tables=True)

# Loop through each table and extract IDs and PASSWORDs
for df in tables:
    if 'ID' in df.columns and 'PASSWORD' in df.columns:
        for index, row in df.iterrows():
            try:
                # Convert the ID value to integer for comparison
                id_value = int(row['ID'])
                
                if 1 <= id_value <= 1000 or id_value > 2000:
                    all_ids.append(id_value)
                    all_passwords.append(row['PASSWORD'])
            except ValueError:
                # This handles the case if the ID value is not an integer, e.g. a header or some other text.
                pass
all_ids = [id_val - 1000 if id_val >= 2000 else id_val for id_val in all_ids]
# Adjust the IDs based on their values and prepend the required prefix
formatted_ids = [
    "R20000" + str(id_val) if 1 <= id_val <= 9 else 
    "R2000" + str(id_val) if 10 <= id_val <= 99 else 
    "R200" + str(id_val) if 100 <= id_val <= 999 else 
    "R20" + str(id_val) 
    for id_val in all_ids ]

print(len(all_ids))
print(len(all_passwords))
# Print the combined values
print("Combined IDs:", all_ids)
print("Corresponding PASSWORDs:", all_passwords)
