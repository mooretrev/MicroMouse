"""
--------------------------------------------------------------------------
Drone Motor Run
--------------------------------------------------------------------------
License:   
Copyright 2018 <Charles Walker Grimes>
Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.
3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------
This program runs all motors on my homebrew drone
Upon startup, the pocket beagle will power on the four motors and run 
them for 5 seconds before shutting down. This serves as a proof of concept
for the drone and the viability of my power/logic setup
This program will also allow for easy control of motor throttle for 
thrust/weight testing. By changing the pulse width, the power of the 
motor can be increased.
"""
# ------------------------------------------------------------------------
# Libraries - import the required libraries
# ------------------------------------------------------------------------
import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
import time


# ------------------------------------------------------------------------
# Constants - N/A
# ------------------------------------------------------------------------


# ------------------------------4.5------------------------------------------
# Global variables - N/A
# ------------------------------------------------------------------------


# ------------------------------------------------------------------------
# Functions 
# ------------------------------------------------------------------------
def main():
    # Arm the motor
    PWM.start("P1_33", 0, 100)  # Initialize all the pins with 0 duty cycle
    PWM.start("P1_36", 0, 100)
    PWM.start("P2_1", 0, 100)
    PWM.start("P2_3", 0, 100)
    time.sleep(1.0)  # Hold for one second
    PWM.set_duty_cycle("P1_33", 10)  # Start the pins a a l;ow duty cycle
    PWM.set_duty_cycle("P1_36", 10)
    PWM.set_duty_cycle("P2_1", 10)
    PWM.set_duty_cycle("P2_3", 10)
    time.sleep(1.0)

    # Run the motor for 5 seconds
    PWM.set_duty_cycle("P1_33", 11)  # Run the pins at high duty cycle to
    PWM.set_duty_cycle("P1_36", 11)  # start the motors
    PWM.set_duty_cycle("P2_1", 11)
    PWM.set_duty_cycle("P2_3", 11)
    time.sleep(1.0)
    PWM.set_duty_cycle("P1_33", 14)  # Ramp up motors for power/current test
    PWM.set_duty_cycle("P1_36", 14)
    PWM.set_duty_cycle("P2_1", 14)
    PWM.set_duty_cycle("P2_3", 14)
    time.sleep(5.0)
    PWM.stop("P1_33")  # Stop PWM signals and clean pins
    PWM.stop("P1_36")
    PWM.stop("P2_1")
    PWM.stop("P2_3")
    PWM.cleanup


# ------------------------------------------------------------------------
# Main script
# ------------------------------------------------------------------------
if __name__ == "__main__":
    main()

