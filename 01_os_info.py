# -*- codding utf-8 -*-

# Нужно собрать информацию об операционной системе

# TODO Запустить этот скрипт и закоммитить резульат его выполнения

import platform
import sys

info = 'OS is \n{}\n\nPython version is {} {}'.format(
        platform.uname(), sys.version, platform.architecture()
)
print(info)

with open('os_info.txt','w') as ff:
    ff.write(info)
