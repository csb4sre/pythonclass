import csv

def write(file,data):
    write = csv.writer(file, delimiter = ',')
    for line in data:
        write.writerow(line)


def read(file):
    data = csv.DictReader(file, delimiter = ',')
    print(data)
    # print(next(data))
    for i in data:
        print(i['name'],i['dept'])

    # read = csv.read(file)
    # print(a)
    # csv.DictReader(file,delimiter = ',')

if __name__ == '__main__':
    file = open('emp.csv','w')
    data = ['name,id,dept'.split(','),
            'emp1,001,IT'.split(','),
            'emp2,002,HR'.split(','),
            'emp3,003,HR'.split(','),
            'emp4,004,SD'.split(','),
            'emp5,005,SD'.split(','),
            'emp6,006,SD'.split(',')]
    write(file,data)
    read(file)
    file.close()
