# MFD-85B DISPLAY FORMATS

The MFD-85B Multifunction Display (MFD) is a flight planning unit used to increase the operational capabilities of the EFIS-85C(14)/86C(14) system. The MFD-85B is used in EFIS-85C(14)/86C(14) installations that do not have a TCAS system or in which the TCAS system is not connected to the EFIS system. Installations in which a TCAS system is connected to the EFIS-85C(14)/86C(14) system use the MFD-85C described later in this book. Standard functions shown on the MFD-85B include:

- · weather radar
- three selections of pictorial navigation maps ("heading up", "north up with aircraft centered", and "north up maximum view")
- an additional fourth selection (map plan) if a compatible LNAV is installed
- and page data for checklists.

The MFD can also show information from compatible LNAV sources in remote data display modes. Also, an extended data display mode can show additional detailed inflight information, from a compatible LNAV source, about navigation sensor data and data for several modes of flight (cruise, approach and CAT II checklists). In addition, diagnostic information for use by maintenance personnel can be shown on the MFD.

MFD-85B Multifunction Display

Pilot's Guide

#### **Overview of Standard Functions**

Weather Radar—The radar display mode shows detected precipitation from the TWR-850 Turbulence Weather Radar System on the MFD. Weather radar mode, range, and other radar system operating parameters are selected on the WXP-850().

Weather radar data can show on the MFD in a dedicated display mode or as part of a composite display of weather radar and navigation information. The navigation portion of the composite display shows only the "heading up" map display mode. If any other NAV mode map is selected ("north up aircraft centered", "north up max view" or "map plan"), the display changes to the "heading up" map when weather radar is added to form the composite display of navigation information and radar data.

The Collins TWR-850 Turbulence Weather Radar System consists of the RTA-852, -854, or -858 Receiver-Transmitter-Antenna, a WXP-850A or -850B Weather Radar Panel, and an EFIS system for the weather radar display. Weather radar data from the TWR-850 is processed by the WXP and shown on the MFD and EHSI displays.

The WXP processes the radar data, controls the radar operating modes, and sets the display range. Data output from the WXP to the EFIS system for display on the MFD includes:

- four color weather (green, yellow, red, and magenta, on a black screen)
- detected turbulence and turbulence alert annunciation
- ground map (MAP display mode)
- PAC Alert annunciation (Path Attenuation Correction, yellow arcs at the perimeter of the display)
- GCS (Ground Clutter Suppression)
- target alert annunciation.

Some WXPs also feature slave switching for use in installations with two radar displays (such as both EHSIs, or an MFD and an EHSI) and two WXP controls. Other WXP features include autotilt and sector scan.

"PAC Alerts" show on the display to indicate that the radar beam, in the area indicated, has encountered a target with rainfall rates heavy enough to greatly attenuate the radar beam. In this situation, targets behind that rainfall may not be detected and shown on the display. A "PAC Alert" shows as a yellow arc or band at the outer perimeter of the radar display. The portion of the radar's scan for the width of the yellow arc and between the arc and the intervening rainfall is the area in which the radar may not detect targets.

Navigation Information—One of four pictorial navigation maps may be selected from the NAV menu as the presentation for the navigation display mode. The four maps are:

- · heading up
- north up with aircraft centered
- north up max view
- map plan (map plan is available only in installations with a compatible LNAV system)

All of the navigation maps are capable of simultaneously showing the location of:

- two VOR/DME stations
- two waypoint strings of up to 3, 5, or 6 waypoints each (depends on the LNAV and the aircraft wiring)
- up to seven closest NAVAIDS (the number available depends on the LNAV installed)
- and up to seven closest airports (the number available depends on the LNAV installed).

#### NOTE

The airport symbols shown in the navigation map display formats are for display purposes only and *do not* in any way show the actual runway headings or the orientation of the airport represented by the symbol. Always refer to the published navigation charts or approach plates for the actual runway headings and the airport orientation.

Navigation information can show on the MFD in a dedicated display mode or as part of a composite display of navigation information and weather radar data. (Weather radar must be set to a weather detection mode to show weather.) The navigation portion of the composite display shows only the "heading up" map display mode. If any other navigation map is selected ("north up aircraft centered", "north up max view" or "map plan"), the navigation display changes to the "heading up" map when weather radar is added to form the composite display of navigation and radar data. When the radar mode is turned off, the MFD changes back to the previously selected navigation map.

Anytime the radar display mode shows on the MFD, as part of a composite display mode or in the dedicated radar mode, the display range is set by the WXP. In the dedicated navigation display mode, the display range is set by the line advance or line reverse keys at the bottom of the MFD front panel. The range set for the dedicated navigation display mode is stored in memory and is recalled when the dedicated navigation display mode is selected.

Page Data—100 pages of user information may be stored in nonvolatile memory in the MFD. This data may be arranged in chapters and can be designated as either normal PGE (page) or EMG (emergency) data. All 100 pages can be input and modified by the user with the handheld RDP-300 Remote Data Programmer or the CEU-85 or CEU-85A Checklist Entry Unit. The CEU-85 is used in conjunction with an Apple<sup>®</sup> II plus, IIe, or IIe enhanced computer with a Collins Pro Line II Interface Card installed and checklist processing disk software. The CEU-85A is used in conjunction with an IBM<sup>®</sup> or compatible personal computer and the master checklist processing program.

#### **Overview of Additional Functions**

When used with a full featured, compatible LNAV, the MFD provides the following additional functions.

Waypoint Definition—When the navigation display mode shows on the MFD as part of a composite display mode or by itself, the MFD joystick may be used to move a waypoint cursor around the map display. Move the joystick in the direction required to place the cursor in the desired position on the display relative to the aircraft symbol and selected display range. When the joystick is moved, the word "ENTER" shows in green next to the third line select key from the top and a bearing and distance annunciator shows in green in the left center of the display. The "ENTER" line key, transfers the bearing and distance data for the waypoint cursor to a compatible LNAV system.

Remote Data— A compatible LNAV system can give pages of navigation information to the EFIS system for display on the MFD in remote (RMT) data display modes. There are three RMT sources available in installations with early versions of DPU and MPU. Later versions have only two RMT sources. The different pages of data (and the colors of the displayed data) are controlled by the control unit for the LNAV, and no control operations are required on the MFD following selection of the remote port.

#### Weather Radar (RDR) Display Mode

Push the RDR button to alternately turn on and off the weather radar display mode on the MFD. In the RDR display mode, the display mode annunciator "RDR" shows in green in the upper left corner of the display.

In the dedicated RDR display format the MFD shows a white aircraft symbol centered at the bottom of the display, and a digital heading read-out centered at the top of the display. The heading type and sensor number (MAG#, TRU#, or DG#) is annunciated to the right of the digital heading display. A dashed range arc shows at full range, and a solid range arc shows at half of the selected range. Range is selected by the "RANGE" control on the WXP. The selected full scale range annunciator shows at the right-hand end of the full-range arc, and the half-range annunciator shows at the right-hand end of the half-range arc. The full-range arc and both range annunciators show in cyan (the annunciators change to yellow when slaved operation is selected). The half-range arc shows in white in the radar ground mapping mode (MAP) and in cyan in all other modes. PAC alert arcs show in yellow along the inside edge of the full range arc.

The weather radar display area extends from the aircraft symbol to the full-range arc. Weather intensity shows on the MFD in four colors on a black background. The minimum rainfall level shows in green, the next level in yellow, the next in red, and the heaviest level shows in magenta. Magenta is also used to show areas of detected precipitation-related turbulence when the WXP is set to the WX+T or TURB mode and the range is set to 5, 10, 25, or 50 nautical miles.

Weather radar mode annunciators (OFF, STBY, TEST, TGT, MAP, WX, WX+T, and TURB) show in cyan at the left end of the half-range arc in the RDR display mode, and in the upper left corner of the MFD when the RDR display mode is not selected. In the slaved mode the radar mode annunciators show in yellow preceded with the letter X (i.e., XWX+T, XMAP, XTURB, etc...).

When the radar target alert (TGT) mode is selected on the WXP, the MFD shows the mode annunciator "TGT" in cyan at the left end of the half-range arc in the RDR mode or in the upper left corner when not in the RDR mode. (Some early EFIS versions show the cyan "TGT" annunciator in the upper left corner of the MFD in all display modes.) Also, a second "TGT" annunciator shows in yellow in a yellow box in the upper right corner of the display in all MFD display modes. The half-range arc shows as a dashed cyan arc and detectable weather does not show on the display. Display range is controlled by the WXP when it is set to the TGT mode, even though detected weather does not show on the display. The WXP controls the display range in all radar operating modes when the MFD is set to show radar data (RDR display mode).

Target alert notifies the pilot of weather targets that are producing rainfall rates greater than 0.5 inch (12.7 millimeters) per hour and/or of turbulence consisting of precipitation areas where the wind velocity shifts in excess of 16.40 feet-per-second (5 meters-per-second). The WXP target alert mode provides a target alert "window" from 7- to 200-nmi range (50 nmi maximum range for turbulence detection) and ±15 degrees of dead ahead, regardless of the range selected on the WXP. When selected on the WXP, the TGT mode is active in all MFD display modes. The yellow "TGT" annunciator in the upper right corner of the display flashes when a precipitation target is detected within the target alert "window". The flashing yellow box shows the letters "TRB" in place of TGT when an area of precipitation related turbulence is detected within the target alert "window". If areas of precipitation and turbulence are both detected within the target alert "window", the flashing annunciation alternates between "TGT" and "TRB" at a faster rate. A radar mode on the WXP that shows weather on the MFD (WX+T or WX), must be selected to see and analyze the detected weather.

Pilot's Guide

Additional radar annunciators shown on the MFD in cyan (yellow in slaved mode) are:

- USTB (antenna unstablized)
- GCS (Ground Clutter Suppression)
- G+1, G+2, G+3, G-1, G-2, and G-3 (transmitter-receiver gain settings other than calibrated)
- +15.5, -15, A+15, A-10.2, etc... (antenna tilt and autotilt settings other than 0).

The USTB annunciator shows on the display when the STB button on the WXP is in the out position. In early versions of the EFIS-85C(14)/86C(14) systems the USTB annunciator shows at the right end of the half-range arc. In later versions the USTB annunciator shows in the upper left corner of the display. Detection of an attitude fault by the radar system shows the USTB annunciator flashing.

#### WARNING

Continuous operation with GCS turned on is not recommended, because some precipitation returns may also be reduced in intensity or eliminated from the display.

The GCS annunciator shows on the display when the GCS button is set to the in position. Early systems show the GCS annunciator at the left end of the half-range arc to the right of the radar mode annunciator. Later systems show the GCS annunciator in the upper left corner of the display to the right of the USTB annunciator. GCS reduces the intensity of ground returns so that many of them disappear from the display to make it easier to view the precipitation returns.

The gain annunciator shows on the display when the GAIN knob on the WXP is set to any position other than CAL (calibrated). Gain annunciators show to the right of the RDR display mode annunciator in the upper right corner of the display in all systems. Higher gain settings are shown with the + symbol in the annunciator (i.e., G+2) and lower gain settings are shown with the - symbol (i.e., G-1). Normal operation is with the GAIN knob on the WXP set to the CAL position and no annunciator shown on the display.

In early systems the tilt/autotilt annunciator shows on the display at the right end of the half-range arc. In later systems the tilt annunciators shows at the left end of the half-range arc. Up tilt is shown by the + symbol in the annunciator (i.e., +10.7) and down tilt is shown with the - symbol in the annunciator i.e., -12.5). When the AUTO switch on the WXP is pulled out, the tilt annunciator shows the letter A in front of the tilt setting (i.e., A+5.2).

With the MODE knob on the WXP set to the "MAP" mode, the MFD shows ground contours in four colors cyan, green, yellow, and magenta (least reflective to most reflective) and the half-range arc as a solid white arc. The "MAP" mode annunciator shows in cyan (yellow in slaved mode) at the left end of the half-range arc.

Setting the WXP MODE knob to the OFF position, or detection of invalid data or loss of signal from the WXP, removes the solid half-range arc from the display, sets the display range to 300 nmi, and shows the radar system mode annunciator "OFF".

Detection of a fault in the radar system shows the yellow annunciator "FAULT" flashing alternately with the selected weather radar mode annunciator. The fault annunciator has priority over any selected weather radar mode. If the fault is in the form of an interrupted communication link between the RTA (receiver/transmitter/antenna) and the WXP, the "FAULT" annunciator shows nonflashing in cyan. Transient faults can be cleared by momentarily setting the WXP to the STBY mode, then re-setting it to the desired operating mode. If the annunciator "FAULT" remains on the display after the reset, then a malfunction of the weather radar system is indicated, and the radar system should be turned off (WXP mode knob set to OFF).

The NAV display mode can also be turned on with the RDR display mode to show a composite display of both radar data and navigation information on the display.

**Example of NAV and RDR Composite Display Mode** 

#### <span id="page-83-0"></span>Navigation (NAV) Display Mode

#### **Display Features and Elements**

The following paragraphs describe the features and display elements that are the same in all NAV mode map displays. Following them are descriptions of the NAV MENU display page and features and display elements specific to each of four NAV mode map displays.

Push the NAV button to alternately turn on and off the navigation display mode on the MFD. In the NAV display mode, the display mode annunciator "NAV" shows in green in the upper left corner of the display. One of four map displays, selected from a NAV menu, shows on the MFD in the NAV mode. The four maps are:

- · "heading up"
- "north up with aircraft centered"
- "north up maximum view"
- and "map plan" (available only in installations with a compatible LNAV).

In addition to the dedicated NAV display mode, a composite display mode of both the NAV and RDR modes can show on the MFD. When the MFD is in the NAV and RDR composite display mode, only the "heading up" map shows for the NAV portion of the display and the display range is controlled by the WXP. Range is always controlled by the WXP when the RDR display mode shows on the MFD.

Line key annunciators show adjacent to the line keys along the right side of the display. Push the line key with the green boxed arrow shown next to it (top line key), to select the NAV menu. Push the line key with the "IDNT>" annunciator shown next to it (second line key from the top), to turn on and off the display of airport and navaid identifiers. The IDNT annunciator shows only when airport and/or navaids are set, in the NAV menu, to show on the display. When the joystick is moved, the annunciator "ENTER" shows next to the third line key. Push the ENTER key to add a joystick positioned waypoint to a flight plan string from a compatible LNAV. Push the line key with the "CAT II>" annunciator next to it (bottom line key) to change the MFD directly to the CAT II checklist with a "yellow" condition of the extended data in the RMT display mode. The CAT II> annunciator shows on the display only when the system is set for for a CAT II approach. Push the NAV button to return to the previously selected display mode.

Display range is set with the line advance ( $\blacktriangledown$ ) and line reverse ( $\blacktriangle$ ) buttons at the bottom of the MFD in all of the dedicated NAV mode map displays. The range arc and/or rings show as dashed cyan arcs or rings. If the RDR mode is selected to show on the display with the NAV mode (composite display mode), the display range is controlled by the WXP and the half-range arc shows as a solid cyan arc. Range is always controlled by the WXP when the RDR mode shows on the display.

When VOR stations are selected, in the NAV menu, they show on the display as octagon-shaped symbols in the proper range and bearing position with respect to the aircraft heading and the selected display range. A course line is drawn through the selected VOR station symbol and its orientation is controlled by the CRS knob on the corresponding CHP. If DCP control is transferred, or if the DCP course is allocated to another navigation sensor, the VOR course line on the MFD is removed from the display. In installations with later versions of DPU and MPU, the VOR1 course line shows on the MFD only when it is selected as the active or preset navigation sensor on the pilot's EHSI and the VOR2 course line shows only when it is selected as the active or preset navigation sensor on the copilot's EHSI.

Course lines show as a solid line on the "to" side of the VOR and as a dashed line on the "from" side. The VOR "ident" and a numerical course read-out show in the lower left corner for VOR1 and in the lower right for VOR2. Left side (pilot's) VORs show in green and right side (copilot's) VORs show in yellow. If a VOR symbol is beyond the selected display range (off scale), an arrow pointing toward the station and the station's "ident" show on the course line. If a VOR's paired DME is placed in hold or fails, the VOR symbol and DME ident are removed from the display and the sensor annunciator shows course if available, otherwise bearing is shown.

When a localizer frequency is tuned, no symbol shows on the display for the station and the sensor annunciator shows LOC1 or LOC2 and the selected course. The colors for these annunciators are green for the left side (pilot's) and yellow for the right side (copilot's).

**NAV Mode Heading Up Display** 

**Electronic Flight Instrument System** 

TCN and RNV stations show similarly to VORs except they do not show identifiers. RNVs show as a star-shaped symbol and TCNs show as a VORTAC symbol. RNV and TCN sensors are selected from the LNV1/LNV2 line of the MFD NAV menu when those sensors are available.

A selected LNAV flight plan string shows on the MFD as star-shaped waypoint symbols with track lines in the proper range and bearing positions. (Some LNAV installations may show waypoint symbols as star-shaped, VORTAC, or airports.) A total of either 3, 5, or 6 waypoints can show on the display. The maximum number is determined by the LNAV type and the aircraft wiring. When turned on, identifiers show next to the LNAV waypoints. For LNAV installations that show a maximum of 3 waypoints, the identifiers show as "WPT #" (# is replaced with the number 1, 2, or 3). For LNAV installations that show a maximum of 5 waypoints, alphanumeric idents show next to the waypoint symbols. For LNAV installations that show a maximum of 6 waypoints, the identifiers show as "TO+#" (# is replaced with the number 1, 2, 3, 4, 5, or 6).

#### NOTE

Airport symbols that may show on the display (in installations with a compatible LNAV system) are for display purposes only and do not in any way represent the actual runway headings or the orientation of the airport.

The LNAV sensor annunciator, a numeric course read-out for the next "to" waypoint, and the waypoint's ident for the pilot's side LNAV, show in the lower left corner below the VOR1 course annunciation. Similarly, the copilot's side LNAV sensor annunciator, course read-out, and waypoint ident show below the VOR2 course annunciation. LNV1 (pilot's) data shows in white and LNV2 (copilot's) data shows in cyan. If the next waypoint is off screen, the course line shows on the display with an arrow showing the direction to that station.

When the distance to a waypoint on the flight plan is greater than the selected range of the display (600 nmi), a line is drawn as if the waypoint was off screen. Breaks in the flight plan can be displayed as can a course line without a waypoint at its end if the information is available from a compatible LNAV. The "to" waypoint symbol flashes to indicate waypoint alert from a compatible LNAV.

In system installations with a compatible LNAV, up to seven each of background NAVAIDS and closest airports show on the display when selected in the NAV menu. The alphanumeric idents for these symbols can be turned on or off by alternately pushing the second line key with the "IDENT" annunciation shown next to it.

To position a waypoint for use in a flight plan string of a compatible LNAV system, select the LNAV system to show on the display (from the NAV menu) and use the joystick to position a waypoint on the display. As soon as the joystick is moved, the third line key (from the top) shows the annunciator "ENTER"; a waypoint shows at the airplane symbol moving in the direction commanded by the joystick; and a numerical heading/distance read-out for the waypoints position shows in the left center of the display. The waypoint, "ENTER" annunciator, and data read-out stay on the display for up to 30 seconds after the waypoint is last moved and then turn off. Push the ENTER line key any time prior to the 30-second time-out to load the waypoint into the compatible LNAV system.

A magenta selected heading display (cursor, selected heading line, and digital selected heading read-out) show on the MFD when selected in the NAV menu. The position of the selected heading cursor and line is controlled by the on-side CHP HDG knob and PUSH SYNC button.

The heading type and sensor number ("MAG#", "TRU#", or "DG#") are annunciated to the right of the digital heading read-out in the NAV mode heading up map and to the right of the N in all other NAV maps. If any selected navigation sensor is incompatible with the type of heading shown on the display (magnetic or true), the NAV sensor annunciator flashes until a compatible selection is made. Installations with later versions of MPU and DPU, show the "MAG#" annunciator only when both the pilot and copilot select the same magnetic sensor on both sides. When this occurs, the "MAG#" annunciator shows in yellow on both sides.

#### **NAV MENU Display**

The NAV menu is used for selecting display modes and various navigation sensors and features that show on the MFD. To show the NAV menu on the display, set the MFD to show the NAV display mode (either the dedicated NAV mode or the composite mode of RDR and NAV) and then push the top line key with the green boxed arrow annunciator. The NAV menu shows the display mode annunciators "<RADAR", "<HEADING UP", "<NORTH UP-A/C CNTR", "<NORTH UP-MAX VIEW" and "<EMERGENCY" on the left side of the display and NAV display mode feature annunciators "VOR1/VOR2>", "LRN1/LRN2>", "NAVAIDS  $\leftrightarrow$ #>", "AIRPORTS \$#>", and " $\Box$  HDG \$\dagger\$" on the right side of the display (# = numbers from 0-7). Each of the annunciators points to its associated button or line key. Annunciators LRN1 and LRN2 are examples only. The actual annunciators shown in a given installation depends on the equipment installed in the aircraft and the aircraft wiring. The annunciators available in no particular order are:

- LNV1, LNV2, or LNV3
- RNV1, RNV2, or RNV3
- FMS1, FMS2, or FMS3
- TCN1, TCN2, or TCN3
- INS1, INS2, or INS3
- VLF1, VLF2, or VLF3
- GPS1, GPS2, or GPS3
- LRN1, LRN2, or LRN3

Push a button or line key to select a desired display mode or NAV display feature. Annunciators for selected modes and features show in green and unselected show in white. For the "VOR1/VOR2>", "LRN1/LRN2>" line keys, each push of the key cycles through a selection sequence of: number 1 sensor, number 2 sensor, number 1 and 2 sensors, and no sensors. For the "NAVAIDS ↔#>", "AIRPORTS ↓#>", and "□□ HDG ↓" line keys, each push alternately turns on and off the display of the associated NAV data. Any combination of sensors and NAV data from the right side of the NAV menu can be selected to show on the display. For selection of a display mode shown on the left side of the NAV menu, push the button for the desired display mode. The MFD changes directly to that display mode. Only one display mode can be selected from the NAV menu at any time.

In the NAV menu the joystick selects the number of navaids and airports that show on the MFD in the NAV display mode. The ↔ portion of the navaids annunciator indicates to move the joystick left or right to set the number of navaids that can show on the display. The ‡ portion of the airports annunciator indicates to move the joystick up or down to set the number of airports that can show on the display. The number following the arrows is the current setting. From a compatible LNAV up to seven navaids and seven airports can show on the MFD in the NAV display mode. Refer to the preceding note regarding the airport symbols. If the LNAV is not compatible, the "NAVAIDS ↔#>" and "AIRPORTS ‡#>" annunciators do not show in the NAV menu.

#### NOTE

Airport symbols that may show on the display (in installations with a compatible LNAV system) are for display purposes only and *do not* in any way represent the actual runway headings or the orientation of the airport.

Push the NAV menu "□□ HDG ↓" (CLR) button at the bottom of the MFD, to alternately turn on and off the magenta selected heading line, heading cursor, and numerical selected heading read-out shown in the NAV and RDR display modes.

Push the NAV menu "RADAR" button to change the MFD directly to the composite RDR and NAV "heading up" display mode. Turning off the RDR mode with the RDR button changes the MFD back to the NAV mode showing the last selected map. To turn off the RDR mode from the NAV menu push any NAV map display button.

Push the NAV menu "EMERGENCY" button to change the MFD directly to the emergency page data checklist. Push the NAV button to return the display to the previously selected mode.

**NAV Menu Display Mode** 

#### Heading Up Map Display

#### NOTE

Only the display features and elements unique to the heading up map are described in this section. Features and elements common to all map displays are described in the beginning of the NAV display format section.

Push the "HEADING UP" button in the NAV menu, to show the NAV mode heading up map display.

In the NAV mode "heading up" map, the display shows an aircraft symbol at the bottom center of the display; a digital heading read-out at the top center of the display; and two dashed range arcs, one at full-range (top of the display) and one at half-range (middle of the display). Range for each arc is annunciated at the right end of each arc and the full range arc annunciator is the selected display range.

Push the RDR button to show weather radar with the NAV mode heading up map (RDR and NAV composite display mode) in the form selected on the WXP. When the RDR mode shows on the display, with or without the NAV mode, the half-range arc shows as a solid arc. Anytime the RDR mode shows on the MFD, it shows in the heading up map. If any other NAV mode map is showing on the display, it is changed to the heading up map when RDR is selected. Turning off the RDR display mode returns the display to the previously selected NAV map.

When the NAV and RDR modes are turned off and no other mode is selected the MFD shows only the heading read-out; dashed full range arc; the weather radar operating mode annunciator in the upper left corner; and if turned on in the NAV menu, the magenta selected heading cursor, line, and the read-out in the upper right corner of the display.

**NAV Mode Heading Up Map Display** 

**RDR and NAV Mode Composite Display** 

#### North Up With Aircraft Centered Map Display

#### NOTE

Only the display features and elements unique to the "north up with aircraft centered" map are described in this section. Features and elements common to all map displays are described in the beginning of the NAV display format section.

Push the "NORTH UP-A/C CNTR" button in the NAV menu, to show the NAV mode "north up with aircraft centered" map display.

In the NAV mode "north up with aircraft centered" map, the display shows a white aircraft symbol in the center surrounded by two dashed cyan range rings; the letter N with an arrow (↑) below it pointing at the top center of the display; and a numeric heading read-out in the upper right corner of the display. The top center of the display is always true or magnetic (if a magnetic compass is selected) north. The white aircraft symbol in the center of the display rotates as the heading of the aircraft changes. The nose of the aircraft symbol and the numeric heading read-out show the aircraft's heading. Waypoints, navaids, and airports move around the display to maintain the proper range and bearing position with respect to the aircraft symbol and selected display range. The inner dashed range ring is the half-range ring and the outer ring is the full-range ring. Annunciators centered on the range rings on the right side of the display show the range for each ring.

Push the RDR button to show the RDR mode with the NAV mode (composite mode) on the MFD. The display changes to the "heading up" map with weather radar information shown in the form selected on the WXP. A second push of the RDR button turns off the RDR mode and returns the MFD to the previously selected "north up with aircraft centered" map.

When the NAV and RDR modes are turned off and no other mode is selected the MFD shows only the north up N and arrow; the heading read-out; the dashed full range arc; the weather radar operating mode annunciator in the upper left corner; and if turned on in the NAV menu, the magenta selected heading cursor, line, and the read-out in the upper right corner of the display.

**NAV Mode North Up Aircraft Centered Map Display** 

#### North Up Maximum View Map Display

#### NOTE

Only the display features and elements unique to the "north up maximum view" map are described in this section. Features and elements common to all map displays are described in the beginning of the NAV display format section.

Push the "NORTH UP-MAX VIEW" button in the NAV menu, to show the NAV mode "north up maximum view" map display.

In the NAV mode "north up-maximum view" map, the display shows a white aircraft symbol; two cyan dashed range arcs one for half-range and one for full-range; range annunciators on each range arc; the letter N with an arrow (↑) below it pointing at the top center of the display; and a numeric heading read-out in the upper right corner of the display. True or magnetic (if a magnetic compass is selected) north is always at the top center of the display. The aircraft symbol is positioned on an imaginary circle near the edge of the display so that the greatest amount of display area is shown in front of the aircraft. Orientation of the aircraft symbol is such that it moves around the edge of the display on the imaginary circle so that current track of the aircraft always shows the nose of the aircraft symbol pointing toward the center of the display. Waypoints, navaids, and airports also move around the display to maintain the proper bearing and range position with respect to the aircraft symbol and selected display range. The range arcs are always centered on the aircraft symbol.

Push the RDR button to show the RDR mode with the NAV mode (composite mode) on the MFD. The display changes to the "heading up" map with weather radar information shown in the form selected on the WXP. A second push of the RDR button turns off the RDR mode and returns the MFD to the previously selected "north up maximum view" map.

When the NAV and RDR modes are turned off and no other mode is selected the MFD shows only the north up N and arrow; the heading read-out; the dashed full range arc; the weather radar operating mode annunciator in the upper left corner; and if turned on in the NAV menu, the magenta selected heading cursor, line, and the read-out in the upper right corner of the display.

**NAV Mode North Up Maximum View Map Display** 

#### <span id="page-95-0"></span>Plan View Map Display

#### NOTE

Only the display features and elements unique to the "plan view" map are described in this section. Features and elements common to all map displays are described in the beginning of the NAV display format section.

Select the plan view display mode on a compatible LNAV and set the MFD to the NAV display mode (NAV button) to show the "plan view" map.

The information shown on the "plan view" map is centered on a waypoint that is received from a compatible LNAV. Only parameters from the LNAV and the available display features (waypoints, NAVAIDS, and airports) selectable from the right side of the NAV menu show on the display. In dual LNAV installations, if both LNAVs are selected on the MFD, only one plan view shows on the display at a time (pilot's side LNAV has priority).

In the NAV mode "plan view" map, the display shows two dashed cyan range rings centered around a waypoint in the center of the display; the letter N with an arrow (↑) below it pointing at the top center of the display; and a numeric heading read-out in the upper right corner of the display. The inner dashed range ring is the half-range ring and the outer ring is the full-range ring. Annunciators centered on the range rings on the right side of the display show the range for each ring. True north (magnetic north is not used in the "plan view" map) is always at the top center of the display. A white aircraft symbol shows on the display only when the aircraft's position is within the selected display range with respect to the waypoint at the center of the display. Orientation of the aircraft symbol is the same as the aircraft's track with respect to the waypoint at the center of the display. The airplane symbol moves around or across the display following the aircraft's progress with respect to the waypoint at the center of the display. VOR, TCN, and RNV stations do not show on the display in the plan view format unless they are part of the LNAV data. VOR, TCN, and RNVs cannot be selected in the NAV menu.

Joystick waypoint entry operation is limited in the plan view. If the aircraft symbol is beyond the selected display range and not shown on the display, the joystick is disabled. When the aircraft symbol is within the selected display range and shows on the display, then the joystick operates normally as previously described.

Push the RDR button to show the RDR mode with the NAV mode (composite mode) on the MFD. The display changes to the "heading up" map with weather radar information shown in the form selected on the WXP. A second push of the RDR button turns off the RDR mode and returns the MFD to the previously selected "plan view" map display.

**LNAV Plan View Map Display** 



---

[🡅](./toc.md) ·•⦁•· [🡄 COMPARATORS, SECTOR FORMAT](./COMPARATORS-SECTOR-FORMAT.md) ·•⦁•· [Remote Data (RMT) Display Mode 🡆](./Remote-Data-RMT-Display-Mode.md)