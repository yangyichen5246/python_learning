class Man:
    # 属性
#初始化对象  自动调用该方法，一般多用于默认值的设定
    def __init__(self,name,age):
        self.name = name
        self,age = age


    def __str__(self):
        pass

   #创建方法
    def dick( self ):
        print("dick is very big")
    def body( self ):
        print("body is so sex")
    def fuck( self ):
        print("%s fuck is: %s"%(self.body,self.face))
# 创建一个对象

yichen = Man("yichen",13)

yichen.dick()
yichen.body()
# yichen.name = "yichen" #对象的属性
# yichen.age = 180
yichen.face = "handsome"

print("%s de name is :%d"%(yichen.name,yichen.geight))

alex = Man()
alex.name = 'alex'
alex.age = 44
alex.fuck()

#如果需要在类外修改类属性，必须通过类对象去引用然后进行修改。如果通过实例对象去引用
# ，会产生一个同名的实例属性，这种方式修改的是实例属性，不
# 会影响到类属性，并且之后如果通过实例对象去引用该名
# 称的属性，实例属性会强制屏蔽掉类属性，即引用的是实例属性，除非删除了该实例属性。



实例方法：
类方法：
静态方法：