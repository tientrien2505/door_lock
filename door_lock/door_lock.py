import Jetson.GPIO as GPIO
<<<<<<< HEAD
=======
from time import sleep
>>>>>>> v1.0
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
<<<<<<< HEAD
=======
    DURATION_PRESS_OF_BUTTON = int(os.getenv('DURATION_PRESS_OF_BUTTON')) if os.getenv('DURATION_PRESS_OF_BUTTON') is not None else 0.04
>>>>>>> v1.0
    logging.info('loaded environment variables successfully')
except:
    logging.warning('loading environment variables is fail')
    BOLT_PIN = 15
<<<<<<< HEAD

=======
    DURATION_PRESS_OF_BUTTON = 40

# class DoorLock(Thread):
>>>>>>> v1.0
class DoorLock():

    def __init__(self, bolt_pin=BOLT_PIN):
        try:
            GPIO.setmode(GPIO.BOARD)
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
        GPIO.output(self.bolt_pin, GPIO.LOW)
        
    def keep_door_opening(self):
        GPIO.output(self.bolt_pin, GPIO.HIGH)
        logging.info("door opening")
        
        
    def close_door(self):
        GPIO.output(self.bolt_pin, GPIO.LOW)
        logging.info("door closing")

if __name__ == '__main__':
    from time import sleep
    dl = DoorLock()
    while True:
        sleep(1000)
