
def is_all_chinese(strs):
    for _char in strs:
        if '\u4e00' <= _char <= '\u9fa5':
            print(_char)
            

is_all_chinese("1.李路加")

AllStudents='''1.李隽瑶
2.叶天翔
3.赵思璇
4.李路加
5.李晋豪
6.陈柯睿
7.刘嘉懿
8.牛俊超
9.杨舒涵
10.何晟宁
11.金辰玥
12.邓博杨
13.张溪芮
14.何诗羽
15.马诺儿
16.张鑫瑞
17.郭佳琳
18.傅琬凌
19.程子林
20.杨锐轩
21.蓝奕璟
22.陈思瑶
23.黄思源
24.赵智杰
25.常凯歆
26.孙启铭
27.陈彦吉
28.陈玥枬
29.梁晟舜
30.曹立洋
31.高汉
32.胡新月
33.王回
34.赵清怡
35.龙奕霏
36.张琪其
37.谢璐珺
38.李泽荣
39.孙小雅
40.邓虞恩
41.何宇浩
42.黄瑞麟
43.周泓羽
44.杨凯麟。                              
45.刘欣怡
46.杨昕睿
47.荣浩然
48.宋宇恒
49.陈柯岐     
50.格让泽多    
51.丁钰凡     
52.龚子成                                53樊筱馨
'''

todayStudents='''
1.李隽瑶
2.赵思璇
3.牛俊超
4.陈柯睿
5.孙小雅
6.傅琬凌
7.胡新月
8.何晟宁
9.丁钰凡
10.常凯歆
11.张溪芮
12.宋宇恒
13.孙启铭
14.张琪其。                                
15.刘欣怡
16.蓝奕璟
17.张鑫瑞
18.赵清怡
19.马诺儿
20.陈彦吉
21.荣浩然
22.李路加
23.金辰玥
24.刘嘉懿
25.杨舒涵
26.邓博杨
27.黄思源
28.叶天翔
29.杨锐轩 
30.格让泽多
31.龚子成
32.高汉                      
33.樊筱馨
34.程子林
35.李晋豪
36.陈玥枬
37.陈思瑶
38.杨昕睿
39.王回
40.龙奕霏
41.谢璐珺
42.邓虞恩
43.赵智杰
44.梁晟舜
45.郭佳琳
46.何宇浩
47.周泓羽
48何诗羽
49陈柯岐
50.杨凯麟
51.曹立洋
52.李泽荣
53.黄瑞麟
'''

AllStudentName =[]
def findAllName(str):
    name = ""
    for char in str:
        if ((char == " " or char == "\n") and name != ""):
            AllStudentName.append(name)
            name = ""
            continue
        if '\u4e00' <= char <= '\u9fa5':
            name += char

findAllName(AllStudents)      
print(len(AllStudentName))
print(AllStudentName)

shouldHaveStudentName = AllStudentName

AllStudentName =[]
findAllName(todayStudents)
print(len(AllStudentName))
print(AllStudentName)

import xlwt #excel write
import xlrd #exel read

workbook = xlwt.Workbook() # create workbook
sheet1 = workbook.add_sheet("missed_students")
sheet1.write(0,0,"Name") #row column value


cnt = 0
row = 1
for str in shouldHaveStudentName:
    if str not in AllStudentName:
        sheet1.write(row,0,str)
        row += 1
        print(str)
        cnt += 1
print(cnt,"students haven't register today")
#workbook.save("test_stu.xls")
cnt = 0
row = 1
for str in AllStudentName:
    if str not in shouldHaveStudentName:
        sheet1.write(row,0,str)
        row += 1
        print(str)
        cnt += 1
print(cnt,"students haven't register today")

morStr = []
for str in AllStudentName:
    if str in shouldHaveStudentName:
        if str in morStr:
            print (str)
            cnt += 1
        morStr.append(str)
