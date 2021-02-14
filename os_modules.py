import os
import shutil
#os.chdir(r"C:\Users\dell\Downloads\python\pytho tutorials\movies2\new")
print(os.getcwd())
#os.mkdir('movies')
#os.mkdir('Upasana')
#print(os.path.exists('movies2'))
#for not to erroroccur in folder creation it can be done like this
# if os.path.exists('movies2'):
#     print("already exists")
# else:
#     os.mkdir('movies2')
# open('movie_ile.txt','a').close()
# os.mkdir(r"E:\ALL VIDEO\movies")
#os.mkdir("new")
#print(os.listdir())
# print(os.listdir(r"E:\ALL VIDEO"))
#______________________________
#if we want to print the listwith its path then that can be done by
# for item in os.listdir():
#     print(os.getcwd()+'\\'+item)
#---------------------------------------
#this can be done by other mtd
# for item in os.listdir():
#      path=os.path.join(os.getcwd(),item)
#      print(path)
#OS MODULE  CONTINUED AND SHUTIL MODULE:
# file_iter=os.walk(r"C:\Users\dell\Downloads\python")
# for current_path,folder_names,file_names in file_iter:
#     print(f"vurrent path:{current_path}")
#     print(f"folders :{folder_names}")
#     print(f"files:{file_names}")
#remove folder
#os.rmdir('Upasana')
# os.mkdir('movies2/new/maggie')
#shutil.rmtree('New')---------Herethe item is permanently deleted i.e not go to the recyclebin
#shutil.copytree('movies2','movies/New_movies2')(COPYING A FOLDER)
#(COPYING FILE CAN BEDONE BY):
#shutil.copy('file2.txt','movies/file2.txt')
#----------------------------
#IF WE WANT TO MOVE A FILE THAT CAN BE DONE BY
#shutil.move('file2.txt','movies/file3.txt')
#MOVINGA FOLDER
shutil.move('file operations','movies/file_op')











