import pyodbc
connection = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-HOLIG319;'
                      'Database=DBMS;'
                      'Trusted_Connection=yes;')
cursor = connection.cursor()
cursor.execute("SELECT B.TITLE, BW.NAME FROM BOOK_LOANS BL, BORROWER BW, BOOK B WHERE BL.DUE_DATE = CONVERT(DATE,GETDATE()-1,120) AND \
    BL.CARD_NO = BW.CARD_NO AND B.BOOK_ID = BL.BOOK_ID")
for i in cursor:
    print(i)