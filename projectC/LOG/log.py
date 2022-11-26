def info(*args):
    for x in args:
        print(type(x))
        print(x)

def infod(classtype, **kwargs):
    print(classtype)
    for key, value in kwargs.items():
        print(f' {key} : {value} ')