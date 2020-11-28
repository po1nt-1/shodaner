import ipaddress
import re

from PySide2 import QtCore
from PySide2.QtCore import QThread
from PySide2.QtWidgets import (QApplication, QFileDialog, QMainWindow,
                               QMessageBox, QTableWidgetItem)

import gui
import shodan_requests

g_last_result = []
g_last_10_result = []

g_info_results = {}
g_ip_list = []

g_error = [False, '']


class Local_error(Exception):
    pass


class Worker(QThread):
    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.second_notifier = QMessageBox()

    def run(self):
        send_request()


class MyQtApp(gui.Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super(MyQtApp, self).__init__(parent)
        self.setupUi(self)

        self.text_ip_list.setPlaceholderText(
            'Enter one IP per line.\n\n'
            'Example:\n172.217.22.14\n40.114.177.156\n5.255.255.60')

        self.worker = Worker()
        self.worker.finished.connect(self.show_tables)

        self.notifier = QMessageBox()

        self.button_change_token.clicked.connect(self.change_token)
        self.button_send_request.clicked.connect(self.worker_start)
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
        except shodan_requests.Local_error as e:
            self.notifier.about(self, " ", str(e))

    def show_user_info(self, data):
        try:
            self.tableWidget_user.clear()
            self.tableWidget_user.setHorizontalHeaderLabels(data.keys())
            self.tableWidget_user.horizontalHeader().setVisible(True)
            self.tableWidget_user.setRowCount(1)

            for i, value in enumerate(data.values()):
                cell = QTableWidgetItem(value)
                self.tableWidget_user.setItem(0, i, cell)

                self.tableWidget_user.horizontalHeaderItem(
                    i).setTextAlignment(QtCore.Qt.AlignHCenter)

            self.tableWidget_user.resizeColumnsToContents()
        except Local_error as e:
            self.notifier.about(self, " ", str(e))
        except shodan_requests.Local_error as e:
            self.notifier.about(self, " ", str(e))

    def worker_start(self):
        try:
            global g_ip_list

            g_ip_list = self.text_ip_list.toPlainText().split('\n')

            self.worker.start()
        except Local_error as e:
            self.notifier.about(self, " ", str(e))
        except shodan_requests.Local_error as e:
            self.notifier.about(self, " ", str(e))

    def show_tables(self):
        try:
            global g_last_result
            global g_info_results
            global g_error

            if g_error[0]:
                raise Local_error(g_error[1])

            self.show_table(g_last_result)
            self.show_user_info(g_info_results)
        except Local_error as e:
            self.notifier.about(self, " ", str(e))
            g_error = [False, '']
        except shodan_requests.Local_error as e:
            self.notifier.about(self, " ", str(e))
            g_error = [False, '']

    def save_last(self):
        try:
            global g_last_result

            shodan_requests.csv_writer(
                g_last_result, shodan_requests.gen_new_csv_name())
        except Local_error as e:
            self.notifier.about(self, " ", str(e))
        except shodan_requests.Local_error as e:
            self.notifier.about(self, " ", str(e))

    def save_last_10(self):
        try:
            shodan_requests.csv_writer(
                g_last_10_result, shodan_requests.gen_new_csv_name())
        except Local_error as e:
            self.notifier.about(self, " ", str(e))
        except shodan_requests.Local_error as e:
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
        except shodan_requests.Local_error as e:
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
        except shodan_requests.Local_error as e:
            self.notifier.about(self, " ", str(e))


def send_request():
    try:
        global g_last_result
        global g_last_10_result
        global g_info_results
        global g_ip_list
        global g_error

        for ip in g_ip_list:
            try:
                ipaddress.ip_address(ip)
            except ValueError:
                raise Local_error('Invalid IP list')

        shodan_requests.start()

        g_last_result = []
        for ip in g_ip_list:
            current_result = shodan_requests.shodan_host(ip)
            g_last_result += current_result

            if current_result not in g_last_10_result:
                if len(g_last_10_result) < 10:
                    g_last_10_result += current_result
                else:
                    g_last_10_result += current_result
                    g_last_10_result.pop(0)

        g_info_results = shodan_requests.shodan_info()
    except Local_error as e:
        g_error = [True, str(e)]
    except shodan_requests.Local_error as e:
        g_error = [True, str(e)]


def main():
    app = QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()


if __name__ == '__main__':
    main()
