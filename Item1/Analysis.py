from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def Salary_Top_10(item_data):
    # Salary Top 10
    # 以Salary为X轴，Salary列中每个（不重复）值出现的次数为Y轴绘制图象分析
    # 数据分析这一行的薪资的大概分布范围，经过分析可以看到数据分析师的薪资主要分布在8-13k*12
    # 这可能与数据分析这个职业的特性有关

    salary_count = item_data['Salary'].value_counts()[0:10]  # 统计出Salary中前10个薪资值

    plt.style.use('ggplot')  # 设置图标格式
    labels = salary_count.index  # 绘制标签
    plt.xlabel('Salary')  # 设置X轴标签
    plt.ylabel('Salary Count')  # 设置Y轴标签
    plt.title('Salary Count')  # 设置图名
    plt.bar(range(len(labels)), salary_count)
    plt.xticks(range(len(labels)), labels, fontsize=12, rotation=90)  # 设置刻度和标签，改变x轴刻度的角度为90度
    plt.show()

def City_Top_10(item_data):
    # City Top 10
    # 以Address为X轴，Address列中排名前10个（不重复）值出现的次数为Y轴绘制图象
    # 分析数据分析这一行的薪资情况，可以看出数据分析师工作的城市主要为北京、上海、
    # 广州和深圳，可能是因为这四个城市比其他城市都发展迅速，其中大型公司的数量也比
    # 较多，相比其他城市对于数据分析师的需求也比较高，相对待遇也比较好，因此数据分
    # 析师比较倾向于这四大城市

    city_count = item_data['Address'].value_counts()[0:10]  # 统计出出现次数最多的前十个城市

    plt.figure(figsize=(10, 6))  # 设置图片大小
    plt.rcParams['font.sans-serif'] = ['simhei']  # 设置默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图象四负号'-'显示为方块的问题
    labels = city_count.index  # 绘制标签
    plt.xlabel('Address')  # 设置X轴标签
    plt.ylabel('Count')  # 设置Y轴标签
    plt.title('Address Count Top 10')  # 设置图名
    plt.bar(range(len(labels)), city_count)
    plt.xticks(range(len(labels)), labels, fontsize=12, rotation=45)  # 设置刻度和标签
    plt.show()


def Position_Salary(item_data):
    # Position & Salary
    # 以工作地点为X坐标，薪资水平为Y坐标，分析因工作地点的转变薪资水平所发生的变化
    # 经过分析可以看出薪资比较高的城市主要有北京、上海、广州、深圳、杭州这几个城市
    # 这与上一次单独对于城市的分析结果相类似，可以看出这些发展迅速的城市对于数据分析师的
    # 的需求比较大，对于数据的重视程度也远大于其他城市

    # print(item_data['Address'],item_data['Salary'])
    plt.rcParams['font.sans-serif'] = ['simhei']  # 设置默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图象四负号'-'显示为方块的问题
    plt.barh(item_data['Address'], item_data['Salary'])  # label=label是为了设置上一行的年份为图例
    plt.xlabel('Address')  # 设置X轴标签
    plt.ylabel('Salary')  # 设置Y轴标签
    plt.title('Position Analyse ')  # 设置标题
    plt.xticks(rotation=45)  # 设置刻度和标签
    plt.show()


def Workexperience_Salary(item_data):
    # Workexperience & Salary
    # 以工作经验为X坐标，薪资水平为Y坐标，分析工作经验对于薪资的影响
    # 经过分析可以看出工作经验在三年以上的数据分析师薪资普遍比较高，
    # 而刚就业的学生薪资在行业中的水平还是比较低的，从中得到工作经验
    # 和薪资之间可能存在一种线性关系

    # print(item_data['Salary'], item_data['Workexperience'])
    plt.rcParams['font.sans-serif'] = ['simhei']  # 设置默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图象四负号'-'显示为方块的问题
    plt.barh(item_data['Workexperience'], item_data['Salary'])  # 绘制柱形图
    plt.xlabel('Address')  # 设置X轴标签
    plt.ylabel('Salary')  # 设置Y轴标签
    plt.title('Workexperience & Salary')  # 设置标题
    plt.xticks(rotation=45)  # 设置刻度和标签
    plt.show()

def Educated_Salary(item_data):
    # Educated & Salary
    # 以学历为X坐标，薪资水平为Y坐标,分析不同的学历对于薪资所产生的影响
    # 通过分析可以看出本科及以上的学历出现的次数做多，并且其薪资也比较好
    # 而大专以上的学历也有一些，而薪资相比于本科及其以上有点低，但是相差
    # 的也不是特别大，硕士及其以上的学历只有一个。因此可以看出数据分析这
    # 个行业对于学历的要求不是特别严格，可能比较注重与个人的技术。

    # print(item_data['Educated'], item_data['Salary'])
    plt.rcParams['font.sans-serif'] = ['simhei']  # 设置默认字体
    plt.rcParams['axes.unicode_minus'] = False  # 解决保存图象四负号'-'显示为方块的问题
    plt.barh(item_data['Salary'], item_data['Educated'])  # 绘制柱形图
    plt.xlabel('Educated')  # 设置X轴标签
    plt.ylabel('Salary')  # 设置Y轴标签
    plt.title('Educated & Salary')  # 设置标题
    plt.xticks(rotation=45)  # 设置刻度和标签
    plt.show()


def Educated_Company(item_data):
    # Educated & Company
    # 以学历为X轴，公司名称为Y轴,分析不同公司对于学历的要求差异,通过分析可以
    # 看出大多数公司对于学历的要求不是特别严格，大专以上基本可以找到一份工作
    # 但是薪资的高低就可能取决于自己的能力

    fig, ax = plt.subplots()
    ax.scatter(item_data['Educated'], item_data['Companyname'])
    ax.set_xlabel('Fandango')  # 设置x轴名称
    ax.set_ylabel('Rotten Tomatoes')  # 设置y轴名称
    plt.title('Educated & Company')
    # plt.xticks(rotation=90)                                      #设置刻度和标签
    plt.show()


def City_Distribution(item_data):
    # City Distribution
    # 绘制城市的分布饼图，对数据分析师主要工作的城市进行展示
    city_count = item_data['Address'].value_counts()
    sum = 0
    for i in range(26):
        sum += city_count[i]
    list1 = []
    rate = 0
    for j in range(26):
        rate = city_count[j] / sum
        list1.append(rate)


    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    label_list = city_count.index  # 各部分标签
    size = list1  # 各部分大小

    patches, l_text, p_text = plt.pie(size, labels=label_list, labeldistance=1.1, autopct="%1.1f%%", shadow=False,
                                      startangle=90, pctdistance=0.6)
    plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.legend()
    plt.show()


def Educated_Distribution(item_data):
    # Educated Distribution
    # 绘制学历的分布饼图，对数据分析师学历要求进行展示
    edu_count = item_data['Educated'].value_counts()  # 统计不同城市的人员分布情况
    print(edu_count)

    sum = 0
    list2 = []
    rate = 0
    for i in range(5):
        sum += edu_count[i]
        # 将统计结果放入list2列表中
    for j in range(5):  # 计算出数据分析师在不同城市中的比例
        rate = edu_count[j] / sum
        list2.append(rate)
    print(list2)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    label_list = edu_count.index  # 各部分标签
    size = list2  # 各部分大小
    explode = [0.05, 0, 0, 0, 0]  # 各部分突出值

    patches, l_text, p_text = plt.pie(size, labels=label_list, explode=explode, labeldistance=1.1, autopct="%1.1f%%",
                                      shadow=False, startangle=90, pctdistance=0.6)
    plt.axis("equal")  # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.legend()
    plt.show()


def main():
    item_data = pd.read_csv('清洗后数据集.csv', encoding='utf-8')

    # 过滤数据，因为面议的薪资不确定，所以过滤掉数据集中所有出现面议的那一行数据
    #item_data = item_data[item_data['Salary'] != '面议']

    item_data.info()  # 描述数据集

    item_data.shape  # 描述数据集的大小

    item_data.describe()  # 随数据及进行简单的描述

    len(item_data['Address'].unique())  # 统计数据集中的Address列有多少个值是独立不重复的


    City_Distribution(item_data)
    City_Top_10(item_data)

    Educated_Salary(item_data)
    Educated_Company(item_data)
    Educated_Distribution(item_data)

    Position_Salary(item_data)
    Position_Salary(item_data)

    Salary_Top_10(item_data)
    Workexperience_Salary(item_data)
main()