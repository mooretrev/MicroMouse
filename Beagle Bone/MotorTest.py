import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time

def main():
    pwm = 'P2_1'
    dir_b1 = 'P2_4'
    dir_b2 = 'P2_6'

    print('setput GPIO')
    GPIO.setup(dir_b1, GPIO.OUT)
    GPIO.setup(dir_b2, GPIO.OUT)

    print('write to GPIO')
    GPIO.output(dir_b1, GPIO.HIGH)
    GPIO.output(dir_b2, GPIO.LOW)

    print('pwm setup')
    PWM.start(pwm, 0)
    time.sleep(1.0)

    print('pwn power on')
    PWM.set_duty_cycle(pwm, 100)

    time.sleep(5.0)

    print('pwm power off')
    PWM.stop(pwm)

    PWM.cleanup

if __name__ == "__main__":
    main()

