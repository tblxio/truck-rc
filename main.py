import multiprocessing
import os


def execute(process):
    os.system(f'python3 {process}')


dirname = os.path.dirname(__file__)

all_processes = (
    dirname + '/UpDown.py', dirname + '/GUI.py', dirname + '/ProximityVisualisation.py', dirname + '/GetDistance.py')
IPselect = dirname + '/IPselect.py'

execute(IPselect)
process_pool = multiprocessing.Pool(processes=4)
process_pool.map(execute, all_processes)
