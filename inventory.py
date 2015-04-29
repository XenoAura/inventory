# -*- coding: utf-8 -*-
import subprocess
from utils import rmN, getWinV
import admin

class Inventory(object):
    cabinet = ''
    user = ''

    def getListFromFile(self, txt_file):
        """
        Возвращает первый номер из списка и список всех комьютеров
        :param txt_file: строка, имя файла со списком
        :return: первый номер из списка и список
        """
        with open(txt_file, 'r') as fin:
            computers = fin.read().splitlines(True)
            computer_name = computers[0]
        print u'Инвентарный номер: ', computer_name
        return computer_name, computers

    def rmFirstElement(self, data):
        """
        Удаляет первую строку из файла
        :param data:  список
        :return:
        """
        with open('list.txt', 'w') as fout:
            print u'Удаляем из списка:', data[0]
            fout.writelines(data[1:])


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
        rename_cmd = r'wmic computersystem where name="%computername%" call rename name={0}'.format(name)
        windows_version = getWinV()
        print u'Версия ОС: Windows '+windows_version
        print u'Переименовываем комьютер'
        if windows_version == 'XP':
            self.callBatchFile('\\\\192.168.1.20\\1c_bd\AIDA64\\rename_xp.bat %s' % str(name))
        else:
            if not admin.isUserAdmin():
                admin.runAsAdmin(['\\\\192.168.1.20\\1c_bd\AIDA64\\rename.bat', ' '+str(name)])

    def AIDA(self, name):
        print u'Сбор информации AIDA64'
        self.callBatchFile('\\\\192.168.1.20\\1c_bd\AIDA64\\report_python.bat %s' % name)
        print u'Данные собраны'

    def addPeriphery(self, number, device_type, device_model):
        number = number.split('\n')[0]
        data_list = []
        data_list += number, self.cabinet, device_type, device_model
        print type(device_type)
        if len(self.user) > 0:
            data_list.append(self.user.decode('utf-8'))
        print type(data_list[4])
        with open('\\\\192.168.1.20\\1c_bd\AIDA64\\%s.txt' % number, 'w')as f:
            for item in data_list:
                f.write(str(item.encode('utf8')+'\n'))
        print u'Добавлено устройство: {0}. Модель: {1}. Присвоен инвентарный номер: {2} Ответственный'.format(device_type, device_model, number)

if __name__ == "__main__":
    application = Inventory()
    print u'Автоматизация инвентаризации'
    application.cabinet = raw_input('Kabinet nomer:')
    print u'Задать ответственного за рабочее место?'
    print u'введите Фамилию для назначения ответственного или цифру 2 для пропуска'
    user = raw_input(u'user name:')
    if user == '2':
        print u'ответственный за рабочее место не назначен'
    else:
        print type(user)
        application.user = user
    while True:
        #Главный цикл
        print u'1. Cменить имя комьютера, собрать информацию'
        print u'2. Выдать номер устройству на рабочем месте'
        print u'3. Выдать номер сетевому устройству в кабинете'
        print u'4. Выход'
        choise = raw_input(u'HOMEP:')
        if choise == '1':
            print u'Ваш выбор:', choise
            computer_name, computer_list = application.getListFromFile('list.txt')
            application.renameComp(computer_name)
            application.AIDA(computer_name)
            application.rmFirstElement(computer_list)
        elif choise == '2':
            computer_name, computer_list = application.getListFromFile('list.txt')
            while True:
                print u'1. Телефон \n2. Принтер'
                device = raw_input(u'Device type:')
                if device == '1':
                    print u'Введите модель телефона'
                    device_type = u'Телефон'
                elif device == '2':
                    print u'Введите модель принтера'
                    device_type = u'Принтер'
                else:
                    print u'Неверный ввод'
                    continue
                device_model = raw_input(u'Device model:')
                break
            application.addPeriphery(computer_name, device_type, device_model)
        elif choise == '3':
            pass
        elif choise == '4':
            break
        else:
            print u'Неверный ввод'

    input('Press any key...')
