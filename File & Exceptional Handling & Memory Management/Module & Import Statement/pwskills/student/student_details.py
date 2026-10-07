import os, sys #functionality for interacting with operating system
from os.path import dirname, join, abspath

parent_dir_path = abspath(join(dirname(__file__), '..')) #To create absolute path of the parent directory of the current script
#__file__  will give the path of current script pwskills/student/student_details.py
#oin(dirname(__file__), '..')>> join the current directory with the parent directory (..)
sys.path.insert(0, parent_dir_path)
#adds the absolute path of the parent directory to the beginning of system path
#it allows to search modules and packages 

# from teacher import teacher_details

def student():
    print("This is student details")

# teacher_details.teacher()