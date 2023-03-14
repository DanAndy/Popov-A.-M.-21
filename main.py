import sys
import sqlite3

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from form_staff import Ui_Form

class MyWidget(QWidget, Ui_Form):
    def __init__(self):
        super(MyWidget, self).__init__()
        self.setupUi(self)
        self.pbOpen.clicked.connect(self.open)

    def open(self):
        #try:
        self.conn = sqlite3.connect('basepomain.db')
        cur = self.conn.cursor()
        data = cur.execute("select * from staff")
        col_name = [i[0] for i in data.description]
        data_rows = data.fetchall()
        #except Exception as e:
            # print("Ошибка с подключением к базе данных")
            # return e
        self.twStaffs.setColumnCount(len(col_name))
        self.twStaffs.setHorizontalHeaderLabels(col_name)
        self.twStaffs.setRowCount(0)
        for i, row in enumerate(data_rows):
            self.twStaffs.setRowCount(self.twStaffs.rowCount()+1)
            for j, elem in enumerate(row):
                self.twStaffs.setItem(i, j, QTableWidgetItem(str(elem)))
        self.twStaffs.resizeColumnsToContents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())