# 导入数据分析包
import pandas as pd
import numpy as np

# 导入csv数据
# dtype=str，最好读取的时候都以字符串的形式读入，不然可能出现数据失真。比如00119读成119
file_name = 'eng-daily-01011987-12311987.csv'
DataDF = pd.read_csv(file_name, encoding="ISO-8859-1", dtype=str)

#####Step1：数据预处理

# 1 从宏观角度：查看dataframe的信息
DataDF.info()
# 1.1 查看每一列的数据类型
print("\n每一列的数据类型：")
print(DataDF.dtypes)
# 1.2 查看行/列数
print("\n行列数：")
print(DataDF.shape)

# 2 检查缺失数据
print("\n每列缺失数据：")
print(DataDF.isnull().sum().sort_values(ascending=False))  # 这是检查每列缺失数据的数量的最快方法

# 3 抽出一部分数据，人工直观地理解数据的意义，尽可能发现一些问题
print("\n抽出一部分数据：")
print(DataDF.head())

#####Step2：调整数据类型

# 1 字符串转换为数值
# 1.1 整型
DataDF['Year'] = DataDF['Year'].astype(int)
DataDF['Month'] = DataDF['Month'].astype(int)
DataDF['Day'] = DataDF['Day'].astype(int)
# 1.2 浮点型
DataDF['Max Temp (Â°C)'] = DataDF['Max Temp (Â°C)'].astype(float)  # 注意Max Temp (°C)的写法

# 2 字符串转换为日期
DataDF.loc[:, 'Date/Time'] = pd.to_datetime(DataDF.loc[:, 'Date/Time'], format='%m/%d/%Y',
                                            errors='coerce')  # format是原始数据中日期的格式；errors='coerce'，如果原始数据不符合日期的格式，转换后的值为空值NaT

#####Step3：修改类名

# 1 建立字典：旧列名和新列名对应关系
colNameDict = {'Max Temp (Â°C)': 'Max Temp', 'Total Snow (cm)': 'Total Snow'}  # 将旧列名放在冒号前，每组对应关系以逗号隔开

# 2 重命名
DataDF.rename(columns=colNameDict, inplace=True)

#####Step4：选择部分子集
# 4.1 选字段
subDataDF = DataDF[['Date/Time', 'Year', 'Max Temp', 'Max Temp', 'Total Precip (mm)', 'Total Rain Flag']]  # 注意这里是双括号
# 4.2 利用切片筛选数据


#####Step5：筛选逻辑问题
subDataDF.loc[:, 'Year'] > 0

#####Step6：格式一致化
# 1 去除空格
DataDF['Total Precip (mm)'] = DataDF['Total Precip (mm)'].str.strip()

#####Step7：缺失值处理
# 7.1 去掉缺失值
DataDF.dropna(axis=1, how='any',thresh=6)  # 一列每一个数据都是NaN才去掉这列
print(DataDF)
