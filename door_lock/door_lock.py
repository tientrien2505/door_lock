import Jetson.GPIO as GPIO
import os
import logging
from dotenv import load_dotenv, find_dotenv
is_loaded = load_dotenv(find_dotenv())

LOG_FILE_PATH = os.getenv('LOG_FILE_PATH')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s', filename=LOG_FILE_PATH)

if LOG_FILE_PATH:
    logging.info(f'log file path is {LOG_FILE_PATH}')
else:
    logging.info('no log file path')
try:
    BOLT_PIN = int(os.getenv('BOLT_PIN')) if os.getenv('BOLT_PIN') is not None else 15
    logging.info('loaded environment variables successfully')
except:
    logging.warning('loading environment variables is fail')
    BOLT_PIN = 15

class DoorLock():

    def __init__(self, bolt_pin=BOLT_PIN):
        try:
            GPIO.setmode(GPIO.BOARD)
            self.bolt_pin = bolt_pin
            GPIO.setup(self.bolt_pin, GPIO.OUT)
            logging.info("door lock system started")
        except Exception as ex:
            logging.error('could not start door lock system')
            raise Exception(ex)
    
    def open_door(self):
        GPIO.output(self.bolt_pin, GPIO.HIGH)
        logging.info("door opening")
        GPIO.output(self.bolt_pin, GPIO.LOW)
        logging.info("door closing")
    
    def keep_door_opening(self):
        GPIO.output(self.bolt_pin, GPIO.HIGH)
        logging.info("door opening")
    def close_door(self):
        GPIO.output(self.bolt_pin, GPIO.LOW)
        logging.info("door closing")

if __name__ == '__main__':
    from time import sleep
    dl = DoorLock()
    sleep(2)
    dl.open_door()
    sleep(10)
    dl.keep_door_opening()
    sleep(10)
    dl.close_door()