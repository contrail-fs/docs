
## **SECTION 2**

## **PAGE DISPLAY DEFINITIONS**

The following section contains definitions pertaining to information and format seen when a particular function key is depressed.

## **PAGE DISPLAYS AT POWER-UP**

For a better understanding of the GNS-XLS functions, this section should be reviewed prior to operating the system.

## **SELF TEST PAGE**

For the first 30 seconds after the system if is turned on, the computer performs extensive internal tests that must be successfully completed before proceeding further. If the system detects a problem the **SELF TEST** display may be replaced by a **NO DATA RECEIVED** message. The unit may have to be removed for service.

Figure 2-1

## **INITIALIZATION PAGE**

After the Self Test is successfully completed, the **INITIAL-IZATION** Page will be displayed. Refer to Figure 2-2.

## **DATE:**

The current Greenwich Date is displayed as day, month and year.

Figure 2-2

## **GMT:**

Time of day is displayed in Greenwich Mean Time hours and minutes.

## **IDENT:**

Displays the airport identifier for the airport closest to the system shut down position. Dashes will be displayed when the cursor is placed over the position **(POS)** field.

## **POS:**

Displays the last system position at shut down. Dashes are displayed when the cursor is over the **IDENT** field.

## **PART NUMBER AND SOFTWARE MODIFICATION STATUS:**

The bottom line of the display shows the unit part number and the software level of the unit.

NOTE: This page cannot be recalled once **DATE, GMT,** and **POS** have been entered. In order to display this again, the system must be turned off and then turned back on.

## **FLIGHT PLAN SECTION (FPL KEY)**

Upon pressing the **FPL** Key the **FLIGHT PLAN LIST 1/1** Page will be displayed and the following can be observed.

NOTE: The **FLIGHT PLAN LIST** page may automatically be displayed if the **ENTER** key is depressed at least three times while on the initialization page.

## **FLIGHT PLAN PAGES**

NOTE: If AFIS equipped the first page displayed after system initialization will be the **AFIS FPL LIST** page in lieu of the **FLIGHT PLAN LIST** page.

NOTE: If the data base contains company routes, the first page displayed after system initialization will be the **COMPANY ROUTES** page in lieu of the **FLIGHT PLAN LIST** page. If both AFIS and Company Routes are present, the **COMPANY ROUTES** page is displayed first.

## **FLIGHT PLAN LIST 1/1 (Page 1 of 1)**

If the initialization airport matches a departure airport on the **FLIGHT PLAN LIST**, the cursor will automatically be positioned over the first matching Flight Plan.

There are seven pages possible with a maximum of 56 flight plans stored in nonvolatile memory. Each stored flight plan's origin and destination points are listed in alphabetical order. (Figure 2-3)

A new **FLIGHT PLAN LIST** Page is created when the previous page has eight flight plan origin-destination pairs

Figure 2-3

on it. Using the **PRV** or **NXT** Key pages through the Flight Plan List subsection. (Figure 2-3)

## **FLIGHT PLAN "X" 1/1 (Page 1 of 1)**

"X" can be Flight Plan numbers 1 through 56. (Figure 2-4)

This stored flight plan page is accessed through the **FLIGHT PLAN LIST** Page by pressing the Line Select Key corresponding to the desired flight plan number, thus, placing the cursor over that number, then pressing **ENTER.** (Figure 2-3)

Figure 2-4

## **Waypoint Identifiers:**

Waypoint identifiers may consist of from one to six alphanumeric characters. Up to 50 waypoint identifiers may be placed on each stored Flight Plan. An identifier may be used more than once on the same Flight Plan. (Figure 2-4) Other indications can be as follows:

• Indented Waypoints: Indicates a SID, STAR, or APPROACH procedure is part of the Flight Plan. (Figure 2-4)

- **HP** (Holding Pattern): Indicates a holding pattern is programmed at a particular waypoint. (Figure 2-5)
- **PT** (Procedure Turn): Indicates a procedure turn is programmed at a particular waypoint.
- **++++++:** A flight plan discontinuity "fence" separating the missed approach way-

Figure 2-5

point from the rest of the approach (Figure 2-5). The system will fly current track beyond the last waypoint prior to the fence but no Auto Leg change will occur. No Altitude constraints will be displayed beyond the fence. This type of fence will not cause waypoints of the active flight plan to be deleted prior to the fence if a waypoint beyond the fence is selected using the d function.

- **IAF** (Initial Approach Fix): Automatically loaded from the data base when a non-precision approach is selected.
- **ARC** (DME Arc end waypoint): Automatically loaded from the data base when a non-precision approach is selected.
- **FAF** (Final Approach Fix): Automatically loaded from the data base when a non-precision approach is selected.
- **MAP** (Missed Approach Point): Automatically loaded from the data base when a non-precision approach is selected.
- **------:** "fence" indicating a discontinuity in the flight plan. No Auto Leg changes will take place beyond the last waypoint prior to the frence and no **ALT, ETE, ETA,** or **DIS** will be displayed. If a d is performed to a waypoint beyond this type of fence all waypoints prior to the fence will be deleted from the active flight plan.
- **\*\*\*\*\*\*** : Follows the last waypoint on the Flight Plan and indicates where the next waypoint entry will normally begin.

## **DEPART:**

Used to access the **DEPARTURE** Page to enter a Standard Instrument Departure (SID). (Figure 2-5)

## **ARRIVE:**

Used to access the **Arrival** Page to enter a Standard Terminal Arrival (STAR) or Profile Descent. (Figure 2-5)

## **APPROACH:**

Used to access the **APPROACH** Page to enter a non-precision approach. (Figure 2-5)

**XFILL:** Used to transfer information between systems in a dual system installation. In a single system installation, this prompt will not be displayed.

## **SELECT** or **INVERT:**

Used to transfer a Stored Flight Plan to the **ACTIVE FLIGHT PLAN** Page. Depressing the **BACK** Key when the cursor is over this field brings up **INVERT?**, which is used to transfer the waypoints of a Stored Flight Plan to the **ACTIVE FLIGHT PLAN** Page in reverse order. (Figure 2-5)

## **ERASE:**

Used to clear an entire flight plan. (Figure 2-5)

## **DEPARTURE Page**

Accessed by pressing the Line Select Key adjacent to **DEPART** on the **FLIGHT PLAN** Page. With the cursor over **DEPART** press **ENTER.**

NOTE: Each field will prefill if there is only one choice for that particular field or **DEPARTURE** airport field will flash if no Departure is available. A **NO SIDS AVAILABLE** message will appear at the bottom of the screen.

## **DEPARTURE:**

Departure airport identifier. This field prefills if first waypoint on the flight plan is an airport or runway, or it can be manually entered. (Figure 2-6)

## **RUNWAY:**

Departing runway. This field prefills if first waypoint on the flight plan is a runway, or it can be selected from a list made available by pressing the Line Select Key adjacent to the **RUNWAY** field. (Figure 2-6)

Figure 2-6

## **SID:**

The Standard Instrument Departure (SID) can be selected from a list made available by pressing the Line Select Key adjacent to the **SID** field.

## **TRANSITION:**

The Transition waypoint can be selected from a list made available by pressing the Line Select Key adjacent to the **TRANSITION** field.

## **WAYPOINTS OF SID:**

The waypoints that constitute the SID**.** (Figure 2-7)

## **SELECT?:**

Used to select the defined SID. (Figure 2-7)

## **ERASE:**

Used to erase a SID. (Figure 2-7)

Figure 2-7

## **ARRIVAL Page**

Accessed by pressing the Line Select Key adjacent to **ARRIVE** on the **FLIGHT PLAN** Page. With the cursor over **ARRIVE** press **ENTER.**

NOTE: Each field will prefill if there is only one choice for that particular field or **ARRIVAL** field will flash if no Arrival is available, and a **NO STARS AVAILABLE** message will appear at the bottom of the screen.

## **ARRIVAL:**

Arrival airport identifier. This field prefills if the last waypoint on the

flight plan is an airport or runway, or can be manually entered. (Figure 2-8)

## **RUNWAY:**

Arriving runway. This field prefills if the last waypoint on the flight plan is a runway, or can be selected from a list made available by pressing the Line Select Key adjacent to the **RUNWAY** field. (Figure 2-8)

Figure 2-8

## **TRANSITION:**

The Transition waypoint may be prefilled or selected from a list made available by pressing the Line Select Key adjacent to the **TRANSI-TION** field.

## **STAR:**

The Standard Terminal Arrival (STAR) can be selected from a list made available by pressing the Line Select Key adjacent to the **STAR** field.

## **WAYPOINTS OF STAR:**

The waypoints that constitute the STAR. (Figure 2-9)

## **SELECT?:**

Used to select the defined STAR. (Figure 2-9)

## **ERASE:**

Used to erase a STAR. (Figure 2-9 )

Figure 2-9

## **APPROACH Page**

Accessed by pressing the Line Select Key adjacent to **APPROACH** on the **FLIGHT PLAN** Page. With the cursor over **APPROACH** press **ENTER.**

NOTE: Each field will prefill if there is only one choice for that particular field or Approach Airport field will flash if no Approach is available and a **NO APPROACH AVAILABLE** message will appear at the bottom of the screen.

## **APCH:**

Approach airport identifier. This field prefills if last waypoint on the flight plan is an airport or runway, or can be manually entered. (Figure 2- 10)

Figure 2-10

## **RUNWAY:**

Approach runway prefills if only one runway is available, last waypoint on Flight Plan is a runway, or can be selected from a list made available by pressing the Line Select Key adjacent to the **RUN-WAY** field. (Figure 2-11)

**TYPE** (Circle, VOR, NDB, or RNAV):

Figure 2-11

Type may be prefilled or selected from a list made available by pressing the Line Select Key adjacent to the **TYPE** field.

NOTE: If the runway selected on the Approach Page differs from the runway dictated by the STAR, **"SEL RWY FROM STAR PG"** is displayed at the bottom of the screen.

## **TRANSITION:**

The Transition waypoint may be prefilled or selected from a list made available by pressing the Line Select Key adjacent to the **TRANSI-TION** field. (Figure 2-10)

## **WAYPOINTS OF APPROACH:**

The waypoints that constitute the **APPROACH.** (Figure 2-11)

- **HP** (Holding Pattern): Indicates a holding pattern is programmed at a particular waypoint. (Figure 2-11)
- **PT** (Procedure Turn): Indicates a Procedure Turn is programmed at a particular waypoint.
- **ARC** (DME ARC): Indicates a DME ARC is programmed at a particular waypoint.
- **IAF:** Indicates the Initial Approach Fix.
- **FAF:** Indicates the Final Approach Fix.
- **MAP:** Indicates the Missed Approach Fix.

## **• FCF :**

Indicates Final Approach Course Alignment Fix.

## **• ++++++:**

Separates the missed approach procedure waypoint from the rest of the approach. When the approach is flown, the system will continue to provide guidance along the final approach course and beyond the **MAP** until the pilot manually sequences to the missed approach waypoint by using a **DIRECT TO** or **HEADING** mode procedure. (Figure 2-11) No Auto Leg changes will occur beyond the last waypoint prior to the fence. This type of fence will not cause waypoints of the active flight plan to be deleted prior to the fence if a waypoint beyond the fence is selected using the d function.

## **SELECT?**:

Used to select the defined **APPROACH**. (Figure 2-11)

## **ERASE:**

Used to erase an **APPROACH.** (Figure 2-11)

## **AIRWAY Page**

Enroute Airways may be manually entered on a Flight Plan Page by preceding the route or airway ident with a pound sign **(#),** e.g., **#J** (Jet Airway), **#V** (VOR Airway), **#UG** (Upper Green) or **#R** (Red Airway). The preceding waypoint on the Flight Plan must be part of the Airway being entered in order for the Airway to be accepted. This waypoint will normally be the From waypoint on the AIRWAY Waypoint Page.

## **AIRWAY:**

Airway identifier. (Figure 2-12)

## **FR:**

Starting point on airway. (Figure 2-12)

## **TO:**

Ending point on airway as selected by the operator. (Figure 2-12)

Figure 2-12

## **SELECT ENDING WPT:**

Select the desired ending waypoint on the airway, by moving the cursor up or down and depress **ENTER.** (Figure 2-12)

## **ACTIVE FPL (Flight Plan)Page**

## **FR:**

Current FROM waypoint. May also display **DIRECT, PSEUDO VORTAC, DME ARC,** or **PROCEDURE TURN.** (Figure 2-13)

## **TO:**

Current **TO** waypoint. (Figure 2-13)

Figure 2-13

Waypoint Identifiers:Up to **100** waypoint identifiers may be placed on the Active Flight Plan Pages. An identifier may be used more than once on the same Flight Plan.

- Indented Waypoints: indicate a **SID, STAR,** or **APPROACH** Procedure is part of the Flight Plan. (Figure 2-13, **DFW**)
- **HP** (Holding Pattern): indicates a holding pattern is programmed at a particular waypoint. (Figure 2-14)
- **PT** (Procedure Turn): indicates a procedure turn is programmed at a particular waypoint.

Figure 2-14

A "fence" separating the current FR/TO leg from the originally selected Active Flight Plan when the TO waypoint is not on the original Flight Plan. Also separates non-continuous Flight Plan segments. (Figure 2-13) No Auto Leg change will occur to waypoints that appear after the fence. This type of fence will not cause waypoints of the active flight plan to be deleted prior to the fence if a waypoint beyond the fence is selected using the d function.

NOTE: When a "fence**" (++++++)** appears in an Approach it separates the missed approach holding fix from the rest of the approach. (Figure 2- 14) No Auto Leg change will occur to waypoints beyond the fence.

\*\*\*\*\*\*:

**------:**

Same as stored Flight Plan Page.

## **DEPART:**

Same as stored Flight Plan Page.

## **ARRIVE:**

Same as stored Flight Plan Page.

## **APPROACH:**

Same as stored Flight Plan Page.

## **ETA: (ETE/DIS/ALT)**

Estimated Time of Arrival at each waypoint on the Active Flight Plan based on current groundspeed. (Figure 2-15)

NOTE: When the cursor is placed over the **ETA** field and the **BACK** Key is pressed, **ETE, DIS,** or **ALT** can be displayed. Press **ENTER** to select the desired option. No **ETE, ETA, ALT** or **DIS** infor-

Figure 2-15

mation is displayed for waypoints beyond the missed approach "fence" (++++++) or the flight plan discontinuity (------).

## **ETE:**

Estimated Time Enroute between waypoints on the Active Flight Plan based on current groundspeed.

## **DIS:**

Distance between each waypoint on the Active Flight Plan.

## **ALT:**

Constraint altitude and waypoint offset of programmed VNAV waypoints for applicable waypoints on the Active Flight Plan (Figure 2-16).

Figure 2-16

NOTE: No database altitude constraints will be displayed at the **MAP** if the **MAP** is abeam or beyond the runway threshold . No altitude constraints are displayed on an approach if a **PT** is part of the approach procedure.

The following may appear in the waypoint altitude field:

**• FL:** Flight Level **• A:** at or above

**• B:** at or below

**• G:** glide path (programmed Flight Path Angle)

NOTE: If an approach is programmed at the destination airport, and the MAP is the end of the runway, the altitude value displayed next to the MAP is approximately 50 feet above the runway threshold elevation. If the MAP is prior to the end of the runway and the approach is straight-in, the altitude displayed at the MAP is computed based on a line drawn from the FAF through the MAP to a point 50 feet above the runway threshold. The altitude may not be the MDA (Figure 2- 16). If no approach is programmed, the altitude value will be the airport elevation regardless of runway selection. The MAP altitude is shown in yellow.

The Waypoint VNAV offset is given in nautical miles where a negative (-)offset is prior to the waypoint (Figure 2-16, interpreted as "cross ten miles before **RYMES** at **3000** feet") and a positive offset is after the waypoint. If dashes appear in the altitude constraint field, NO altitude is programmed at that waypoint.

## **ERASE:**

Same as for Stored Flight Plans except the current FROM/TO leg cannot be erased. The Active Flight Plan is automatically erased upon system shut-down.

## **NAVIGATION SECTION (NAV KEY)**

Upon pressing the **NAV** Key the **NAVIGATION 1/4** Page will be displayed and the following can be observed.

## **NAVIGATION PAGES**

NOTE: If AFIS is installed in the system, the **NAV** section will consist of five pages.

## **NAVIGATION 1/4 (Page 1 of 4)**

## **FR**:

The FROM waypoint identifier is displayed on the left. If the system has a valid ground speed, the time of departure or time overhead at that waypoint displayed on the right. This line can also display **DIRECT, HOLD, PROCE-DURE TURN, DME ARC** or **PSEUDO VORTAC.** (Figure 2-17)

Figure 2-17

## **TO:**

The **TO** waypoint identifier is displayed on the left. If the system has a valid ground speed, the ETA at that waypoint is displayed on the right. The **TO** field may also display **AR, HP** or **PT** if the waypoint indicates a DME ARC, Holding Pattern or Procedure Turn. The ETA field can be changed to display constraint altitude and waypoint offset distance if an altitude constraint has been programmed at the current **TO** waypoint by placing the cursor over this field and dressing the **BACK** Key (Figure 2-17) See Section 3 for the procedure.

## **NX:**

This line is normally blank (Figure 2-18) except during Waypoint Alert (30 seconds prior to crossing the **TO** waypoint). In this case the next (**NX**) waypoint identifier on the Active FlightPlan and the ETA at that waypoint is displayed (Figure 2-19). When a Procedure Turn, Holding Pattern, Heading, or Heading Intercept mode is in use, appropriate information pertaining to that mode will be displayed in this field.

#### DIS:

The distance in nautical miles and tenths from the aircraft present position to the **TO** waypoint. During Waypoint Alert, the distance in whole nautical miles to the **NX** waypoint on the Active Flight Plan is displayed in parentheses. (Figure 2-18)

Figure 2-18

#### ETE:

The estimated time enroute in hours, minutes and tenths, from the aircraft present position to the **TO** waypoint based on current ground-speed. (Figure 2-18)

#### DTK:

The desired track is the Great Circle course in whole degrees between the FROM and TO waypoints. When in the **PSEUDO VORTAC** mode, the **DTK** is entered by the operator. During the Waypoint Alert, desired track to the next (**NX**) waypoint on the Active Flight Plan is displayed in parentheses. (Figure 2-18)

NOTE: The **DTK** field will be dashes if the FROM waypoint or present position are north of N 70° or south of S 60° Latitude, unless a manual MAG VAR is entered or a discrete MAG/True switch is moved to the True position.

#### GS:

The current groundspeed. (Figure 2-19)

#### WIND.

The current wind direction referenced to True North and speed in knots. (Figure 2-19)

Figure 2-19

#### **XFILL:**

If the aircraft is configured for dual systems, the **XFILL** prompt will appear on line 10 indicating the systems contain dissimilar data.

NOTE: **XFILL** will not appear when DME ARC, ARC Intercept, Procedure Turn or Holding Pattern are in progress on the system performing the procedure.

#### AUTO:

The leg change mode. **AUTO** or **MAN**, may be selected if the cursor is over this field using the **BACK** Key. (Figure 2-19) If **Auto** is selected the system will sequence to the next leg on the FPL. If **MAN** is selected the system will not sequence to the next leg on the FPL and fly the current track.

**NAVIGATION 1/4** with a Holding Pattern, Procedure Turn, Heading, or Heading Intercept Programmed.

#### HOLD:

Indicates that a Holding Procedure has been initiated and is displayed 30 seconds prior to crossing the HP waypoint. (Figure 2-20)

#### • RIGHT or LEFT:

Indicates the programmed turn direction around the holding pattern as entered on the **HOLD** Page. (Figure 2-20)

Figure 2-20

#### MANUAL or AUTO:

Indicates the programmed exit mode as entered on the Hold Page. Selecting **MANUAL** initiates a continuous hold at the fix until some action is taken by the pilot to exit the hold. Selecting **AUTO** will cause the aircraft to **EXIT HOLD** the next time the aircraft passes over the fix (Figure 2-21). If **AUTO** is programmed during the hold procedure, the aircraft will sequence to the next waypoint on the Active Flight Plan the next time the hold fix is crossed. This field can be edited using the **BACK** Key when the cursor is over this field. (Figure 2-20)

#### AT:

The Holding Pattern procedure is in progress at the **TO** waypoint and the ETA next time over the holding fix if ETA has been selected and the system has a valid ground speed. This field can also display the following: (Figure 2-20)

## **• HP** (Holding Pattern):

Indicates a holding pattern is programmed at the **TO** waypoint.

## **• PT** (Procedure Turn):

Indicates a procedure turn is programmed from the database at the **TO** waypoint. The airplane will fly the procedure turn. The next time over the **PT** waypoint, the system will sequence to the following waypoint on the flight plan.

## **• AR** (DME Arc)

Indicates a DME Arc is programmed at the **TO** waypoint.

## **HOLDING STATUS MESSAGE: (Line 4)**

## **• DIRECT ENTRY:**

Indicates the system will use a direct entry to the holding pattern. (This message appears 30 seconds prior to entering the holding procedure and changes to **HOLDING** after crossing the fix.) (Figure 2- 20)

## **• TEARDROP ENTRY:**

Indicates the system will use a teardrop entry to the holding pattern. (This message appears 30 seconds prior to entering the hold procedure and changes to **HOLDING** after crossing the fix the second time.)

## **• PARALLEL ENTRY:**

Indicates the system will use a parallel entry to the holding pattern. (This message appears 30 seconds prior to entering the hold procedure and changes to **HOLDING** after crossing the fix the second time.)

## **• HOLDING:**

Normal status while holding.

## **• EXIT HOLD:**

Indicates the system will exit the holding pattern the next time over the holding fix. The **ETE** to the holding fix is also displayed.

## **DIS:**

The direct distance in nautical miles and tenths from the aircraft present position to the holding fix. (Figure 2-21)

## **ETE:**

The estimated time enroute to the next time over holding fix based on the path around the Hold "racetrack". (Figure 2-21)

Figure 2-21

## **INBOUND CRS** (course):

The inbound holding course in whole degrees. (Figure 2-21)

## **GS:**

The current groundspeed. (Figure 2-21)

## **WIND:**

The current wind direction referenced to True North and speed in knots. (Figure 2-21)

NOTE: The leg change mode (**AUTO** or **MAN** normally displayed on the last line of **NAVIGATION** Page 1) is not displayed while holding.

## **NAVIGATION 2/4 (Page 2 of 4)**

Pressing the **NAV** Key again will display the second **NAVIGATION** Page and the following can be observed.

## **FR/DIRECT/HOLD/PROCEDURE TURN/DME ARC:**

Same as discussed for **NAVIGATION 1/4.**

## **TO/AT/AR/HP/PT:**

Same as discussed for **NAVIGATION 1/4.**

## **NX**/Holding Status:

Same as discussed for **NAVIGATION 1/4.**

## **WIND:**

The first field displays headwind/tailwind in knots with an up arrow (↑) for tailwind or a down arrow (↓) for headwind. The second field displays the crosswind component in knots with a right pointing arrow (→) for a left crosswind or a left pointing arrow (← ) for a right crosswind. (Figure 2-22)

Figure 2-22

## **ETA:**

Estimated Time of Arrival at the last waypoint on the Active Flight Plan prior to a "fence" (- - - - - or ++++++ ). A "fence" is a discontinuity in the flight plan. No data is computed beyond the fence and there is no Auto Leg change across the fence. (Figure 2-22)

## **FUEL:**

Estimated fuel remaining at destination. (Figure 2-22)

## **TKE:**

The Track Angle Error as defined as the difference between the desired track and the actual track in degrees. **R** (right) and **L** (left) are displayed to show the direction of error in relation to the desired track.

## **XTK:**

The crosstrack distance is the lateral displacement of the aircraft in nautical miles and tenths left or right of the desired track (125 NM maximum). **TRMNL, APRCH** or **ENRTE** is displayed to indicate the current CDI sensitivity. A parenthesis around any of these indicates the displayed sensitivity has been selected manually. See Section 3 for operating procedures (Figure 2-22). Scaling for the **TRMNL, APPR,** and **ENRTE** CDI sensitivity is as follows:

> Enroute: 5NM full scale deflection. Terminal: 1NM full scale deflection. Approach: 0.3NM full scale deflection.

## **SXTK:**

The selected crosstrack distance entered by the pilot to provide steering to an offset course parallel to the desired track (99.9 NM maximum). (Figure 2-22)

## **NAVIGATION 3/4 (Page 3 of 4)**

Pressing the **NAV** Key again will display the third **NAVIGATION** Page and the following can be observed.

## **FR/DIRECT/HOLD/PROCEDURE TURN/DME ARC:**

Same as **NAVIGATION 1/4.**

## **TO/AT/AR/HP/PT:**

Same as **NAVIGATION 1/4.**

**NX/**Holding Status:

Same as **NAVIGATION 1/4.**

## **DRIFT:**

The drift angle, in whole degrees, left or right of aircraft heading compared to current track. (Figure 2-23)

## **VAR**:

The magnetic variation value in whole degrees computed automatically between N70 00.0 and S 60 00.0 latitude. Manual variation can be

Figure 2-23

entered and overrides the automatic computation. Manual entry of variation is required north of N70:00.0 and south of S60:00.0 latitude. **(MAN)** will be displayed in the **VAR** field after a manual entry is made. See Section 3 for procedures. (Figure 2-23)

## **TAS:**

The aircraft true airspeed in knots received from the Air Data Computer. If **TAS** is manually inserted, **MAN** will be displayed. (Figure 2-23)

NOTE: The maximum enterable manual **TAS** is 850 knots. The **TAS** field is enterable only if airdata is invalid.

## **HDG:**

The heading input received from an IRS or the aircraft compass system. If **HDG** can be manually inserted, **MAN** will be displayed. (Figure 2-23)

## **BRG**:

The bearing in whole degrees from the aircraft present position to the TO waypoint. (Figure 2-23)

## **TK:**

The track angle in whole degrees. (Figure 2-23)

## **NAVIGATION 4/4 (Page 4 of 4)**

Pressing the **NAV** Key again will display the fourth **NAVIGATION** Page and the following can be observed.

## **IDENT:**

A waypoint identifier of a fix to be overflown can be entered here to update the system position. (Figure 2-24)

## **POS:**

The current composite position (latitude and longitude) computed in degrees, minutes, and hundredths of minutes. (Figure 2-24)

Figure 2-24

## **IRS/INS, VPU,** and **GPS:**

A listing of all interfaced sensors. The radial difference between the individual sensor position and the composite position is displayed in nautical miles and tenths. Sensors not being used in the composite position solution will display the radial difference in yellow. Sensors being used will display the radial difference in green. The internal GPS sensor will normally be the sole contributing sensor to the composite position as long as RAIM is available. (Figure 2-24)

NOTE: IRS radial error is always green because velocity values are used to aid GPS position.

## **IRS/INS SUBSECTION PAGES**

## **IRS (or INS) SUBSECTION 1/2 (Page 1 of 2)**

## **POS:**

The position in this field is the same as **POS** on **NAVI-GATION 4/4.** (Figure 2-29)

## **IRS/INS:**

The actual position computed by the specified sensor when in NAV mode. (Figure 2-29)

Figure 2-29

## **DIF:**

The difference between the composite position and the sensor computed position in degrees, minutes, and hundredths. (Figure 2-29)

## **IRS SUBSECTION 2/2 (Page 2 of 2)**

## **TIME TO NAV:**

The time remaining until alignment is complete. (Figure 2-30)

## **CURRENT MODE:**

This field annunciates the current mode of the IRS. The messages that can appear are **ATTITUDE, ALIGN,** or **NAV.** (Figure 2-30)

NOTE: Page 2 is only displayed with an IRS.

Figure 2-30

## **VPU SUBSECTION PAGES**

Accessed through the **NAVIGATION 4/4** Page (if AFIS is installed in the system, access is through the **NAVIGATION 4/5** Page) by pressing the Line Select Key corresponding to the VPU sensor, then pressing **ENTER**.

## **VPU SUBSECTION 1/4 (Page 1 of 4)**

## **POS:**

The position in this field is the same as **POS** on **NAVI-GATION 4/4.** (Figure 2-31)

## **VPU:**

The actual position computed by the sensor, when in the NAV mode. (Figure 2-31)

**DIF:** Figure 2-31

The difference between the composite position and the sensor computed position in degrees, minutes and hundredths. (Figure 2-31)

## **VPU SUBSECTION 2/4 (Page 2 of 4)**

Pressing the **NXT** Key again will display the second **VPU SUBSEC-TION** Page and the following can be observed.

## **QUALITY:**

The numerical display in this field indicates the reliability of the position data from the VPU. The number will range from 2 to 99 (with 2 being optimum and 99 as dead reckoning). (Figure 2-32)

## **ADVISE IF>:**

This field is an enterable field in which the operator may input a quality factor value from 2 to 98. If the VPU **QUALITY** exceeds this value a message is displayed on **SENSOR MESSAGES** Page. (Figure 2-32)

Figure 2-32

NOTE: Entering 99 in this field will eliminate any previously entered value and no **CHECK QUALITY** message will appear.

**CURRENT MODE:** Indicates the current mode of VPU navigation. The messages that can appear under it: (Figure 2-32)

- **NO MEASUREMENTS** indicates that VPU is not receiving valid data for navigation.
- **VOR/DME** indicates that distance and bearing (rho/theta) information is used to generate VPU position.
- **DME/DME** indicates distance (rho/rho) data is received and used to generate VPU position.
- **BAD GEOMETRY** indicates that station geometry is inadequate for navigation.

## **NAV 1 - CONFLICT** or **NAV 2 - CONFLICT:**

The VPU is not using a manually or keyboard tuned station because of a possible station frequency conflict within the aircraft's current line-of-sight. (Figure 2-32)

## **VPU SUBSECTION 3/4 (Page 3 of 4)**

Pressing the **NXT** Key again will display the third **VPU SUBSECTION** Page and the following can be observed.

## **VPU Sensor With Single Channel DME Inputs (Figure 2-33)**

## **NAV 1 and NAV 2:**

The station identifier and frequency being used for navigation.

## **RNG:**

The range in nautical miles and tenths from aircraft present position to the DME station.

Figure 2-33

**BRG:**

Bearing in whole degrees from aircraft present position to the VOR.

## **VPU with Multiple Channel DME Inputs (Figure 2-34)**

## **NAV 1:**

The stations received by the NAV 1 VOR/DME receivers. The station identifier is shown adjacent to the field with the ACTIVE frequency.

## **RNG:**

Same as above.

## **BRG:**

Same as above.

Figure 2-34

## **CH 2:**

The station identifier and frequency for an additional station that the multiple channel DME is receiving. This frequency may or may not be displayed on the control head.

## **RNG:**

The range in nautical miles and tenths from the aircraft's present position to the Channel 2 DME station.

## **CH 3:**

The station identifier and frequency for the third station that is being received. This frequency is not displayed on the control head, and is automatically tuned by the system.

## **RNG:**

Same as for CH 2.

NOTE: When the DM441B DME, dedicated DM441B, or dedicated DME42 is configured, the **VPU SUBSECTION 3/4** page is different. The bearing information is suppressed and DME is annunciated instead of NAV.

## **VPU SUBSECTION 4/4 (Page 4 of 4)**

Pressing the **NXT** Key again will display the fourth VPU SUBSEC-TION Page and the following can be observed. If the VPU has multiple channel DME inputs **VPU SUBSECTION 4/4** appears and displays NAV 2 data. The page appears the same as **VPU SUBSEC-TION 3/4.**

## **GPS SUBSECTION PAGES**

The GNS-XLS has an internal GPS receiver that is the main navigation sensor of the system. External GPS sensors are optional.

Accessed through the **NAVIGATION 4/4** Page (if AFIS is installed in the system, access is through the **NAVIGATION 4/5** Page) by pressing the Line Select Key corresponding to the GPS sensor, then pressing **ENTER.**

## **GPS SUBSECTION 1/3 (Page 1 of 3)**

See Figure 2-35.

## **POS:**

The current composite position (latitude and longitude) computed in degrees, minutes, and hundredths of minutes.

## **GPS:**

The current GPS position.

Figure 2-35

This information is only displayed when GPS is in the NAV mode.

## **DIF:**

The difference between the composite position and sensor computed position in degrees, minutes and hundredths.

## **GPS SUBSECTION 2/3 (Page 2 of 3)**

Pressing the **NEXT** Key will display the second **GPS SUBSECTION** Page and the following can be observed. See Figure 2-36.

NOTE: All references to FDE prediction do not apply to 17960-0101 units. FDE prediction is only available in 17960-0102, 17960-0203 and 17960-0204 units.

## **HPE:**

Horizontal Position Error displayed in nautical miles as a measure of GPS accuracy.

Figure 2-36

## **POS UNCERT:**

Estimated Position Uncertainty, in nautical miles, when GPS is in navigation mode.

## **GPS TIME:**

GPS Time in hours, minutes and seconds. The advisory time is displayed when at least one satellite is being tracked, other-wise the time field displays dashes.

NOTE: GPS TIME may vary several seconds from GMT due to leap second input of UTC.

**STATE:** The GPS receiver state can be one of the following:

Dashes: Idle or no mode data.

**INITIALIZE:** The receiver is updated with initial position and time

information.

**SKY SEARCH:** No almanac is available. The system searches for

any satellite in the visible table based on the internal or external time, data, and position and then assigns

channels in order received.

**ACQUISITION:** Constellation selection and channel assignments are

being done. Carrier and code lock are in progress.

**TRANSITION**: The receiver is transitioning from one state, such as

**ACQUISITION,** to another state, such as **NAVIGA-**

**TION.**

**NAVIGATION:** The GPS receiver is in navigation mode and has at

least a two dimensional position fix.

**DR:** The system is in dead reckon mode. When the posi-

tion is valid and sufficient satellite measurements are unavailable, the receiver will continue to output valid position for a maximum of 30 seconds while using the last known velocity and track information. The

position is invalid after 30 seconds.

## **MODE:**

Possible receiver modes are **ENROUTE, OCEANIC/REMOTE**, **TER-MINAL,** and **APPROACH.** These modes are used to determine what accuracy parameters should be used for a particular phase of flight.

## **ALT AIDED?:**

Indicates the GPS receiver is using an externally supplied altitude input for position calculation.

## **RAIM/FDE?:**

Indicates **RAIM** and/or **FDE** is **AVAIL**able or **UNAVAIL**able.

## **SATS TRACKED:**

Indicates the number satellites presently being tracked.

## **GPS SUBSECTION 3/3 (Page 3 of 3)**

Pressing the **NXT** Key again will display the third **GPS SUBSECTION** Page and the following can be observed.

This page displays the GPS receiver status. The GPS receiver is an 8 channel receiver, therefore, up to 8 lines of satellite information is displayed. The information displayed is as follows: (Figure 2-37)

Figure 2-37

## **GPS SAT:**

This is the satellite (PRN) number.

## **AZ:**

This is the satellite azimuth position displayed in degrees.

## **EL:**

Satellite elevation displayed in degrees above the horizon.

## **SNR:**

This the received signal-to-noise ratio for each satellite.

## **HLTH:**

Satellite health is displayed as **BAD** or **GOOD.**

## **T:**

**YES** or **NO** displayed as to whether this satellite is presently being tracked.

## **EXTERNAL GPS SENSOR SUBSECTION PAGES**

Optional external GPS sensors may also be connected to the GNS-XLS. The external sensors do not provide RAIM functions and the external sensor may not be used as the primary navigation source for GPS/GPS Overlay approaches per TSO C129.

The external GPS sensor will be displayed as **GPS1** on **NAV PAGE 4/4**. If two external GPS sensors are installed, the second will be displayed as **GPS2**. The internal GPS receiver is displayed as **GPS**.

## **GPS1 SUBSECTION 1/2 (Page 1 of 2)**

See Figure 2-37a.

## **POS:**

The current composite position (latitude and longitude) computed in degrees, minutes, and hundredths of minutes.

# POS N 34 38.83 GPS1 N 34 38.82 W112 25.10 GPS1 SUBSECTION 1/2

Figure 2-37a

## **GPS1:**

The current GPS1 position. This information is only displayed when GPS1 is in the NAV mode.

## **DIF:**

The difference between the composite position and sensor computed position in degrees, minutes and hundredths.

## **GPS SUBSECTION 2/2 (Page 2 of 2)**

Pressing the **NEXT** Key will display the second **GPS1 SUBSECTION** Page and the following can be observed. See Figure 2-37b.

The following information is displayed for the external GPS:

Figure 2-37b

## **GPS HDOP:**

The GPS Horizontal Dilution of Precision. HDOP is a statistical measure of GPS navigation quality. The lower the HDOP, the greater the precision.

## **GPS HFOM:**

Estimated horizontal GPS position accuracy, in nm, with 95% probability.

## **GPS TIME:**

GPS Time in hours, minutes and seconds.

## **SATS TRACKED:**

The number of satellites presently tracked.

## **MODE:**

The mode of the GPS receiver. Possible modes are:

**SELF TEST** Receiver is in self test.

**INITIALIZATION** Receiver initializing position information.

**ACQUISITION** Receiver acquiring satellite information.

**NAVIGATION** Receiver in normal navigation mode.

**ALTITUDE/CLOCK AIDED** Receiver using altitude for

navigation.

**DIFFERENTIAL**Receiver applying differential corrections.

**AIDED** Receiver using other navigation information besides

satellite.

**FAULT** Receiver has detected a fault and is unusable.

**LINK FAIL** No communications between the FMS and external

GPS

## **VERTICAL NAVIGATION SECTION (VNAV KEY)**

Upon pressing the **VNAV** Key the **VNAV 1/3** Page will be displayed and the following can be observed.

## **VNAV PAGES**

NOTE: AFIS flight plans do not support any altitudes, including airport elevation. As a result no altitude constraints will be provided for SIDS, STARS or Approaches. If the airport, SIDs, STARS or Approaches are obtained from the database altitudes will be provided.

In some programmed approaches, the altitude associated with the MAP waypoint is computed from the FAF through the MAP waypoint to a point 50 feet above the runway threshold. MDA may be reached prior to the MAP waypoint. The MDA must be observed if the runway is not in sight.

## **VNAV 1/3 (Page 1 of 3)**

#### **VNAV MODE:**

Mode required to fly to the vertical TO waypoint and Baro Altitude in feet. Can display one of the following:

- **INVALID:** Indicates **VNAV** function is invalid. In order to be set valid the following must be met:
- 1. Air Data valid (baro altitude and altitude rate)
- 2. Valid lateral TO Waypoint
- 3. Valid vertical TO waypoint
- 4. NO SXTK programmed
- 5. Crosstrack **(XTK)** < 12.5NM
- **INACTIVE:** VNAV system is not activated because non-volatile memory was erased during software update or it was manually set inactive before shutdown. Using **BACK** Key with the cursor over the inactive field can display one of the following:

NOTE: When VNAV Mode is inactive, all external VNAV outputs are disabled, including VERT DEV, EFIS altitude constraints at waypoints and VNAV WPT ALERT annunciation.

- **CLIMB:** Indicates climb required to cruise altitude or to next altitude restriction. (Figure 2-38)
- **CRUISE:** Indicates holding altitude while enroute to Top of Descent **(#TOD)** point. (Figure 2-39)
- PATH DESCENT: Indicates descent via programmed Flight Path Angle. Vertical Deviation will be enabled on the Vertical Deviation needle and the VERT DEV field is active. The VERT DEV field will not be displayed if there is no vertical path programmed. (Figure 2-40)
- **DESCENT:** Indicates nonpath or Air Mass descent to altitude restriction.
- LEVEL: Indicates aircraft should fly level to next constraint

#### **TO** Waypoint:

Vertical **TO** waypoint with constraint altitude and applicable waypoint offset. Letters preceding or following the altitude constraint have the following meaning: **FL**=Flight Level, **A**= At or Above, **B**=At or Below, **G**=Glide Path, and a blank space=At constraint.

Figure 2-38

```
VNAV 1/3
CRUISE
TO #TOD
RANGE (NM)
ETE
W#TOD FPM DN
ACTUAL FPM UP
VERT DEV
DATA

VNAV 1/3
FL350
1214.4
800
1214.4

08:06.8
800

-----
```

Figure 2-39

```
VNAV 1/3
PATH DESCENT
TO ELD
-5
EST CROSSING
REQUIRED FPM DN
ACTUAL FPM DN
WERT DEV HIGH
DATA?

VNAV 1/3
FL345
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL250
FL2
```

Figure 2-40

One of the following system generated VNAV profile points may also appear as the **TO** waypoint:

• **#TOC:** Indicates the Top of Climb target altitude. This point becomes the Vertical TO Waypoint once the aircraft has passed the final climb constraint waypoint and is climbing. (Figure 2-40)

**• #TOD:** Indicates the Top of Descent target altitude where the aircraft should begin its descent in order to arrive at the Descent Reference Waypoint at the required altitude. (Figure 2-39)

NOTE: If no Descent Reference Waypoint with crossing altitude is programmed, the system will use the arrival airport elevation to fix the **#TOD** as long as an airport is the last waypoint on the Active FPL.

## **EST CROSSING:**

Altitude trajectory computed by the system to the Vertical **TO** waypoint based on current groundspeed and vertical speed (Figure 2-40). This field will display **RANGE (NM)** in miles and tenths when the Vertical **TO** Waypoint is a **#TOD** or **#TOC** profile point. (Figure 2-39)

## **ETE:**

The estimated time enroute in hours, minutes and tenths, from the aircraft present position to the Vertical **TO** Waypoint **#TOC** or **#TOD**. (Figure 2- 39)

## **REQUIRED FPM:**

Required vertical speed in feet per minute to make the altitude constraint based on current ground speed. **UP** indicates a positive vertical speed and **DN** indicates a negative vertical speed (Figure 2-40). This field will display **@#TOD FPM DN** when the Vertical **TO** Waypoint is the Top of Descent and indicate the descent target vertical speed. (Figure 2-39)

## **ACTUAL FPM:**

Actual vertical speed in feet per minute. **UP** indicates a positive vertical speed and **DN** indicates a negative vertical speed. (Figures 2-39 and 2- 40)

## **VERT DEV:**

Vertical deviation of aircraft from this descent path in feet. **HIGH** indicates aircraft is above the path (Figure 2-40); **LOW** indicates aircraft is below path. **CLIMB GRAD xxx/NM** is displayed during **CLIMB** mode to indicate current aircraft climb performance in feet per nautical mile. (Figure 2-38)

NOTE: **VERT DEV** data field is dashes if the **ETE** to descent path intercept is greater than one minute. This line will be blank if no FPA is programmed at descent reference waypoint. In this case **#TOD** will be determined using the default FPA from the **VNAV DATA** Page. However the FPA must still be entered for the system to provide a path.

#### DATA:

A prompt to access the **VNAV DATA** Page, by placing the cursor over the **DATA** field and pressing the **ENTER** Key. (Figure 2-40)

Figures 2-41 and 2-42 further illustrate the meanings of the fields on **VNAV** Page 1.

Progression of Vertical Waypoints from Climb to Path Decent on VNAV 1/1 Figure 2-41

Definition of Climb and Decent on VNAV 1/1 Figure 2-42

## VNAV 2/3 (Page 2 of 3) - FLIGHT PLAN WayPoint

Pressing the **VNAV** Key will display the second VNAV Page and the following can be observed.

VNAV MODE: Mode required to fly to the vertical TO waypoint and Baro Altitude in feet. Can display one of the following:

• INVALID: Same as on VNAV 1/1.

• INACTIVE: Same as on VNAV 1/1.

• CLIMB: Same as on VNAV 1/1.

• CRUISE: Same as on VNAV 1/1.

PATH DESCENT: Same as on VNAV 1/1.

• DESCENT: Same as on VNAV 1/1.

LEVEL: Same as on VNAV 1/1.

## **WAYPOINTS:**

Lateral and Vertical waypoints listed in order of occurrence with respect to the vertical profile, with constraint altitude and applicable waypoint offset, where **FL**=Flight Level, **A**= At or Above, **B**=At or Below, **G**=Glide Path, and a blank space=At constraint. (Figure 2-43)

One of the following system generated VNAV profile points may also appear:

- **#TOC:** Indicates the Top of Climb target altitude.
- **#TOD:** Indicates the Top of Descent target altitude. (Figure 2-44)

Figure 2-43

Figure 2-44

**• #PRESL:** Indicates the estimated position where the aircraft will arrive at the altitude shown on the Altitude Pre-Selector. Field does not appear unless the system is configured for an altitude preselector and the aircraft is flying toward this altitude. (Figure 2-44)

## ++++++ :

A discontinuity in the flight plan that separates the missed approach waypoint from the rest of the approach. (Figure 2-43) No Auto Leg change will occur beyond this point.

## **WAYPOINT IDENTIFIERS:**

May consist of from one to six alphanumeric characters. If more identifiers are present than can be listed on this page, subsequent pages will list the remaining waypoints. (Figure 2-45)

NOTE: Waypoints cannot be added to the active flight plan from the VNAV section. Enter new waypoints on **ACTIVE FLIGHT PLAN** Page.

Figure 2-45

## **ERASE:**

Used to erase all altitude constraints, except the altitude constraint at the current lateral **TO** Waypoint.

## **VNAV DATA 1/1 (Page 1 of 1)**

NOTE: This page is accessed by using the Line Select Key to place the cursor over the **DATA** prompt on **VNAV** Page 1/X and pressing **ENTER** Key.

## **CRUISE ALT:**

Manually entered cruise altitude in feet or Flight Level (FL). Any altitude entered greater than the transition level is converted and displayed as flight level (rounded off to the nearest hundred feet). An altitude less than 1000 feet must be entered with a preceding zero. (Figure 2-46)

NOTE: In a climb, when the aircraft is within 200ft of the Preselect Altitude, the **CRUISE ALT** changes to the same value as the **PRE-SEL ALT**.

The field also goes to dashes during a descent (digital systems only) when the aircraft is 200ft lower than the CRUISE ALT and the Preselect is set to a lower value. If the PRESEL is analog the altitude value will remain in the CRUISE ALT field. When the aircraft is within 200ft of the PRESEL ALT the CRUISE ALT changes again to the same value as the PRESEL ALT.

#### TRANS LEVEL:

Transition Level used to determine the altitude at which the system converts altitudes to Flight Levels. This field defaults to **FL180** if the pilot does not enter a value. (Figure 2-46)

#### **DEFAULT FPA:**

The FPA defaults to the 3.0 unless it is manually entered. The default descent Flight Path Angle can be manually

Figure 2-46

entered in degrees and tenths (0.1 to 6.0 range) (Figure 2-46). **DEFAULT FPA** is used to calculate **#TOD** to the first altitude constraint on the Active Flight Plan. However an FPA must be entered on the VNAV waypoint page to establish a **PATH DESCENT** and for Vert Dev or vertical deviations to be valid.

NOTE: Pilot enters numbers only, as the decimal point (.) prefills as a default.

#### PRESEL ALT:

If configured, Preselected Altitude input from system, in feet or Flight Level. (Figure 2-46)

NOTE: An analog type preselector only displays **PRESEL ALT** when the aircraft is within 1000ft of actual altitude.

## RANGE (NM):

If configured, Range to Pre-selected Altitude in nautical miles and tenths (0.0 to 999.9 range). (Figure 2-46)

#### ETE:

If configured, the estimated time enroute to the Pre-selected Altitude in hours, minutes and tenths. (Figure 2-46)

## **VNAV WAYPOINT 1/1 (Page 1 of 1)**

Accessed by placing the cursor over a lateral WPT and pressing the **VNAV** Key or by placing the cursor over a WPT in the VNAV section and pressing **ENTER** key.

## **WAYPOINT:**

VNAV waypoint will consist of from one to six alphanumeric characters.

## **ALT:**

Constraint altitude prefills from database or can be manually entered. Any altitude entered greater than the transition level (from the **VNAV DATA** Page) is converted and displayed as flight level rounded off to the nearest hundred feet. An altitude less than 1000 feet must be entered with a preceding zero. Altitudes below sea level are limited to -1000 feet. The following may appear in the altitude field:

- **FL:** Flight Level (Preceding the Altitude Value)
- **A:** At or Above (Following the Altitude Value)
- **B:** At or Below (Following the Altitude Value)
- **Blank space:** At (Following the Altitude Value)

NOTE: If the destination airport or runway is manually entered, or if the airport/runway is loaded from the database, the airport elevation will be displayed in the altitude field. If the flight plan is loaded through AFIS, the airport elevation will not be available.

## **EST CROSSING:**

Altitude trajectory computed by the system to the Vertical **TO** Waypoint based on current groundspeed and Vertical speed. (Figure 2-47) This field is displayed for the active vertical waypoint.

```
ALT 2000
EST CROSSING FL250
  VNAV WAYPOINT 1/1
```

Figure 2-47

## **PLAN CROSSING:**

System determined crossing based on programmed constraints and flight path angles for descent. (Figure 2-48) This field is displayed for other than the Active Vertical Waypoint and will be displayed in place of **EST crossing.**

Figure 2-48

## **OFFSET:**

Pilot entered value in nautical miles (-99 to +99 range) where a positive entry (+) indicates an offset beyond the waypoint and a negative (-) entry is prior to the waypoint.

NOTE: Pilot must enter the leading (+) sign for the offset to be beyond the fix, but a (-) prefills as a default to cross prior to the fix.

## **REQ FPM** (Required Feet Per Minute):

Required vertical speed in feet per minute the aircraft must maintain to reach the Vertical waypoint. **UP** indicates a positive vertical speed and **DN** indicates a negative vertical speed is required.

NOTE: If **PLAN CROSSING** is displayed, then the **REQ FPM** is the planned vertical speed for the waypoint. **REQ FPM** will be dashes if ground speed or air data is not valid.

## **FPA** (Flight Path Angle):

Flight Path Angle for path descent to waypoint in degrees and tenths with valid range 0.1 to 6.0. The following may appear in parentheses:

- **DB:** Indicates **FPA** from database.
- **MAN:** Indicates manually entered **FPA.**
- **DIR:** Indicates direct **FPA** programmed. (Figure 2-49)
- **AUTO:** Indicates system computed **FPA**.

Figure 2-49

**• DEF:** Indicates **FPA** default from **VNAV DATA** Page.

NOTE: **DIR, AUTO,** and **DEF** can be accessed using the **BACK** Key.

## **DIRECT FPA:**

Direct Flight Path Angle from the current aircraft altitude to the Vertical waypoint in degrees and tenths (valid range 0.0 to 90.0), where **DN** indicates negative **FPA** and **UP** indicates positive **FPA.**

## **AFIS SECTION (AFIS KEY)**

Refer to Section 7 for description and operation of AFIS.

## **PLANNING SECTION (PLAN KEY)**

Upon pressing the **Plan** Key the **PLAN 1/8** Page will be displayed and the following can be observed.

## **PLAN PAGES**

## **PLAN 1/8 (Page 1 of 8) FUEL STATUS**

## **FUEL STATUS LB:**

Indicates that fuel is being computed in pounds. This unit can be manually changed to **KG** if desired, using the **BACK** Key when the cursor is over the **LB** field. (Figure 2-50)

NOTE: the cursor must first be placed over the remaining field so the **LB** field can be activated.

Figure 2-50

## **REMAINING:**

The total fuel on board in pounds or kilograms. This quantity must be initially entered or verified by the pilot and may require periodic verification or update. (Figure 2-50)

## **RESERVE:**

The desired reserve, as entered or verified by the operator, displayed in pounds or kilograms. This may require periodic verification or update. (Figure 2-50)

## **FLOW:**

The current fuel flow in pounds or kilograms input automatically from fuel flow indicators. **(MAN)** indicates a pilot manual entry and the entry must be manually verified and periodically updated. (Figure 2-51)

NOTE: The above three quantities will flash after 15 minutes and will require veri-

Figure 2-51

fication by using the Line Select and **ENTER** Keys if **MAN** fuel flow was selected.

## **VERIFY INPUTS:**

Each of the flashing values must be verified or entered by pressing the **ENTER** Key when the cursor is over each field. This field is only displayed after the system is turned on and will be displayed in place of the **Last Input** field on line 6. (Figure 2-51)

## **LAST INPUT:**

The time in hours and minutes since the above three quantities were verified. This field only appears if fuel flow is input manually. (Figure 2-51)

NOTE: This field displays **VERIFY INPUTS** at system turn-on since **REMAINING** and **RESERVE** are stored in non-volatile memory during system shut-down.

## **HOURS:**

The hours and minutes of fuel remaining until the reserve fuel quantity is reached. (Figure 2-50) Fuel flow and ground speed must be valid.

## **RANGE:**

The nautical mile range available until the reserve fuel quantity is reached. (Figure 2-50) Fuel flow and ground speed must be valid.

## **NM/LB:**

The number of nautical miles for each pound (or kilogram) of fuel consumed. (Figure 2-50)Fuel flow and ground speed must be valid.

## **PLAN 2/8 (Page 2 of 8) TRIP PLAN**

Pressing the **PLAN** Key again will display the **PLAN 2/8** Page.

This page may be used to monitor the Active Flight Plan progress or a stored flight plan may be loaded on this page for planning purposes.

## **TRIP PLAN:**

The flight plan selected will be designated by an **"A"** for the Active Flight Plan, a number (1 to 56) for a stored flight plan, or - - - dashes if no active Flight Plan is loaded. (Figure 2-52)

## **FR:**

The **FROM** waypoint identifier is followed on the same line by the first waypoint (origin) on the selected flight plan (**KDAL**). The **FROM** waypoint is usually replaced by **DIRECT.** (Figure 2-52)

## **TO:**

The **TO** waypoint identifier is followed on the same line by the last waypoint (destination) on the selected flight plan (**RW34**). (Figure 2-52)

## **GS:**

The groundspeed in knots is input automatically when the groundspeed is valid or can be inserted manually which is indicated by **(MAN)**. The **GS** value, **(MAN)** and ETA

Figure 2-52

value will change to yellow. **(CALC)** will replace **(MAN)** field if a manual ETA is entered on line 9. (Figure 2-52)

## **DIS/DTK:**

The distance in nautical miles and tenths between either the **FROM** and **TO** waypoints or between the aircraft's present position and the **TO** waypoint. The desired track is the Great Circle course between the **FROM** and **TO** waypoints. The **DTK** will have a **T** adjacent to it if a true heading input is received or if the **FROM** waypoint is north N 70° or south S 60° latitude. (Figure 2-52)

## **ETE:**

The estimated time enroute in hours, minutes and tenths of minutes between the aircraft's present position and the **TO** waypoint or the **FROM** and **TO** waypoints based on the **GS** value. (Figure 2-52)

## **FPL:**

The total active or stored flight plan distance and time remaining via the Flight Planned route from the **FROM** waypoint, (or the aircraft's present position when a Direct To leg is displayed), to the last waypoint on the selected flight plan that precedes a "fence". Distance is displayed in whole miles and time is in hours and minutes. (Figure 2-52)

## **ETA @:**

Estimated time of arrival at the destination, or last waypoint on the Active Flight Plan that precedes a "fence", appears when a **DIRECT TO** leg is displayed. (Figure 2-52)

NOTE: The **ETA** value field will turn yellow if a ground speed is entered manually, indicating that the **ETA** is calculated based on the manual ground speed value. The **GS** field will turn yellow and **(CALC)** will be displayed if a manual ETA value is entered.

## **RAIM @:**

Receiver Autonomous Integrity Monitoring at the last flight plan waypoint will display **AVAIL** (available) or **NOT AVAIL** (not available) at the ETA. If a manual ground speed or ETA has been entered, **STANDB**Y will be displayed momentarily while the system calculates RAIM availability. If **GPS** is not functioning, **NO NAV** will be displayed.

## **PLAN 3/8 (Page 3 of 8) FUEL PLAN**

Pressing the **FPL** Key again will display the **PLAN 3/8** Page.

## **FUEL PLAN:**

The **"A"** indicates that Active Flight Plan information is being displayed. A numeric entry in the field provides fuel planning for stored flight plans. (Figure 2-53) Dashes are displayed if there is no active Flight Plan.

## **FR:**

The **FROM** waypoint identifier is followed on the same

Figure 2-53

line by the first waypoint (origin) on the selected flight plan. The **FROM** waypoint is usually replaced by **DIRECT.** (Figure 2-53)

## **TO:**

The **TO** waypoint identifier is followed on the same line by the last waypoint (destination) on the selected flight plan. (Figure 2-53)

## **GS:**

The ground speed in knots is input automatically when the groundspeed is valid or can be input manually, which is indicated by **(MAN). GS** value and **(MAN)** will be yellow. (Figure 2-53)

## **FLOW:**

The fuel flow in pounds or kilograms is input automatically from fuel flow indicators/transmitters or can be inserted manually, which is indicated by **(MAN)**. (Figure 2-53)

## **LEG FUEL:**

The amount of fuel in pounds (or kilograms) used on the current FROM/TO leg or from the aircraft's present position to the current **TO** waypoint, based on groundspeed, fuel flow and distance. (Figure 2- 53)

## **FPL FUEL:**

The total amount of fuel anticipated to be consumed to the last waypoint on the flight plan that precedes a "fence". This calculated value is based on the current fuel flow, groundspeed values and distance. (Figure 2-53)

## **REM @:**

Appears only if a DIRECT TO leg is displayed. It indicates the amount of fuel remaining overhead at destination, or the last waypoint on the Flight Plan that precedes a "fence", under current conditions. This value is based on the **REMAINING** fuel quantity from the **FUEL STATUS** page minus the total FPL fuel (Figure 2-53). The entire **REM @** field will turn yellow if the **REM @** value is less than the programmed reserve on **PLAN 1/8** Page.

#### **PLAN 4/8 (Page 4 of 8) FUEL FLOW**

Pressing the **FPL** Key again will display the **PLAN 4/8** Page.

## **ENGINE:**

The fuel flow, in pounds or kilograms per hour, for each engine as taken from the fuel flow indication system. the number of engines shown will depend on system configuration. (Figure 2-54).

## **TOTAL:**

The total fuel flow, in pounds or kilograms per hour, from all engines. (Figure 2-54)

Figure 2-54

NOTE: This page will appear only if the system is configured for automatic fuel flow and the individual engine fuel flow is available.

## **PLAN 5/8 (Page 5 of 8) DATE/GMT**

Pressing the **PLAN** Key again will display the **PLAN 5/8** Page.

## **DATE:**

Same as the Initialization Page.

## **GMT:**

Same as the Initialization Page.

NOTE: If necessary, both **DATE** and **GMT** can be corrected on this page but the takeoff and time values will be affected.

## **TAKEOFF**:

The **GMT** at weight-offwheels plus 10 seconds. (Figure 2-55)

## **LAND:**

The **GMT** at weight-onwheels. This field is not displayed until weight-on-wheels plus 10 seconds occurs. (Figure 2-55)

Figure 2-55

NOTE: **TAKEOFF** and **LAND** times may be based on groundspeed and/or TAS valids depending upon system configuration.

## **FLIGHT TIME:**

The elapsed flight time is displayed in hours and minutes. (Figure 2-55)

## **PLAN 6/8 (Page 6 of 8) AIRCRAFT WEIGHT**

Pressing the **PLAN** Key again will display the **PLAN 6/8** Page.

## **BASIC OP WT:**

The combined weight in pounds or kilograms of the empty aircraft, crew members, and crew baggage. (Figure 2-56)

## **PAYLOAD:**

Weight in pounds or kilograms of passengers, cargo, and baggage (excluding crew). (Figure 2-56)

Figure 2-56

## **FUEL ON BOARD:**

Weight in pounds or kilograms of fuel on board. (Figure 2-56)

## **VERIFY INPUTS:**

Each of the flashing values must be verified or entered by pressing the **ENTER** Key when the cursor is over each field. This field is displayed only after system turn on.

## **VERIFY FUEL:**

This is displayed in the same field as **VERIFY INPUTS** if a manual fuel flow has been entered and has not been verified for 15 minutes or more.

## **FUEL USED:**

If configured for Automatic Fuel Flow, the weight in pounds or kilograms of fuel consumed. (Figure 2-56)

*NOTE: This field appears as dashes at power up and increments as auto fuel flow data is available.*

## **GROSS WT:**

The total weight in pounds or kilograms of basic operating weight, payload and fuel on board displayed after all values have been entered. (Figure 2-56)

## *PLAN 7/8 (Page 7 of 8) FDE Prediction*

**All references to FDE prediction do not apply to 17960-0101 units. FDE prediction is only available in 17960-0102, 17960-0203 and 17960-0204 units.**

Pressing the **PLAN** Key again will display the **PLAN 7/8** Page. This page is used if GPS will be the sole navigation source in Oceanic/Remote operation. The following information is entered to make the necessary FDE prediction to determine sufficient satellite

availability, integrity, and accuracy. All entries made on this page will remain until changed or the system is powered down. See Figure 2-57.

## **DEPART DT**:

Date for which FDE prediction is to be calculated.

*Figure 2-57*

Time for which FDE prediction is to be calculated.

## **ROUTE SPACING**:

**DEPART GMT**:

Centerline to centerline route spacing of segment for which FDE is being calculated. 1 to 99 nautical miles may be entered. 60NM is a normal entry.

## **EXPECTED GS**:

Estimated ground speed for the route segment. A value of 100 to 999 may be entered.

## **START FDE WPT**:

First waypoint on the Oceanic/Remote route segment. Placing the cursor over this field allows waypoint entry. Pressing the **BACK** Key will cycle through the waypoints on the active flight plan. Dashes are displayed prior to the last waypoint on the flight plan. Pressing **ENTER** while the dashes are displayed will clear the start and end waypoints, resulting in an undefined Oceanic/Remote segment.

## **END FDE WPT**:

Last waypoint in the Oceanic/Remote route segment. The **BACK** and dashes operate the same here as in the **START FDE WPT** field.

## **EXCLUDE SATS (QTY x)**:

Displays the number of satellites currently being excluded from the FDE prediction. Up to seven satellites may be excluded at a given time. When the cursor is placed over this field and **ENTER** is pressed, the **FDE EXCLUDE SATS 1/1** Page will be displayed. See Figure 2-58

Figure 2-58

## **ENTRY REQUIRED**:

This is displayed If the aircraft is on the ground and not all the data has been entered. The following is a list of the other possible messages displayed in this field:

## • **START CALC? ENTER**:

This is displayed when the aircraft is on the ground and all data has been entered. Pressing ENTER will start the FDE calculation and display PLAN 7/8 FDE COMPUTA-TION. See Figure 2-59

Figure 2-59

- **NEED ACTIVE FPL**: This will be displayed if there are less than two waypoints on the active flight plan.
- **BACK FOR NEXT WPT**: Displayed when the cursor is over the start or end waypoint field.
- **PRED IN PROGRESS**: This is displayed when an FDE prediction is in progress. All other fields are disabled at this point.
- **PREDICTION UNAVAIL**: This will be displayed if the GPS is not in the idle state or the aircraft is not on the ground.

#### **FDE EXCLUDE SATS 1/1 (Page 1 of 1)**

This page is accessed by placing the cursor over the **EXCLUDE SATS (QTY x)** field on **PLAN 7/8** Page and pressing **ENTER**.

## **EXCLUDE SATS LIST**:

The designated satellite number being excluded from the FDE prediction is listed here.

Figure 2-60

**SAT #**:

The desired satellite being excluded from FDE prediction is entered by pressing the Line Select Key by this field and entering the number of the satellite. Press **ENTER** to add the satellite to the list. Entering a number already listed and pressing **ENTER** will remove the number from the list. Pressing the Line Select Key next to **CLEAR ALL** and pressing **ENTER** will remove all satellites from the exclusion list.

## **PLAN 8/8 (Page 8 of 8) FDE COMPUTATION**

## **COMPUTING - STANDBY**:

This display will flash while FDE prediction is being calculated. See Figures 2-61

## **xx% COMPLETE**:

The number displayed is the percentage of calculation completed.

Figure 2-61

When the FDE prediction is complete, the system will display either FDE and NAV are available or unavailable. Normal calculation time is from ten to twenty minutes. See Figures 2-62 and 2-63.

Figure 2-62

Figure 2-63

## **HEADING SECTION (HDG KEY)**

Upon pressing the **HDG** Key the **HEADING VECTOR 1/1** Page will be displayed and the following can be observed.

## **HEADING PAGE**

## **HEADING VECTOR 1/1 (Page 1 of 1)**

## **HDG:**

Commanded heading in whole degrees. This field may also prefill with current aircraft heading if heading is valid. Pilot may manually enter heading preceded by a turn direction **R** or **L**. A **T** indicates the system is operating in the true heading mode. After a heading entry is made and the **ENTER** Key

Figure 2-64

is pressed, the cursor will move to the Heading Mode field and **HDG SELECT?** will be displayed.

## **HEADING MODE:**

Use **BACK** Key to select one of the following:

- **INTERCEPT:** indicates Heading Mode is **ON** and will intercept next leg of the flight plan if the remaining fields are verified or entered. (Figure 2-65)
- **CANCEL:** indicates Heading Mode is **OFF**.
- **HDG SELECT:** indicates Heading Mode is **ON,** but no intercept.

Figure 2-65

NOTE: If any of the mode words are followed by a **?** the mode is not active. The **ENTER** key must be pressed to activate the mode.

## **TO WAYPOINT:**

Prefills with current **TO** Waypoint or is enterable (from one to six alphanumeric characters). (Figure 2-65)

NOTE: With the cursor over the **TO** Waypoint field, using the **BACK** Key will step through to the end of the Active Flight Plan waypoints. The system will identify an IAF, ARC, PT, HP, FCF, FAF or MAP waypoint above the TO Waypoint field.

## **DTK:**

Desired track is the Great Circle course in whole degrees between the **FROM** and **TO** waypoints from Navigation Page 1. (Figure 2-58) If the system is displaying Direct **To** a waypoint, the **DTK** will be from present position to the current **To** waypoint.

NOTE: If the default desired track is changed, a Pseudo Vortac (selected course) leg will be programmed on the **NAVIGATION 1/4** Page.

## **INTERCEPT** Messages:

If the Intercept Mode is programmed one of the following messages may appear. (Figure 2-65)

- **INTERCEPT BEYOND FIX** indicates the commanded heading will cause the aircraft to intercept the programmed course on the FROM side of the fix.
- **NO COURSE INTERCEPT** indicates the commanded heading will cause the aircraft to diverge from the programmed course (crosstrack deviation will increase).
- No Message indicates an intercept is not programmed, or the commanded heading will intercept the programmed course prior to the fix. (The **TO** side of the fix)
- **NO ARC INTERCEPT** indicates commanded heading will not intercept the arc programmed on the approach procedure.

## **OK? ENTER:**

The procedure for accepting the entered heading, **TO** waypoint or **DTK** is to depress the **ENTER** Key. (Figure 2-65)

## **TUNING SECTION (TUNE KEY)**

Upon pressing the **TUNE** Key the **TUNE 1/4** Page will be displayed and the following can be observed.

## **TUNING PAGES**

## **TUNE 1/4 (Page 1 of 4) COMM**

NOTE: If the system is configured for two or less communications radios, the tune section will display only three pages.

## **COMM 1** or **COMM 2:**

The information for each Comm radio. (Figure 2-66)

## **ACTIVE:**

NOTE: If the frequency currently tuned and displayed on the respective control head, appears briefly but turns to dashes, the system interface does not provide a return frequency input.

Figure 2-66

**(MAN)** in this field indicates the frequency was manually entered via the control head (Figure 2-66). If the **(MAN)** field is blank, the system was tuned via the CDU keyboard.

## **PRESET:**

The pilot can enter and store a frequency in this field through the keyboard. (Figure 2-66)

## **TRANSFER?:**

The displayed **PRESET** frequency can be transferred to **ACTIVE** when the **ENTER** key is depressed. The control head will reflect this change. (Figure 2-66)

## **TUNE 2/4 (Page 2 of 4) COMM**

The same information from the first page is displayed here for additional **COMM** radios.

## **TUNE 3/4 (Page 3 of 4) NAV**

Pressing the **TUNE** Key again will display this page and the following information may be observed.

## **NAV 1** or **NAV 2:**

The station identifier to which the respective **NAV** receiver is tuned. **(KEY)** will be displayed when the frequency or identifier of the station has been entered using the CDU keyboard.

## **FREQ:**

The frequency currently tuned and displayed on the respective control head. **(MAN)** in this field indicates the frequency was manually

entered via the control head. The field may also show **(KEY)** if the ident is unknown and the frequency was tuned via the CDU keyboard. **(KEY)** will appear in the **NAV 1** or **NAV 2** field if the I**DENT** is known. No annunciation in this field indicates the VPU is automatically tuning the NAV radio. (Figure 2-67)

Figure 2-67

## **RANGE:**

The range in nautical miles and tenths from aircraft present position to the DME. (Figure 2-67) The station identifier can also appear in the field between the range and range value field if the control head is placed in the DME HOLD mode. **NO ID** is displayed in this field if the identifier of the held station is unknown.

## **BRG:**

The bearing in whole degrees from aircraft present position to the VOR. (Figure 2-67)

When the dedicated DM441B or the dedicated DME42 is configured, the **TUNE 3/4** page is different (Figure 2.67a). The Bearing information is suppressed and DME is annunciated instead of NAV.

When the non-dedicated DM441B is configured, the **TUNE 3/4** page is different (Figure 2.67b). The Bearing information is suppressed and the radios cannot be manually tuned.

#### **TUNE 4/4 (Page 4 of 4) XPDR/ADF**

Pressing the **TUNE** Key again will display this page and the following information may be observed.

#### **XPDR:**

NOTE: If the transponder reply code appears briefly after tuning but turns to dashes, the system interface does not provide a return frequency input. **(MAN)** indicates the entry was made through the control head. (Figure 2-68)

Figure 2-67a

Figure 2-67b

Figure 2-68

## **ADF:**

NOTE: If the frequency that the **ADF** is tuned to appears briefly but turns to dashes because the system interface does not provide a return frequency input. It may also be annunciated with (**MAN**). (Figure 2-68)

NOTE: If either the **XPDR** or **ADF** frequencies are tuned via the CDU keyboard the **(MAN)** field will be blank.

## **HOLDING PATTERN SECTION (HOLD KEY)**

## **HOLDING PATTERN PAGE**

This page is accessed by depressing the **HOLD** Key when the cursor is positioned over a Waypoint Identifier.

## **HOLDING PATTERN 1/1 (Page 1 of 1)**

## **AT:**

The Holding Fix and country name or airport ident. (Figure 2-69)

## **• HOLDING PATTERN ENTRY AND STATUS MESSAGE:**

If the entry course to the holding fix can be determined, the entry procedure will be annunciated after all the holding pattern parameters are entered.

Figure 2-69

- **DIRECT ENTRY:** indicates the system will use a direct entry to the holding pattern. See Figure 2-70 for Direct Entry pattern.
- **TEARDROP ENTRY:** indicates the system will use a teardrop entry to the holding pattern. See Figure 2-71 for Teardrop Entry pattern.
- **PARALLEL ENTRY:** indicates the system will use a parallel entry to the holding pattern. See Figure 2-72 for Parallel Entry pattern.

Direct Entry Pattern Figure 2-70

Teardrop Entry Pattern Figure 2-71

Parallel Entry Pattern Figure 2-72

- **HOLDING:** indicates the system has entered the Holding Pattern. (Figure 2-73)
- **EXIT HOLD:** indicates the system will exit the holding pattern the next time over the holding fix.

## **INBOUND CRS** (course):

The inbound holding course in whole degrees. This field can be True or Magnetic according to the display mode selected by the TRUE/MAG switch input. A **T** appears if in the True mode (Figure 2-73). The **T** field will be blank if the system is Magnetic mode.

Figure 2-73

## **MAX HOLDING TAS:**

This field is computed based on configuration module max holding indicated airspeed and worst case winds. It represents the maximum true airspeed in the holding pattern that will assure that the aircraft remains in protected airspace. (Figure 2-73)

## **TURN DIR** (direction):

**RIGHT** indicates the standard default holding pattern turn direction. The non-standard **LEFT** turn can be accessed using the **BACK** Key when the cursor is over this field. (Figure 2-73)

## **LEG TIME:**

Holding Pattern inbound leg time in minutes and tenths (1.0 to 9.9). (Figure 2-73)

NOTE: The **LEG TIME** may be in parentheses indicating that the time has been calculated using **LEG DIS.**

## **LEG DIST** (distance):

Holding Pattern inbound leg distance in nautical miles (1.0 nm to 50.0 nm). (Figure 2-73)

NOTE: The **LEG DIS** may be in parentheses indicating that the distance has been calculated using **LEG TIME.**

## **EXIT MODE:**

The **MANUAL** default indicates the system will stay in the holding pattern indefinitely. Using the **BACK** Key with the cursor over this field **AUTO** can be selected if the **ENTER** key is pressed. The system will then execute a holding pattern entry and exit the next time crossing the fix waypoint. (Figure 2-73)

NOTE: If a holding pattern is selected an **HP** is annunciated next to the waypoint on Flight Plan, Navigation and Direct To Pages.

## **OK? ENTER:**

Depressing **ENTER** Key when this prompt appears at the bottom of the Holding Pattern Page programs a Holding Pattern for a particular waypoint.

NOTE: The cursor will not appear in this field.

## **CANCEL:**

Used to cancel a holding pattern. (Figure 2-73)

## **POSITION FIX PAGE**

This page is accessed by depressing the **HOLD** Key anytime the cursor is not displayed over a waypoint.

## **POS:**

The composite (system) position coordinates at the moment the **HOLD** Key was depressed in degrees, minutes, and hundredths of minutes. (Figure 2-74)

## **IDENT:**

The alphanumeric designator of the reference waypoint used to check or update position. (Figure 2-74)

## **FIX** :

The actual coordinates of the reference point in degrees, minutes, and hundredths of minutes. (Figure 2-74)

Figure 2-74

## **DIF:**

The difference between the composite position and the **FIX** (or other sensor) position in degrees, minutes and hundredths of minutes. (Figure 2-74)

NOTE: Position coordinates of individual sensors and the difference between those sensor positions and the composite (system) position may be displayed by moving the cursor over the **FIX** field and depressing the **BACK** Key. The composite position may be updated to the most accurate sensor by pressing the **BACK** Key until the desired sensor appears, then pressing the **ENTER** Key twice.

## **DIRECT TO SECTION (** d **KEY)**

## **DIRECT TO PAGES**

## **DIRECT 1/2 (Page 1 of 2)**

This display is accessed through the d key and presents a listing of all Active Flight Plan waypoints on as many pages as is appropriate to display all of the waypoints. The cursor may be positioned over any desired identifier (ahead of or behind the aircraft) to proceed **DIRECT** (Figure 2-75). A new waypoint may be added to the flight plan to proceed direct.

## **TO:**

When this page is accessed, the cursor is displayed over the current **TO** waypoint. (Figure 2-75)

The following may also be displayed with a waypoint: **HP** (Holding Pattern), **PT** (Procedure Turn), **MAP** (Missed Approach Point), **FAF** (Final Approach Fix), and **IAF** (Initial Approach Fix).

Figure 2-75

## **DIR CLOSEST ARP 2/2 (Page 2 of 2)**

**DIRECT TO CLOSEST AIR-PORT:** The Closest Airport page is the last page in the **DIRECT TO** section. Up to nine airports are displayed, in order of their proximity to the aircraft, with the closest airport listed first. (Figure 2- 76)

Figure 2-76

NOTE: Airports listed from the database on this page have runways 3000 ft long or greater and are hard surfaced.

## **WAYPOINT SECTION**

## **WAYPOINT PAGES**

Waypoints fall into four categories:

- Database generated
- Pilot entered (personalized/ offset)
- Special
- Obsolete

Waypoint Pages can be accessed from any **FLIGHT PLAN, NAV,** d **, HOLD, INITIALIZATION, HEADING,** or **TRIP PLAN/FUEL PLAN** Pages.

## **DATABASE WPT 1/1 (Page 1 of 1) Database Generated Waypoints**

This page is accessed by typing in a waypoint identifier or by placing the cursor over a waypoint identifier and pressing ENTER.

Database Generated Waypoints are automatically updated when accessed and cannot be modified by the operator. The four basic types of waypoints residing in the data base are navaids, airports, intersections and special waypoints.

## **VHF Navaids**

## **WAYPOINT:**

Alphanumeric designator for the Navaid. (Figure 2-77)

NOTE: If the waypoint has a duplicate identifier in the database, for another location, the closest waypoint to the aircraft position will be shown and the country code will be displayed beneath the waypoint identifier. (Figure 2-78)

Press the **NXT** Key to sequence to the next waypoint page with a different country code. The **PRV** Key can be used to sequence backward through the waypoint pages. Additional country codes and corresponding **POS** coordinates will be sequentially displayed.

Figure 2-77

Figure 2-78

## **POS:**

The coordinates of the waypoint as stored in the database memory. (Figure 2-77)

## **FREQ:**

The VHF frequency for the station. (Figure 2-77)

## **VAR:**

The magnetic variation of the station. (Figure 2-77)

## **ELEV:**

The elevation in feet of the station (DME equipped VHF Navaids only). A (-) indicates elevation is below sea level. (Figure 2-77)

## **NDB -ENTER:**

The procedure for accepting the waypoint from the Navigation Data Base is to depress the **ENTER** Key. (Figure 2-78)

## **Non-Directional Beacons (NDBs)**

NDBs stored in the internal database are listed in Jeppesen publications with a 2 or 3 letter identifier. To distinguish these NDBs from VHF NAVAIDS, you must add an "NB" suffix to the database identifier. Example: To access the Prince Rupert (PR) NDB, you must enter PRNB. (Figure 2-79)

Figure 2-79

## **Airports**

International Civil Aviation Organization (ICAO) identifiers are used to access data in the database.

ICAO identifiers differ in some cases from those familiar to many pilots.

The following are guidelines to access information from the database:

Except for a few hundred 3 or 4 letter/number airport identifiers in Alaska, Canada and the Continental USA, all airport identifiers stored in the database have 4 letters.

In most cases, these identifiers begin with a letter that corresponds to the geographic area in which the airport is located. The ICAO code letter prefix for Continental USA airports is **"K"**. Hawaii and Alaska identifiers begin with **"P"**.

To access a 4 character identifier, use the IDENTIFI-ER found in the Jeppesen charts. For example, enter

**KSNA** for Santa Ana. (Figure 2-80)

Figure 2-80

- If the airport shows a 3 letter IDENTIFIER, add the correct ICAO prefix letter. Example: **NEW** (New Orleans Lake Front) add a **"K"** prefix and enter **KNEW** (Figure 2-81).
- If the airport shows a 3 character (letters and numbers) IDENTIFIER, enter the identifier as printed. Example: 31J (Lake City, Florida) enter 31J. (Figure 2- 82)

## **Airport Reference Points, Outer Markers, Runway Thresholds**

Airport Reference Point **(ARP)** coordinates are always displayed in response to the airport identifier.

Outer markers and runway thresholds for which data is stored in the database are also displayed on the airport waypoint page (also known as airport continuation records page) and can be accessed by pressing the **PRV** or **NXT** Key or Line Select Keys. (Figure 2-83)

The selected outer marker or runway threshold will then be displayed in place of the airport identifier in the waypoint field. The airport identifier Shifts to and replaces the **ARP** field below. (Figure 2- 83)

Figure 2-81

Figure 2-82

Figure 2-83

## **Intersections/Enroute Waypoints**

Most intersection waypoint identifiers consist of 5 letters. However, 3, 4, and 5 letter and number combinations exist. To access these waypoints, simply enter the identifier from the Jeppesen chart. Example: **WHALE** intersection. (Figure 2-84)

## **SPECIAL DATABASE WAYPOINTS**

## **PILOT ENTERED WPT (Personalized) Waypoint**

The operator is responsible for generating the waypoint data and maintaining its accuracy.

Figure 2-84

## **WAYPOINT:**

The alphanumeric designator selected by the pilot. Identifiers can consist of up to six characters, and can be composed of any of the characters on the keyboard. (Figure 2-85) However, the asterisk (\*) and pound sign (#) have special functions.

## **POS:**

Blank fields for entering the latitude and longitude of the waypoint. When initially accessed (waypoint not yet in memory) the coordinate fields are both dashed and covered by a double cursor. (Figure 2-85)

Figure 2-85

## **WPTS AVAILABLE**:

The number of waypoints available in memory after this waypoint is defined. Maximum waypoint storage in non-volatile memory is 999. (Figure 2-85)

## **WAYPOINT**:

(Figure 2-86). Same as previous.

## **POS:**

If the waypoint has been previously defined, the coordinates of the waypoint will be displayed as stored in memory. These coordinates may be changed at any time. (Figure 2-86)

Figure 2-86

## **OK? ENTER:**

The procedure for accepting the waypoint if the coordinates are correct is to depress the **ENTER** Key. (Figure 2-86)

#### **OFFSET WAYPOINT**

An offset waypoint is a set of coordinates determined by a selected radial and distance from a previously defined or database (parent) waypoint. An **\*** following the parent waypoint denotes an offset waypoint. (Figure 2-87)

More than one offset waypoint is allowed from one parent, using [\*], [\*1], [\*A1], etc. as identifying notation.

Figure 2-87

NOTE: The offset waypoint uses station declination, if available, or it uses the calculated magnetic variation of the parent waypoint. All waypoints defined by a VHF Navaid in the National/International Airspace System are based on the VHF Navaid station declination. Since the magnetic variation and station declination may not be the same at a given Navaid, the FMS calculated position and the defined position may differ.

## **WAYPOINT:**

The parent waypoint identifier followed by an **\*.** When an offset waypoint identifier is entered and the waypoint has not been previously defined, the **RAD, DIS,** and **POS** fields are all dashed.

When the waypoint has been previously defined the coordinates will be displayed and the radial and distance values will be computed based on the location of the parent waypoint. (Figure 2-87)

If the parent waypoint is a waypoint from an airport continuation record (runway or outer marker associated with a specific airport), the airport identifier will be displayed immediately below the offset waypoint identifier.

If a parent waypoint has a duplicate identifier in the database, the country code will be displayed immediately below the offset waypoint identifier. (Figure 2-87)

## **RAD:**

The radial from the parent waypoint in degrees and tenths of degrees, along which the offset is established. This entry will be annunciated with a **T** if a true heading input is received or if the parent waypoint is north of N 70° or south of S 60° latitude. (Figure 2-87)

NOTE: The radial can be entered in whole numbers without a trailing 0. i.e. enter 070 or 70 and 070.0 will be displayed. To enter a tenth of a radial all 4 digits must be entered. i.e. 0701 will be displayed as 070.1. The **DIS** entry requires a trailing 0 be entered for any **DIS** value greater than .9. i.e. enter 100 to display 10.0.

## **DIS:**

The distance from the parent waypoint to the offset waypoint (1999.9 maximum enterable). (Figure 2-87)

## **POS:**

The computed offset waypoint coordinates based on the pilot entered radial and distance from the parent waypoint. (Figure 2-87)

## **OK? ENTER:**

The procedure for accepting the waypoint if the coordinates are correct is to depress the **ENTER** Key. (Figure 2-87)

#### **SPECIAL WAYPOINTS**

**#0,#1** and **#OFF** are special waypoints defined automatically by the system based on the airplane position.

**#0** After pressing the d key and **ENTER** key the position after the turn where the airplane intercepts the course to the direct to waypoint. The **#0** waypoint is defined as the point from which a DIRECT TO waypoint leg has begun. Should the DIRECT TO procedure require a turn, **#0** will be defined as the point at which the aircraft completes the turn and intercepts the direct course to the fix. **#0** will momentarily be displayed on an EFIS map. **#0** can only be defined by the system.

**#1** The position at the point where the **POSITION FIX** Page was last accessed via the **HOLD** Key. #1 can only be defined by the system.

## **Power Off Waypoint**

The Power Off Waypoint is a set of coordinates retrieved as the last known position when power is lost enroute. This page should be accessed by inserting **#OFF** in the **IDENT** field on the **POSITION FIX** Page after power has been restored and Initialization Enroute has been performed.

## **WAYPOINT #OFF:**

The Power Off Waypoint designator. (Figure 2-88)

## **POS:**

The last present position coordinates at loss of power. Coordinates are stored in non-volatile memory. (Figure 2-88)

Figure 2-88

## **GMT OFF:**

The actual time (Greenwich Mean Time) of power loss. (Figure 2-88)

## **MINUTES OFF:**

The total time elapsed during power off. (Figure 2-88)

## **LAST TK:**

Aircraft track at time of power off. (Figure 2-88)

## **LAST GS:**

Last groundspeed in knots at time of power off. (Figure 2-88)

## **OCEANIC REPORTING WAYPOINTS**

These waypoints are in the database and are used for oceanic position reporting. These waypoints can be added to the FPL by typing special numbers. See Section 3, ADDING A WAYPOINT.

## **OBSOLETE WAYPOINT**

Obsolete Waypoints are typically created when a multiply defined database waypoint used on a stored flight plan is no longer found in the database. This may happen when a new data-base is loaded. An obsolete waypoint can be accessed only by verifying it as an existing waypoint on a flight plan. It will be lost once it is erased from a stored flight plan.

## **MESSAGES (MSG KEY)**

System and Sensor messages are displayed on separate pages in the Message Section. They are accessed by depressing the **MSG** Key. The Message Section will consist of as many pages as are required to display current messages. The **MSG** Key is used to sequence through the System and Sensor Message Pages and to return to the page that was displayed before accessing the Message Section.

**NXT, BACK,** and **PRV** keys can be used to page forward and backward through the message pages.

System Messages describe the system's operation with all related aircraft systems

Figure 2-89

Figure 2-90

(Figure 2-89). Sensor Messages describe the operational status of each navigation sensor (Figure 2-90).

In most instances when new messages are added, the Message light will flash and a flashing yellow asterisk will appear adjacent to the new message.

## **SYSTEM MESSAGES**

#### **ACTION REQUIRED:**

The following are the action required messages that may appear on the **SYSTEM MESSAGES** Page. All will cause the message annunciator to flash.

| System Message  | Explanation                                                                                                                                                                                                                             |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ENTRY REQUIRED  | Information required on the Initialization<br>Page must be verified/entered. (Date, GMT<br>and Position).                                                                                                                               |
| VERIFY POSITION | Aircraft composite (blended) position is in<br>question and must be manually verified.                                                                                                                                                  |
| VAR WARNING     | Magnetic variation cannot be automatically<br>computed, and<br>MAN VAR REQD.<br>A<br>manual<br>variation entry must be made on NAV Page<br>3 (i. e. aircraft position is north of 70°<br>N lati<br>tude or south of 60°<br>S latitude). |

#### **ADVISORY:**

The following are the advisory messages that may appear on the **SYSTEM MESSAGES** Page. All will cause the message annunciator to flash unless otherwise noted with an asterisk \*.

| System Message                   | Explanation                                                                                                                                                                                                                                                                                               |
|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AFIS LINK FAIL                   | For AFIS equipped operation, communica<br>tion to the AFIS DMU has failed.                                                                                                                                                                                                                                |
| AFIS XFER FAIL                   | For AFIS equipped operation, a flight plan<br>transfer from the AFIS DMU to the FMS has<br>failed.                                                                                                                                                                                                        |
| ALTITUDE FAIL                    | The altitude input to the system has failed.                                                                                                                                                                                                                                                              |
| *APRCH ARMED<br>ENTER TO CANCEL? | Approach is ready to be executed. Pressing<br>ENTER<br>will cancel the sequence. Displayed<br>within 30NM radius of the airport. CDI sensi<br>tivity changes to 1NM full scale deflection.<br>VNAV Deviation changes to 500 ft. full scale<br>deflection. The message annunciator will<br>not illuminate. |

**\*APRCH NEXT** Aircraft is within 3NM of the FAF. CDI sen-**ENTER TO CANCEL?** sitivity changes from 1NM to .3NM full scale deflection. The message annunciator will not illuminate.

**\*APRCH ACTIVE** Approach sequence is being executed. **ENTER TO CANCEL?** Pressing **ENTER** will cancel the approach. The message annunciator will not illuminate.

**APRCH CANCELED** System is in an Approach Mode and the approach is changed or deleted from the Active Flight Plan.

**APRCH WARN** The aircraft is within 2 NM from the FAF and GPS is in Dead Reckoning (DR) or there is no RAIM available. HSI is flagged.

**BARO ALT FAIL** The barometric altitude input has failed.

**\*CAL CLOCK FAIL** The internal calendar/clock function has failed.

**CNFG DATA CHANGED** The configuration module data from the present power up and previous power up sequence is different.

**CNFG DATA LOST** CDU non-volatile memory has lost its configuration information and the configuration module has failed.

**CNFG MODULE FAIL** Configuration module has failed. CDU nonvolatile memory configuration information will be used.

**COMPASS FAIL** The aircraft's compass heading input to the system is invalid.

**DATA BASE INVALID** The data base is invalid because the last **UPDATE ABORTED** attempt to update the data base was aborted.

**DR HDG/GS**

**DR HDG/TAS** The system is in the Dead Reckoning (DR) **DR TK/TAS** Mode and is using one of these four combi-**DR TK/GS** nations of inputs to compute position.

**EXT WPT REJECT** CDU has rejected an external waypoint input from a radar or EFIS. (Maximum 99 external waypoints received or 999 waypoints stored).

**ADVISORY: (continued)**

**System Message Explanation**

**FMS LINK FAIL** In dual system operation, communications

with the cross-side FMS has been lost.

**HIGH HOLDING SPD** During Holding or when system is about to

enter a Holding pattern, TAS is high enough to cause the aircraft to stray outside the

boundaries of protected airspace.

**HIGH PROC TURN SPD** The ground speed on entry of a pro-

cedure turn is too high. The message appears approximately three minutes prior to entry of the procedure turn or at any time

during the procedure turn.

**INTERCEPT PAST FIX** A heading intercept mode capture will be on

the from side of the fix.

**IRS ONLY>30 MIN** System has been operating enroute in IRS

Only Mode for more than 30 minutes. The message annunciator will not illuminate if the

aircraft is Weight On Gear.

**IRS ONLY>10 MIN** System has been operating in the terminal

area in IRS Only Mode for more than 10 minutes. The message annunciator will not illuminate if the aircraft is Weight On Gear.

**MEM FAIL** Non-volatile memory has failed at least par-

tially.

**\*NAV RDY** The system is ready to be placed in the

Primary Navigation Mode. Message annun-

ciator will not illuminate.

**NDB FAIL** Database has failed.

**NDB OUTDATED** Expiration date of the database has been

reached. Database should be updated.

**NDB-WW EXP 27OCT** Worldwide (WW) or North American/

European (NA) database and expiration

date.

**NO AUTO LEG CHG** An automatic leg change will not occur upon

reaching the TO waypoint. Message annun-

ciator will not illuminate most of the time.

**ADVISORY: (continued)**

**System Message Explanation**

**NO ARC INTERCEPT** A heading intercept to arc mode will not cap-

ture the arc.

**NO COURSE INTERCEPT** A heading intercept mode will not

capture the desired track.

**NO NAV** The system is not navigating. Message

annunciator will not illuminate.

**POS WARN>1.7 NM** Based on the signal strength or geometry,

the VPU sensor quality may be such that the composite position may have more than 1.7 nm error and may not be suitable for naviga-

tion in the terminal areas.

**POS WARN>2.8 NM** Based on the signal strength or geometry,

the VPU or VLF sensor quality may be such that the composite position may have more than 2.8 nm error and may not be suitable

for enroute navigation on J/V routes.

**POS WARN>3.8 NM** Based on the signal strength or geometry,

the VPU or VLF sensor quality may be such that the composite position may have more than 3.8 nm error and may not be suitable for enroute navigation on J/V or Random

routes.

**POWEROFF POS** The system has lost power in flight for more

than 7 seconds and the **#OFF** waypoint is available. Reviewing the **#OFF** waypoint

page removes this message.

**SENSOR MISCOMPARE** The difference between the CDU composite

(blended) position and a sensor position

exceeds a predetermined amount.

**\*STRG INVALID** The system has stopped computing a roll

command steering output due to invalid heading, auto-TAS, navigation leg, groundspeed or crosstrack distance. Message

annunciator will not illuminate.

**TAS FAIL** The True Airspeed input to the system from

the Air Data Computer is invalid.

Jun/00

**ADVISORY: (continued)**

**USING MAN HDG** An H-field antenna is installed with the RPU

and a manual heading input is being used.

**\*WPT ALERT** The aircraft is within 30 seconds ETE of the

next leg lateral change. Message annuncia-

tor will not illuminate.

**WPT MEM FULL** All 999 waypoint locations have been used

in flight plans or as FROM or TO waypoints.

**VNAV WPT ALERT** Aircraft is within 1 minute ETE of **#TOD** or

path intercept point. Message annunciator will not illuminate. However the discrete WPT annunciator will flash for 10 seconds

then go steady

**VSPD FAIL** The system vertical speed input has failed.

## **SENSOR MESSAGES**

The following are sensor messages that may appear on the **SEN-SOR MESSAGES** Page. All messages will cause the **MSG** annunciator to flash unless other wise noted with an asterisk\*.

| Sensor Message | Explanation                               |
|----------------|-------------------------------------------|
| ACCURACY WARN  | The integrity monitoring system that moni |

tors the satellite constellation (RAIM) has detected a GPS horizontal position error that is outside the alarm threshold for the phase of flight in progress. (.3NM Approach; 1NM

Terminal; 2NM Enroute)

**ALIGN** The IRS is in the alignment mode and is not

yet **NAV RDY**.

**ATTITUDE** The IRS is in the Attitude mode.

**BATTERY WARN** The sensor is operating on its own internal

battery.

**CHECK QUAL** The VPU quality factor has exceeded the

pilot entered advisory quality factor.

**SENSOR MESSAGES: (continued) Sensor Message Explanation**

**\*DESELECTED** The sensor has been manually deselected

and will no longer contribute to the computation of composite (blended) position. Message annunciator will not illuminate.

**DR** Either the GPS or VPU sensor is in the

Dead Reckoning (DR) mode of navigation. The message annunciator will not illuminate

for VPU.

**ENTR SET HDG** The IRS is in the attitude mode and a head-

ing value must be entered.

**LINK FAIL** Data exchange between the sensor and

CDU has failed.

**\*NAV RDY** The sensor is capable of navigation, but has

not been placed in the navigation mode. Message annunciator will not illuminate. Only dispayed when GPS sensor is not

available.

**\*NO NAV** The sensor has not navigated since system

power up. Message annunciator will not illu-

minate.

**NO RAIM** RAIM is not available at this time.

**NO RAIM @ DEST** RAIM is available at the present time, but

will not be available at the destination arrival

time.

**THIS PAGE INTENTIONALLY LEFT BLANK**
