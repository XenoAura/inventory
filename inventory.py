# -*- coding: utf-8 -*-
import subprocess
from utils import rmN, getWinV

class Inventory(object):

    def getListFromFile(self, txt_file):
        """
        Возвращает первый номер из списка и список всех комьютеров
        :param txt_file: строка, имя файла со списком
        :return: первый номер из списка и список
        """
        with open(txt_file, 'r') as fin:
            computers = fin.read().splitlines(True)
            computer_name = computers[0]
        print 'Инвентарный номер: ', computer_name
        return computer_name, computers

    def rmFirstElement(self, data):
        """
        Удаляет первую строку из файла
        :param data:  список
        :return:
        """
        with open('list.txt', 'w') as fout:
            print 'Удаляем из списка:', data[0]
            fout.writelines(data[1:])
        print 'Оставшиеся номера: ', rmN(data[1:])


    def callBatchFile(self, command):
        cmd = command
        PIPE = subprocess.PIPE
        p = subprocess.Popen(cmd, creationflags=subprocess.CREATE_NEW_CONSOLE)
        p.wait()
        #p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
        #        stderr=subprocess.STDOUT,  creationflags=subprocess.CREATE_NEW_CONSOLE)
        #data = p.stdout.read()
        #print data

    def renameComp(self, name):
        rename_cmd = 'WMIC computersystem where caption=%computername% rename '+name
        windows_version = getWinV()
        print 'Версия Windows: '+windows_version

        if windows_version == '7':
            application.callBatchFile('ping 8.8.8.8 -n 4')
        elif windows_version == 'XP':
            application.callBatchFile(rename_cmd)

    def AIDA(self, name):
        #self.callBatchFile('URL TO BAT %s' % name)
        pass


if __name__ == "__main__":
    application = Inventory()
    computer_name, computer_list = application.getListFromFile('list.txt')
    application.renameComp(computer_name)

    application.AIDA(computer_name)
    application.rmFirstElement(computer_list)
