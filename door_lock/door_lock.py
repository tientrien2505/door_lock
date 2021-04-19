import Jetson.GPIO as GPIO
from time import sleep
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
    BUTTON_PIN = int(os.getenv('BUTTON_PIN')) if os.getenv('BUTTON_PIN') is not None else 11
    BOLT_PIN = int(os.getenv('BOLT_PIN')) if os.getenv('BOLT_PIN') is not None else 15
    DURATION_PRESS_OF_BUTTON = int(os.getenv('DURATION_PRESS_OF_BUTTON')) if os.getenv('DURATION_PRESS_OF_BUTTON') is not None else 0.04
    logging.info('loaded environment variables successfully')
except:
    logging.warning('loading environment variables is fail')
    BUTTON_PIN = 11
    BOLT_PIN = 15
    DURATION_PRESS_OF_BUTTON = 40

# class DoorLock(Thread):
class DoorLock():

    def __init__(self, daemon=False, button_pin=BUTTON_PIN, bolt_pin=BOLT_PIN, duration=DURATION_PRESS_OF_BUTTON):
        try:
            GPIO.setmode(GPIO.BOARD)
            self.button_pin = button_pin
            self.bolt_pin = bolt_pin
            self.duration = duration
            
            GPIO.setup(self.button_pin, GPIO.IN)
            GPIO.setup(self.bolt_pin, GPIO.OUT)
            GPIO.add_event_detect(self.button_pin, GPIO.RISING, self.__callback, self.duration)
            self._deactivate = False
            logging.info("door lock system started")
        except Exception as ex:
            logging.error('could not start door lock system')
            raise Exception(ex)
    

    def deactivate(self):
        GPIO.remove_event_detect(self.button_pin)
    
    def __callback(self, channel):
        self.open_door()
    
    def activate(self):
        if self._deactivate is True:
            try:
                self._deactivate = False
                GPIO.add_event_detect(self.button_pin, GPIO.RISING, self.__callback, self.duration)
                logging.info('door lock started')
            except:
                self._deactivate = True
                logging.error("door lock couldn't start")
        else:
            logging.info('door lock system is still running')
    
    
    def open_door(self):
        GPIO.output(self.bolt_pin, GPIO.HIGH)
        logging.info("door opening")
        sleep(0.3)
        GPIO.output(self.bolt_pin, GPIO.LOW)

if __name__ == '__main__':
    dl = DoorLock()
    while True:
        sleep(1000)