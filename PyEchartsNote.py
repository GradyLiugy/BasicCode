from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Pie
from random import randint



'''
# V1 版本开始支持链式调用
bar = (
    Bar()
    .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
)
bar.render()

# 不习惯链式调用的开发者依旧可以单独调用方法
bar = Bar()
bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
bar.render()
'''

def pie_base() -> Pie:
    p = (
        Pie()
        .add('',[list(z) for z in zip(['宝马','法拉利','奔驰','奥迪','大众','丰田','特斯拉'],
                                      [randint(1,20) for _ in range(7)])])
        .set_global_opts(title_opts=opts.TitleOpts(title='Pie-基本示例'))
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}'))
    )
    return p
pie_base().render('pie_pyecharts.html')

def bar_series() -> Bar:
    b = (
    Bar()
    .add_xaxis(['宝马','法拉利','奔驰','奥迪','大众','丰田','特斯拉'])
    .add_yaxis("销量", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("产量", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar的主标题",subtitle='Bar的副标题'))
    )
    return b
bar_series().render('bar_series.html')