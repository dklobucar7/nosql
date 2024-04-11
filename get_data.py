''' Import podataka: https://archive.ics.uci.edu/dataset/890/aids+clinical+trials+group+study+175'''
from ucimlrepo import fetch_ucirepo 
import pandas as pd
import json
  
# fetch dataset 
aids_clinical_trials_group_study_175 = fetch_ucirepo(id=890) 


# FEATURES
# data - pandas dataframes
X = aids_clinical_trials_group_study_175.data.features 
print("\n features\n----------\n")
print(X)

# Save data FEATURES as JSON file 
json_file_path = 'aids_clinical_trials_group_study_175_data_features.json'
X.to_json(json_file_path, orient='records', lines=True)

# TARGETS
# data - pandas dataframes
y = aids_clinical_trials_group_study_175.data.targets 
print("\n targets\n----------\n")
print(y)

# Save data TARGETS as JSON file
json_file_path = 'aids_clinical_trials_group_study_175_data_targets.json'
y.to_json(json_file_path, orient='records', lines=True)

# METADATA
print("\nmetadata\n----------")
print(aids_clinical_trials_group_study_175.metadata) 
z = aids_clinical_trials_group_study_175.metadata

# Save METADATA as JSON file
json_file_path_metadata = 'aids_clinical_trials_group_study_175_data_metadata.json'
with open(json_file_path_metadata, 'w') as json_file:
    json.dump(z, json_file)


# VARIABLES 
print("\nvariable\n----------")
print(aids_clinical_trials_group_study_175.variables) 
w = aids_clinical_trials_group_study_175.variables

# Convert DataFrame to dictionary
w_dict = w.to_dict(orient='records')

# Save VARIABLE as JSON file
json_file_path_variable = 'aids_clinical_trials_group_study_175_data_variable.json'
with open(json_file_path_variable, 'w') as json_file:
    json.dump(w_dict, json_file)

# ---------------------------- INDEXING -------------------------------  
# FEATURES 
# Add column index on features table
X['index'] = range(1, len(X) +1)
print("\n\nPrinting Features with a new index column\n----------")
print(X)

# TARGETS
# Add column index on targets table
y['index'] = range(1, len(y) + 1)
print("\n\nPrinting Targets with a new index column\n----------")
print(y)

# MERGE DOCUMENTS with index column
merge_docs = X.merge(y)
print("\n\nPrinting MERGE Documents\n-----------------------------")
print(merge_docs)

# Drop a index column
merge_docs = merge_docs.drop(columns=['index'])
print("\n\nPrinting MERGE Documents without INDEX column\n-----------------------------")
print(merge_docs)

print("\nSPREMI U JSON MERGANO\n")
# Save Merge docs to json 
json_file_merge_docs = 'aids_clinical_trials_group_study_175_data_merge_docs.json'
merge_docs.to_json(json_file_merge_docs, orient='records', lines=True)
print("\nSPREMLJENO\n")
# Save to .csv
merge_docs.to_csv('data.csv')

# Save to excel
excel_file_path = 'data.xlsx'
merge_docs.to_excel(excel_file_path, index=True)