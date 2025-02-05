import csv


class MyDialect(csv.Dialect):
    """
    Класс MyDialect.
    """
    delimiter = ';'
    quotechar = '"'
    lineterminator = '\n'
    quoting = csv.QUOTE_ALL


csv.register_dialect('tester', MyDialect)

with open('student.csv', encoding='utf-8', newline='') as csv_file:
    data = csv.reader(csv_file, dialect='tester', delimiter=',')
    for row in data:
        print(" ".join(row))
