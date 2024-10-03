from ase import Atom
from ase.io import read, write
from ase.io.trajectory import Trajectory
import tqdm
import argparse

from ase.neighborlist import NeighborList, NewPrimitiveNeighborList
#atoms = read("mobley_clean_without_P_F_processed.extxyz")
#print(atoms)
def checkStructure(atoms):
    natoms = len(atoms)
    cutoffs = [5] * natoms
    #nl = NeighborList(cutoffs, skin=0.0)
    nl = NewPrimitiveNeighborList(cutoffs, skin=0.0)
    nl.update(atoms.pbc, atoms.get_cell(), atoms.positions)

    for i in range(len(atoms)):
        indices, offsets = nl.get_neighbors(i)
        for j in indices:
            if j > i:
                distance = atoms.get_distance(i, j)
                if distance < 0.8:
                    return True
        
    return False

atoms_list=read("engrad_non_equ_geoms_clean_nequip_100K_nvt.extxyz", index=":")
print(len(atoms_list))
for i, atoms in enumerate(atoms_list):

    if checkStructure(atoms):
        print("Problematic structure found!")
        print("Frame:", i)
        quit()
    else:
        print("Structure is fine.")


