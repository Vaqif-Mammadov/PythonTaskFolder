import os
import shutil

yol=os.getcwd()
try:
    os.mkdir("main_directory")
    os.chdir(yol+"/main_directory")
    os.mkdir("Subdirectory")
except FileExistsError :
    print("Bu adda qovluq var")

# os.chdir(yol)
# for file in os.listdir():
#     if not os.path.isdir(file) and not file.endswith(".py"):
#         shutil.move(file,yol+"\\main_directory\\Subdirectory\\{}".format(file.split("\\")[-1]))

os.chdir(yol+"\\main_directory\\Subdirectory")
for file in os.listdir():
    if file.endswith(".txt"):
        shutil.move(file,yol+"\\main_directory\\{}".format(file.split("\\")[-1]))

