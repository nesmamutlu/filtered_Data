import os
from ase.io import read, write

folder_path = "/truba_scratch/emutlu/nequip/works/mobley/data/clean/"


exclude_elements = {"F", "P", "Cl", "I", "B", "Br", "S"}

for filename in os.listdir(folder_path):
    if filename.endswith(".sdf"):
        file_path = os.path.join(folder_path, filename)
        atoms_list = read(file_path, index=":")

        for atoms in atoms_list:
            
            symbols = atoms.get_chemical_symbols()
            
            
            if any(element in symbols for element in exclude_elements):
                continue

            
            atoms.info["label"] = filename.replace(".sdf", "")
            
           
            output_file = os.path.join(folder_path, filename.replace(".sdf", "_filtered.xyz"))
            
            
            write("mobley_clean_without_P_F.extxyz", atoms, append=True)
