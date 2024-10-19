from spike import PrimeHub, Motor, MotorPair, ForceSensor, Speaker
import time

hub = PrimeHub()
motor_a = Motor('A')
motor_b = Motor('B')
force_sensor = ForceSensor('F')
speaker = Speaker()

GRAVITY = 9.81
MASS = 1
EXPECTED_FORCE = MASS * GRAVITY

hub.light_matrix.write(str(round(EXPECTED_FORCE, 2)) + "N")

while True:
    measured_force = force_sensor.get_force_newton()
    hub.light_matrix.write(str(round(measured_force, 2)) + "N")

    if abs(measured_force - EXPECTED_FORCE) < 0.1:
        motor_a.run_to_position(0, 'shortest path')
    else:
        motor_a.start_at_power(50)

    if measured_force >= EXPECTED_FORCE:
        motor_b.run_for_degrees(360)
        speaker.start_beep(60)
        time.sleep(1)
        speaker.stop()

    time.sleep(0.1)
