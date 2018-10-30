def print_fozu():
    print("                            _ooOoo_  ")
    print("                           o8888888o  ")
    print("                           88  .  88  ")
    print("                           (| -_- |)  ")
    print("                            O\\ = /O  ")
    print("                        ____/`---'\\____  ")
    print("                      .   ' \\| |// `.  ")
    print("                       / \\||| : |||// \\  ")
    print("                     / _||||| -:- |||||- \\  ")
    print("                       | | \\\\\\ - /// | |  ")
    print("                     | \\_| ''\\---/'' | |  ")
    print("                      \\ .-\\__ `-` ___/-. /  ")
    print("                   ___`. .' /--.--\\ `. . __  ")
    print("                ."" '< `.___\\_<|>_/___.' >'"".  ")
    print("               | | : `- \\`.;`\\ _ /`;.`/ - ` : | |  ")
    print("                 \\ \\ `-. \\_ __\\ /__ _/ .-` / /  ")
    print("         ======`-.____`-.___\\_____/___.-`____.-'======  ")
    print("                            `=---='  ")
    print("  ")
    print("         .............................................  ")
    print("                  佛祖镇楼                  BUG辟易  ")
    print("          佛曰:  ")
    print("                  写字楼里写字间，写字间里程序员；  ")
    print("                  程序人员写程序，又拿程序换酒钱。  ")
    print("                  酒醒只在网上坐，酒醉还来网下眠；  ")
    print("                  酒醉酒醒日复日，网上网下年复年。  ")
    print("                  但愿老死电脑间，不愿鞠躬老板前；  ")
    print("                  奔驰宝马贵者趣，公交自行程序员。  ")
    print("                  别人笑我忒疯癫，我笑自己命太贱；  ")
    print("                  不见满街漂亮妹，哪个归得程序员？")

print_fozu()


#  第二个函数

# def suam_1 ( mun1, mun2 ):
#     result = mun1 + mun2
#     print (result)
# mun1 = int (input ("第一个数为:"))
# mun2 = int (input ("第二个数为:"))
#
#
# suam_1(mun1,mun2)

#第三个函数实验
def get_wendu():
    wendu = 22
    print("当前温度为：%d"%wendu)
    return wendu
result = get_wendu()
def get_wendu_huashi(wendu):
    wendu = wendu +3
    print("当前华式温度为：%d"%wendu)
get_wendu()
get_wendu_huashi(result)


def test():
    a = 11
    b = 22
    c = 33

    # return [a,b,c]
    # return (a,b,c)
    return a,b,c
mun = test()
print(mun)
#  return 总结
# 1、结束函数 封装成数组即刻返回
# 2、如果需要调用该结果的时候看是否需要使用 return
#break 用于 结束循环


# 函数的嵌套调用 直接在函数下面调用即可

#示范1
def text1():
    pass
def test2():
    print("a = 1")
    print("b = 2")


def test3():

    test2()
    print("c=4")
test3()

#示范2
def print_line():
    print("_"*50)
def print_5():
    i = 0
    while i< 6:
        print_line()
        i+=1
print_5()


# %c	字符
# %s	通过str() 字符串转换来格式化
# %i	有符号十进制整数
# %d	有符号十进制整数
# %u	无符号十进制整数
# %o	八进制整数
# %x	十六进制整数（小写字母）
# %X	十六进制整数（大写字母）
# %e	索引符号（小写'e'）
# %E	索引符号（大写“E”）
# %f	浮点实数
# %g	％f和％e 的简写
# %G	％f和％E的简写

a = 100
def aaa():
    global a
    a = 200
    print(a)
def aa():
    print(a)

aaa()
aa()

#列表和字典的都可以作为全局变量


def numksj(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

numksj(11,22,33,33,aaaa = 23)

# *args 多余的不带名字的
# **kwargs 多余的带名字的

def numksj ( a, b, *args, **kwargs ):
    print (a)
    print (b)
    print (args)
    print (kwargs)

A=(190,234,321)
B={"NAME":'ijdfgh',"AGE":19}
numksj (11, 22, 33, 33,*A,**B)  #拆包


#数字 、字符串 元组不可修改 可以作为字典里面的key
#字典 列表 可以修改 不可作为key


#递归函数

def xxx(num):
    if num >=1:
       result=num * xxx(num-1)
    else:
        result =1
    return result

aaaf = xxx(4)
print(aaaf)