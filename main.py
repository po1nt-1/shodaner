import ipaddress
import re

from PySide2 import QtCore
from PySide2.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QTableWidgetItem)

import gui
import shodan_requests

g_last_result = []
g_last_10_result = []


class Local_error(Exception):
    pass


class MyQtApp(gui.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setupUi(self)

        self.notifier = QMessageBox()

        self.button_change_token.clicked.connect(self.change_token)
        self.button_send_request.clicked.connect(self.send_request)
        self.button_save_last.clicked.connect(self.save_last)
        self.button_save_last_10.clicked.connect(self.save_last_10)
        self.button_upload_to_table.clicked.connect(self.upload_to_table)

    def show_table(self, data):
        try:
            self.tableWidget_main.clear()
            self.tableWidget_main.setHorizontalHeaderLabels(data[0].keys())
            self.tableWidget_main.horizontalHeader().setVisible(True)
            self.tableWidget_main.setRowCount(len(data))

            for i, result in enumerate(data):
                for j, value in enumerate(result.values()):
                    cell = QTableWidgetItem(value)
                    self.tableWidget_main.setItem(i, j, cell)

                    self.tableWidget_main.horizontalHeaderItem(
                        j).setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget_main.resizeColumnsToContents()
        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def show_user_info(self, data):
        try:
            self.tableWidget_main.clear()
            self.tableWidget_main.setHorizontalHeaderLabels(data.keys())
            self.tableWidget_main.horizontalHeader().setVisible(True)
            self.tableWidget_main.setRowCount(1)

            for i, value in enumerate(data.values()):
                cell = QTableWidgetItem(value)
                self.tableWidget_user.setItem(0, i, cell)

                self.tableWidget_user.horizontalHeaderItem(
                    i).setTextAlignment(QtCore.Qt.AlignHCenter)
            self.tableWidget_user.resizeColumnsToContents()
        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def send_request(self):
        try:
            global g_last_result
            global g_last_10_result

            ip_list = self.text_ip_list.toPlainText().split('\n')

            for ip in ip_list:
                try:
                    ipaddress.ip_address(ip)
                except ValueError:
                    raise Local_error('Invalid IP list')

            shodan_requests.start()

            g_last_result = []
            for ip in ip_list:
                current_result = shodan_requests.shodan_host(ip)
                g_last_result += current_result

                if current_result not in g_last_10_result:
                    if len(g_last_10_result) < 10:
                        g_last_10_result += current_result
                    else:
                        g_last_10_result += current_result
                        g_last_10_result.pop(0)

            self.show_user_info(shodan_requests.shodan_info())

            self.show_table(g_last_result)
        except Local_error as e:
            self.notifier.about(self, " ", str(e))
        except shodan_requests.Local_error as e:
            self.notifier.about(self, " ", str(e))

    def save_last(self):
        try:
            global g_last_result

            shodan_requests.csv_writer(
                g_last_result, shodan_requests.gen_new_csv_name())
        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def save_last_10(self):
        try:
            shodan_requests.csv_writer(
                g_last_10_result, shodan_requests.gen_new_csv_name())
        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def upload_to_table(self):
        try:
            path_to_csv = QFileDialog.getOpenFileName(
                dir=shodan_requests.os.path.join(
                    shodan_requests._get_script_dir(), 'results'),
                filter='*.csv'
            )[0]

            if not path_to_csv:
                raise Local_error("csv file not found")

            results = shodan_requests.csv_reader(path_to_csv)

            self.show_table(results)

        except Local_error as e:
            self.notifier.about(self, " ", str(e))

    def change_token(self):
        try:
            token = self.lineEdit_token.text()

            if bool(re.match("^[A-Za-z0-9]{32}$", token)):
                shodan_requests.start(token)
            else:
                raise Local_error('Invalid API key')

        except Local_error as e:
            self.notifier.about(self, " ", str(e))


def main():
    app = QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()


if __name__ == '__main__':
    main()
