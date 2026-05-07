# **EADI WITH CROSS-POINTERS**

#### **EADI Displays and Annunciators**

Attitude Display—Pitch attitude is indicated by the position of the blue sky and brown ground area containing the pitch scale with reference to the airplane symbol. Pitch attitude marks are in 5-degree increments up to ±30 degrees. Expanded markings are shown from there up to ±90 degrees.

Roll attitude is indicated by the position of the moving roll attitude pointer with reference to the fixed roll attitude scale. Roll attitude reference marks are located at 0, 10, 20, 30, 45, and 60 degrees on the roll attitude scale.

Aircraft Symbol—This symbol is a stationary representation of the aircraft. Aircraft pitch and roll attitudes are shown by the relationship between the aircraft symbol and the movable pitch and roll attitude display. The aircraft is maneuvered so that the aircraft symbol is 'flown into' the command bars until the two are aligned to satisfy the commands of the selected flight director mode.

Command Bar Display—The magenta command bars are in view when the flight director is being used. The command bars are out of view when the flight director is turned off or flagged, or when the attitude is extreme.

The command bars display computed steering commands to capture and maintain a desired flight path. The command bars move up or down to command a climb or descent, and turn right or left to command a right or left bank. V-bar or cross-pointer command bars are provided as an EFIS system strapping option.

**Inclinometer**—The inclinometer or slip indicator consists of a weighted ball in a liquid-filled curved tube. It is attached to the lower front of the EADI, can be either lighted or unlighted, and is used as an aid to coordinated maneuvers.

| SELECTED<br>ATTITUDE<br>SENSOR                                                | ANNUNCIATION<br>SHOWN ON PILOT'S<br>EADI | ANNUNCIATION<br>SHOWN ON COPILOT'S<br>EADI |  |
|-------------------------------------------------------------------------------|------------------------------------------|--------------------------------------------|--|
| P=#1, C=#2                                                                    | None                                     | None                                       |  |
| P=#1, C=#1                                                                    | ATT1 (yellow)                            | ATT1 (yellow)                              |  |
| P=#2, C=#2                                                                    | ATT2 (yellow)                            | ATT2 (yellow)                              |  |
| P=#3, C=#2                                                                    | ATT3 (white)                             | None                                       |  |
| P=#3, C=#3                                                                    | ATT3 (yellow)                            | ATT3 (yellow)                              |  |
| P=#1, C=#3                                                                    | None                                     | ATT3 (white)                               |  |
| P=#1, C=#4                                                                    | None                                     | ATT4 (white)                               |  |
| P=#4, C=#4                                                                    | ATT4 (yellow)                            | ATT4 (yellow)                              |  |
| P=#3, C=#4                                                                    | ATT3 (white)                             | ATT4 (white)                               |  |
| NOTE: The first five lines apply to both three and four sensor installations. |                                          |                                            |  |

Attitude Sensor Annunciation—Attitude sensor annunciation is displayed in the right center portion (to the left of the vertical deviation scale) of the EADI when any attitude sensor except the primary sensor is selected. A maximum of four attitude sensors, either gyro, ARINC 429 or AHRS (attitude heading reference system) may be installed with the EFIS-86C system.

The pilot's primary sensor is #1 and his secondary sensor is #3. The copilot's primary sensor is #2 and his secondary sensor is #3 with three attitude sensors installed, or #4 with four attitude sensors installed. The above table shows combinations of sensors and annunciations. In the first column, 'P' stands for the pilot's attitude sensor, and 'C' stands for the copilot's attitude sensor.

Flight Control Mode Annunciation—The FCS (flight control system) vertical and lateral modes are annunciated along the top of the EADI. Vertical modes are shown to the right of the lubber line and lateral modes are shown to the left of the lubber line. The active vertical and lateral modes are shown in green and the armed modes and submodes in white. The vertical mode commanded reference data are shown in green and the advisory reference data are shown in white when available.

When a new active mode is displayed, either by being selected or by automatic capture, the mode annunciation flashes for 5 seconds before becoming steady.

#### Autopilot/Yaw Damper and Trim/Sync Annunciation

autopilot/yaw damper annunciation—The autopilot and yaw damper annunciation is displayed at the upper right of the EADI. The autopilot and yaw damper engaged annunciation is 'AP' and 'YD' for a single flight control system, and 'AP →' or '←AP' and 'YD' for a dual flight control system. The engage annunciators are green.

If a disengagement occurs (for both the autopilot and yaw damper), the 'AP' turns yellow (or red if strapped on the DCP) and flashes. Upon acknowledgment by the crew (through the FCS), the engage messages disappear for a single FCS, or the 'AP' and 'YD' disappear and the arrow turns white and becomes steady for a dual FCS.

trim and vertical sync annunciation—The trim annunciation is displayed at the upper left of the EADI. The trim annunciation is a boxed message in yellow that indicates the axis that is mistrimmed (A = aileron, E = elevator and R = rudder). The -003 and later versions of the DPU and MPU have a strapping option for R = roll, P = pitch and Y = yaw annunciation. The annunciation flashes for 5 seconds each time a mistrim occurs and is removed from view immediately when the input is removed.

The annunciation may also be an unboxed 'SYNC', or no message at all (blank). The 'SYNC' message is a flight director function that overrides the trim messages on the side (pilot's or copilot's) that the SYNC button is actuated.

Marker Beacon Display—Marker beacon passage is indicated by a box with 'OM', 'MM', or 'IM' inscribed appearing at the upper right side of the EADI. Outer marker is cyan, middle marker is yellow, and airway or inner marker is white. All marker beacon annunciations flash when they are displayed.

#### **Vertical Deviation Display**

A scale and pointer on the right side of the EADI indicates deviation from a selected vertical flight path. The scale consists of two white dots above and below a yellow center index. The aircraft is below the selected vertical flight path if the pointer is deflected upward. The EFIS-86C system can simultaneously display vertical deviation from primary sensors and second course related sensors depending on DPU/MPU status configurations, selected nav sensor and strapping options.

primary vertical deviation sensors—One of five primary vertical deviation sensors may be displayed. These are: GS, MGP, PGS (LNAV pseudo glideslope), FGS (LNAV controlled glideslope), and VNAV. The deviation pointers for the primary vertical deviation sensors are always displayed to the right of the vertical deviation scale. The primary deviation pointers for GS, MGP, PGS, and FGS are dual green triangles for on-side sensors, and dual yellow triangles for cross-side sensors. The VNAV pointer is a green star-shaped symbol for an on-side sensor and yellow if cross-side.

When GS is the sensor and back localizer mode is selected, the glideslope scale is removed from view and 'B/C' is annunciated vertically to the right of the active course sensor annunciation. The glideslope scale and pointer are removed from view when operating in back course conditions during an LNAV approach.

When LNAV pseudo glideslope is the sensor, the letters 'PGS' are displayed vertically to the right of the top two dots on the vertical deviation scale. When LNAV controlled glideslope is the sensor, the letters 'FGS' are displayed.

Vertical deviation scaling varies with the data source/sensor, LNAV mode and autopilot mode selections.

- For GS, MGP, FGS, and PGS, each of the enroute inner deviation scale dots represent 1/4-degree displacement and each of the outer dots represent 1/2-degree displacement from the vertical flight path.
- For VNAV deviation in -001 version DPU/MPU, each of the inner deviation scale dots represent 200 feet of displacement and each of the outer dots represent 400 feet of displacement from the vertical flight path.
- For VNAV deviation in -002 and -003 version DPU/MPU, each of the inner deviation scale dots represent 500 feet of displacement and each of the outer dots represent 1000 feet of displacement from the vertical flight path.
- For VNAV deviation from an LNAV set to FMS approach mode, -002 and -003 versions DPU/MPU each of the inner deviation scale dots represent 100 feet of displacement and each of the outer dots represent 200 feet of displacement from the vertical flight path.
- For the -004 DPU/MPU version, if the LNAV is using GPS vertical navigation data, the FMS will send the EFIS a scaling word which can range from 1024 feet per dot enroute to 1.00 foot per dot in approach.

second course related vertical deviation sensors—One of two second course related vertical deviation sensors may be displayed. These are: PGS (LNAV pseudo glideslope) and FGS (LNAV controlled glideslope). The deviation pointers for these sensors are cyan triangles and are always displayed to the left of the vertical deviation scale with the apex of the triangles pointing to the right.

The -001 versions of DPU and MPU can show 2ND CRS vertical deviation on the EADI and EHSI at the same time The -002 and later versions DPU/MPU show only the active primary vertical deviation on the EADI and the 2ND CRS vertical deviation shows on the EHSI.

- Radio Altitude Display—Radio altitude is displayed in the lower right corner in green digits. The radio altitude display appears automatically when the radio altitude system is within range (2500 feet with the ALT-55 or standard ARINC radio altimeter, or 2000 feet with the ALT-50) and changes in 50-foot increments above 1000 feet, and 10-foot increments below 1000 feet.
- Radio Altitude Test—When the RA TEST button on the DCP is pushed, the radio altimeter is placed in self-test and outputs a fixed value. If the decision height happens to be set higher than this value, the DH annunciator turns on during the test.
- Decision Height Display—Decision height up to a maximum of 999 feet is displayed in the lower right corner of the display with the letters 'DH' to the left of the digits. This indication is cyan in color if set from the on-side DCP or yellow if from the cross-side DCP.

If the DH/RNG knob on the DCP is pushed in, the decision height display is in view continuously and may be changed by rotating the DH/RNG knob. A rapid turn of the knob gives a minimum 300 -foot change in the DH. If the DH/RNG knob is pulled out, the decision height display is removed from view. It remains out of view until the knob is pushed in again, or until the aircraft descends through 1000 feet agl (radio altitude) at which time the DH display appears flashing for 10 seconds and is then removed from view.

Decision Height Annunciator—When decision height is reached during descent, the yellow letters 'DH' appear in the upper left center portion of the attitude display, flash for 5 seconds, and then become steady.

The DH annunciator is off when the strut switch is compressed (weight-on-wheels), and for 20 seconds after the strut switch is extended. Also, the DH annunciator remains off if DH is set to zero or turns off if the radio altimeter fails.

#### **Lateral Deviation Display**

A scale and pointer in the bottom center of the EADI indicates deviation from a selected lateral navigation path. The scale is the same for all sensor types and consists of two white dots on either side of a white center index. Various deviation pointer symbols move laterally along the deviation scale. All onside sensor pointers show in green and cross-side sensor pointers show in yellow. The EFIS-86C system can simultaneously display lateral deviation from primary sensors and second course related sensors.

primary lateral deviation sensors—The primary lateral deviation pointer may be driven by VOR, LOC, MAZ, PLOC (LNAV pseudo localizer), FLOC (LNAV controlled localizer), TCN, or LNAV (FMS, LNV, RNV, LRN, VLF, INS, GPS, etc) sensors. The scaling for lateral deviation changes, as follows, depending on the selected sensor, autopilot mode, and LNAV mode:

- <span id="page-37-0"></span>• For all angular sensors (VOR, TCN, RNV, etc.) the scale is 5° per dot.
- For VOR sensors in linear mode the enroute scale is 5 nmi per dot.
- For VOR sensors in linear mode with an autopilot in approach mode the scale is 1 nmi per dot.
- For an LNAV sensor the enroute scale is 3.75 nmi per dot.
- For an LNAV in approach mode the scale is 1 nmi per dot.
- For GPS (-004 DPU/MPU), the FMS will send the EFIS a scaling word which can range from 8 nmi
  per dot enroute to 0.015 nmi per dot in approach. The EFIS limits the scale factor at the upper and
  lower bounds.

In the LNAV approach mode, the annunciator 'APPR' shows just above the left side of the lateral deviation to indicate the approach mode deviation scaling is in use. In the case of GPS, if the scaling word is changing from one level to the next, a 'SCALING' annunciation is shown at a position located above the 'APPR' annunciator location. When conditions exists such that a final approach can be made, the 'APPR' annunciation is displayed if the final approach scaling is linear. The 'LIN' annunciation is removed if the final approach segment simulates a pseudo localizer approach. In GPS, if the GPS data is invalid the scale reverts to previous operations.

When an approach is being flown and the appropriate sensor is selected, the pointer changes to a rising runway symbol after descending to a radio altitude of 200 feet. At 200 feet of radio altitude, the runway symbol begins expanding both vertically and laterally until at zero-foot altitude, the top edge of the runway symbol just touches the bottom edge of the aircraft symbol. The bottom edge of the runway symbol remains adjacent to the deviation scale. In -002 and later versions DPU and MPU, the pointer symbol for PLOC (LNAV pseudo localizer is a diamond-shaped rectangle. In these systems, if PLOC is the sensor during an approach, the diamond-shaped pointer does *not* change to the rising runway symbol at 200 feet radio altitude.

second course related lateral deviation sensors—Second course lateral deviation is displayed on the EADI only in configurations using the -001 version DPU and MPU. DPU and MPU -002 and later versions show second course lateral deviation only on the EHSI (see EHSI Display Formats section).

In the case of the -001 DPU/MPU, one of two second course related lateral deviation sensors may be displayed. These are: PLOC (LNAV pseudo localizer) and FLOC (LNAV controlled localizer).

If pseudo ILS approach data is received from the LNAV selected as the active sensor, the EFIS-86C uses this data in place of real ILS data. This is annunciated by the letters PLOC' located above the right two lateral deviation dots. A second deviation pointer, cyan in color, is also displayed showing the deviation from the second course. This should coincide with the actual runway heading. When the pseudo localizer is within capture range, the second course PLOC replaces the active sensor, and the only remaining deviation is PLOC.

The LNAV controlled localizer is selected on the LNAV's CDU and is displayed on the EADI when the LNAV is selected as the active sensor. The operation is the same as the pseudo ILS described above except that the annunciation is 'FLOC'.

Acceleration (When On The Ground) or Mach Display—The same display location in the lower left corner is used for acceleration when on the ground, or airborne Mach readout. When on the ground, a three-digit magenta readout preceded by a decimal point represents longitudinal acceleration in g's. A leading minus sign indicates deceleration. In flight, the three-digit green readout displays Mach number in .002 Mach increments. The readout comes into view above .300 Mach and falls out of view below .290 Mach.

- **Speed Displays**—The EFIS-86C may display indicated airspeed, fast/slow speed deviation from a digital air data system, angle of attack system, or an analog air data system, or no speed display at all. These are installation strapping options.
  - IAS (Indicated Airspeed) Display—IAS is shown by one of two scales on the left side of the EADI. The two scales are referred to as the 'low-IAS' and the 'high-IAS' scales. The determination of which scale is to be displayed is based on actual airspeed. The scales and scale markings are white.

The low-IAS scale covers the range from 60 to 190 knots and is divided into 10-knot increments. The high-IAS scale covers the range from 160 to 400 knots and is divided into 20-knot increments. Scale markings are on the left of the vertical scales. The low-IAS scale is displayed at power on. (See page 35.)

There are three continuation dots at the upper end of the low-IAS scale and three continuation dots at the bottom end of the high-IAS scale. These dots serve to remind the pilot that the currently displayed scale is continued in the direction of the dots. If the low-IAS scale is shown, as "IAS increases toward the dots at the top, the pilot knows that the scale will change over and continue on the high-IAS scale. Conversely, if the high-IAS scale is shown, as IAS decreases toward the dots at the bottom, the pilot knows that the scale will change over and continue on the low-IAS scale.

The scale changeover point from low-IAS to high-IAS occurs as follows:

- --- IAS 190 knots, or
- —IAS 160 knots <u>and</u> flaps up <u>and</u> trend limited at upper edge <u>and</u> acceleration has been 1.5 kts per second for more than 30 knots.

The scale changeover point from high-IAS to low-IAS occurs as follows:

- —IAS 160 knots, or
- -IAS 170 knots and trend limited at lower edge, or
- —IAS 190 knots <u>and</u> flaps extended <u>and</u> scale has not switched from low to high with flaps extended within the last 30 seconds

If the difference between the pilot's and copilot's air data is less than 10 knots, then the copilot's scale switching follows the pilot's side. If the difference between the two sides is greater than 10 knots or if the pilot's side is flagged, then the copilot's scale switching is independent of the pilot's side.

Actual IAS is shown by the position of a small green rectangular marker extending across the low-or high-IAS scale, and is repeated in green digits to the right of the marker. The marker and digital readout move below the end of the low-IAS scale for values below 60 knots until they have moved out of the viewing area on the display. For actual IAS values above 400 knots, the marker and digital readout park at the upper end of the high-IAS scale with the digital readout continuing to display actual IAS.

On the high-IAS scale, Vmo is indicated by two parallel red lines that extend upward from Vmo a maximum of 1/2 inch. The right hand red line covers the scale. Above Vmo, the actual IAS marker, digital readout, and Mach display turn red.

Selection of cross-side air data is indicated by the green actual IAS marker, digital readout, and Mach display all turning yellow. In addition, a yellow 'XADC' (cross-side air data) annunciation appears on the left side of the EADI just above the horizon line. If actual IAS becomes greater than Vmo, the yellow values turn red until actual IAS drops below Vmo.

Reference Airspeed—Reference indicated airspeed is displayed by a cyan colored triangular shaped bug to the left of the scale. Under certain special equipment and interconnect conditions, reference airspeed is repeated digitally in a half-box at the upper left of the low-IAS scale or at the lower left of the high-IAS scale. When in view, the digital readout and half-box are also cyan.

The reference IAS bug setting has to be within the range of the IAS scale presently in view before the bug is displayed. The bug never appears outside the limits of either scale, and never appears next to the three continuation dots at the upper end of the low-IAS scale or the bottom end of the high-IAS scale.

The reference airspeed digital readout and half-box appear only under the following conditions:

- In view full time whenever the reference IAS bug is not on the IAS scale presently being displayed.
- If the reference IAS bug is on scale, the digits and half-box appear whenever the reference IAS is being changed and for 10 seconds thereafter.
- Whenever a scale changeover occurs, the digits and half-box will be in view for 10 seconds.
- If not already in view, the digits and half-box appear for 20 seconds when descending through 1000 feet radio altitude in approach.

The reference airspeed display is removed from view whenever the reference airspeed is set below 70 knots. If a failure is detected in the reference airspeed, the bug and digital readout are removed from view.

In the -003 and later DPU/MPU and also depending upon installation configuration, up to eight reference IAS bugs can be displayed along the IAS scale. All bugs have a programmed initial value at power up (these values come from the air data computer and are determined at certification). These bugs are set/controlled by the ARP-86() Air Data Reference Panel. The symbols used to represent the bugs come from the air data computer and may vary depending upon user preference. Bug colors (determined in the air data module during certification) may be cyan, green, amber, red, magenta, blue, or white. Once set, the bugs move up or down the IAS scales. The -001 and -002 DPU and MPU can display only the reference IAS bug as presented in the paragraphs above.

IAS Acceleration Trend—Extending upward or downward from the center of the actual IAS digital readout is an acceleration trend vector consisting of two parallel magenta bars. It is in view only when the strut is extended, but is removed if radio altitude is less than 30 feet or if speed is less that 50 knots. When the trend vector reaches the display edge limit or the maximum length limit, a horizontal line shows across the end of the trend vector.

A digital readout of acceleration (in g's) shows in the lower left corner of the display when the airplane is on the ground and the source of longitudinal acceleration is valid. The acceleration readout consists of a decimal point, three magenta numbers, and minus sign (the minus sign shows only during ground deceleration).

The acceleration trend information is derived from actual IAS, longitudinal acceleration, and pitch. The trend vector shows on the display even if an acceleration fault is detected. Detection of a fault shows a red box with the letters 'ACC' inscribed in place of the acceleration numbers when the airplane is on the ground and for 20 seconds after strut extension. This flag flashes for 10 seconds and stays on. Push the master warn reset to stop the flashing prior to the 10 second timeout. Also, if longitudinal acceleration is invalid, the 'ACC' flag shows during the first 4 seconds of the self-test.

The loss of pitch angle data from the attitude source degrades the trend vector, but continues to show on the display for -001 and -002 versions of the DPU and MPU. In -003 and later versions

DPU/MPU, detection of a loss of pitch angle data from the attitude source turns off the display of the trend vector.

Speed Deviation Display—If the IAS scale and display are not used in a particular installation, then one of three sensors may be selected as the input for the fast/slow speed deviation display. These are:

- · Digital air data system
- · AOA (angle of attack) system
- · Analog air data system

The speed deviation display is located on the left side of the EADI (in the same location that the IAS display would normally occupy). The speed deviation scale consists of four dots with the letters 'F' and 'S' to the left of the top and bottom dots respectively. The speed deviation pointer is green and consists of two concentric squares which move in relation to the scale such that if the pointer is next to the upper dot, then actual airspeed is 10 knots higher than desired.

With a digital air data system, the EFIS-86C compares actual IAS with the reference IAS being received from the air data system, and positions the pointer accordingly. With either the AOA or analog air data input, the EFIS-86C positions the pointer with reference to the analog voltage received from the respective system.

When speed deviation is from a digital air data system, the digital reference airspeed is displayed below the letter 'S' on the speed scale. When speed deviation is AOA based, the letters 'AOA' appear below the speed scale, and if speed deviation is analog air data based, the letters 'SPD' appear below the speed scale. These displays are always cyan in color.



---

[🡅](./toc.md) ·•⦁•· [🡄 **EADI WITH V-BARS**](./EADI-WITH-V-BARS.md) ·•⦁•· [**LATERAL AND VERTICAL MODE NOTES:** 🡆](./LATERAL-AND-VERTICAL-MODE-NOTES.md)