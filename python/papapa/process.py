import pandas as pd
import xlrd
import re
import xlutils.copy
import matplotlib.pyplot as plt

def ExceptNull():
    """
    数据清洗第一步：去除表中空值
    @param df: 传入读取的xls表格数据
    @return: 保存数据后返回，
    """
    df = pd.DataFrame(pd.read_excel(r'D:\实例\Python实例\爬虫\111.xls'))
    #查找面积列空值,使用99999填充空缺值后删除所在行
    print(df['面积'].isnull().value_counts())
    df["面积"] = df["面积"].fillna('99999')
    NullKey = df[(df.面积 == '99999')].index.tolist()
    print(NullKey)
    df = df.drop(NullKey)
    print("*"*30)
    print(df['面积'].isnull().value_counts())

    print("*"*30)
    #查找总价列空值,使用99999填充空缺值后删除所在行
    print(df['总价'].isnull().value_counts())
    df["总价"] = df["总价"].fillna('99999')
    NullKey1 = df[(df.总价 == '99999')].index.tolist()
    print(NullKey1)
    df = df.drop(NullKey1)
    print("*"*30)
    print(df['总价'].isnull().value_counts())
    df.to_excel('111.xls',index=False,encoding='uf-8')


    print("修改后数据保存成功")


def LeiChuli():
    Data = xlrd.open_workbook(r"D:\实例\Python实例\爬虫\111.xls")
    ws = xlutils.copy.copy(Data)
    Table = Data.sheet_by_name("Sheet1")
    Nrows = Table.nrows
    list_A = []
    for i in range(1,Nrows):
        A = Table.cell_value(i,6)
        A_Str = re.sub('/套','',A,Nrows)
        list_A.append(A_Str)
    Replace = []
    for i in range(len(list_A)):
        Price_Str = list_A[i]
        Last_Str = Price_Str[-1]
        if Last_Str == '万':
            A_Str = re.sub('万', '0000', Price_Str, 1)
            Replace.append(A_Str)
        else:
            Replace.append(Price_Str)
    table = ws.get_sheet(0)
    for i in range(len(Replace)):
        table.write(i + 1, 6, Replace[i])
        print("------>开始写入修改后数据<------")
        print("---->第{}项写入成功<----".format(i))
        ws.save(r"F:\实例\Python实例\爬虫\111.xls")
        print("------>数据写入完成<------")


def Data_Analysis_One():
    Data = xlrd.open_workbook(r"D:\实例\Python实例\爬虫\111.xls")
    ws = xlutils.copy.copy(Data)
    Table = Data.sheet_by_name("Sheet1")
    Nrows = Table.nrows
    a,b,c,d,e,f = 0,0,0,0,0,0

    for i in range(1, Nrows):
        A = Table.cell_value(i, 5)
        if A == "价格待定":
            f += 1
        else:
            if int(A) <= 5000:
                a += 1
            elif int(A) <= 10000:
                b += 1
            elif int(A) <= 15000:
                c += 1
            elif int(A) <= 20000:
                d += 1
            else:
                e += 1

    # 开始准备绘制饼状图

    #价格区间数据准备
    sizes = []
    Percentage_a = (a / Nrows) * 100
    sizes.append(int(Percentage_a))
    Percentage_b = (b / Nrows) * 100
    sizes.append(int(Percentage_b))
    Percentage_c = (c / Nrows) * 100
    sizes.append(int(Percentage_c))
    Percentage_d = (d / Nrows) * 100
    sizes.append(int(Percentage_d))
    Percentage_e = (e / Nrows) * 100
    sizes.append(int(Percentage_e))
    Percentage_f = (f / Nrows) * 100
    sizes.append(int(Percentage_f))
    #设置占比说明
    labels = '0-5000','5001-10000','10001-15000','15001-20000','20000-','Undetermined'
    explode = (0,0,0.1,0,0,0)
    #开始绘制
    plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
    plt.axis('equal')
    plt.show()
    ws.save(r"D:\实例\Python实例\爬虫\111.xls")


if __name__ == '__main__':
    # ExceptNull()
    # LeiChuli()
    Data_Analysis_One()