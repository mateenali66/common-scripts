#check if my service is running fine, or else, it would restart it

import urllib
import time
import os
import logging
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger()
logger.setLevel(logging.INFO)
file_handler = TimedRotatingFileHandler("healthcheck_myservice.log", when="midnight", interval=1)
file_handler.suffix = "%Y%m%d"
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(file_handler)
#logger.addHandler(ch)

THE_URL = "http://localhost:8080/myservice/hello"
RESTART_SH = '/opt/myservice/restart.sh'
SLEEP_INTERVAL = 60


#perform the health check, return True if the url is accessible.
def health_check(url):
    try:
        logger.info("start access url %s" % (url))
        a=urllib.urlopen(url)
        if a:
            if a.getcode()==200:
                lines = a.readlines()
                if lines is not None and len(lines)==1:
                    if lines[0]=='world':
                        logger.info("health ok")
                        return True
            else:
                logger.info("warning code:"+str(a.getcode()))
    except Exception as e:
        logger.error('health check failed %s ' % (str(e)))
    logger.info("health not ok")
    return False

#check the health for specified period
def check_periodically(url,failed_action_func):
    while True:
        try:
            time.sleep(SLEEP_INTERVAL)
            logger.info("check awake, start check")
            if not health_check(url):
                failed_action_func()
        except Exception as e:
            logger.error('check periodically failed %s ' % (str(e)))
        pass

def restart_server():
    do_script(RESTART_SH)
    pass

def do_script(the_scripts):
    logger.info("=========start script %s======"%the_scripts)
    result = os.popen(the_scripts).read()
    logger.info(result)
    logger.info("=========end   script %s======" % the_scripts)
    pass

if __name__ == '__main__':
    check_periodically(THE_URL,restart_server)
    pass

