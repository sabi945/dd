# import time
# # a function that accept a function as input 
# # and the return value is a function
# def timer(fn):
#     def wrapper(x, y):
#         res = fn(x, y)
#         return res
#     return wrapper
# def add(x, y):
#     a = time.time()
#     res = x + y
#     print('Waktu : ', time.time() - a)
#     return res
# sup = timer(add)
# def sub(x, y):
#     a = time.time()
#     res = x + y
#     print('Waktu : ', time.time() - a)
#     return res
# sib = timer(sub)
# print('Hasil: ', add(1, 2))
# print('Hasil: ', add(3, 4))
# print('Hasil: ', add(10, 20))
# print('Hasil: ', sub(50, 20))
# print('Hasil: ', sub(40, 10))
# print('Hasil: ', sub(20, 1))

def fungsi_pertama():
    x = 10
    breakpoint()  # Program akan berhenti di sini

def fungsi_kedua():
    y = 20
    print("Ini fungsi kedua")

fungsi_pertama()
fungsi_kedua()
