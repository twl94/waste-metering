
# Waste Metering (LEGO Spike Prime)

This Python script controls motors and a force sensor using the LEGO Spike Prime hub. It calculates the expected force on an object based on its mass and gravity, compares this with sensor data, and performs motor actions and sound outputs accordingly.

## Code Overview

### Imports
```python
from spike import PrimeHub, Motor, MotorPair, ForceSensor, Speaker
import time
```
- **PrimeHub**: Represents the LEGO Spike Prime hub.
- **Motor & MotorPair**: Used to control motors connected to specific ports.
- **ForceSensor**: Detects force in Newtons, used to measure weight.
- **Speaker**: Plays sound or beep.
- **time**: Provides delay functionality for better control flow.

### Initialization
```python
hub = PrimeHub()
motor_a = Motor('A')
motor_b = Motor('B')
force_sensor = ForceSensor('F')
speaker = Speaker()
```
- Initializes the **hub** and assigns ports `A`, `B`, and `F` to **motor_a**, **motor_b**, and **force_sensor** respectively.
- Initializes the **speaker**.

### Constants
```python
GRAVITY = 9.81
MASS = 1
EXPECTED_FORCE = MASS * GRAVITY
```
- **GRAVITY**: Gravity constant (m/s²).
- **MASS**: Represents the mass of the object (in kilograms).
- **EXPECTED_FORCE**: The expected force (in Newtons) calculated by multiplying mass by gravity.

### Display Force on Hub
```python
hub.light_matrix.write(str(round(EXPECTED_FORCE, 2)) + "N")
```
- Displays the expected force (in Newtons) on the hub's light matrix.

### Main Loop
```python
while True:
    measured_force = force_sensor.get_force_newton()
    hub.light_matrix.write(str(round(measured_force, 2)) + "N")
```
- Continuously measures the force using the force sensor and displays it on the hub.

### Motor and Force Control
```python
    if abs(measured_force - EXPECTED_FORCE) < 0.1:
        motor_a.run_to_position(0, 'shortest path')
    else:
        motor_a.start_at_power(50)
```
- If the measured force is approximately equal to the expected force, **motor_a** will stop.
- If the force differs significantly, **motor_a** will run at 50% power.

### Action on Force Match
```python
    if measured_force >= EXPECTED_FORCE:
        motor_b.run_for_degrees(360)
        speaker.start_beep(60)
        time.sleep(1)
        speaker.stop()
```
- When the measured force matches or exceeds the expected force, **motor_b** rotates by 360 degrees and the **speaker** produces a beep for 1 second.

### Loop Control
```python
    time.sleep(0.1)
```
- Adds a short delay between loops to prevent rapid execution.

---

This code is designed to work with the LEGO Spike Prime Python API
