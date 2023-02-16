import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_comsol_data(path, gate)->pd.DataFrame:
    full_path = path + f'\{gate}.txt'
    if data_exist(full_path):
        df = pd.read_csv(full_path,
                         sep="\s+",
                         names=['x', 'y', 'z', 'V', 'CD'],
                         skiprows=9)
    return df

def load_comsol_FEM(path: str,
                    gate='S1')->pd.DataFrame:
    full_path = path + f'\{gate}.txt'
    if data_exist(full_path):
        return load_comsol_data(path, gate).loc[:, ['x', 'y']]
    elif data_exist(path):
        raise IOError(f'Dataset of gate {gate} doesn\'t exist.')
    else:
        raise IOError(f'Invalid path: {path}.')
    
def load_comsol_pot(path: str, 
                    gate: str)->pd.DataFrame:
    # read elementary potential
    return load_comsol_data(path, gate).V


def data_exist(path: str):
    # validate the full path (raw string)
    # WindowsPath won't work
    return os.path.exists(path)