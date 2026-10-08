import os,sys
from os.path import dirname, join, abspath

Parent_dir_path = abspath(join(dirname(__file__),'..'))
sys.path.insert(0,Parent_dir_path)

from student_details import student

New = student.Student()

print(New.addition())

print(New.Divition())

print(New.Multiplaycaion())

print(New.Subtraction())
