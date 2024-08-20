import os
import shutil

def count_atoms(smiles):
    return len([char for char in smiles if char in {'C', 'H', 'O', 'N', 'F'}])

def convert_smiles_to_alpha(smiles):
    allowed_atoms = {'C', 'H', 'O', 'N', 'F'}
    filtered_atoms = [char for char in smiles if char in allowed_atoms]
    return ''.join(sorted(filtered_atoms))

def contains_any_of(smiles, atoms):
    return any(atom in smiles for atom in atoms)

input_file_path = '/home/esma/Downloads/database.txt'
sdf_directory = '/home/esma/workspace/sdffiles/'  
output_directory = '/home/esma/workspace/filtered_sdf/'

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

with open(input_file_path, 'r') as file:
    lines = file.readlines()

excluded_atoms = ['Cl', 'Br', 'B', 'r', 'S']

filtered_names = set()
for line in lines:
    parts = line.split()
    name = parts[0].strip()
    smiles = parts[1].strip()
    if not contains_any_of(smiles, excluded_atoms) and count_atoms(smiles) <= 10:
        filtered_names.add(name.replace(';', ''))

sdf_files = os.listdir(sdf_directory)
print("Files in the directory:")
for file_name in sdf_files:
    print(file_name)

for name in filtered_names:
    clean_name = name.split(';')[0]
    sdf_file_path = os.path.join(sdf_directory, f"{clean_name}.sdf")
    # Check if the SDF file exists and copy it
    if os.path.exists(sdf_file_path):
        shutil.copy(sdf_file_path, output_directory)
    else:
        print(f"SDF file did not found: {sdf_file_path}")

print("Filtered SDF files corresponding to the SMILES codes have been copied to the directory.")

