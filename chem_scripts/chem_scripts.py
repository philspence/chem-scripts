import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem, Draw
import os
from os.path import join


def sdfs_to_mols(sdfs):
    mols = []
    for i in sdfs:
        suppl = Chem.SDMolSupplier(i)
        num = 0
        for mol in suppl:
            mol.SetProp('_Name', f'{i}_mol_{num}')
            mols.append(mol)
            num += 1
    return mols


def sdfs_in_dir(dir_path):
    return [join(dir_path, f) for f in os.listdir(dir_path) if f.endswith('.sdf')]


def mols_to_img_file(mols, out_file, per_row=4, img_size=(600, 600), legends=False):
    if legends:
        img = Draw.MolsToGridImage(mols, molsPerRow=per_row, subImgSize=img_size,
                                   legends=[m.GetProp("_Name") for m in mols])
    else:
        img = Draw.MolsToGridImage(mols, molsPerRow=per_row, subImgSize=img_size)
    img.save(out_file)
    return


def dir_sdfs_to_img_file(dir_path, legends=False):
    sdfs = sdfs_in_dir(dir_path)
    mols = sdfs_to_mols(sdfs)
    mols_to_img_file(mols, join(dir_path, 'grid_image.png'), legends=legends)
    return


def display_mols(mols):
    if type(mols) == rdkit.Chem.rdchem.Mol:
        mols = [mols]
    for mol in mols:
        Draw.ShowMol(mol, size=(400, 400))
