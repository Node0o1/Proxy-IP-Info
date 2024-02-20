import sys
from multiprocessing import Pool as pThread
import utils
from globals import PROCESSES, MAX_TASK


def check_list(in_file= None):
    if(in_file == None):
        in_file=str(input("ENTER PROXY FILE PATH/NAME: "))
    print(f'YOUR PUBLIC IP: {utils.get_pub_ip()}')
    try:
        with open(in_file, mode='r') as fhandle:
            pThread(processes=PROCESSES, maxtasksperchild=MAX_TASK).map(utils.check,['http://'+ str(prx).strip() for prx in fhandle.read().split()]) 
    except FileExistsError as e:
        print(f'{type(e).__name__} ERROR :: {e.args}')
    except Exception as e:
        print(f'{type(e).__name__} ERROR :: {e.args}')

if __name__=="__main__":
    try: check_list(sys.argv[1])
    except: check_list(None)
