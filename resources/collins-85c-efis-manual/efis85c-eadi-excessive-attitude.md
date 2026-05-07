# **EADI Excessive Attitude Display**

Excessive attitude is when the pitch attitude exceeds 30 degrees up or 20 degrees down, or when the roll attitude exceeds 65 degrees right or left. In the extreme pitch attitudes, a portion of the blue (sky) or brown (ground) area is retained in view to aid in interpretation of pitch attitude. The pitch markings continue to move to provide accurate pitch information. When in an excessive attitude condition, all information except the airplane symbol, attitude display, and the IAS display is removed from the EADI. All information is restored to the EADI after the pitch attitude decreases to +25 degrees (pitch up) or increases to -15 degrees (pitch down), or after the roll attitude decreases to ±60 degrees.

If the excessive attitude condition is due to excessive pitch, then upward or downward pointing (as appropriate) excessive pitch red chevrons pop into view as part of the pitch display. These chevrons are out of view until the extreme pitch attitude is entered at pitch angle greater than 30 degrees pitch up, or 20 degrees pitch down. The red upward or downward pointing chevrons indicate which direction (up or down) is required to correct for the excessive pitch attitude. In the EFIS-86C system, there are two downward pointing chevrons for excessive pitch up attitudes, and three upward pointing chevrons for excessive pitch down attitudes. If the aircraft passes through the vertical, the attitude display switches 180 degrees in the roll axis and continues to provide the correct ground-sky reference during the inverted portion of the maneuver.

### <span id="page-46-0"></span>**EADI Warning Flags**

#### NOTE

Unless otherwise noted, when an EADI warning flag appears, it flashes for 10 seconds and then becomes steady. The flashing can be eliminated by pushing the master warn reset.

Attitude Flag—If a failure of the attitude sensor is detected, the pitch scale, roll scale, roll pointer, sky/ground display, and command bars disappear and a red box with the letters 'ATT' inscribed appears above the airplane symbol. The ATT flag remains in view until an alternate sensor is selected or until the fault is cleared.

Drive Unit (MPU or DPU) Flag—If an MPU or DPU fails, the non-flashing letters 'DRV' appear in a red box centered on the display. Nothing is removed from the EADI when a DRV flag appears.

#### **Vertical Deviation Flags**

primary vertical deviation sensor flags—A detected failure of any of the primary vertical deviation sensors removes the vertical deviation scale and pointer from view and replaces them with the following flags. If a failure of the glideslope or MLS glidepath receiver is detected, a red box with the letters 'GS' or 'MGP' inscribed appears. If an LNAV failure is detected while it is being used for LNAV pseudo or controlled glideslope, a red box with the letters 'PGS' or 'FGS' appears. If a VNAV failure is detected, a red box with the letters 'VNV' appears.

- second course related vertical deviation flags—In -001 version DPU and MPU, if an LNAV failure is detected while it is being used for second course related LNAV pseduo or controlled glideslope, the cyan 'PGS' or 'FGS' annunciations are replaced by a red box with the letters 'PGS' or 'FGS' inscribed. For -002 and later versions DPU/MPU, the EADI does not show vertical second course sensors or the associated flags.
- Radio Altimeter Flag—If a failure of the radio altimeter system is detected, the radio altitude display is replaced by a red box with the letters 'RA' inscribed. The DH set display and the DH annunciator are also removed from view.
- Display Control Panel Flag—If a failure of the display control panel occurs, a red box with the letters 'CTL' inscribed appears in the lower right corner replacing the DH set display. Flight control system mode annunciators that are derived from the DCP are also removed from view. The EFIS-86C continues to operate in the mode that was active prior to the DCP failure.

#### **Lateral Deviation Flag**

- primary lateral deviation sensor flags—A detected failure of any of the primary vertical deviation sensors removes the vertical deviation scale and pointer from view and replaces them with the following flags. If a failure of the localizer or MLS azimuth receiver is detected, a red box with the letters 'LOC' or 'MAZ' inscribed appears. If an LNAV failure is detected while is is being used for LNAV pseudo or controlled localizer, a red box with the letters 'PLOC' or 'FLOC' appears. For the remaining sensors, a red box with the letters 'VOR', 'RNV', or 'LRN' appears.
- second course related lateral deviation flag—For the -001 version DPU and MPU, if an LNAV failure is detected while it is being used for second course related LNAV pseudo or controlled localizer, the cyan 'PLOC' (LNAV pseudo localizer) and FLOC (LNAV controlled localizer) are replaced by a red box with the letters 'PLOC' and 'FLOC' inscribed. The -002 and later DPU/MPU versions second course related lateral deviation sensors do *not* show on the EADI. The second course sensors show only on the EHSI.
- Accelerometer/Mach Flag—If an accelerometer failure is detected, the digital readout is replaced by a red box with the letters 'ACC' inscribed. This flag can only be displayed when the aircraft is on the ground. For a Mach flag, the Mach digits are blanked.
- Cross-Side Data Flag—If a failure of the cross-side data bus occurs, a red box with the letters 'XDTA' inscribed appears in the lower left of the EADI. Data from the cross-side sensors is no longer available, and any display driven by cross-side data is flagged.
- **Speed Deviation Flags**—If the speed deviation is digital air data based and a failure is detected on the digital air data or referenced airspeed bus, the fast/slow scale, pointer, and digital readout are removed from view.
  - If an AOA failure is detected when displaying AOA based speed deviation, the speed deviation scale and pointer disappear and the letters 'AOA' that are beneath the scale turn red and are boxed.
  - If a detected failure of an analog air data based speed deviation input occurs, the speed deviation scale and pointer disappear and the letters 'SPD' appear at the left center of the display in red and are boxed.

- Flight Director Flag—If the flight director system fails, the command bars disappear and a red box with the letters 'FD' inscribed appears at the lower left of the aircraft symbol.
- Indicated Airspeed Flag—If a failure of the digital air data system is detected, the IAS display in the left center of the EADI is replaced by a red box with the letters 'IAS' inscribed. The IAS scale and pointers, reference airspeed pointer and display, acceleration trend vector, and Vmo display are removed from view.

### **EADI Comparators and Master Warn**

Comparator monitoring is performed in each DPU and MPU in the EFIS-86C system. On-side data is read and stored by each DPU and the MPU. Each DPU sends its information to the cross-side DPU so that each of the processors has the information required to perform the comparison function. When the MPU is driving the EADI, it provides the comparator function in place of the failed DPU.

#### **EADI Comparator Warnings**

#### NOTE

When an EADI comparator warning occurs, it appears nonflashing. The messages disappear when the external comparator reset switch is actuated, if the comparator error is no longer present.

In addition to the comparator warnings displayed on the EADI, the EFIS-86C provides individual attitude and ILS comparison outputs from each DPU and MPU when in drive transfer. These comparator warning outputs are used to turn on remote mounted attitude and ILS annunciators (not part of the EFIS-86C system).

- Comparator Reset—Momentarily actuating an installer supplied comparator reset switch turns off the EADI comparator warnings and the external comparator warning flag annunciator(s). If the condition causing the compare error is no longer present, the EADI comparator warning display and the external comparator warning annunciator(s) remain off when the comparator reset switch is released. If the warn condition is still present when the comparator reset switch is released, the EADI comparator warning display and the external comparator warning annunciator(s) turn on again, but the master warn annunciator does not.
- Master Warn and Master Warn Reset—A master warn which serves as an overall compare function output is provided from each DPU and from the MPU when in drive transfer. These outputs are used to turn on installer supplied master warning annunciators (not part of the EFIS-86C system).

Momentarily actuating an installer supplied master warn reset switch stops the flashing of the EADI comparators and of the remote mounted attitude and ILS comparators, and turns off the master warning annunciator.

EADI DISPLAY FORMATS

### Pitch and Roll Attitude Comparators

Enable Logic—The pitch and roll attitude comparators are enabled full time unless:

- · Either side has an ATT flag
- · A cross-side data failure is detected

Comparison Limits—An attitude comparator warning is annunciated when:

| GLIDESLOPE CAPTURED | SENSOR SOURCE TYPE<br>DIFFERENCE | PITCH OR ROLL<br>DIFFERENCE MORE<br>THAN |
|---------------------|----------------------------------|------------------------------------------|
| Yes                 | Yes                              | 5°                                       |
| Yes                 | No                               | <b>3°</b>                                |
| No                  | Yes                              | . 6°                                     |
| No                  | No                               | 4°                                       |

Annunciation—When a pitch or roll attitude comparator warning is detected, the letters 'ATT', boxed and in yellow, appear above the aircraft symbol. The external 'PITCH' and/or 'ROLL' comparator annunciators (if installed) and the master warn comparator also turn on.

#### <span id="page-50-0"></span>**IAS Comparator**

Enable Logic—A comparison of the two indicated airspeeds is made when:

- · Cross-side data is valid
- Both air data computers are valid
- IAS scale is displayed
- Either IAS 90 knots

Comparison Limits—A comparator warning occurs when the enable conditions are met and the two indicated airspeeds differ by more than 10 knots.

Annunciation—When an indicated airspeed comparator warning is detected, the letters 'IAS', boxed and in yellow, appear to the left of the aircraft symbol. The external master warn comparator (if installed) also turns on.

### **ILS Localizer Comparator**

Enable Logic—A comparison of the two localizer deviations is made when:

- On-side DCP is valid and its active course is VOR/LOC
- · Cross-side data is valid
- Both localizer signals tuned and valid for at least 15 seconds (localizer tuned and valid on both VORs)
- · Alternate DCP is not selected
- Glideslope is captured on the side that the autopilot is coupled to

Comparison Limits—A comparator warning occurs when the enable conditions are met and the two localizer deviations differ by more than 30 microamperes + 1/8 of the absolute value of deviation 1 + deviation 2.

Annunciation—When a localizer comparator warning is detected, a yellow box with the letters 'LOC' inscribed appear above the lateral deviation scale. The external 'ILS' comparator annunciator (if installed) and the master warn comparator also turn on.

#### **ILS Glideslope Comparator**

**Enable Logic—**A comparison of the two glideslope deviations is made when:

- Both DCPs are valid and their active courses are VOR/LOC
- · Cross-side data is valid
- Both glideslope valid and both localizer signals tuned for at least 15 seconds
- · Alternate DCP is not selected
- · Both sides not in back course
- Glideslope is captured on the side that the autopilot is coupled to

Comparison Limits—A comparator warning occurs when the enable conditions are met and the two glideslope deviations differ by more than 40 microamperes + 1/8 of the absolute value of deviation 1 + deviation 2.

Annunciation—When a glideslope comparator warning is detected, a yellow box with the letters 'GS' inscribed appear near the center of the vertical deviation scale. The external 'ILS' comparator annunciator (if installed) and the master warn comparator also turn on.



---

[🡅](./toc.md) ·•⦁•· [🡄 DESCRIPTION OF VERTICAL MODES](./DESCRIPTION-OF-VERTICAL-MODES.md) ·•⦁•· [Radio Altitude Comparator 🡆](./Radio-Altitude-Comparator.md)