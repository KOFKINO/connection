import sqlite3


conn = sqlite3.connect('homework.sqlite')
cursor = conn.cursor()
user_nofity = """
请输入查询选项:
请输入1：查询整个数据库
请输入2：基于姓名查询
请输入3：基于年龄查询
请输入4：基于作业数查询
请输入0：退出
"""

while True:
    print(user_nofity)
    user_input = input('请选择')
    if user_input == '0':
        break
    elif user_input == '1':
        cursor.execute('select * from homework')
        result = cursor.fetchall()
        for stu in result:
            print(stu)
    elif user_input == '2':
        if not user_input:
            continue
        input_name = input('请输入姓名')
        cursor.execute('select * from homework where 姓名 = ?', (input_name,))
        result = cursor.fetchall()
        if not result:
            print('未找到学员信息')
        for stu in result:
            print(stu)
    elif user_input == '3':
        if not user_input:
            continue
        input_age = input('查找大于输入年龄的学员，请输入学员年龄')
        cursor.execute('select * from homework where 年龄 > ?', (input_age,))
        result = cursor.fetchall()
        if not result:
            print('未找到学员信息')
        for stu in result:
            print(stu)
    elif user_input == '4':
        if not user_input:
            continue
        input_work = input('查找作业数大于输入的学员，请输入作业数')
        cursor.execute('select * from homework where 作业数 > ?', (input_work,))
        result = cursor.fetchall()
        if not result:
            print('未找到学员信息')
        for stu in result:
            print(stu)
    else:
        print('输入错误，请重新输入')




