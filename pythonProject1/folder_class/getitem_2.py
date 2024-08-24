class MyClass:
    def __init__(self):
        self.items = []

    def __getitem__(self, index):
        return self.items[index]

    def add_item(self, item):
        self.items.append(item)
    

my_object = MyClass()
while True:
    user_input = input('Masukkan input Anda (atau ketik "selesai" untuk keluar): ')
    if user_input == 'selesai':
        break
    my_object.add_item(user_input)

print('Input yang telah dimasukkan:')
for i, item in enumerate(my_object):
    print(f'{i+1}. {item}')
