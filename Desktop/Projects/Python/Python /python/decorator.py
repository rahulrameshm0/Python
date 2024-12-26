def f1():
    print("called f1")

def f2(f):
    f()

f2(f1)
