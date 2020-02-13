import multiprocessing
import os


def execute(process):
    os.system(f'python3 {process}')


dirname = os.path.dirname(__file__)

all_processes = (
    dirname + '/rpi_camera.py', dirname + '/serialcommunication3.py', dirname + '/Start_Sbrick.py')
IPselect = dirname + '/IPselect.py'

execute(IPselect)
process_pool = multiprocessing.Pool(processes=3)
process_pool.map(execute, all_processes)
