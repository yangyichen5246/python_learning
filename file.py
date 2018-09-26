

with open("./ceshi_09_26.txt") as m_file:
    m_file.read()
    # print("file open sucess")
    # contents = m_file(read)
    # print(contents)

# filepath = './c/ceshi_09_26.txt'
# with open(filepath) as file_object:
#      for line in file_object:
#         print(line)


filename = 'loving.txt'

with open (filename,'w')as file_object:
    file_object.write("i loving programing.\n")
    file_object.write("i loving yichen.\n")