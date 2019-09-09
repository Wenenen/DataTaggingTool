import openpyxl

if __name__ == "__main__":
    wb = openpyxl.load_workbook('tongyong.xlsx')
    sheets = wb.sheetnames
    for sheet in wb:
        # 创建一个文件保存通用词
        tmp = ''
        for row in sheet.values:
            for value in row:
                if value is not None:
                    tmp += value + '\n'
        with open(sheet.title, mode='w', encoding='utf-8') as f:
            f.write(tmp)