import logging
import time
from threading import Thread
import os
import logging.handlers
import datetime

today = time.strftime('%Y-%m-%d', time.localtime(time.time()))
FORMAT = '%(asctime)s %(message)s'
DATEFMT = '[%Y-%m-%d %H:%M:%S]'

LOGPATH = os.path.join(os.path.abspath(os.getcwd()), 'Log')
if not os.path.exists(LOGPATH):
    os.mkdir(LOGPATH)

FILENAME = './Log{}.log'.format(str(today))
logging.basicConfig(
    handlers=[logging.handlers.TimedRotatingFileHandler(filename=FILENAME, when='D', interval=60*60*24, backupCount=2)],
    level=logging.DEBUG,
    format=FORMAT,
    datefmt=DATEFMT
)


def DeleteLog(day):
    today = datetime.datetime.now()
    offset = datetime.timedelta(days=-day)
    re_date = (today + offset)
    re_date_unix = time.mktime(re_date.timetuple())

    logmsg('Delete log check, current date {}'.format(today.strftime('%Y-%m-%d')))
    logmsg('Delete log, {} days ago, start at {}'.format(day, re_date.strftime('%Y-%m-%d')))
    ret = os.listdir(LOGPATH)

    logmsg('Delete log, check list {}'.format(ret))
    for f in ret:
        file = os.path.join(LOGPATH, f)
        file_modify_time = os.path.getmtime(file)
        timeArray = time.localtime(file_modify_time)
        otherStyleTime = time.strftime('%Y-%m-%d %H:%M:%S', timeArray)
        logmsg('[{}] document last time change: {}'.format(file, day))
        if file_modify_time <= re_date_unix:
            os.remove(file)
            logmsg('[{}] already expired {} days'.format(file, day))


def logmsg(msg):
    t1 = Thread(target=threadjob, args=(msg,))
    t1.start()


def threadjob(msg):
    print(msg)
    logging.info(msg)


def logError(msg):
    t1 = Thread(target=threadjob1, args=(msg,))
    t1.start()


def threadjob1(msg):
    print(msg)
    logging.exception(msg)

