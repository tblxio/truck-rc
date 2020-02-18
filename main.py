import multiprocessing
import os

print("main.py launched")

def execute(process):
    os.system(f'python3 {process}')


all_processes = ('./UpDown.py', './GUI.py', './ProximityVisualisation.py', './GetDistance.py')
IPselect = './IPselect.py'

execute(IPselect)
process_pool = multiprocessing.Pool(processes=4)
process_pool.map(execute, all_processes)
