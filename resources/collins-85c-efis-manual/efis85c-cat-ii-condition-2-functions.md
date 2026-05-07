# **Condition 2 Functions**

- Any of the following occurs on the side that the autopilot is coupled:
- -0n-side flight director flag in view.
- -0n-side attitude flag in view.
- -0n-side heading flag in view.
- -Glideslope capture and the on-side localizer flag in view.
- -Glideslope capture and the on-side glide slope flag in view.
- Attitude comparator warning is present.
- Autopilot is disconnected.
- Either of the following occurs below 200 feet of radio altitude:
- -Excessive localizer deviation is present.
- -Excessive glideslope deviation is present.

49

#### <span id="page-56-0"></span>**EHSI Display Formats**

The EHSI brings together numerous displays to show a map-like presentation of the aircraft's horizontal navigation situation. The EHSI shows aircraft heading and aircraft displacement relative to VOR radials, localizer, and glideslope beams. Deviation from other lateral and vertical sensors may also be shown.

The EHSI can display three formats that are selected with the HSI MODE button on the DCP-85F/85H Display Control Panel. These are the full compass rose, sector, and sector with map formats. The EHSI provides the following display information:

#### Rose, Sector, or Sector With Map Formats

- · Aircraft symbol
- Heading display and sensor type (MAG#, TRU#, or DG#) annunciation
- · Selected heading cursor
- Active selected arrow pointer and lateral deviation bar
- · Active selected course digital display
- Annunciation of deviation type (ANG, LIN, XTK, or B/C)
- · Active selected course navigation sensor annunciation
- Active selected course to/from arrow (rose format)
- Active selected course 'TO'/FR' annunciation (sector and sector with map formats)
- Second course arrow and course deviation (no deviation scale or to/from information is provided)
- Second course navigation sensor annunciation
- · Vertical deviation display
- · Bearing pointer display and sensor annunciation
- Distance to VOR/DME or waypoint
- Waypoint or DME identifier and waypoint alert
- DME hold annunciation
- Navigation data display (GS/TTG/ET, or TAS)
- Wind direction/speed from a compatible LNAV
- DR and MSG annunciation from a compatible LNAV
- · Separate (second) heading cursor controlled by a compatible LNAV
- · Weather radar target alert
- Reversionary source annunciation
- Flags and comparator warnings

#### **Sector Format**

- Expanded compass segment across the top of the display
- · Aircraft symbol relocated at bottom center of display
- Second course VOR/DME/VOR-DME/waypoint symbol with identifier or number placed in rho-theta position with respect to the aircraft symbol and selected range
- Second course arrow automatically appears when a compatible LNAV is in a NAV to NAV capture mode.
- Weather radar range and mode annunciation
- · Weather radar display
- Range is selected from the WXP when a weather radar mode is selected or with the DH/RNG knob on the DCP when weather radar is not selected

#### **Sector With Map Format**

- Also uses the expanded compass segment
- Places VOR and/or waypoint symbols for both active selected and second course in proper rho-theta
  position with respect to the aircraft symbol and selected range
- DME ident is shown next to the VOR/DME symbols
- · Selected course lines are drawn through the symbols
- Waypoint strings (up to five waypoints) are shown with their numbers or identifiers next to the symbol and with the symbols connected by desired track lines
- · Weather radar display and range selection same as in sector format

#### EHSI Displays and Annunciators in the Rose Format

### **NOTE**

For all EHSI formats, when the navigation sensor is selected from the on-side DCP, the course arrow, deviation bar, to-from arrow, digital course readout, navigation sensor annunciator, distance display, bearing pointer sensor annunciator, data display, and LIN/ANG annunciation are green. If control has been transferred to the cross-side, these displays are yellow for all navigation sensors.

Bearing Pointer Display—The bearing pointer indicates relative bearing to the selected NAVAID. In the EFIS-86C system, the bearing pointer is magenta and may be driven by a #1, #2, or #3 sensor (available sensors are determined during installation).

Bearing pointer selection is made using the BRG button on the DCP. Sequentially pushing the BRG button steps through the available sensors. The selected sensor is annunciated in magenta in the lower left of the EHSI for 5 seconds after a selection is made. This annunciation then blanks until another sensor is selected. If the BRG button is pushed and held for approximately 1/2 second, the bearing pointer turns off.

The letters 'A' (ADF), 'V' (VOR), 'T' (TCN), or 'N' (LNAV) appear beneath the head of the pointer to indicate the sensor type. If the bearing is from a #1 sensor, the pointer has a single bar on both the head and tail of the pointer. If the bearing is from a #2 or #3 sensor, the pointer has a double or triple bar head and tail respectively.

When VOR is the sensor and a localizer frequency is tuned, the bearing pointer is removed from view. The pointer is also removed from view if a failure is detected in the sensor currently driving the pointer.

If the heading sensor is not compatible with the navigation sensor, the letter 'A', 'V', 'T', or 'N' flashes as follows. For ADF, the 'A' flashes for 10 seconds then becomes steady, except GPS -004 version DPU/MPU do not flash. For VOR, TCN, or LNAV, the 'V', 'T', or 'N' flashes continuously until a compatible selection has been made (for LNAV, the flashing 'N' will be corrected and not flash if magnetic variation is available).

LNAV Annunciation—When the active selected course is from an LNAV, 'MSG' (flashing yellow) and 'DR' (yellow) annunciations may appear as received from the LNAV. 'MSG' appears below the waypoint identifier at the upper left of the EHSI, and 'DR' appears to the left of the distance display, also at the upper left of the EHSI.

The letters 'APPR', in white, are annunciated above the left dots of the lateral deviation scale if a compatible LNAV is controlling pitch and bank commands during an approach. For GPS -004 version DPU/MPU, a white 'SCALING' annunciation shows above 'APPR'.

Compass Display and Heading Sensor Type—The compass display is a full 360-degree compass rose with letters at the cardinal points and numbers at the 30-degree marks. Aircraft heading is read against the lubber line which has a 'MAG#', 'TRU#', 'DG#', or 'HDG#' annunciation to the right of the lubber line to indicate whether the source of heading information is magnetic or true referenced, or if DG (directional gyro) mode is selected or heading failure exsists. Markings are provided every 45 degrees around the perimeter of the card to aid in procedure turns.

The '#' symbol behind the 'MAG', 'TRU', 'DG', or 'HDG' annunciation may be a '1', '2', '3', or '4', depending upon the number of sensors in the installation. The on-side 'MAG' annunciation is not displayed unless both sides have that sensor selected. Any time the left and right heading displays are from the same sensor, annunciations are displayed in yellow on both EHSIs. Secondary sensor annunciation is in white if not the same on both sides.

The following table describes the heading sensor annunciation. In all columns, the number symbol (#) shown before the digit represents either 'MAG', 'TRU', 'DG', or 'HDG'. In the first column, 'P' stands for the pilot's heading sensor, and 'C' stands for the copilot's heading sensor.

| SELECTED<br>HEADING SENSOR | ANNUNCIATION SHOWN ON PILOT'S EHSI | ANNUNCIATION SHOWN ON COPILOT'S EHSI |
|----------------------------|------------------------------------|--------------------------------------|
| P= #1, C= #2               | Note (1)                           | Note (2)                             |
| P= #1, C= #1               | #1 (yellow)                        | #1 (yellow)                          |
| P= #2, C= #2               | #2 (yellow)                        | #2 (yellow)                          |
| P= #3, C= #2               | #3 (white)                         | Note (2)                             |
| P= #3, C= #3               | #3 (yellow)                        | #3 (yellow)                          |
| P= #1, C= #3               | Note (1)                           | #3 (white)                           |
| P= #1, C= #4               | Note (1)                           | #4 (white)                           |
| P= #4, C= #4               | #4 (yellow)                        | #4 (yellow)                          |
| P= #3, C= #4               | #3 (white)                         | #4 (white)                           |

NOTE (1): Blank if MAG heading is selected, 'TRU1', 'DG1', or 'HDG1' for the other selections.

NOTE (2): Blank if MAG heading is selected, 'TRU2', 'DG2', or 'HDG2' for the other selections.

NOTE (3): The first five lines apply to both three and four sensor installations.

NOTE (4): The legend MAG was used as an example; it can be replaced by TRU, DG, or HDG.

Selected Heading Display—Selected heading is shown by the location of two adjacent magenta rectangles (heading cursor) with respect to the compass card. The selected heading is repeated digitally in magenta in the lower right corner of the EHSI below the magenta letters 'HDG'.

The HDG knob on the CHP may be used to set the heading cursor or it can be made to rotate to the lubber line by momentarily pushing the PUSH HDG SYNC button on the HDG knob (the heading sync function may also be remotely actuated by mode logic from some digital autopilots). If a single CHP-85C is used and the left side DCP and cross-side data are valid, the right side selected heading cursor follows the left side. If two CHP-86Cs are used, or if cross-side data is invalid, each side's heading cursor acts independently.

In -002 and later version DPU and MPU, if a compatible LNAV is selected, it may be used to control the heading cursor instead of using the HDG knob on the CHP. A separate LNAV heading cursor shows around the outside edge of the compass card to show the selected LNAV heading. The cursor

shows in green as a single line arc parallel to the arc of the compass card with three perpendicular lines, one at each end and one in the center, from the arc to the outer edge of the compass card. When centered over the magenta heading cursor, it surrounds it on three sides. An annunciator 'FDHG#' (# is the navigator number) and a numeric readout show in green above the magenta HDG annunciator in the lower right corner of the display. A heading change entered from the LNAV will cause both heading cursors to slew to the entered heading. The present position of the selected heading cursor is also transmitted on the MPU bus so the LNAV can stay updated with any change in the selected heading. This feature does not inhibit the CHP from controlling the heading cursor. If a secondary LNAV is selected on either side, it will then control the heading cursor in place of that side's primary LNAV.

Active Selected Course Display—Active selected course is shown by the relationship of the solid double bar course arrow with respect to the compass card. The aircraft symbol pictorially shows actual aircraft position in relation to this selected course. The active selected course is repeated digitally in the lower left corner of the EHSI below the letters 'CRS'. The active selected course navigation sensor is annunciated at the lower left center of the EHSI.

The course is selected with the CRS knob on the CHP when in VOR, LOC, RNV, TCN, ADF, or MLS mode, or is automatically set by a lateral navigation system (INS, VLF, GPS, LRN, LNV, FMS, etc) when an LNAV is selected. (ADF course selection has been removed from -004 GPS version DPU and MPU). Once set, the course arrow rotates with the compass card to provide a continuous display of the selected course and course error with respect to aircraft heading. This data is supplied to the flight control system. If a localizer frequency has been tuned, VOR/LOC has been selected, and the selected course is more than 105 degrees from the lubber line, the ANG legend to the right of the selected course annunciation changes to B/C (back course).

If a VOR approach is being flown, the letters 'APPR', in green (on-side sensor) or yellow (cross-side sensor), are annunciated in the lower left quadrant of the EHSI as well as in the lower portion of the EADI. This annunciation indicates lateral deviation rescaling has occurred in support of VOR approach condition.

#### NOTE

During a VOR approach, select APPR mode only when within normal approach distances and not until after VOR capture. The autopilot automatically changes to dead reckoning (DR) mode when a VOR station is crossed. DR is *not* a recommended approach mode. If the VOR approach is one that crosses the VOR on the way to the airport, select HDG mode at station passage instead of continuing with NAV or APPR mode (ensure the heading cursor is under the lubber line before selecting HDG mode). The reason for this is if the distance between the VOR and the airport is short, the system may not have time to come out of DR mode after crossing the station.

If the selected navigation sensor is incompatible with the heading type (TRU or MAG), the sensor annunciation flashes until a compatible selection is made. If the sensor is an LNAV and magnetic variation is available, the LNAV data is corrected and no flashing occurs.

To/From Arrow—The to-from arrow indicates that the selected course is either 'to' or 'from' the selected NAVAID. The to-from arrow can also indicate the course to the next waypoint or the course from an overflown waypoint when an LNAV is the navigation sensor. If a compatible LNAV is installed and LNAV is selected, the 'to' arrow flashes to indicate waypoint alert. The to-from arrow is removed from view whenever a localizer frequency is selected.

<span id="page-60-0"></span>TWR-850 Weather Annunciation—When TGT (target alert) mode is selected on the WXP-850, the letters 'TGT' appear in cyan. Target alert notifies the pilot of the following two weather phenomena:

- —When weather targets that are producing rainfall rates greater than 0.5 inch (12.7 millimetre) per hour are detected.
- —When turbulence consisting of *precipitation* areas where *horizontal* wind velocity shifts in excess of 16.40 feet-per-second (5 metres-per-second) are detected.

#### NOTE

Doppler turbulence detection techniques used in the TWR-850 Turbulence Weather Radar System rely on the presence of at least light precipitation. The pilot should note that the TWR-850 system is *not* capable of detecting clear air turbulence.

The TGT mode provides a target alert 'window' from 7- to 200-nmi range (50 nmi maximum range for turbulence detection) and ±15 degrees of dead ahead, regardless of the range selected on the WXP.

A flashing yellow box with the letters 'TGT' inscribed appears when a precipitation target is detected within the target alert 'window'. A flashing yellow box with the letters 'TRB' inscribed appears when an area of precipitation related turbulence is detected within the target alert 'window'. If areas of precipitation and turbulence are both detected within the target alert 'window', the flashing annunciation alternates between 'TGT' and 'TRB' but at a faster rate of flashing.

The flashing annunciation tells the pilot that areas of precipitation and/or turbulence have been detected, and weather radar should be put back on the display and analyzed.

Data Display—Pushing the NAV DTA button on the CHP sequentially selects elapsed time, ground speed, time-to-go, or true airspeed for display under the letters 'ET', 'GSP', 'TTG', or 'TAS' as applicable. The last data display selected is stored and reappears at the next power up.

Ground speed and time-to-go are from the same sensor selected for the active course, and are the same color. If that sensor is VOR, the calculation occurs in the EFIS system. Otherwise, the navigation system transmits the data. No-computed-data from a valid VOR/DME source replaces the TTG or GS numeric readout with dashes in the same color as the annunciator label. Failure of the VOR/DME or LNAV data source; or detection of an inactive data bus from the data source turns off the numeric readout for TTG or GS. Failure or an invalid flag from the air data source turns off the TAS numeric readout and failure of a DCP turns off the ET numeric readout.

True airspeed shows cyan if from the on-side air data system and yellow if from the cross-side system.

Ground speed and true airspeed display range is 0-999 knots with 1 knot resolution, and time-to-go display range is 0 to 399 minutes with 1 minute resolution.

Elapsed time is shown in minutes and seconds up to 59:59 and then in hours and minutes up to H9:59. Above H9:59, the display is dashed. Sequentially pushing the ET button on the CHP controls the reset/start/stop cycle of the timer. The elapsed time display is cyan unless DCP control has been transferred in which case the display changes to yellow. Sequentially pushing an installer supplied switch controls the reset/start/stop cycle of the timer. The first push of the switch starts the timer. The second push stops the count and the next push resets the timer to zero. Once the timer has been started, other data may be selected for display via the NAV DTA button on CHP without disturbing the count.

<span id="page-61-0"></span>The -002 and later versions DPU and MPU, in combination with appropriate LNAV systems, can show LNAV-generated TTG and GS data. In this mode the data is annunciated FTTG and FGS to identify LNAV-generated data. For this data mode to occur, the DME/VOR sensor must be turned on, be valid and in the no-computed-data mode or dashes will be displayed. All other functions of FTTG and FGS are the same as described for the TTG and GS annunciators.

Wind Display—Relative wind speed (digitally in knots) and direction (via an arrow), if available as an input from a compatible LNAV, is displayed full time to the left of the lubber line.

The wind display is white if from the on-side LNAV and is yellow if from the cross-side LNAV. If the on-side LNAV is not valid, the wind display automatically switches to the cross-side system. The wind display is blanked if data is not available from either LNAV.

Second Course Display—Second course arrow selection is made using the 2ND CRS button on the DCP. Sequentially pushing the 2ND CRS button steps through the available sensors. If the 2ND CRS button is pushed and held for approximately 1/2 second, the second course arrow turns off.

When the second course arrow has been selected for display, it appears in cyan as a single-line course arrow with a solid arrowhead. The center portion of the course arrow is the second course lateral deviation bar. The deviation displayed is always angular and is never linearized. No deviation scale or to-from indicator is provided for the second course arrow. The navigation sensor selected for the second course is annunciated in cyan immediately above the navigation sensor annunciation for the active selected course arrow.

If the second course navigation sensor is incompatible with the heading sensor (true or magnetic), the navigation sensor annunciator flashes until a compatible selection is made. If the sensor is an LNAV and magnetic variation is available, the LNAV data is corrected and no flashing occurs.

second course VOR/LOC, TCN, or RNV sensors—When the second course is a VOR/LOC, TCN, or RNV, the on-side CHP's selected CRS knob controls the course setting if the CRS knob is not being used for a different sensor. If the CRS knob is being used for the active selected course, the second course arrow is set to the bearing with the deviation zeroed.

If the DME associated with the displayed VOR, TCN, or RNV is put into hold, a yellow 'H' is added to the right of the numeral in the second course navigation sensor annunciation. If the DME associated with the displayed VOR, TCN, or RNV fails, a yellow 'D' is added to the right of the numeral in the navigation sensor annunciation.

When the second course is a VOR or TCN and a localizer frequency has been tuned, the sensor annunciation changes to 'LOC1' or 'LOC2'.

second course LNAV sensors—One of two second course related lateral navigation sensors may also be displayed. These are: PLOC (LNAV pseudo localizer) and FLOC (LNAV controlled localizer).

If pseudo ILS approach data is received from the LNAV selected as the active sensor, the EFIS-86C uses this data in place of real ILS data. This is annunciated by forcing the second course sensor annunciation to be 'PLOC#' where '#' is the active LNAV reference number. The second course arrow is driven by data from the LNAV and overrides any pilot selected second course. This second course data should coincide with the actual runway heading. When the pseudo localizer is within capture range, the second course PLOC replaces the active sensor, and the only remaining deviation is PLOC.

<span id="page-62-0"></span>The LNAV controlled localizer is selected on the LNAV's CDU and is displayed on the EHSI when the LNAV is selected as the active sensor. The operation is the same as the pseudo ILS described above except that the annunciation is 'FLOC#'.

Vertical Deviation Display—A scale and pointer on the right side of the EHSI indicates deviation from a selected vertical path. The scale consists of two white dots above and below a yellow center index. The pointer is green from an on-side sensor and yellow if from a cross-side sensor. The aircraft is below the selected vertical path if the pointer is deflected upward.

The output from one of five vertical deviation sensors may be displayed. The sensors are GS, MGP (microwave glidepath), PGS (LNAV pseudo glideslope), FGS (LNAV controlled glideslope), and VNAV (vertical navigation). One of three scale types may be displayed. The conditions governing these are as follows:

- GS = VOR/LOC selected, LOC tuned and not back course.
- MGP = MLS selected.
- PGS = LRN selected and pseudo ILS capture initiated.
- FGS = LRN selected and ILS capture initiated.
- VNAV = VNAV enabled and no GS, MGP, PGS, or FGS display.
- None = None of the above

GS and MGP vertical deviation—For GS and MGP, each of the inner scale dots represents a 1/4-degree displacement and each of the outer scale dots represents a 1/2-degree displacement. The deviation pointer shape is a dual triangle, green for on-side and yellow for cross-side. When GS is the sensor and back localizer mode is detected, the glideslope scale is removed from view and 'B/C' is annunciated to the right of the active course navigation sensor annunciator.

PGS and FGS vertical deviation—When PGS or FGS is the selected vertical deviation sensor, the letters 'PGS' or 'FGS' are annunciated vertically to the right of the top two dots on the vertical deviation scale. This annunciation coincides with the PGS and FGS annunciation on the EADI for LNAV pseudo glideslope and LNAV controlled glideslope respectively.

The shape of the deviation pointer is the same as for GS and MGP in all cases, except for -002 and later DPU and MPU. In this case the pointer symbol shows as a diamond on its side with a horizontal center line.

If a compatible LNAV is selected and is in approach mode, one-dot deviation from the selected vertical path represents 100-foot displacement. LNAV approach mode is annunciated by the white letters 'APPR' located just above left center of the display.

VNAV vertical deviation—The VNAV deviation pointer is a green star-shaped symbol for the on-side sensor and yellow star-shaped symbol for cross-side. The vertical deviation pointer represents the center of ther VNAV track and the center of the scale represents the airplane position relative to ther VNAV track.

VNAV deviation scaling varies with DPU/MPU configuration status as follows:

- For -001 version DPU/MPU, each of the inner deviation scale dots represent 200 feet of displacement and each of the outer dots represent 400 feet of displacement from the vertical flight path.
- For -002 and -003 version DPU/MPU, each of the inner deviation scale dots represent 500 feet of displacement and each of the outer dots represent 1000 feet of displacement from the vertical flight path.

**EHSI DISPLAY FORMATS** 

- For the -004 DPU/MPU version, if the LNAV is using GPS vertical navigation data, the FMS will send the EFIS a scaling word which can range from 1024 feet per dot enroute to 1.00 foot per dot in approach.
- For all LNAVs set to FMS approach mode, each of the inner deviation scale dots represent 100 feet of displacement and each of the outer dots represent 200 feet of displacement from the vertical flight path. The white annunciator 'APPR' shows above the left two dots of the lateral deviation scale.
- Lateral Deviation Bar-The center portion of the course arrow is the lateral deviation bar which represents the centerline of the selected course. This bar moves laterally with respect to the course arrow and the white deviation dots to indicate deviation from the selected course.

If a localizer frequency is tuned, VOR/LOC is selected on the DCP, and the selected course is more than 105 degrees from the lubber line, the annunciation 'B/C' (back course) appears to the right of the active course navigation sensor annunciator. When 'B/C' is annunciated, the course deviation automatically reverses to provide the correct left/right deviation for back course approaches.

LIN/ANG/XTK and B/C (Back Course) Annunciations—When flying VOR, TCN, or RNV with the deviation linearized, 'LIN' is annunciated. Linear deviation optimizes computation while tracking a VOR. TCN, or RNV course, especially close in to the station. EFIS always linearizes deviation whenever DME is present and not in DME hold, unless an external switch is actuated to defeat linearization and display angular deviation ('ANG' is annunciated).

Linear deviation is turned off if a localizer frequency is tuned in either VOR or APPR mode. Angular deviation is used in approach mode, but is not annunciated. 'XTK' (cross-track deviation) is annunciated when the LNAV is flying an offset.

When VOR, TCN, or RNV is the active sensor and the deviation changes from 'LIN' to 'ANG' (such as would occur if the DME is lost or DME hold is selected), the 'ANG' annunciator flashes for 10 seconds before becoming steady. The flashing can be eliminated by pushing the master warn reset.

'B/C' (back course) is described in the preceding lateral deviation bar paragraphs.

Waypoint or DME Identifier and Waypoint Alert—The station ident of the selected DME or the ident of the first waypoint is shown directly below the digital distance display. When the ident is for a waypoint, it flashes to indicate waypoint alert.

Distance Display-The distance to the VOR, TCN, RNV, or waypoint selected for display by the active course arrow is shown digitally below the letters 'DIST'. Resolution is 0.1 nmi below 100 nmi, and 1 nmi above 100 nmi. When DME hold has been selected, the letter 'H', in yellow, appears to the right of the digits.



---

[🡅](./toc.md) ·•⦁•· [🡄 **Condition 1 Functions**](./Condition-1-Functions.md) ·•⦁•· [COMPARATORS, ROSE FORMAT 🡆](./COMPARATORS-ROSE-FORMAT.md)