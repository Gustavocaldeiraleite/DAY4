from DAY4 import progress


def progress1():
    result = progress([3, 4, 1, 2]) 
    assert result == 2


def progress2():
    result = progress([10, 11, 12, 9, 10])
    assert result == 3


def progress3():
    result = progress([6, 5, 4, 3, 2, 9]) 
    assert result == 1

def progress4():
    result = progress([9,9])
    assert result == 0

if __name__ == "__main__":
    progress1()
    progress2()
    progress3()
    progress4()
    print('all tests passed')



