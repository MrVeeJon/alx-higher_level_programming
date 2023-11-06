class MyInt(int):
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)

my_i = MyInt(3)
print(my_i)
print(my_i == 3)
print(my_i != 3)
