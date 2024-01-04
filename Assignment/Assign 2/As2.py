import openpyxl as xl

def list_from_xl(sheet):
    mylist = []
    for row in sheet.iter_rows():
        temp = [cell.value.replace(' ', '') if cell.value is not None and isinstance(cell.value, str) else None
                for cell in row]
        mylist.append(temp)

    return mylist

def search_in_list(mylist, word):
    return next((row[0] for row in mylist if word.replace(' ', '') in row[1:]), 'Word not found!')

xl_sheet = xl.load_workbook('Assignment/Test1.xlsx')
sheet = xl_sheet['Sheet1']

word = input("Enter a Punjabi word to search: ")
mylist = list_from_xl(sheet)

result = search_in_list(mylist, word)
print("Punjabi word:", result)
