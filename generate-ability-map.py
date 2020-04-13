import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.colors as mcolors
import matplotlib as mpl
import pandas as pd
import seaborn as sns

# 导入中文
mpl.rcParams['font.sans-serif'] = ['SimHei']  # matploblib解决中文显示的问题
mpl.rcParams['axes.unicode_minus'] = False    # 用来正常显示正负号

# 启用主题
plt.style.use('ggplot')


# 获取极径范围
def get_range(data_list):
    max = min = 0
    for _, data in data_list.items():
        for v in data:
            if v < min:
                min = v
            if v > max:
                max = v
    return [min, max]


# 生成能力分布图
def generate_ability_map(abilities, data_list, rows=3):
    min, max = get_range(data_list)
    # 根据能力项等分圆
    angles = np.linspace(0, 2 * np.pi, len(abilities), endpoint=False)
    angles = np.append(angles, angles[0])
    # 生成n个子图
    fg, axes = plt.subplots(math.ceil(len(data_list) / rows), rows, subplot_kw=dict(polar=True))
    # 打散为一维数组
    axes = axes.ravel()
    # 获取所有支持的颜色
    colors = list(mcolors.TABLEAU_COLORS)
    # 循环绘制
    i = 0
    for name, data in data_list.items():
        data = np.append(np.array(data), data[0])
        ax = axes[i]
        # 绘制线条
        ax.plot(angles, data, color=colors[i])
        # 填充颜色
        ax.fill(angles, data, alpha=0.7, color=colors[i])
        # 设置角度
        ax.set_xticks(angles)
        # 设置坐标轴名称
        ax.set_xticklabels(abilities)
        # 设置名称
        ax.set_title(name, size=10, color='black', position=(0.5, 0.4))
        # 设置极径最小值
        ax.set_rmin(min)
        # 设置极径最大值(最大值加0.1，要不线条最外圈线显示不完全)
        ax.set_rmax(max + 0.1)
        i = i + 1
    plt.show()


abilities = ['智力', '力量', '速度', '耐力', '能量', '技能']
super_heros = {
    '美国队长': [5, 4, 3, 4, 3, 7],
    '钢铁侠': [6, 3, 5, 5, 3, 3],
    '绿巨人': [6, 7, 3, 7, 1, 5],
    '蜘蛛侠': [5, 4, 5, 4, 2, 5],
    '灭霸': [7, 7, 7, 7, 7, 7],
    '雷神': [2, 5, 6, 7, 6, 6],
    '绯红女巫': [3, 3, 3, 3, 7, 3],
    '黑寡妇': [5, 3, 2, 3, 3, 7],
    '鹰眼': [5, 3, 3, 2, 2, 7],
}
generate_ability_map(abilities, super_heros)


abilities = ['忍', '体', '幻', '贤', '力', '速', '精', '印']
super_heros= {
    '旗木卡卡西': [10, 9, 8, 10, 7, 9, 6, 10],
    '自来也': [10, 9, 6, 9, 9, 9, 10, 9],
    '纲手': [10, 10, 7, 10, 10, 7, 8, 8],
    '宇智波鼬': [10, 9, 10, 10, 7, 10, 5, 10],
}
generate_ability_map(abilities,super_heros, 2)