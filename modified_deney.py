from ase.io import read, write
import matplotlib.pyplot as plt
import numpy as np

atoms_list = read("/home/esma/workspace/engrad_non_equ_geoms_clean_without_P_F.extxyz", index=":")



filtered_energies = []

for atoms in atoms_list:
    energy_per_atom = atoms.get_potential_energy() / len(atoms)   
    #energy_per_atom = atoms.get_potential_energy()
    if energy_per_atom < -800:    
        continue
    filtered_energies.append(energy_per_atom)  
    write("engrad_non_equ_geoms_clean_without_P_F_eng800.extxyz", atoms, append=True)

quit()
#print(filtered_energies)

plt.figure(figsize=(8,6))
plt.hist(filtered_energies, bins=30, edgecolor='black')
plt.xlabel('energy')
plt.ylabel('frekans')
plt.grid(True)
plt.show()
    #symbols = atoms.get_chemical_symbols()
    #if "F" in symbols or "P" in symbols:
    #    continue

    #write("engrad_non_equ_geoms_clean_without_P_F.extxyz", atoms, append=True)
