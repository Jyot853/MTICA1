student=[[11,'jyothsna',99,34],[44,'venni',66,39],[51,'ninna',77,88],[2,'mohan',99,55]]
student.sort(key=lambda temp:temp[0])
print(student)





output:
================================ 
    
student.sort(key=lambda temp:temp[1])
[[11, 'jyothsna', 99, 34], [2, 'mohan', 99, 55], [51, 'ninna', 77, 88], [44, 'venni', 66, 39]]
================================ 
    
student.sort(key=lambda temp:temp[2])
[[44, 'venni', 66, 39], [51, 'ninna', 77, 88], [11, 'jyothsna', 99, 34], [2, 'mohan', 99, 55]]

================================ 
    
student.sort(key=lambda temp:temp[3])
[[11, 'jyothsna', 99, 34], [44, 'venni', 66, 39], [2, 'mohan', 99, 55], [51, 'ninna', 77, 88]]
================================ 
    
student.sort(key=lambda temp:temp[0])
[[2, 'mohan', 99, 55], [11, 'jyothsna', 99, 34], [44, 'venni', 66, 39], [51, 'ninna', 77, 88]]

================================ 
student.sort(key=lambda temp:temp[4])

Traceback (most recent call last):
  File "E:/pythonpractice(24)/day4a.py", line 2, in <module>
    student.sort(key=lambda temp:temp[4])
  File "E:/pythonpractice(24)/day4a.py", line 2, in <lambda>
    student.sort(key=lambda temp:temp[4])
IndexError: list index out of range
