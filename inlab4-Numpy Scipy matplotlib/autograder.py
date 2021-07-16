import utils
import argparse
import os
import inlab4_tasks as stud
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--task', type=str, default='all')
parser.add_argument('--tcdir', type=str, default='testcases')

if __name__=='__main__':
    args = parser.parse_args()
    task = args.task
    tasklist = []
    if task == "all":
        tasklist = list(range(1,6))
    elif task not in map(str, range(1,6)):
        print("task should be between 1 and 5 (both inclusive. given task: {}".format(task))
    else:
        tasklist = [int(task)]
    print("tasklist:", tasklist)
    tcdir = args.tcdir
    task_fnmap = {
        1: 'checkerboard',
        2: 'SimpleNonLinearity',
        3: 'normalise',
        4: 'top_k',
        5: 'is_magic_square'
    }

    for task in tasklist:
        taskfn = getattr(stud, task_fnmap[task])
        tcfilename = os.path.join(tcdir, 'task{}.pkl'.format(task))
        tcdict = utils.load(filename=tcfilename)
        for i in tcdict.keys():        
            vals = list(tcdict[i])
            retval = vals[-1]
            argss = vals[:-1]
            student_retval = taskfn(*argss)
            if task < 5:
                try:
                    iscorrect =  np.allclose(student_retval, retval)
                except Exception as e:
                    # print("exception thrown", e)
                    iscorrect = False
            else:
                iscorrect = retval == student_retval
            if not iscorrect:
                print("Task {}: testcase# {} failed!".format(task, i))
            else:
                print("Task {}: testcase# {} passed!".format(task, i))
