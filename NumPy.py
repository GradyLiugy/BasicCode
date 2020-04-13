import numpy as np 
'''
在NumPy中默认不采用矩阵运算，而是数组(ndarray)运算。
矩阵只是二维，而数组可以是任何维度，因此数组运算更通用些。
通常我们也把n维数组称为张量
'''

'''
创建数组（array）
1.按部就班的np.array()用在列表和元组上
2.定隔定点的np.arange()和np.linspace()
3.一步登天的np.ones(),np.zeros(),np.eye()和np.random.random()

注：用函数print()打印numpy数组就没有array()的字样了，只有其内容，
    而且元素之间的逗号也没有了

'''
a = [3.5, 4.3, 5.2, 6.7, 8.4]
print(np.array(a))

b = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]] #用三维列表生成三维数组
print(np.array(b))

c = np.arange(2,8,2) #arange(start,stop,step)
print(c)

d = np.linspace(2,10,10) #linspace(start,stop,num)
print(d)

e = np.zeros(5) #创建全是0的n维数组
print(e)
f = np.ones((5,3)) #创建全是1的n维数组
print(f)
g = np.random.random((5,3)) #创建随机n维数组
print(g)
h = np.eye(4,k=1) #创建对角矩阵（二维数组），
                  #默认参数k=0，代表1落在对角线上，
                  #k=1，代表1落在对角线右上方；k=-1，代表1落在对角线左下方
print(h)


'''
数组的变形
重塑(reshape)和打平(ravel,flatten)
'''
arr = np.arange(12)
print(arr)
print(arr.reshape((4,3)))

print(arr.reshape((2,-1))) #当你重塑高维矩阵时，不想花时间算某一维度的元素个数时，
                           #可以用-1代替，程序会自动帮你计算出来。

ravel_arr = arr.ravel() #用ravel()或flatten()函数将n维数组arr打平成一维数组
print(ravel_arr)


'''
数组的计算
1.元素层面计算，包括：加减乘除，倒数、平方、指数、对数、比较等
2.线性代数计算，包括：转置、求逆、相乘等
 （在NumPy中默认不采用矩阵运算，而是数组(ndarray)运算。
   矩阵只是二维，而数组可以是任何维度，因此数组运算更通用些。）
'''
#1.元素层面计算
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.ones((2,3)) * 2
print(arr1,'\n',arr2)
#加减乘除
print(arr1 + arr2 + 1)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
#倒数、平方、指数、对数
print(1 / arr1)
print(arr1 ** 2)
print(np.exp(arr1))
print(np.log(arr1))
#比较
print(arr1 > arr2)

#2.线性代数计算
arr2d = np.array([[1,2],[3,1]]) #创建数组
A = np.asmatrix(arr2d) #创建矩阵

#转置
print(arr2d.T) #数组用arr2d.T或arr2d.transpose()转置
print(arr2d.transpose()) 
print(A.T) #矩阵用A.T转置，因为.T只适合二维数据

#求逆
print(np.linalg.inv(arr2d))
print(A.I)
print(A ** -1)

#相乘
#数组相乘是在元素层面进行，矩阵相乘就是数学定义的矩阵相乘
arr1d = np.array([1,2]) #定义一维数组
B = np.asmatrix(arr1d).T
print(arr2d * arr1d)
print(A * B)
print(np.dot(arr2d,arr2d)) #在数组上实现矩阵相乘向量和矩阵相乘矩阵

'''
广播机制计算
当对两个形状不同的数组按元素操作时，可能会触发广播机制。
具体做法，先适当复制元素使得这两个数组形状相同后再按元素操作，两个步骤：
1.广播轴：比对两个数组的维度，将形状小的数组的维度（轴）补齐
2.复制元素：顺着补齐的轴，将形状小的数组里的元素复制，使得最终形状和另一个数组吻合
'''
a1_3 = np.array([1,2,3])
b3_1 = np.array([[4],[5],[6]])
c = a1_3 + b3_1
print('a1_3 is:\n',a1_3)
print('b3_1 is:\n',b3_1)
print('c = a1_3 + b3_1 = :\n',c)