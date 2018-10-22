# def dick_user(name,length=18):
#     print("i like " + "the dick of " + name)
#     print(name + " dick is " + length + " cm")
#
# dick_user('yichen' ,'18.45')
#
#
# def make_food(*foodings):
#     print("\nMaking a food with the following foodings:")
#     for food in foodings:
#         print("-" + food)
# make_food('patota')
# make_food('egg','humbags','water')


class Man():
    def __init__(self,name,length):
        #初始化属性 name 和 length
         self.name = name
         self.length = length
    def fuck(self):
        print(self.name.title()+",come to fuck me" )

    def suck(self):
        print(self.name.title+",i like your big dick")

my_man = Man('zhaomeng','18')
print("my man's name is " + my_man.name.title()+"!")
print("my man is " + my_man.length + " cm")
my_man.fuck()


class Bigman(Man):
    def __init__(self,name,length):
        #初始化属性 name 和 length
         super().__init__(self,name,length)


my_bigman = Bigman('yien','1')
print(my_bigman.fuck())