import os
 
#path为批量文件的文件夹的路径
path = r'D:\MyFiles\MyCode\姓名学号=学号姓名\会计12班会计制度设计实训报告'
 
#文件夹中所有文件的文件名
file_names = os.listdir(path)
 
#外循环遍历所有文件名，内循环遍历每个文件名的每个字符
for name in file_names:
 for s in name:
  if s == '1':
   
   index_num=name.index(s)  #index_num为要删除的位置索引
    
   #采用字符串的切片方式删除编号
   os.renames(os.path.join(path,name),os.path.join(path,name[index_num:-5] + name[:index_num] +'.xlsx')) 
   break  #重命名成功，跳出内循环