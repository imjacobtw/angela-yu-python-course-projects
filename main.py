import os
import pathlib

directory = pathlib.Path(r"E:\code\repos\angela-yu-python-course-projects")

for name in os.listdir(directory):
    if name.startswith("0"):
        og_dir_path = directory / name
        new_dir_path = directory / name[1:]
        os.rename(og_dir_path, new_dir_path)
