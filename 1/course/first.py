name ="tom"
age =18
print("姓名"+name+"年龄"+str(age))
print("姓名%s年龄%d"%(name,age))
print("姓名{}年龄{}".format(name,age))

# str ="Hello world"
# for i in str:
#     print(i)

#list列表 dictionary字典
#1.list是有序的,可变的数据结构,可以存储不同类型的数据结构,列表可以通过索引访问
my_list =[1,2,3,"Hello World"]
first_list =my_list[0]
print(first_list)
my_list[3]="New Element"#修改索引为3的元素
my_list.append("4")#追加到末尾
print(my_list)
my_list.remove("4")#移除元素
print(my_list)
# for i in my_list:
#     print(i)

#2.dictionary是无序的,可变的的数据结构,存储键值对,字典中的键必修是唯一,而值可以是任何类型的
my_dict ={}
my_dict ={"name":"Alice",
          "age":25,
          "city":"NewYork"
          }
#修改键为city的元素
my_dict["city"] ="Los Angeles"
#添加键值对
my_dict["country"]="USA"

keys =my_dict.keys()
vals =my_dict.values()
items =my_dict.items()
for key,value in my_dict.items():
    print(key,value)

#3.Tuple与列表类似，也是一种有序的集合，但元组是不可变的，这意味着一旦创建了元组，就不能修改其中的元素。元组通常用于存储一系列不需要改变的数据 
my_tup =()
my_tup=(1,2,3,"HelloWorld")
# my_tup[0]=2
# print(my_tup)

#4.set是一种无序的,不可重复的的数据结构,自动去重
my_set = {1,2,3,"HelloWorld",1}
print(my_set)
my_set.add("helloworld")
print(my_set)
my_set.remove("helloworld")
print(my_set)

set1 ={1,2,3,4}
set2 ={3,4,5,6}
print(f"交集:{set1&set2}")
print(f"并集:{set1|set2}")
print(f"差集:{set1-set2}")
