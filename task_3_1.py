class Matrix:
    def __init__(self, columns, rows):
        '''Инициализация матрицы'''
        self.content = []
        self.rows = rows
        self.columns = columns
        for row in range(rows):
            if rows is not None:
                self.content.append([1]*columns)
            
    def __str__(self):
        return 'Содержимое: ' + ''.join(str(self.content))
    
    
    def add_row(self, obj = []):
        '''Поместить строку в матрицу'''
        self.content.append(obj)

    def set_row(self, row, val):
         '''Изменить целую строку'''
         self.content[row-1] = val
         
    def set_cell(self, column, row, val):
        '''Изменить значение ячейки'''
        self.content[row-1][column-1] = val

    def inspect(self):
         '''Проверка содержимого матрицы'''
         print('Содержание матрицы:')
         for item in self.content:
            print('  ', item)

    def count_columns(self):
        '''Вывод числа строк и колонок'''
        print("Количество строк в матрице:", len(self.content), '\nКоличество столбцов в матрице', len(self.content[0]))

matrix_1 = Matrix(10,10)
matrix_1.add_row([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
matrix_1.set_row(1, [5, 7, 9, 8, 0, 1, 5 , 4, 8 , 5])
matrix_1.set_cell(2, 3, 5)
matrix_1.inspect()
matrix_1.count_columns()