import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib as mpl
'''
图(figure),坐标系(axes),坐标轴(axis),刻度(tick)
点(marker),图例(legend),网格(grid)
'''

mpl.rcParams['font.sans-serif'] = ['SimHei']  # matploblib解决中文显示的问题
mpl.rcParams['axes.unicode_minus'] = False    # 用来正常显示正负号

#fig = plt.figure(figsize = (16,6),dpi=100)#设置dpi
#x = [1,2,3,4,5,6,7,8,9]
#y = [2,3,4,5,6,7,8,9,10]
x = np.linspace(-np.pi,np.pi,256)
y1 = np.cos(x)
y2 = np.sin(x)

plt.plot(x,y1,label='cos(x)',color = 'blue',linewidth = 1.0,linestyle = '-',zorder=1)
plt.plot(x,y2,label='sin(x)',color = 'red',linewidth = 2.0,linestyle = '--',zorder=1)

#显示图例
#loc='upper left'是让图例出现在右上角，也可以不设置该函数，图例会自动调整位置 
plt.legend(loc='upper left') #需在plt.plot函数中指明 label = 'cos(x)'
#plt.legend(['cos(x2)','sin(x2)'],loc='upper left') #也可以用这种方式添加图例


#控制坐标轴边界
plt.xlim(-4,4)
plt.ylim(-1.5,1.5)

#显示坐标轴名字
plt.xlabel('name of x axis')
plt.ylabel('name of y axis')
#显示图片标题
plt.title('sin(x) and cos(x)')
#显示中文标题
#plt.title('数据可视化',fontproperties='SimHei',fontsize=16)
'''
设置字体时，英文直接写，中文需要后面加上fontproperties属性表示中文可见，不乱码
'''

##重新设定坐标轴刻度
#plt.xticks([-4,-2,0,2,4])
#plt.yticks([-4,-2,0,2,4],['minus four','minus two','zero','two','four'])

#图的脊柱
ax = plt.gca()
ax.spines['right'].set_color('none') #指定右边脊柱颜色为透明
ax.spines['top'].set_color('none')
#使用set_position函数将下面以及左边位置脊柱移动到x=0和y=0的位置
#ax.spines['bottom'].set_position(('data',0)) 
ax.spines['left'].set_position(('data',0))

#标注
#画一条红色虚线以及红色实心点；用annotate函数进行文字标记
t = 2*np.pi/3
plt.plot([t,t],[-1.5,np.sin(t)],color='red',linewidth='1.5',linestyle='-.')#画红色虚线
plt.scatter([t],[np.sin(t)],50,color='red')#画红色实心点
plt.annotate(r'$\sin(\frac{2\pi}{3})=\frac{\sqrt{3}}{2}$',#文字部分，latex公式
             xy=(t,np.sin(t)),#表明注释的位置
             xycoords='data',#基于数据的值来选位置
             xytext=(+10,+30),#对于标注相对位置的描述和xy偏差值
             textcoords='offset points',fontsize=12,#标注字体设置
             arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=0.2')#对图中箭头类型的一些设置
             )


#添加文字
plt.text(-2.0,-1.4,'This is the plot of sin(x) and cos(x)',#添加文字的位置和内容
         fontdict={'size':10,'color':'green'}#设置添加文字的大小和颜色
        )


#能见度，用来解决画出来的线和坐标轴有重合的问题
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)#设置刻度标注的字体大小
    #set_bbox就是设置坐标刻度标注周围一个方块范围内的颜色以及能见度
    label.set_bbox(dict(facecolor='white',edgecolor='none',alpha=0.7,zorder=2)) 
    #alpha负责能见度，zorder=2是呼应前面的zorder=1，让更高级别的设置可以覆盖更低级别的设置

#这里尤其要注意的是，想要成功保存的话，一定要把保存语句写在show语句之前！！！否则你保存下来的将是一个新的空白图。
plt.savefig(r'D:\MyFiles\MyCode\figpath.tif', dpi=400, bbox_inches='tight')  #dpi，控制每英寸长度上的分辨率
                                                                              #bbox_inches, 能删除figure

#显示图片,seaborn也用这个函数来显示图片
#plt.show()