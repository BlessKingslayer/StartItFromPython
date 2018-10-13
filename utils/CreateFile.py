import os, time

# 创建日志文件
def createLog():
    curtime = time.strftime("%Y%m%d_%H%M%S")
    dir_path = os.path.abspath(os.path.dirname(__file__))
    path = dir_path + '/log/' + str(curtime) + '.log'
    if not os.path.exists(path):
        file = open(path, 'w')
        file.close()

def createFile(filename, pathname=''):
    try:
        default_path = os.path.abspath('G:\EveryDayCode\JustPython\StartItFromPython\DataHub') \
            if pathname.strip()=='' else os.path.abspath(pathname)
        path = default_path + '/' + filename
        if not os.path.exists(path):
            file = open(path, 'w')
            file.close()
        return path
    except Exception as ex:
        print('utils -> create(filename, pathname) has errors. \n', ex)
        raise ex
