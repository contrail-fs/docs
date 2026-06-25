## Basic Modes

**PITCH Mode (no switch)**
- This is the basic vertical mode of both the autopilot and the flight director.
- With autopilot ON, the pitch command bar can be slewed by using the pitch wheel.
- With autopilot OFF, the pitch of the command bar can be changed by manually flying the aircraft to the desired pitch attitude and pressing the SYNC switch on the yoke
- Overspeed protection is available: When the overspeed warning horn sounds, SPEED mode will automatically be selected and the flight director will command a speed of V(mo)/M(mo) - 2 kts.

**PSA - Preselect Altitude Mode**
- When capture conditions are met, the flight director generates commands to level the aircraft at, and maintain the selected altitude.
- PSA mode is automatically armed when Altitude alerter knob is activated, if not in the Go-around (GA) mode. (If in GA mode, PSA will be armed when: vertical SYNC switch is pressed OR another vertical mode is selected OR autopilot is engaged).
- PSA cannot be armed when GS has been captured.
- Selecting a new altitude in the alerter during capture will cause the flight director to go into basic PITCH mode, and re-arm the PSA mode.
- Selecting a different vertical mode during PSA capture or track will put the system into the new mode and disengage the PSA mode. PSA will not be re-armed until the altitude alerter knob is re-activated

**GA - Go-around Mode**
- GA mode is selected simultaneously for both pilots by pressing either pilot's Go-around button on the yoke.
- The GA mode commands the flight director (FD) in 2 axes: vertical command to pitch up to approximately 14 degrees, and lateral command to maintain the aircraft heading at the time of GA selection. The autopilot servos are disengaged in GA mode — the pilot hand-flies the aircraft to follow the FD command bars.
- Note: The lateral mode uses the EHSI heading at time of selection UNLESS the aircraft is on the ground (weight on wheels). On takeoff, with GA mode selected, the lateral go-around mode uses the EHSI heading at liftoff.
- GA mode automatically disengages the autopilot and disarms all other vertical and lateral modes, including PSA. To re-select PSA mode while in GA mode, press vertical SYNC switch on yoke, manually select another vertical mode, or engage the autopilot. Re-engaging the autopilot while in GA mode will put the system in ROL (roll hold) mode, and basic PITCH mode. If other vertical or lateral modes are desired, they must be re-selected.
- GA can also be selected with the autopilot OFF and on the ground (takeoff guidance): pressing GA engages the FD with 14 deg pitch + wings level commands, providing pitch and roll guidance for the takeoff roll and initial climb. Once airborne, the lateral target latches to the heading at liftoff.

## Lateral Modes

**½ BANK - Half Bank**
- Reduces commanded bank angle to a maximum of 12.5 degrees.

**HDG - Heading Select Mode**
- Flight director will generate commands to fly and maintain the heading selected on the EHSI with the heading set bug. Commanded bank angle will not exceed 27 degrees.

**NAV - Navigation Mode**
- Arms when selected and the flight director operates in HDG mode until capture.
- Captures when capture conditions are satisfied. Flight director will generate commands to intercept and maintain the displayed nav system's selected course.
- If the nav data source on EHSI is changed after capture, the flight director will automatically clear NAV mode, synchronize the heading bug, and revert to HDG mode.
- GPS approaches should be flown in the NAV mode

**APPR - Approach Mode**
- As with NAV mode, APPR mode arms when selected, and the flight director operates in HDG mode until capture. When capture conditions are satisfied, the flight director will generate commands to intercept and maintain the displayed nav system's selected course. If nav data source on EHSI is changed after capture, the flight director will automatically clear APPR mode, synchronize the heading bug, and revert to HDG mode.
- When ILS data is being used, the flight director arms for glideslope (GS) capture after localizer (LOC) capture. At GS capture, the currently active vertical mode is automatically cleared, and the flight director will generate commands to intercept and maintain the GS.
- VOR, LOC and ILS approaches should be flown with the APPR mode.

## Vertical Modes

**ALT - Altitude Mode**
- Generates commands to maintain the altitude at time of the selection

**CLIMB - Climb Mode**
- The flight director will generate commands to fly and maintain one of two speed profiles:
  - Normal - 250 KIAS to 10,000 ft, then 260 KIAS to 0.72 mach, to aircraft max altitude.
  - High - 250 KIAS to 10,000 ft, then 300 KIAS to 0.8 mach, to aircraft max altitude.
- When CLIMB mode is selected the Normal profile will be selected automatically. To select the High profile, press the CLIMB switch a second time. Pressing the switch a third time will de-select the mode, and return the flight director to the basic PITCH mode.
- The CLIMB mode is indicated on the EADI with CLM or CLM H for the High profile. The commanded IAS or Mach is also displayed. The IAS reference bug (on the side the autopilot is transferred to) will follow the commanded IAS.

**DESCEND - Descend Mode**
- As in the CLIMB mode, the flight director will generate commands to fly and maintain one of two speed profiles:
  - Normal - 0.8 mach to 300 KIAS to approximately 13,500 ft, decreasing to 250 KIAS at 10,500 ft, then maintaining 250 KIAS down to sea level.
  - High - 0.83 mach to 330 KIAS to approximately 14,000 ft, decreasing to 250 KIAS at 10,500 ft, then maintaining 250 KIAS down to sea level.
- The DESCEND mode has a min descent rate of 100 fpm until the desired speed is achieved. Aircraft power may need adjusting in order to achieve the desired descent profile.
- When DESCEND mode is selected below 5000 ft, a 1000 fpm descent will be commanded.
- When DESCEND mode is selected above 5000 ft, the Normal profile will be selected automatically.
- To select the High profile, press DESCEND switch a second time. Pressing the switch a third time will de-select the mode, and return the flight director to the basic PITCH mode.
- DESCEND mode is indicated on the EADI with DES or DES H for the High profile. The commanded IAS, Mach, or vertical speed is also displayed. The IAS reference bug (on the side the autopilot is transferred to) will follow the commanded IAS when following a speed profile.

**SPEED - Airspeed/Mach Hold Mode**
- Commands are generated to maintain the speed existing at the time of selection.
- The commanded IAS or MACH is displayed on the EADI, and on the airspeed indicator by the location of the airspeed bug.
- The commanded speed may be changed with the pitch wheel, or for IAS, with the airspeed bug on the airspeed indicator.
- NOTE: Large changes in commanded IAS or MACH can result in the reversal of a climb or descent to attain the selected speed.
- When selected above approximately 32,000 ft, the MACH mode results. The selected mode may then be changed by pressing the SPEED switch a second time.

**VS - Vertical Speed Mode**
- Commands are generated to maintain the vertical speed existing at the time of selection.
- The commanded vertical speed is displayed, along with a direction arrow (up or down), on the EADI.
- The commanded VS may be changed with the pitch.
- The maximum vertical speed in this mode is 6000 fpm.
- There is overspeed protection: When the overspeed warning horn sounds, SPEED mode will automatically be selected, and the flight director will command a speed of Vmo/Mmo - 2 kts.

**VNAV - Vertical Nav Mode**
- Arm the system to capture the VNAV Mode, while system continues in the currently active vertical mode until capture. When capture conditions are met, Commands are generated to fly and maintain the vertical navigation signal from the system selected for display on EFIS. If LOC is selected on EFIS after VNAV capture, the system automatically goes to the basic PITCH mode.
- VNAV vertical deviation is displayed on the right side of both the EADI and the EHSI.
- There is overspeed protection: When the overspeed warning horn sounds, SPEED mode will automatically be selected, and the flight director will command a speed of Vmo/Mmo - 2 kts.
