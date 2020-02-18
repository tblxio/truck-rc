import multiprocessing
import os


def execute(process):
    os.system(f'python3 {process}')




all_processes = (
   './rpi_camera.py', './serialcommunication3.py', './Start_Sbrick.py')

process_pool = multiprocessing.Pool(processes=3)
process_pool.map(execute, all_processes)
