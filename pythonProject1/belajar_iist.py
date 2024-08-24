
import sys
anga = [10,40,30,40]

def list_angka(angka):
    anga.append(angka)

with open('belajar_iist.py', 'a') as file:
    file.write('\n'.join([f"my_list.append({n})" for n in anga if n not in anga]) + '\n')
print(anga)

def has():
    print("hallo world")

def basss(baso,siji):
    return baso+siji

print("baso",sys.platform)






























