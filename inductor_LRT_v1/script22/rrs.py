import yaml
import os
import subprocess
import random
import csv
import time
import csv
import numpy as np
import math
import pandas as pd
import shutil

#from pycaret.regression import load_model



REFERENCE_SCRIPT_FILE_NAME = f'run_ansys_ref.py'
f = open("../computer_name.txt", 'r')
COMPUTER_NAME = f.readline()
																																																

REFERENCE_SCRIPT_FILE_NAME = f'run_ansys_ref.py'

def random_choice(X) :
    return round(np.random.choice( np.arange( X[0] , X[1]+X[2] , X[2]) ),X[3])
    
def run_simul(version_idx_str):
    #0 Initialize random variables

    N1_range = [2, 10, 1, 0]

    w1_range = [20, 60, 0.1, 1] # under, upper, resolution
    l1_range = [5, 15, 0.1, 1]
    l2_range = [5, 40, 0.1, 1]
    h1_range = [25, 50, 0.1, 1]

    per_range = [1000,10000,100,0]

    space1_range = [5, 20, 0.1, 1] 
    space2_range = [5, 20, 0.1, 1] 
   
    coil_width_range = [2, 15, 0.1, 1] 
    
    move_z_range = [1,6,0.1,1]

    offset_range = [-15,15,0.1,1]

    gap_range = [0,10,0.1,1]

    freq_range = [10000, 100000, 1000, 0]

    air = 500



    # Design 1

    N1 = random_choice(N1_range)

    offset = random_choice(offset_range)
    
    move_z = random_choice(move_z_range)

    coil_width = random_choice(coil_width_range)

    per = random_choice(per_range)

    space1 = random_choice(space1_range)
    space2 = random_choice(space2_range)

    w1 = random_choice(w1_range)
    l1 = random_choice(l1_range)
    l2 = random_choice(l2_range)
    h1 = random_choice(h1_range)

    gap = random_choice(gap_range)

    freq = random_choice(freq_range)

    skin = (1.678*10**-8/(3.1415*freq*1.2566*10**-6))**0.5*1000

    height_h = 1.5*(coil_width + move_z) + offset
    height_l = (1-N1)*(coil_width + move_z) + offset - coil_width/2
    height = 1.5 * N1 * (coil_width + move_z) + offset
    length = coil_width + space2
    core_height = h1/2

   
    if length>l2 :
        l2_range = [length+ 5, length + 40, 0.1, 1]
        l2 = random_choice(l2_range)
        
    
    if height_h > core_height or height_l < -core_height:
        h1_new_range = [height+10,height+40, 0.1, 1]
        h1 = random_choice(h1_new_range)
    

   
  


    #FIXME : add some variables


    #0.5 Config Identifier-Variable set.
    config = {
        "$VERSION_IDX_STR"  :   version_idx_str,
        "$air"  :  air,
        "$N1"  :  N1,
        "$w1"  :  w1,
        "$l1"  :  l1,
        "$l2"  :  l2,
        "$h1"  :  h1,
        "$gap" : gap,
        "$per" : per,
        "$space1"  :  space1,
        "$space2"  :  space2,
        "$coil_width"  :  coil_width,  
        "$move_z"  :  move_z,
        "$offset"  :  offset,
        "$freq"    :  freq,
        "$skin"    :  skin,
        #FIXME : add some idt : variables
    }


    #1 Make Folder
    folder_name = f'SIMUL_{version_idx_str}'
    os.makedirs(f'.\ML\SIMUL_{version_idx_str}')


    #2 Make Variable info file
    with open(f'.\ML\SIMUL_{version_idx_str}\info.yaml', "w") as info_file:
        yaml.dump(config,info_file)


    #3 Make python script file
    #Load file string
    
    ref_script_str = ""
    with open(REFERENCE_SCRIPT_FILE_NAME) as f :
        lines = f.readlines()
    ref_script_str = "\n".join(lines)

    #Change Identifiers
    for idt, var in config.items() :
        ref_script_str = ref_script_str.replace(idt, str(var))

    #Save file
    with open(f'.\\ML\\SIMUL_{version_idx_str}\\run_ansys_{version_idx_str}.py',"w") as f :
        f.write(ref_script_str)


    #4 make batch file.
    filepath2 = os.path.join('ML',folder_name,f'run_bat_{version_idx_str}.bat')
    with open(f'.\\ML\\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat',"w") as f :
        f.write(f'"C:\\Program Files\\AnsysEM\\AnsysEM21.1\\Win64\\ansysedt.exe" -iconic -runscriptandexit ".\\run_ansys_{version_idx_str}.py"')


    workingDir = f'.\\ML\\SIMUL_{version_idx_str}'
    executeFile = f'Y:\\git\\ML_inductor\\inductor_LRT_v1\\script22\\ML\\SIMUL_{version_idx_str}\\run_bat_{version_idx_str}.bat'
    os.chdir(workingDir)
    try :
        os.system(executeFile)
        print("success")
    except :
        time.sleep(1)
        print("fail")


    temp1 = pd.read_csv(f'Y:\git\\ML_inductor\inductor_LRT_v1\script22\ML_data\inductance_{version_idx_str}.csv', sep=",")
    temp1 = temp1.to_numpy()
    
  
    temp2 = pd.read_csv(f'Y:\git\ML_inductor\inductor_LRT_v1\script22\ML_data\loss_{version_idx_str}.csv', sep=",")
    temp2 = temp2.to_numpy()

    parameter = np.array([N1,w1,l1,l2,h1,per,space1,space2,coil_width,move_z,offset,freq])

    temp1 = np.append(parameter,temp1)
    temp2 = np.append(parameter,temp2)


    print(temp1)
    print(temp2)
    


    data1 = np.loadtxt(f'Z:\Autosimul_data\inductor\inductor_LRT_v1\{COMPUTER_NAME}\script22\inductance.csv', delimiter=",")
    new_data1 = np.vstack((data1, temp1))
    np.savetxt(f'Z:\Autosimul_data\inductor\inductor_LRT_v1\{COMPUTER_NAME}\script22\inductance.csv',new_data1,delimiter=",")

    data2 = np.loadtxt(f'Z:\Autosimul_data\inductor\inductor_LRT_v1\{COMPUTER_NAME}\script22\loss.csv', delimiter=",")
    new_data2 = np.vstack((data2, temp2))
    np.savetxt(f'Z:\Autosimul_data\inductor\inductor_LRT_v1\{COMPUTER_NAME}\script22\loss.csv',new_data2,delimiter=",")



for i in range(1, 10000): 

    #run_simul(i)
    print({i})

    try :
        try:
            os.remove(f'.\ML_aedt\ML22.aedt.lock')
        except:
            time.sleep(1)
        if os.path.isfile(f'.\ML_aedt\ML22.aedt') :
            os.remove(f'.\ML_aedt\ML22.aedt')
        time.sleep(1)	

        shutil.copy(f'.\ML_aedt\ML_ref.aedt',f'.\ML_aedt\ML22.aedt')
        time.sleep(1)

        try:
            run_simul(i)
        except Exception as e: 
            print(f'error number {i}')
            print(e)

        if os.path.isfile(f'.\ML_aedt\ML22.aedt') :
            os.remove(f'.\ML_aedt\ML22.aedt')
        time.sleep(1)	

        shutil.rmtree(f'.\ML_aedt\ML22.aedtresults')
        try:
            os.remove(f'.\ML_aedt\ML22.aedt.lock')
        except:
            time.sleep(1)
    except :
        time.sleep(1)	
    
    time.sleep(1)


os.system("pause")
