list1=[688251,688163,600769,600936,603626,605169,603607,600778,603060,603728]
list2=['井松智能','赛伦生物','祥龙电业','广西广电','科森科技','洪通燃气','京华激光','友好集团','国检集团','鸣志电器']
list3=[14.91,14.87,6.47,2.16,6.78,8.56,13.94,5.05,7.14,33.55]
result=list(zip(list1,list2,list3))
res1=sorted(result ,key=lambda x:x[0])
res2=sorted(res1 ,key=lambda x:x[1])
print("按股票代码排序：")
print("股票代码    股票名称    股票价格")
for list1, list2, list3 in res1:
    print(f"{list1}    {list2}    {list3}")
res2=sorted(result ,key=lambda x:x[2])
print("\n按股票价格排序：")
print("股票代码    股票名称    股票价格")
for list1, list2, list3 in res2:
    print(f"{list1}    {list2}    {list3}")
