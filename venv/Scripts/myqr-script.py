#!D:\定做区\2019-2021年定做\洋子2021年新建文件夹\二手车爬虫分析\myproject\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'MyQR==2.3.1','console_scripts','myqr'
__requires__ = 'MyQR==2.3.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('MyQR==2.3.1', 'console_scripts', 'myqr')()
    )
