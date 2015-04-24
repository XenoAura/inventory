# -*- coding: utf-8 -*-

import platform

def rmN(data):
    '''
    Удаляет перенос строки в элементах списка
    :param data: LIST
    :return: LIST список элементов без переноса строки
    '''
    out_data = []
    for i in data:
        out_data.append(i.replace("\n", ""))
    return out_data


def getWinV():
    return str(platform.release())


#print getWinV()


'''
import sys
def _getWinIndex():
    wv = sys.getwindowsversion()
    if hasattr(wv, 'service_pack_major'):  # python >= 2.7
        sp = wv.service_pack_major or 0
    else:
        import re
        r = re.search("\s\d$", wv.service_pack)
        sp = int(r.group(0)) if r else 0
    return (wv.major, wv.minor, sp)


def getWinVersion(index):
    WIN_8 = (6, 2, 0)
    WIN_7 = (6, 1, 0)
    WIN_SERVER_2008 = (6, 0, 1)
    WIN_VISTA_SP1 = (6, 0, 1)
    WIN_VISTA = (6, 0, 0)
    WIN_SERVER_2003_SP2 = (5, 2, 2)
    WIN_SERVER_2003_SP1 = (5, 2, 1)
    WIN_SERVER_2003 = (5, 2, 0)
    WIN_XP_SP3 = (5, 1, 3)
    WIN_XP_SP2 = (5, 1, 2)
    WIN_XP_SP1 = (5, 1, 1)
    WIN_XP = (5, 1, 0)
    if index > WIN_SERVER_2008:
        return 'srv2008'
    elif index > WIN_SERVER_2008:
        return ''
    else:
        return ''
'''
