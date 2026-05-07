# <span id="page-32-0"></span>EFIS-86C(14) Display Formats

### **EADI Display Formats**

This section describes the functions of the EADI displays that are used in the EFIS-86C Electronic Flight Instrument System. The EADI has one basic format and shows the familiar attitude display with lateral and vertical computed steering signals needed to give the commands to intercept and maintain a desired flight path. Also presented are FCS mode annunciation, autopilot engage status, attitude comparator warnings and decision height set. Other parameters are displayed as a function of pilot selection or operational mode. The EADI provides the following display information:

- Attitude display and sensor annunciation (ATT1 or ATT2, ATT3 or ATT4)
- Attitude comparator warnings
- Flight director commands and FCS mode annunciation
- · Autopilot/yaw damper engage status
- Primary vertical deviation from GS, MGP, PGS (LNAV pseudo glideslope), FGS (LNAV controlled glideslope) or VNAV sensors
- Second course related vertical deviation from PGS or FGS
- Lateral deviation from VOR, LOC, PLOC (LNAV pseudo localizer), FLOC (LNAV controlled localizer), MAZ, TCN, or LNAV (FMS, RNV, LRN, etc) sensors
- LOC/GS or MAZ/MGP deviation displayed only when a LOC/MLS frequency is tuned and not in back LOC/MLS. LOC/MAZ deviation is displayed in back LOC/MAZ mode, GS/MGP is not displayed
- Second course related lateral deviation from PLOC or FLOC
- LNAV (GPS) "SCALING" annunciation for GPS vertical and lateral deviation data
- LNAV APPR mode that allows a compatible LNAV to control pitch commands (if available) and bank commands during approach
- Pseudo APPR mode that allows a compatible LNAV to control pseudo LOC and GS deviations
- CAT II excessive deviation and comparator warning for ILS, indicated airspeed, and radio altitude
- · Radio altitude is displayed only when the radio altimeter system is within range or in self-test mode
- · Decision height set and DH annunciation
- Air data information (IAS, airspeed trend, reference airspeed bugs, MACH)
- Speed deviation from a fast/slow or an angle-of-attack system
- Marker beacon
- Flags

In addition, interconnect wiring straps allow several EADI format changes to be made. These are:

- V-bar commands or cross-pointer commands (and style of airplane symbol)
- FCS lateral modes may be shown on the left and vertical on the right, or they may be swapped (lateral
  on the right, vertical on the left)
- · Inhibit speed deviation display
- · Rising runway symbol or no rising runway symbol
- Autopilot mistrim annunciator display
- Composite format or no composite format in reversionary mode
- Inhibit display of digital air data parameters



---

[🡅](./toc.md) ·•⦁•· [🡄 Radar and Navigation) Button](./Radar-and-Navigation-Button.md) ·•⦁•· [**EADI WITH V-BARS** 🡆](./EADI-WITH-V-BARS.md)