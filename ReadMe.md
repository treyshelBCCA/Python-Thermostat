# Thermostat Simulation

Your job for this benchmark is to create a program that simulates a simple thermostat. This thermostat has the following features:

It can be turned on and off
The temperature can be increased and decreased
The mode can be cycled between heating, cooling, and fan
To use these features, the user can press the following buttons: P, T+, T-, M.

The P button toggles the power. While the thermostat is turned off, only the power button should be processed. In other words, you can't change the temperature or mode while the thermostat is powered off.
The T+ and T- buttons increase and decrease the temperature. The minimum temperature is 50°F and the maximum temperature is 90°F. Pressing T+ or T- changes the temperature by 1°F in the appropriate direction.
The M button cycles to the next mode in the order: heating, cooling, and fan. After fan, the next mode would be to start over with heating.
After each user interaction, you should update the state of the thermostat and display its state. If the user provides the input quit, the program should finish.

```
Power: Off
> P
Power: On
Temperature: 70°F
Mode: Heating
> M
Power: On
Temperature: 70°F
Mode: Cooling
> T+
Power: On
Temperature: 71°F
Mode: Cooling
> P
Power: Off
> P
Power: On
Temperature: 71°F
Mode: Cooling
> quit

```

### Rubric

The thermostat:

- can be powered on and off
- ignores T+, T-, and M while powered off
- can have the temperature increase and decrease
- minimum: 50°F
- maximum: 90°F
- changes in increments of 1°F
- can cycle through modes and repeats
- heating -> cooling -> fan

### Style Guide

- Variables should have meaningful names that accurately describe what they refer to.
- No sloppy/unnecessary/commented out code.
