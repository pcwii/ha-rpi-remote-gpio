from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
pin = 21

app = Flask(__name__)


@app.route('/GPIO/<state>', methods={'GET', 'POST'})
def red_light(state):
    if state == 'on':
        GPIO.output(pin, GPIO.HIGH)
    elif state == 'off':
        GPIO.output(pin, GPIO.LOW)


if __name__ == '__main__':
    app.run(host='0.0.0.0')