def count_atoms(smiles):
    return len([char for char in smiles if char in {'C', 'H', 'O', 'N', 'F'}])

def convert_smiles_to_alpha(smiles):
    allowed_atoms = {'C', 'H', 'O', 'N', 'F'}
    filtered_atoms = [char for char in smiles if char in allowed_atoms]
    return ''.join(sorted(filtered_atoms))

def contains_any_of(smiles, atoms):
    return any(atom in smiles for atom in atoms)

with open('/home/esma/Downloads/database.txt', 'r') as file:
    lines = file.readlines()

excluded_atoms = ['Cl', 'Br', 'B', 'r', 'S']

filtered_data = [
    (line.split()[0].strip(), line.split()[1].strip())  # Extract name and SMILES code
    for line in lines
    if not contains_any_of(line.split()[1].strip(), excluded_atoms)
]

# Convert SMILES to alphabetical characters, filter allowed atoms, and filter based on atom count
filtered_smiles_with_names = [
    (name.replace(';', ''), convert_smiles_to_alpha(smiles))  # Remove semicolon from name
    for name, smiles in filtered_data
    if count_atoms(smiles) <= 10
]

# Print results
for name, smiles in filtered_smiles_with_names:
    print(f"{name}: {smiles}")

print("SMILES codes and their names have been printed.")

