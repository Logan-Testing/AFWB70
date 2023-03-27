import openpyxl


class Excel:
    @staticmethod
    def get_data(xlpath, sheet, row, column):
        try:
            wb = openpyxl.load_workbook(xlpath)
            value = wb[sheet].cell(row, column).value
            print('Data from Xl', value)
            wb.close()
            return value
        except:
            print("Exception while reading data from excel")
            return " "
