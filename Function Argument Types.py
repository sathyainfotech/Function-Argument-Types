"""
    *args
    **kwargs

    Name="Ram"  Keyword:Value
"""

def fun(**kwargs):
    for key,val in kwargs.items():
        print("%s:%s"%(key,val))

fun(Name="Sathya",Age=26,Address="Chennai")





# def fun(*args):
#     sum = 0
#     for data in args:
#         sum+=data
#     print("Sum:",sum)
#
# fun(10,20,30,40)


