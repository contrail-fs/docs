**GA - Go-around Mode**
- GA mode is selected simulatenously for both pilots by pressing either pilot's Go-around button on the yoke.
- The GA mode commands the flight director (FD) in 2 axes: vertical command to pitch up to approximately 14 degrees, and lateral command to maintain the aircraft heading at the time of GA selection. The autopilot servos are disengaged in GA mode — the pilot hand-flies the aircraft to follow the FD command bars.
- Note: The lateral mode uses the EHSI heading at time of selection UNLESS the aircraft is on the ground (weight on wheels). On takeoff, with GA mode selected, the lateral go-around mode uses the EHSI heading at liftoff.
- GA mode automatically disengages the autopilot and disarms all other vertical and lateral modes, including PSA. To re-select PSA mode while in GA mode, press vertical SYNC switch on yoke, manually select another vertical mode, or engage the autopilot. Re-engaging the autopilot while in GA mode will put the system in ROL (roll hold) mode, and basic PITCH mode. If other vertical or lateral modes are desired, they must be re-selected.
- GA can also be selected with the autopilot OFF and on the ground (takeoff guidance): pressing GA engages the FD with 14 deg pitch + wings level commands, providing pitch and roll guidance for the takeoff roll and initial climb. Once airborne, the lateral target latches to the heading at liftoff.

**PIT - Mitch Mode (no switch)**
- This is the basic vertical mode of both the autopilot and the flight director.
- With autopilot ON, the pitch command bar can be slewed by using the pitch wheel.
- With autopilot OFF, the pitch of the command bar can be changed by manually flying the aircraft to the desired pitch attitude and pressing the SYNC switch on the yoke
- Overspeed protection is available: When the overspeed warning horn sounds, SPEED mode will automatically be selected and the flight director will command a speed if V(mo)/M(mo) - 2 kts.

**PSA - Preselect Altitude Mode**
- When capture conditions are met, the flight director generates commands to level the aircraft at, and maintain the selected altitude.
- PSA mode is automatically armed when Altitude alerter knob is activated, if not in the Go-around (GA) mode. (If in GA mode, PSA will be armed when: vertical SYNC switch is pressed OR another vertical mode is selected OR autopilot is engaged).
- PSA cannot be armed when GS has been captured.
- Selecting a new altitude in the alerter during capture will cause the flight director to go into basic PITCH mode, and re-arm the PSA mode.
- Selecting a different vertical mode during PSA capture or track will put the system into the new mode and disegage the PSA mode. PSA will not be re-armed until the altitude alerter knob is re-activated

**ALT - Altitude Mode**
- Generates commands to maintain the altitude at time of the selection

**NAV - Navigation Mode**
- Arms when selected and the flight director operates in HDG mode until capture.
- Captures when capture conditions are satisfied. Flight director will generate commands to intercept and maintain the displayed nav systems selected course.
- If the nav data source on EHSI is changed after capture, the flight director will automatically clear NAV mode, synchronize the heading bug, and revert to HDG mode.
- GPS approaches should be flown in the NAV mode

**APPR - Approach Mode**
- As with NAV mode, APPR mode arms when selected, and the flight director operates in HDG mode until capture. When capture conditions are satisfied, the flight direcot will generate commands to intercept and maintain the displayed nav system's selected course. If nav data source on EHSI is changed after capture, the flight director will automatically clear APPR mode, synchronize the heading bug, and revert to HDG mode.
- When ILS data is being used, the flight director amrs for glideslope (GS) capture after localizer (LOC) capture. At GS capture, the currently active vertical mode is automatically cleared, and the flight director will generate commands to intercept and maintain the GS.
- VOR, LOC and ILS approaches should be flown with the APPR mode.

