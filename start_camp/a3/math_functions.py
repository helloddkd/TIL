print(__name__)

def average(numbers) :
    return print('평균은', sum(numbers)/len(numbers))


def cube(x):
    return print(x,'의 세제곱은', x*x*x)


def main():
    print(cube(3))
    print(average([8,10]))
    my_score = [79,84,66,93]
    print(average(my_score))

if __name__ == '__main__':
    main()