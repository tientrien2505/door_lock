import Jetson.GPIO as GPIO
from time import sleep
from threading import Thread
import os
import logging
from dotenv import load_dotenv, find_dotenv

is_loaded = load_dotenv(find_dotenv())
print(is_loaded)

LOG_DIR = os.getenv('LOG_DIR')
print(LOG_DIR)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s', filename=LOG_DIR)
try:
    BUTTON_PIN = int(os.getenv('BUTTON_PIN')) if os.getenv('BUTTON_PIN') is not None else 11
    BOLT_PIN = int(os.getenv('BOLT_PIN')) if os.getenv('BOLT_PIN') is not None else 15
except:
    BUTTON_PIN = 11
    BOLT_PIN = 15

class DoorLock(Thread):

    def __init__(self, daemon=False, button_pin=BUTTON_PIN, bolt_pin=BOLT_PIN):
        try:
            GPIO.setmode(GPIO.BOARD)
            self.button_pin = button_pin
            self.bolt_pin = bolt_pin
            self._deactivate = False
            GPIO.setup(self.button_pin, GPIO.IN)
            GPIO.setup(self.bolt_pin, GPIO.OUT)
            super().__init__(daemon=daemon)
            self.start()
            logging.info("door lock system started")
        except Exception as ex:
            logging.error('could not start door lock system')
            raise Exception(ex)
    
    def run(self):
        self.process_button()

    def deactivate(self):
        self._deactivate = True
    
    def activate(self):
        if self._deactivate is True:
            try:
                self._deactivate = False
                self.start()
                logging.info('door lock started')
            except:
                self._deactivate = True
                logging.error("door lock couldn't start")
        else:
            logging.info('door lock system is still running')
    
    def process_button(self):
        try:
            while True:
                value = GPIO.input(self.button_pin)
                if value == GPIO.LOW:
                    self.open_door()
                if self._deactivate:
                    break
        except:
            GPIO.cleanup()
    
    def open_door(self):
        GPIO.output(self.bolt_pin, GPIO.HIGH)
        logging.info("door opening")
        sleep(0.3)
        GPIO.output(self.bolt_pin, GPIO.LOW)

if __name__ == '__main__':
    dl = DoorLock()
    sleep(2)
    dl.open_door()