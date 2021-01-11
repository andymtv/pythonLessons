class SuperList(list):
    def __len__(self):
        return super().__len__() * 1000

my_list = SuperList()
for i in range(5):
    my_list.append(i)
print(len(my_list))

my_list[4] = 15
print(my_list
      )