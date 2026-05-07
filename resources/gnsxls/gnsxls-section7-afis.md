# **SECTION 7 AFIS**

## **AIRBORNE FLIGHT INFORMATION SYSTEM**

## **AND**

## **SATELLITE DATA COMMUNICATIONS SYSTEM**

This section applies only to aircraft equipped with an AFIS system.

The purpose of this section is to acquaint users of AFIS Flight Plan and Weather Advisory Services with the equipment, its capabilities, and its operation. AFIS services are ADVISORY only, as they contain elements provided by the National Weather Service and information supplied by the pilot. Therefore, it is the responsibility of the pilot in command to exercise reasonable and prudent judgment in the use of these ADVISORY services.

**THIS PAGE INTENTIONALLY LEFT BLANK**

## **DESCRIPTION**

AFIS is an Airborne Flight Information System that provides integrated flight planning and performance management interfaces to the GNS-XLS Nav Management System.

*NOTE: The displays in this section apply to installations with MOD 11 or later DMU.*

These interfaces consist of three major capabilities:

- 1. Access to ground based Global Data Center computers from a Personal Computer for the purpose of generating or retrieving performance optimized flight plans and current aviation weather;
- 2. Digital transfer of AFIS Flight Plan and weather data into the Nav Management System for display and performance monitoring on the GNS-XLS Color CDU; and
- 3. Air/ground computer link interfacing the GNS-XLS Nav Management System to the ground based Global Data Center computers for the purpose of providing enroute flight plan, weather, performance updates, requesting pre-departure clearance, and sending or receiving messages.

AFIS interfaces with ARINC, SITA and AVICOM VHF networks and the Inmarsat satellite network to provide a communication link between the aircraft and the Global Data Center. ARINC provides coverage within the continental United States, Hawaii, Alaska, the Aleutians, Guam, Saipan, Mexico, Puerto Rico, and parts of Canada; SITA covers Europe, the South Pacific, Southeast Asia, the Caribbean, and South and Central America; and AVICOM covers Japan. In most areas while using the VHF networks, data link coverage is excellent above Flight Level 200, but deteriorates below this flight level. Satellite data link coverage is excellent both on the ground and in-flight between 70° North and 70° South.

Many variables, including the amount of processing time and the length of the message, effect the turnaround time for information. Depending on the nature of the update request, the pilot should expect a turnaround time of approximately five minutes when using the VHF network and twelve minutes when using the satellite network.

**AFIS** consists of the following components: Global Data Center (GDC), Data Transfer Unit (DTU), Data Management Unit (DMU), and Antenna Switching Unit (ASU).

## **GLOBAL DATA CENTER (GDC)**

The Global Data Center (GDC) is a ground based computer facility built and operated by Honeywel for the purpose of providing flight planning, aviation weather, and message forwarding services to AFIS operators on a subscription basis. The GDC communicates with the operator via data quality telephone lines to a Personal Computer as well as through the ACARS and satellite networks directly to the aircraft in flight.

## **DATA TRANSFER UNIT (DTU)**

The Data Transfer Unit (DTU) is a 3.5 inch micro floppy disk drive mounted in the cockpit. Once the GNS-XLS is switched on and the disk inserted in the DTU, the AFIS Flight Plan and weather data are transferred to and stored in the Data Management Unit.

## **DATA MANAGEMENT UNIT (DMU)**

The Data Management Unit (DMU) computer formats the disk information and presents it to the GNS-XLS for display on the CDU.

The DMU also incorporates a data quality VHF transceiver. This radio is tuned automatically by the DMU computer to the appropriate ground station for the purpose of transmitting data to and receiving data from the Global Data Center while in flight.

## **ANTENNA SWITCHING UNIT (ASU)**

The Antenna Switching Unit (ASU) is required for those installations where the DMU transceiver shares an existing VHF communications antenna. The ASU switches the transmit side of the antenna between the DMU data transmitter and the VHF voice transmitter.

During power up, the ASU defaults to the voice transmitter, if AFIS is configured for a shared antenna. Selecting the AFIS annunciator on the instrument panel switches the transmit side of the antenna to the DMU data transmitter. Selecting the annunciator again, or pressing the "push to talk" button on the VHF communications radio switches the transmit side of the antenna back to the voice transmitter.

If AFIS is configured for non-shared antenna or there is no configuration module, during power up the system will assume an antenna is dedicated to AFIS.

The Satellite Data Communications System consists of the following components: Satellite Communications Unit (SCU), High Power Amplifier/ Low Noise Amplifier (HPA/LNA) and Satellite Antenna.

## **SATELLITE COMMUNICATIONS UNIT (SCU)**

The Satellite Communications Unit (SCU) incorporates the satellite transceiver and instruction for transmitting to and receiving data from the satellite network. The SCU also contains information to allow it to tune the appropriate satellite operating region automatically and to the appropriate ground stations.

## **HIGH POWER AMPLIFIER/ LOW NOISE AMPLIFIER (HPA/LNA)**

The High Power Amplifier/ Low Noise Amplifier (HPA/LNA) amplifies transmitted and received information while minimizing noise.

## **SATELLITE ANTENNA**

The antenna is designed to meet the Inmarsat system specification.

## **REMOTE PROCESSING UNIT (RPU)**

The Remote Processing Unit (RPU) supplies AFIS™ weather Graphical Data to the GNS-XLS.

## **PAGE DISPLAY DEFINITIONS**

## **AFIS FLIGHT PLAN LIST PAGE**

If the GNS-XLS is configured for AFIS, this page appears directly after the Initialization Page. The DTU reads the inserted disk and displays one of the following messages:

## **NO AFIS FLT PLANS ON**

**DISK:** There are no AFIS Flight Plans stored on the disk. (Figure 7-1)

**NO DISK:** Either no disk was inserted into the DTU prior to power up or the DTU cannot read the disk.

**READING DISK:** The DTU is transferring data from the disk to the DMU.

*Figure 7-1*

**AIRCRAFT TYPE:** The Global designated aircraft type as transferred from the disk or obtained by an Update or Recall procedure.

*NOTE: Once the system is initialized, the page appears between the*

*Active Flight Plan Page and the first GNS-XLS FLIGHT PLAN LIST Page.*

**AFIS FLT PLAN LIST:** A list of AFIS generated Flight Plan origin/destination identifiers with date of issue. (Figure 7-2)

*NOTE: Additional pages can be accessed when more than 6 Flight Plans are listed by DEPRESSING the FPL Key to access page.*

*Figure 7-2*

**LOADING FLIGHT PLAN:** The system is loading a selected AFIS Flight Plan.

**REPLACE ACTIVE FPL?:** Allows a selected AFIS Flight Plan to replace an existing Active Flight Plan.

**UPDA-XXXX:** (Where XXXX is an ident) Indicates a Flight Plan Update for an active Flight Plan has occurred.

## **FLIGHT PLAN PROGRESS (NAVIGATION PAGE 5)**

**HEC:KVNY:** Current FROM and TO waypoints. (Figure 7- 3) The FROM waypoint can be replaced by **DIR TO** for DIRECT TO.

**FL:** AFIS planned flight level for leg being flown.

*NOTE: Field is dashes when aircraft is projected to be climbing or descending.*

HEC:KVNY FL390 PLAN ACT F REM2150 3380 FF P/E 625 0 ETA 00:06 18:52 NAVIGATION 5/5 <sup>&</sup>lt;

*Figure 7-3*

**PLAN:** Planned

This column is AFIS planned data either transferred from the disk or received via the data link.

*NOTE: Planned fields become dashes when no planned data is available for the current leg.*

(Figure 7-4).

**ACT:** Actual

This column is GNS-XLS data.

*NOTE: Actual fields become dashes when cursor is posi-*

*tioned over the leg identifiers.*

(Figure 7-5).

**F REM:** Fuel Remaining

Planned: AFIS planned fuel remaining at aircraft present position based on DMU interpolated values.

Actual: The total fuel on board as calculated by the GNS-XLS.

*NOTE: Field changes to F REQ when cursor is positioned over the leg identifiers* 

**F REQ:** Fuel Required

Planned: The AFIS planned fuel required to fly the leg displayed.

**FF P/E:** Fuel Flow per Engine

Planned: AFIS planned fuel flow per engine for leg displayed.

Actual: Total actual fuel flow divided by the number of engines. This is an averaged quantity.

**ETA:** Estimated Time of Arrival

Planned: The sum of the AFIS planned time enroute for the leg displayed and the actual time of arrival over the previous waypoint.

Actual: The estimated time of arrival over TO waypoint based on current groundspeed.

*Figure 7-4*

*Figure 7-5*

*NOTE: Field changes to ETE when cursor is positioned over the leg identifiers. (Figure 7-6)*

**ETE:** Estimated Time Enroute

Planned: The AFIS planned time enroute for leg displayed.

**TAS:** True Airspeed

Planned: AFIS planned true airspeed for leg displayed.

*Figure 7-6*

Actual: Actual true airspeed of

aircraft. The **TAS** value shown is the same as on **NAVIGATION** Page 3.

**GS:** Groundspeed

Planned: AFIS planned groundspeed for leg displayed.

Actual: Actual groundspeed of the aircraft as calculated by the GNS-XLS. The **GS** value shown is the same as on **NAVIGATION** Page 1.

## **WIND:**

Planned: AFIS forecast wind for leg displayed. Direction is displayed relative to True North with velocity in knots.

Actual: Actual wind for leg as computed by the system. Direction is displayed relative to True North with velocity in knots.

## **AFIS MENU PAGE**

**AFIS FLT PLAN:** Review of the AFIS Flight Plan displaying:

- Fuel and time requirements
- Weights, flight level, and route
- Operator inputs used in generating Flight Plan
- Performance bias entered by operator

*Figure 7-7*

**SIGMETS:** Review of all SIGMETS(SIGnificant METeorology) transferred via the disk and/or received via the data link.

**TERMINAL WX:** Review of all Terminal Weather transferred via the disk and/or received via the data link. Additional requests can be entered.

**WINDS ALOFT:** Review of all Winds Aloft identifiers transferred via the disk and/or received via the data link. Additional requests can be entered.

**RECALL AFIS FPL:** Allows operator to recall a previously accessed flight plan and associated weather from the Global Data Center via the data link.

**SEND AFIS MSG:** Allows operator to send non-flight related text messages via the satellite data link and flight related text messages via the satellite or VHF data link.

**DISPL AFIS MSG:** Allows operator to display flight related messages received via the data link.

**OPERATING MODES:** Allows operator to select operating mode for:

- AUTO REPORT
- AUTO WX UPDT
- VHF NETWORK (ARINC, SITA/AVICOM) and if applicable,
- SAT (satellite) NETWORK.

*Note: If Weather Graphics is configured, the AFIS MENU page is as shown in the AFIS Weather Graphics section.*

## **AFIS FLT PLAN PAGES**

The AFIS Flight Plan Pages are accessed by selecting **AFIS FLT PLAN** on the **AFIS MENU** Page.

## **AFIS FLT PLAN PAGE 1**

## *FUEL AND TIME REQUIRE-MENTS*

**FR:** The origin airport identifier. (Figure 7-8) When there is an enroute update to the flight plan, the identifier will change to

*Figure 7-8*

**UPDATE**. UPDATE refers to the Lat/Lon position of aircraft at time of last update request. (Figure 7-9).

**TO:** The TO waypoint identifier.

**TO/FUEL:** Projected fuel required from FROM waypoint to TO waypoint as transferred from disk or updated enroute via the data link.

*Figure 7-9*

**TO/TIME:** The estimated time enroute in hours and minutes from the FROM waypoint to the TO waypoint as transferred from the disk or updated through the data link.

**HOLDING/FUEL:** Projected fuel required for Holding Time as transferred from disk or received via the data link.

**HOLDING/TIME:** The holding time in hours and minutes as transferred from disk or received via the data link.

**TO/FUEL:** Projected fuel required from TO waypoint to alternate airport as transferred from disk or received via the data link.

**TO/TIME:** The estimated time enroute in hours and minutes from TO waypoint to alternate airport as transferred from disk or received via the data link.

**RESERVE FUEL:** Projected reserve fuel at TO waypoint as transferred from the disk or received via the data link.

**RESERVE TIME:** Projected flight time remaining at TO waypoint to consume the displayed **RESERVE FUEL**.

**TOTALS**: Sum of planned enroute and reserve fuel and sum of planned enroute and reserve time.

## **AFIS FLT PLAN PAGE 2**

## *WEIGHTS, FLIGHT LEVEL AND ROUTE*

**RAMP WT:** Planned ramp weight in lbs prior to starting engines as transferred from disk or received via the data link. (Figure 7-10)

**GROSS WT:** Sum of basic operating weight, payload, and fuel remaining as calculated by GNS-XLS. (Figure 7-11)

*NOTE: RAMP WT changes to GROSS WT if there is an automatic FUEL FLOW input, FUEL REMAINING quantity, and input for basic operating weight and PAYLOAD input.*

**FPL LDWT:** Flight planned landing weight of aircraft at destination as transferred from disk or received via the data link.

*Figure 7-10*

*Figure 7-11*

**FLT LVL:** Planned flight

level(s) as transferred from disk or received via the data link.

**ROUTE:** Planned route of flight as computed by Global Data Center and transferred from disk or received via the data link.

*NOTE: Pressing the AFIS or NXT Key displays the remainder of the route (up to 50 waypoints).*

**UPDATE:** Waypoint identifier defining position of aircraft at time of last update request.

#### **AFIS FLT PLAN PAGE 3**

#### **OPERATOR INPUTS**

FROM: Origin airport identifier as transferred from disk or received

via the data link, or UPDATE waypoint defining position of aircraft at time of last update request. (Figure 7-12)

**TO:** Destination waypoint transferred from disk or received via the data link.

**DEP TIME:** Estimated time of departure in GMT. This field changes to **UPDATE TIME** when a flight plan is updated and indicates time of issued update. (Figure 7-13)

**BASIC OP WT:** AFIS planned basic operating weight as transferred from disk or received via the data link.

**PAYLOAD:** AFIS planned payload weight as transferred from disk or received via data link.

RAMP FUEL: AFIS planned total trip fuel as transferred from disk or received via data link. This field changes to **UPDATE** FUEL when a flight plan is

Figure 7-12

Figure 7-13

updated and refers to the actual fuel remaining at time of last update request.

**FPL RES FUEL:** AFIS planned reserve fuel remaining at destination as transferred from disk or received via the data link. This field changes to **RESERVE FUEL** when a flight plan is updated and refers to the updated estimate of fuel remaining at destination.

**PERF OPTION:** AFIS planned cruise mode as transferred from disk or received via the data link. Alternate cruise mode options may be requested and updated via the data link.

## **AFIS FLT PLAN PAGE 4**

## *PERFORMANCE BIAS*

This page allows a review of the operator entered performance bias data transferred from disk or received via the data link. (Figure 7-14)

## **SIGMETS PAGES**

**AFIS SIGMETS** pages are accessed by selecting **SIG-METS** on the **AFIS MENU** Page.

This page allows a review of all SIGMETS transferred from disk or received via the airborne data link. SIGMETS may consist of one or more pages of text and display their FAA code names followed by text.

**DATE:** Issue date of SIGMET. This field may be blank if transferred from disk.

*NOTE: Date field will remain blank if no date is supplied on disk or by UPDATE.*

**FR:** Desired start VOR, airport, waypoint, Lat/Lon, VORTAC ident, or NAT (North Atlantic Tracks). (Figure 7-15 or 7-16)

*NOTE: Parentheses remain until a SIGMET update is received via the data link.*

**TO:** Desired end VOR, airport, waypoint, Lat/Lon or VORTAC ident. No entry is required if **FR** is **NAT**.

*Figure 7-14*

*Figure 7-15*

*Figure 7-16*

**TRANSMIT REQUEST?:** When cursor is on this field and **ENTER** is pressed, a SIGMET update request is sent to the Global Data Center via data link. **DATA LINK DISABLED** will appear if the data link is disabled and the request will not be transmitted.

*NOTE: This field only appears when the FR or TO fields are in parentheses.*

If no SIGMETS are on disk, the message **NO SIGMETS ON DISK** appears. If there are no SIGMETS via a Flight Plan update the message reads **NO SIGMETS**.

(Figure 7-17)

*Figure 7-17*

## **TERMINAL WEATHER PAGES**

The **TERMINAL WEATHER** Menu Page is accessed by selecting **TERMINAL WX** on the **AFIS MENU** Page.

Terminal identifiers for which associated weather data is available to review are listed. The identifiers in parentheses represent pilot entered requests for additional weather not stored in the DMU. The parentheses disappear when weather updates have been received via the data link.

## **TRANSMIT REQUEST?:**

When cursor is on this field and **ENTER** is pressed, a weather update request is sent to the Global Data Center via data link. (Figure 7-18)

**DATA LINK DISABLED:** Aircraft equipped with the Antenna Switching Unit must DEPRESS momentary AFIS annunciator to enable the air to ground data link. VHF or satellite network must also be enabled.

*Figure 7-18*

## **TERMINAL WX DATA PAGES**

These pages are accessed by selecting a terminal weather identifier on the **TERMINAL WEATHER** Menu Page.

They allow review of Terminal Weather by identifier as transferred from disk or received by the Global Data Center via the data link.

**DATE:** Issue date of actual weather. This field may be blank if transferred from disk.

*Figure 7-19*

Weather available for review includes:

- **SA** (Sequence Reports)
- **FT** (Terminal Forecasts)
- **NOTAMS** (Notices to Airmen)
- **PIREPS** (Pilot Reports)

## **WINDS ALOFT PAGES**

The **AFIS WINDS ALOFT** Menu Page is accessed by selecting **WINDS ALOFT** on the AFIS MENU Page.

The WIND identifiers represent VOR, airport, waypoint, Lat/Lon or VORTAC locations, for which associated weather data is available.

## **WINDS ALOFT DATA PAGES**

*Figure 7-20*

These pages are accessed by selecting a wind identifier on the **WINDS ALOFT MENU** page.

They allow review of Winds Aloft data by VOR, airport, waypoint, Lat/Lon or VORTAC identifier as transferred from disk or received via the data link.

**DATE/TIME:** Actual day and time of the issue of the wind information. This field may be blank if transferred from disk. The number is read 12th day 2356 ZULU.

(Figure 7-21)

Wind data available to review includes:

- Flight Level
- Wind Direction (True North)
- Wind Velocity (Knots)
- Temperature (Degrees Celsius)

*Figure 7-21*

## **RECALL AFIS FPL PAGE**

This page is accessed by selecting **RECALL AFIS FPL** on the **AFIS MENU** Page.

This page allows the pilot to recall previously computed AFIS Flight Plan and Weather requests from the Global Data Center via the data link.

**FPL-#:** A Global Data Center generated Flight Plan number. Entered as an alpha character followed by four numeric digits. If **FPL#** is entered, other entries are not required. (Figure 7-22)

**DATE:** Issue date of recalled AFIS Flight Plan.

**ETD:** Estimated time of departure in GMT of recalled AFIS Flight Plan .

**FR:** Origin of recalled AFIS Flight Plan.

**TO:** Destination of recalled AFIS Flight Plan. (Figure 7-23)

*Figure 7-22*

*Figure 7-23*

**TRANSMIT REQUEST?:** When cursor is on this field and **ENTER** is pressed, the recall request is sent to the Global Data Center via data link. (Figure 7-22)

**DATA LINK DISABLED:** Aircraft equipped with the Antenna Switching Unit, must DEPRESS momentary AFIS annunciator to enable the air to ground data link. VHF or satellite network must also be enabled.

## **SEND AFIS MESSAGE PAGE**

This page is accessed by selecting **SEND AFIS MSG** on the **AFIS MENU** Page.

↑ ↓ indicate that pressing the Line Select Key adjacent the arrow will move the cursor in the direction of the arrow.

**PPM:** Preprogrammed messages that can be stored in non-volatile memory, selected and sent without being re-entered.

**TO:** Receiver of message.

**FROM:** Sender's identification (name or tail number).

**#:** Receiver's address. See Table A-1 for possible address variations and the method in which the Global Data Center processes the message.

**MESSAGE TEXT:** Fifteen lines of text entry available. Text must be flight related when using the VHF network operating mode.

**SEND MESSAGE:** When cursor is over this field and **ENTER** is pressed the message is sent via the data link. (Figure 7-24)

**DATA LINK DISABLED:** Aircraft equipped with the Antenna Switching Unit, must DEPRESS momentary AFIS annunciator to enable the air to ground data link. VHF or satellite network must also be enabled.

*Figure 7-24*

| Phone number<br>• | GDC will deliver message verbally to given number.                                                                                     | #206 869 6450                            |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| •                 | AFIS-equipped aircraft<br>GDC will deliver message to aircraft specified.                                                              | #N4322B                                  |
| •                 | "A" followed by phone number<br>GDC will deliver message to PC at given number.                                                        | #A206 869 6458                           |
| •                 | "AI" followed by Country Code, City Code, and phone number<br>GDC will deliver message to PC located outside the<br>US or Canada.      | #AI4118106530                            |
| •                 | "F" followed by phone number<br>GDC will deliver message to FAX machine at given number                                                | #F206 869 6464                           |
| •                 | "FI" followed by Country Code, City Code and phone number<br>GDC will deliver message FAX machine located<br>outside the US or Canada. | #FI4118108708                            |
| •                 | "A" followed by ARINC or SITA address<br>GDC will deliver message to ARINC or SITA address given.                                      | #AHDQGLXH                                |
| •                 | Auto Forward Code<br>GDC will deliver message to PC, FAX, or ARINC/SITA<br>as defined in GDC database.                                 | #GWSOPS                                  |
| GDC Code<br>•     | GDC will search database for phone number and special<br>contact name or message associated with code and<br>deliver message verbally. | #GWSPJC                                  |
| ADCUS XXX<br>•    | GDC will search database for customs phone number<br>at specified airport and deliver message verbally.                                | #ADCUS TEB                               |
| PDC XXX<br>•      | GDC will search database for pre-departure clearance<br>and forward to aircraft if found.                                              | #PDC LAX                                 |
|                   | Global Defined Codes                                                                                                                   |                                          |
| •                 | BASEOPS International                                                                                                                  | #BASEOPS or<br>#BOPS                     |
| •<br>•            | Air Routing International<br>Universal Weather                                                                                         | #ARC<br>#UNIVERSAL or<br>#UV or #UVAIR   |
| •                 | Jeppesen Data Plan                                                                                                                     | #JETPLAN or<br>#DATAPLAN<br>or #JEPPESEN |
| •                 | Medlink                                                                                                                                | #MEDLINK                                 |
| GDC<br>•          | Message will be printed at GDC further action.                                                                                         | #GDC                                     |

AFIS Addresses Table 1

## **PPM MENU PAGE (PREPROGRAMMED MESSAGES)**

This page is accessed from the **SEND MESSAGE** Page by selecting **PPM** in the upper right hand corner.

**PPM** can only be selected when an entry has been made in the **TO** or **#** fields on the **SEND MESSAGE** Page. The **TO**, **FROM**, and **#** data are used when sending a preprogrammed message.

Titles for up to six preprogrammed messages can be listed for selection to review, change, and send.

*Figure 7-25*

## **PREPROGRAMMED MES-SAGE PAGES**

These pages display the message text for each preprogrammed message title selected from the **PPM MENU** Page. Up to seven lines of text may be entered. Preprogrammed Messages will remain in nonvolatile memory and can be removed by editing the title on the **PREPROGRAMMED MSG** Menu Page.

*Figure 7-26*

## **DISPLAY AFIS MSG PAGE**

The message page is displayed by selecting **DISPLAY AFIS MSG** on the **AFIS MENU** Page.

All text messages sent to the tail number of the aircraft being flown appear in this section. Up to 15 pages of text can be stored according to time received, with the newest message appearing first. Messages can originate from:

*Figure 7-27*

- Another AFIS equipped aircraft,
- third party, or
- Global Data Center.

## **OPERATING MODES PAGE (FOR AFIS USERS EQUIPPED WITH SATELLITE DATA COMMUNICATIONS SYSTEM)**

Operating modes information is accessed by selecting **OPERATING MODES** on the **AFIS MENU** Page.

## *AUTO REPORT:*

**ON:** The aircraft will automatically report position and station ID for weather updates to the Global Data Center via the data link on a timed basis.

**OFF:** The automatic reporting capability has been manually inhibited by the pilot.

*Figure 7-28*

## *AUTO WX UPDT (WEATHER UPDATE):*

**ON:** The Global Data Center will automatically send weather/wind updates for the displayed idents when new information is issued.

**OFF:** The auto weather update function is not enabled.

**VHF NETWORK:** Ground networks that AFIS interfaces with to establish a data link with the Global Data Center.

**ON:** The appropriate VHF network will automatically be selected whenever the aircraft present position is within the specified boundaries. (Figure 7-28)

**OFF:** Network is not enabled.

**SAT NETWORK:** Satellite network that AFIS interfaces with to establish a data link with the Global Data Center.

**ON:** The appropriate satellite region will automatically be selected whenever the aircraft present position is within the specified boundaries.

**OFF:** Network is not enabled.

**ACTIVE LINK:** Indicates the network in service, i.e. **ARINC**, **SITA**, or **SATCOM**. (Figure 7- 29)

*NONE: All networks are turned OFF or current position does not correspond with the manually selected boundaries.*

*NOTE: The VHF network has precedence over the satellite network in areas of shared coverage and must be turned OFF*

*Figure 7-29*

*in order for SATCOM to be the Active Link. AUTO REPORT, AUTO WX UPDT and OPERATING MODE selection status are stored in non-volatile memory. If the operator turns to OFF the operator must reselect to turn ON*

## **VHF LINK CONTROL PAGE**

This page is accessed when the VHF Network is turned **ON**.

**ARINC, SITA/AVICOM:** Ground networks that AFIS interfaces with to establish a data link with the Global Data Center.

**AUTO:** The VHF network will automatically be selected whenever the aircraft present position is within the appropriate boundaries. (Figure 7-30)

*Figure 7-30*

**MAN (manual):** The desired network will be maintained independent of the present position. In manual, the system will only allow transmission when present position is within the appropriate boundaries. All other networks will be turned **OFF** if one is in **MAN**.

**OFF:** Network is not enabled.

## **SAT LINK CONTROL PAGE**

This page is accessed when the SAT Network is turned **ON**.

## **SAT COMM:**

**AUTO:** The satellite network will automatically be selected whenever the aircraft present position is within the appropriate boundaries and VHF Network is turned **OFF** or is not in VHF coverage.

**MAN (manual):** The desired region will be maintained independent of the present position. In manual, the system will only allow transmission when present position is within the appropriate boundaries and VHF network is turned **OFF** or is not in VHF coverage.

**OFF:** Network is not enabled.

**REGION:** The four satellite regions, West Atlantic, East Atlantic, Pacific Ocean and Indian Ocean, that AFIS interfaces with to establish a data link with the Global Data Center. (Figure 7-31)

## **LINK:**

**OPERATIONAL:** Message indicating the SAT COMM link is enabled.

**NONE:** Current position does not correspond with the manually selected boundaries or satellite link is not operational.

**ACTIVATE?:** Use to enable satellite network in **AUTO** or **MAN**. (Figure 7-32)

*Figure 7-31*

*Figure 7-32*

## **OPERATING MODES PAGE (FOR AFIS USERS NOT EQUIPPED WITH SATELLITE DATA COMMUNICATIONS SYSTEM)**

Operating Modes information is accessed by selecting **OPERATING MODES** on the **AFIS MENU** Page.

## *AUTO REPORT:*

**ON:** The aircraft will automatically report position and station ID for weather updates to the Global Data Center via the data link on a timed basis.

**OFF:** The automatic reporting capability has been manually inhibited by the pilot.

## *AUTO WX UPDT (WEATHER UPDATE):*

**ON:** The Global Data Center will automatically send weather/wind updates for the displayed idents when new information is issued.

**OFF:** The auto weather update function is not enabled.

**ARINC, SITA, AVICOM:** Ground networks that AFIS interfaces with to establish a data link with the Global Data Center.

*Figure 7-33*

**AUTO:** The desired network will automatically be selected

whenever the aircraft present position is within the appropriate boundaries.

**MAN (manual):** The desired network will be maintained independent of the present position. In manual, the system will only allow trans-

mission when present position is within the appropriate boundaries.

**OFF:** Network is not enabled.

*NOTE: If a ground network is placed in manual mode, all others will go to OFF.*

**ACTIVE LINK:** Indicates the network in service, i.e. **ARINC**, **SITA** or **AVICOM**.

*Figure 7-34*

**NONE:** All networks are turned

**OFF** or current position does not correspond with the selected mode.

*NOTE: AUTO REPORT, AUTO WX UPDT and OPERATING MODE selection status are stored in non-volatile memory. If the operator turns to OFF or MAN, the operator must reselect to turn ON.* 

## **ACTIVE FLIGHT PLAN PAGE (FOR AFIS FLIGHT PLAN UPDATING)**

**AFIS UPDATE:** Allows pilot to:

- Amend an existing AFIS Flight Plan
- Update SIGMETS
- Request a new AFIS Flight Plan

## **AFIS UPDATE VERIFICATION PAGE**

**ACTUAL FL:** Actual flight level of aircraft rounded to nearest 100 ft. as entered by the pilot.

**ASSIGNED FL:** Current Flight Level assigned by ATC as verified or amended by the pilot.

**PAYLOAD:** Current aircraft payload verified or amended by the pilot.

**FUEL REM:** Actual fuel remaining as calculated by the GNS-XLS or amended by the pilot.

**CRUISE MODE:** Current aircraft Cruise Mode as verified or amended by the pilot.

**TRANSMIT REQUEST:** When cursor is over this field and **ENTER** is pressed, the update request is sent via the data link. (Figure 7-36)

**DATA LINK DISABLED:** Aircraft equipped with the Antenna Switching Unit, must DEPRESS momentary AFIS

*Figure 7-35*

*Figure 7-36*

*Figure 7-37*

annunciator to enable the air to ground data link. VHF or satellite network must also be enabled.

## **SYSTEM MESSAGES PAGE**

AFIS related messages appear on the **SYSTEM MESSAGES** Page (see Section 2 of the Operators Manual). When new messages are added, the **MSG** Key will flash and a flashing asterisk will appear next to the new message.

## **SYSTEM MESSAGES**

## *ADVISORY:*

*Figure 7-38*

The following are the advisory messages which pertain to AFIS and may appear on the GNS-XLS **SYSTEM MESSAGES** Page.

## **SYSTEM MESSAGE EXPLANATION**

**WX UPDATED** The DMU has received an AFIS terminal weather update from the Global Data Center.

**WINDS UPDATED** The DMU has received an AFIS Winds Aloft update from the Global Data Center.

**SIGMETS UPDATED** The DMU has received an AFIS SIGMETS update from the Global Data Center.

**FPL UPDATED** The DMU has received an AFIS Flight Plan update from the Global Data Center.

1 **NO COMM** AFIS update request initiated by the pilot has not been acknowledged by the ground communications network.

**DOWNLINK FAIL** The last AFIS downlink request contained an invalid character and was not transmitted to the ground network.

**UPLINK FAIL** The last AFIS uplink attempt by the ground network was not accepted by the DMU.

**FPL RECALLED** The DMU has received a previously accessed AFIS Flight Plan from the Global Data Center.

**DATA CENTER AK** Global Data Center has acknowledged a downlink request.

**AFIS CONFIG CHG**. Configuration information in the DMU has been changed to agree with interfaced configuration module

**AFIS CONFIG FAIL** Configuration module has failed. DMU nonvolatile memory configuration information will be used.

**AFIS CONFIG LOST** DMU non-volatile memory has lost its configuration information and the configuration module has failed.

*NOTE: Message may not cause MSG Annunciator to flash.*

## **ACTION REQUIRED:**

The following are the action required messages which pertain to AFIS and may appear on the GNS-XLS **SYSTEM MESSAGES** Page.

**SEE AFIS MSG** There is a text message on the **AFIS MESSAGES** page which requires acknowledgement and possibly pilot action.

## **SYSTEM OPERATION**

## **PRE-DEPARTURE**

## **AFIS FLIGHT PLAN SELECTION**

The **AFIS FLIGHT PLAN LIST** Page appears after the Initialization Page. The page also appears between the Active Flight Plan Page and the first GNS-XLS **FLIGHT PLAN LIST** Page.

*NOTE: For aircraft equipped with the Antenna Switching Unit, DEPRESS momentary AFIS annunciator to enable the air to ground data link.*

## **TO ENTER AN AFIS FLIGHT PLAN**

- 1. Preprogrammed AFIS Disk INSERT disk into DTU.
- 2. Select **AFIS FLIGHT PLAN LIST** Page using either (a) or (b).
  - a. Initialization Page Enter Date, GMT, and Initial Position. **AFIS FLIGHT PLAN LIST** Page appears.

*Figure 7-39*

b. **FPL** Key - DEPRESS until desired **AFIS FLIGHT PLAN LIST** Page appears. (Figure 7-39)

*NOTE: Desired flight plan may be found on a subsequent page if more than six flight plans have been either transferred from the disk or received via the data link. If there is more than one Flight Plan with the*

*same Departure/ Destination pair a random letter will be displayed between the Depart?Dest pair and the date. This letter and the date distinguish one FPL from the other.*

3. Line Select Key - DEPRESS to place cursor over desired Flight Plan. (Figure 7-40)

*Figure 7-40*

- 4. FPL Date VERIFY.
- 5. **ENTER** Key DEPRESS.

*NOTE: If an Active Flight Plan exists, the message REPLACE ACTIVE FPL? appears. DEPRESS ENTER to replace the Active Flight Plan with the AFIS Flight Plan.* 

6. ACTIVE FPL - CONFIRM. AFIS Flight Plan becomes the Active Flight Plan. The initial leg must be established on the NAV Page so the system can navigate normally.

## **ENROUTE**

## **REVIEWING FLIGHT PLAN PROGRESS**

- 1. **NAV** Key DEPRESS until **NAVIGATION** Page 5, Flight Plan Progress Page appears. (Figure 7-41)
- 2. Current Leg Data CON-FIRM. Observe AFIS Planned data vs. Actual GNS-XLS calculated data.

## **REVIEWING AFIS PLANNED LEG DATA**

3. Line Select Key - DEPRESS to position cursor over Leg Identifiers. (Figure 7-42)

*NOTE: ACTUAL data fields become dashes, F REM field becomes F REQ and ETA field becomes ETE.*

4. **ENTER** Key - DEPRESS to review Planned data for future legs of the Active AFIS Flight Plan.

*Figure 7-41*

*Figure 7-42*

*Figure 7-43*

- 5. **BACK** or **PRV** Key DEPRESS to review Planned data for previous legs of the AFIS Flight Plan.
- 6. Line Select Key DEPRESS to remove cursor from page and return to Current Leg Progress.

*NOTE: If the current leg displayed does not agree with a planned AFIS leg, the PLAN fields display dashes. (Figure 7-43) If AFIS Flight Plan is updated via the data link, new values will appear. Refer to Updating AFIS Flight Plan for update procedure.*

## **REVIEWING AFIS FLIGHT PLAN DATA**

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key Place cursor over **AFIS FLT PLAN**. (Figure 7-44)
- 3. **ENTER** Key DEPRESS.

*Figure 7-44*

## **AFIS FLIGHT PLAN PAGE 1**

4. REVIEW fuel and time data. (Figure 7-45) If the Flight Plan has been updated, the **FROM** identifier (origin airport) will be changed to **UPDATE**. (Figure 7-46)

Fuel and time data change as a result of the updated information. The **TOTALS** reflect the changes in the **TO** and **RESERVE** fields.

*Figure 7-45*

*Figure 7-46*

5. **AFIS** or **NXT** Key - DEPRESS to display AFIS Flight Plan Page 2.

*NOTE: Pressing the PRV or BACK Key will re-display the AFIS MENU Page with the cursor positioned over AFIS FLT PLN.*

## **AFIS FLIGHT PLAN PAGE 2**

6. WEIGHTS, FLIGHT LEVEL and ROUTE - REVIEW (Figure 7-47). If the Flight Plan has been updated, the first route identifier will be **UPDATE**, followed by the updated route to destination. **FPL LDWT** and **FLT LVL** values may change as data is updated.

*NOTE: If Automatic Fuel Flow is interfaced to the GNS-XLS, RAMP WT changes to GROSS WT after the engines are started and the GROSS WT value field decreases on a periodic basis as the GNS-XLS recalculates. (Figure 7-48)*

*Figure 7-47*

*Figure 7-48*

7. **AFIS** or **NXT** Key - DEPRESS. Subsequent pages of the Route will appear as needed (up to 50 waypoints) or **AFIS FLT PLAN** Page 3 appears.

*NOTE: DEPRESSING PRV or BACK Key will display AFIS FLT PLAN Page 1.*

## **AFIS FLIGHT PLAN PAGE 3**

8. Pilot Inputs - REVIEW. (Figure 7-49)

*NOTE: If there has been an update to the flight plan: FROM identifier (origin airport) changes to UPDATE; DEP TIME changes to UPDATE TIME; RAMP FUEL changes to UPDATE FUEL; FPL RES FUEL changes to RESERVE FUEL; and the values in the respective fields change to reflect the updated information. (Figure 7-50)*

9. **AFIS** or **NXT** Key - DEPRESS to display **AFIS FLT PLAN** Page 4.

*NOTE: DEPRESSING PRV or BACK Key will display AFIS FLT PLAN Page 3.*

- 10. Performance Bias Data REVIEW. (Figure 7-51)
- 11. **AFIS** or **NXT** Key DEPRESS to return to **AFIS MENU** Page, where the cursor will be positioned over **AFIS FLT PLN**.

*NOTE: Pressing the BACK or PRV Key throughout the Flight Plan Pages will cause the previous Flight Plan Page to appear.*

*Figure 7-49*

*Figure 7-50*

*Figure 7-51*

## **SIGMETS REVIEW/UPDATE**

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **SIGMETS**.
- 3. **ENTER** Key DEPRESS to display first **SIGMETS** Page. (Figure 7-52 or 7-53)

*NOTE: If no SIGMETS have been recorded on the disk, a page appears displaying the message NO SIGMETS ON DISK. If there are no SIGMETS via a Flight Plan update the message reads NO SIGMETS. Depress AFIS, PRV, or BACK Key to return to AFIS MENU Page.*

*Figure 7-52*

- 4. Select Key DEPRESS TO POSITION cursor over **FROM** field
- 5. FROM Identifier VERIFY or INSERT.
- 6. **ENTER** Key DEPRESS. The cursor will automatically move to the TO Identifier field.
- 7. TO Identifier- VERIFY or INSERT.
- 8. ENTER Key DEPRESS. The cursor will automatically move to **TRANSMIT REQUEST?** (Figure 7-54)
- 9. **ENTER** Key DEPRESS. The request is downlinked and the system will display the **AFIS MENU** Page with the cursor over **TERMINAL WX**.

*Figure 7-53*

*Figure 7-54*

*NOTE: Wait for DATA CENTER AK message if sending multiple requests. A ( ) around the FR and TO waypoints indiates that the updated information has not yet been received.*

10. **AFIS** or **NXT** Key - DEPRESS. Subsequent **SIGMETS** Pages will appear or **AFIS MENU** Page returns with cursor positioned over **TERMINAL WX**.

## **TERMINAL WEATHER MENU - DATA UPDATE AND REVIEW**

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **TERMINAL WX**. (Figure 7-55)
- 3. **ENTER** Key DEPRESS to display **TERMINAL WX** Menu Page. (Figure 7-56)
- 4. Line Select Key DEPRESS to position cursor over the desired Terminal Wx airport identifier.

*Figure 7-55*

5. **ENTER** Key - DEPRESS.

If the desired identifier is enclosed in parentheses, pressing the **ENTER** Key will cause it to blink, indicating no weather information is available for that identifier.

If no identifiers are displayed, they may be inserted by pressing the Line Select Key, which will create a cursor over the first blank identifier position. INSERT an airport identifier.

*Figure 7-56*

- 6. **ENTER** Key DEPRESS
- 7. Line Select Key DEPRESS to position cursor over **TRANSMIT REQUEST?**

8. **ENTER** Key - DEPRESS. Identifiers listed on this page will be transmitted to the ground via the data link.

*NOTE: Wait for DATA CENTER AK message if sending multiple requests.*

- 9. If there are identifiers: Placing the cursor over the selected identifier on the terminal weather and pressing **ENTER** will display the weather information for the airport. (Figure 7-57)
- 10. Weather information REVIEW.

*Figure 7-57*

## *TO INSERT A NEW IDENTIFIER:*

- 11. Line Select DEPRESS to position the cursor over the identifier field.
- 12. IDENTIFIER INSERT. The data text fields will go blank.
- 13. **ENTER** Key DEPRESS. The **TERMINAL WX** Menu Page appears with the new identifier in place of the original identifier, and the cursor positioned at the location of the original identifier selected. If there is no data available for this new identifier, it will appear in parentheses.

## *TO DELETE TEXT WHEN THERE IS NO DATA ENTRY IN PROGRESS:*

- 14. Place cursor over airport identifier on **TERMINAL WX** page.
- 15. Depress **BACK** key. **DELETE?** will appear.
- 16. **ENTER** Key- Depress to delete the airport identifier.

## **WINDS ALOFT MENU - DATA UPDATE AND REVIEW**

- 1. **AFIS** Key DEPRESS to display AFIS MENU Page.
- 2. Line Select Key DEPRESS to position cursor over **WINDS ALOFT**. (Figure 7-59)

*Figure 7-59*

- 3. **ENTER** Key DEPRESS to display **WINDS ALOFT** Menu Page. (Figure 7-60)
- 4. Line Select Key DEPRESS to position cursor over the desired Wind identifier.
- 5. **ENTER** Key DEPRESS.

If the desired identifier is enclosed in parentheses, pressing the **ENTER** Key will

*Figure 7-60*

cause it to blink, indicating no weather information is available for that identifier.

If no identifiers are displayed, they may be inserted by pressing the Line Select Key, which will create a cursor over the first blank identifier position. INSERT an identifier. (Usually a VOR or intersection)

- 6. **ENTER** Key DEPRESS
- 7. Line Select Key DEPRESS to position cursor over **TRANSMIT REQUEST?**
- 8. **ENTER** Key DEPRESS. Identifiers listed on this page will be transmitted to the ground via the data link.

*NOTE: Wait for DATA CENTER AK message if sending multiple requests.*

9. If there are identifiers, upon depressing the **ENTER** Key, the **WINDS ALOFT** Data Pages pertaining to the selected identifier appear. (Figure 7-61)

*Figure 7-61*

10. Wind information - REVIEW.

## *TO INSERT A NEW IDENTIFIER:*

- 11. Press Line Select Key to position the cursor over the identifier field.
- 12. IDENTIFIER INSERT. The data text fields will go blank.

13. **ENTER** Key - DEPRESS. The **WINDS ALOFT** Menu Page appears with the new identifier in place of the original identifier, and the cursor positioned at the location of the original identifier selected. If there is no data available for the new identifier, it will appear in parentheses.

## *TO DELETE TEXT WHEN THERE IS NO DATA ENTRY IN PROGRESS:*

- 14. Place cursor over identifier on **AFIS WINDS ALOFT** page.
- 15. Depress **BACK** key the the **ENTER** Key.

## **RECALLING AFIS FLIGHT PLAN**

This procedure allows a previously accessed AFIS Flight Plan and associated weather to be recalled from the Global Data Center.

## *RECALL OPTION 1:*

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **RECALL AFIS FPL**. (Figure 7-63)
- 3. **ENTER** Key DEPRESS. **RECALL AFIS FPL** Page appears.
- 4. Line Select Key DEPRESS to position cursor next to **FPL #** field.
- 5. **FPL #** INSERT desired AFIS Flight Plan number. (Figure 7-64)

*Figure 7-63*

*Figure 7-64*

- 6. **ENTER** Key DEPRESS. Cursor is positioned over **TRANSMIT REQUEST?** (Figure 7-65)
- 7. **ENTER** Key DEPRESS to initiate recalling of AFIS Flight Plan from Global Data Center.

*NOTE: For aircraft equipped with the Antenna Switching Unit, if DATA LINK DISABLED message appears DEPRESS momentary AFIS annunciator to enable the air to ground data link. Also enable VHF or satellite network.*

*Figure 7-65*

Wait for **DATA CENTER AK** message if sending multiple requests.

## *RECALL OPTION 2:*

If Flight Plan Number field is blank:

1. **ENTER** Key - DEPRESS. Cursor will position itself over date field. (Figure 7- 66)

*Figure 7-66*

- 2. DATE INSERT issue date (day, month, year, digits only) of AFIS Flight Plan being recalled.
- 3. **ENTER** Key DEPRESS.
- 4. **ETD** INSERT estimated time of departure in GMT of AFIS Flight Plan being recalled.
- 5. **ENTER** Key DEPRESS.
- 6. **FR** field INSERT origin ICAO Identifier.
- 7. **ENTER** Key DEPRESS.
- 8. **TO** field INSERT destination ICAO Identifier.

- ENTER Key DEPRESS. Cursor is positioned over TRANSMIT REQUEST? (Figure 7-67)
- ENTER Key DEPRESS to initiate recalling of AFIS Flight Plan from Global Data Center. AFIS MENU Page will appear with cursor positioned over SEND AFIS MSG.

Figure 7-67

NOTE: SIGMETS , Winds and

Term Wx are automatically updated once the **FPL** is recalled.

NOTE: Wait for **DATA CENTER AK** message if sending multiple requests.

# SENDING A TEXT MESSAGE OR PDC

- AFIS Key DEPRESS to display AFIS MENU Page.
- 2. Line Select Key DEPRESS to position cursor over **SEND AFIS MSG**. (Figure 7-68)
- ENTER Key DEPRESS. SEND AFIS MESSAGE Page appears. (Figure 7-69) If not requesting PDC proceed to step 7
- 4. Line Selct Key Depress to position cursor over #: field.
- INSERT PDCXXX (XXX is departure airport identifier).
- 6. **ENTER** Key Depress twice to transmit request.
- TO INSERT receiver of message.

Figure 7-68

Figure 7-69

- 8. **ENTER** Key DEPRESS.
- 9. **FR** INSERT sender's identification (name or tail number).
- 10. **ENTER** Key DEPRESS.
- 11. **#** INSERT receiver's address. See Table 1 for possible addresses.
- 12. **ENTER** Key DEPRESS.
- 13. Message INSERT text message using the ENTER Key to access each successive line. (Figure 7-70)

*NOTE: The cursor remains fixed and the page display moves up or down one line at a time through the cursor. Fifteen lines of text can be entered. (Figure 7-71)*

The following guidelines are used for entering and editing text:

> a. Entering a character causes the character at the cursor position and all the characters to the right to be shifted one position.

*Figure 7-70*

*Figure 7-71*

- b. The **BACK** Key may be used to delete characters one at a time from right to left.
- c. The **SP** Key may be used as a spacer to separate words.
- d. The **PRV** Key may be used to move the cursor one space to the left.
- e. The **NXT** Key may be used to move the cursor one space to the right.

- f. The Line Select Key moves cursor to **SEND MESSAGE?** field if a **TO** or **#** entry field has been inserted.
- g. Top two left Line Select keys move cursor up and down page.
- 11. Line Select Key DEPRESS to position over **SEND MES-SAGE?** It will be necessary to press the **ENTER** Key after 15 lines of text, or if there are two succeeding blank lines, in order for the cursor to appear over **SEND MESSAGE**? field. (Figure 7-72)
- 12. **ENTER** Key DEPRESS. The message is sent to the Global Data Center via the data link.

*Figure 7-72*

*NOTE: Wait for DATA CENTER AK message if sending multiple requests.*

## **TO RETURN TO THE AFIS MENU PAGE**

13. Press **AFIS** or **NXT** Key with the cursor off the page.

## **SENDING/BUILDING A PREPROGRAMMED MESSAGE**

The PREPROGRAMMED MESSAGES MENU Page is accessed

from the **SEND AFIS MSG** Page. (Figure 7-73) An entry in the TO or # field must be made before access to PPM is available.

- 1. Line Select Key DEPRESS to position cursor over the PPM field.
- 2. **ENTER** Key DEPRESS. Up to six messages can be listed on the **PPM MENU** Page which appears.

*Figure 7-73*

- 3. Line Select Key DEPRESS to position cursor over desired message title or blank title field. (Figure 7-74)
- 4. MESSAGE TITLE VERIFY or ENTER. A new title may be entered with a maximum of 18 characters.

To change an existing title, type characters over the old Title. The **BACK** Key can be used to delete characters one at a time.

*Figure 7-74*

*NOTE: Whenever a title is changed or erased, the preprogrammed message associated with the title will be erased also.*

5. **ENTER** Key - DEPRESS. The preprogrammed message associated with that title will appear. If no message has been programmed the display will be blank. Insert message as requied up to 7 lines of text.

## **EDITING/ENTERING A PREPROGRAMMED MESSAGE**

- 6. TEXT EDIT or ENTER using the following guidelines.
  - a. Entering a character causes the character at the cursor position and all the characters to the right to be shifted one position.
  - b. The **BACK** Key may be used to delete characters one at a time from right to left.
  - c. The **SP** Key may be used as a spacer to separate words.
  - d. The **PRV** Key may be used to move the cursor one space to the left.
  - e. The **NXT** Key may be used to move the cursor one space to the right.

*Figure 7-75*

## **CONTINUE SENDING MESSAGE**

- 7. **NXT** Key DEPRESS to position cursor over the **SEND MESSAGE?** field. It will be necessary to press the **ENTER** Key after seven lines of text in order for the **SEND MESSAGE?** field to appear. (Figure 7-76)
- 8. **ENTER** Key DEPRESS. The message will be downlinked and the **AFIS MENU** Page will appear. **TO**, **FROM** and **#** field information of **SEND MESSAGE** Page will be used in downlink message.

*Figure 7-76*

*NOTE: DATA LINK DISABLED will appear in the SEND MES-SAGE? field if the downlink is disabled.*

Wait for **DATA CENTER AK** message if sending multiple requests.

## **AFIS MESSAGES REVIEW**

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **DISPL AFIS MSG**. (Figure 7-77)
- 3. **ENTER** Key DEPRESS. **DISPLAY AFIS MSG** Page appears.
- 4. MESSAGE REVIEW. (Figure 7-78)
- 5. **AFIS**, **NXT**, **PRV** or **BACK** Key - DEPRESS. Subsequent message pages appear or old **AFIS MENU** Page returns with cursor positioned over **OPERATING MODES**.

*NOTE: Messages will remain in the system until the system is powered off.*

*Figure 7-77*

*Figure 7-78*

**SELECTING OPERATING MODES (FOR AFIS USERS EQUIPPED WITH SATELLITE DATA COMMUNICATIONS SYSTEM)**

## *AUTO REPORTING*

When the system is initialized, the Automatic Reporting and Auto Wx update function will retain the status at aircraft shutdown. The following procedures allow the function to be turned **OFF** and back **ON**.

## *TURNING AUTO REPORT / AUTO WX UPDATE OFF*

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**. (Figure 7-79)

3. **ENTER** Key - DEPRESS.

*Figure 7-79*

4. Line Select Key - DEPRESS to position cursor over **ON** option of **AUTO REPORT** or **AUTO WX UPDATE** field. (Figure 7-80)

5. **BACK** Key - DEPRESS. OFF appears in the cursor. (Figure 7-81)

*Figure 7-80*

6. **ENTER** Key - DEPRESS to turn **OFF** the **AUTO REPORT** or **AUTO WX UPDATE** function.

*NOTE: If all networks are OFF, then AUTO REPORT and AUTO WX UPDATE will be OFF.*

*Figure 7-81*

## *RETURNING TO AUTO REPORT/AUTO WX UPDATE*

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERAT-ING MODES**. (Figure 7-82)
- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **OFF** option of **AUTO REPORT** or **AUTO WX UPDATE** field. (Figure 7-83)
- 5. **BACK** Key DEPRESS. **ON** appears in the cursor. (Figure 7-84)
- 6. **ENTER** Key DEPRESS to turn **ON** the **AUTO REPORT** or **AUTO WX UPDATE** function.

*NOTE: If all networks are OFF, then AUTO REPORT and AUTO WX UPDATE will be OFF.*

*Figure 7-82*

*Figure 7-83*

*Figure 7-84*

## *AUTO WEATHER UPDATE*

When the system is initialized, the Automatic Weather Update function will retain the status at aircraft shutdown. The following procedures allow the function to be turned **OFF** and back **ON**.

## *TURNING AUTO WX UPDT OFF*

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**. (Figure 7-85)
- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **ON** option of **AUTO WX UPDT** field. (Figure 7-86)
- 5. **BACK** Key DEPRESS. **OFF** appears in the cursor. (Figure 7-87)
- 6. **ENTER** Key DEPRESS to turn **OFF** the **AUTO WX UPDT** function.

*NOTE: A Weather Update Request must be performed to notify the GDC of the change in status of AUTO WX UPDT.*

*Figure 7-85*

*Figure 7-86*

*Figure 7-87*

## *RETURNING TO AUTO WX UPDT*

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**. (Figure 7-88)

3. **ENTER** Key - DEPRESS.

*Figure 7-88*

- 4. Line Select Key DEPRESS to position cursor over **OFF** option of **AUTO WX UPDT** field. (Figure 7-89)
- 5. **BACK** Key DEPRESS. **ON** appears in the cursor. (Figure 7-90)

*Figure 7-89*

6. **ENTER** Key - DEPRESS to turn **ON** the **AUTO WX UPDT** function.

*NOTE: A Weather Update Request must be performed to notify the GDC of the change in status of AUTO WX UPDT.*

*Figure 7-90*

## **VHF AND SATELLITE NETWORK OPERATING MODES**

The status of each network is held in non-volatile memory. When the system is initialized, all networks will prefill with the status at system shut-down. The following procedures allow the VHF and satellite networks to be manually operated, turned **OFF**, or returned to **AUTO**.

## *TURNING VHF NETWORK OFF*

The VHF network has precedence over the satellite network in areas of shared coverage and must be turned **OFF** in order for **SATCOM** to be the Active Link.

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**. (Figure 7-91)
- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **ON** option of **VHF NETWORK** field. (Figure 7-92)
- 5. **BACK** Key DEPRESS. **OFF**? appears in the cursor. (Figure 7-93)
- 6. **ENTER** Key DEPRESS to turn the VHF network **OFF**.

*NOTE: The ACTIVE LINK information at the bottom of the page indicates the network that is*

*Figure 7-91*

*Figure 7-92*

*Figure 7-93*

*being serviced at that time. If all networks are turned OFF or none are operational, NONE will be displayed.*

## *TURNING VHF NETWORK ON*

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**.
- AFIS OPERATING MODES AUTO REPORT ON AUTO WX UPDT ON VHF NETWORK OFF SAT NETWORK ON ACTIVE LINK: SATCOM > > >
- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **OFF** option of **VHF NETWORK** field. (Figure 7-94)
- 5. **BACK** Key DEPRESS. **ON**? appears in the cursor. (Figure 7-95)
- 6. **ENTER** Key DEPRESS to turn VHF network on. **VHF LINK CONTROL** Page

appears. (Figure 7-96)

*Figure 7-94*

*Figure 7-95*

*NOTE: The ACTIVE LINK information at the bottom of the page indicates the network that is being serviced at that time.*

7. Line Select Key - DEPRESS to position cursor over **AUTO** option of desired ground network.

*Figure 7-96*

## *TURNING AUTO TO MAN OR OFF*

*NOTE: SITA/AVICOM are two different ground networks covering different regions. The appropriate network is automatically selected for operation based on current Lat/Lon location of aircraft, if mode is set to AUTO.*

- 8. **BACK** Key DEPRESS until **MAN** or **OFF** appears in the cursor.
- 9. **ENTER** Key DEPRESS to select **MAN** or **OFF**.

*NOTE: If MAN is selected, all other networks will indicate OFF. (Figure 7-97)*

10. Repeat Steps 7 through 9 to turn **OFF** desired ground networks or DEPRESS

*Figure 7-97*

**ENTER** Key to cursor through option fields and return to **AFIS OPERATING MODES** Page.

## *RETURNING TO AUTO*

- 11. Line Select Key DEPRESS to position cursor over **OFF** or **MAN** option of desired ground network.
- 12. **BACK** Key DEPRESS until **AUTO** appears in cursor. (Figure 7-98)
- 13. **ENTER** Key DEPRESS to select **AUTO** option.
- 14. Repeat Steps 11 through 13 to return desired ground networks to **AUTO** or DEPRESS **ENTER** Key to cursor through option fields and return to AFIS Operating Modes Page.

*Figure 7-98*

## *TURNING SATELLITE NETWORK OFF*

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**. (Figure 7-99)

3. **ENTER** Key - DEPRESS.

*Figure 7-99*

- 4. Line Select Key DEPRESS to position cursor over ON option of **SAT** (satellite) **NETWORK** field. (Figure 7-100)
- 5. **BACK** Key DEPRESS. **OFF**? appears in the cursor.

*Figure 7-100*

6. **ENTER** Key - DEPRESS to turn the satellite network **OFF**. (Figure 7-101)

*NOTE: The ACTIVE LINK information at the bottom of the page indicates the network that is being serviced at that time. If all networks are turned OFF or none are operational, NONE will be displayed.*

*Figure 7-101*

## *TURNING SATELLITE NETWORK ON*

The satellite network must be turned **ON** to send non-flight related messages. Since the VHF network has precedence over the satellite network in areas of shared coverage, the **VHF NETWORK** must be turned OFF in order for SATCOM to be the Active Link. If the VHF network cannot be received and the SAT-COM mode is set to ON the system will automatically select the SATCOM mode for transmit and receive.

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**.
- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **OFF** option of **SAT NETWORK** field. (Figure 7-102)
- 5. **BACK** Key DEPRESS. **ON**? appears in the cursor. (Figure 7-103)

*NOTE: The ACTIVE LINK information at the bottom of the page indicates the network that is being serviced at that time.*

6. **ENTER** Key - DEPRESS to turn satellite network on. **SAT** (satellite) **LINK CONTROL** Page appears with cursor over **AUTO**. (Figure 7-104)

*Figure 7-102*

*Figure 7-103*

*Figure 7-104*

DEPRESS **ENTER** Key to cursor through option fields and return to **AFIS OPERATING MODES** Page or proceed to Step 7.

## *TURNING AUTO TO MAN*

- 7. Line Select Key DEPRESS until **MAN** appears in the cursor.
- 8. **ENTER** Key DEPRESS. Cursor moves to **REGION** field.
- 9. **BACK** Key DEPRESS until desired region appears in cursor, either **W. Atlantic**, **E. Atlantic**, **Pacific**, or **Indian**. (Figure 7-105)

*NOTE: All other regions are now considered OFF.*

11. **ENTER** Key - DEPRESS to ACTIVATE the SAT network link as operational and return to **AFIS OPERATING MODES** Page.

*Figure 7-105*

*Figure 7-106*

*NOTE: When in MAN mode, the ACTIVE LINK will display NONE until the aircraft is within the boundaries of the selected region.*

## *RETURNING TO AUTO*

- 12. Line Select Key DEPRESS to position cursor over **MAN** field.
- 13. **BACK** Key DEPRESS until **AUTO** appears in cursor.
- 14. **ENTER** Key DEPRESS to select **AUTO** option. Cursor moves to the **LINK** field.
- 15. **ENTER** Key DEPRESS to ACTIVATE the SAT network link as operational and return to **AFIS OPERATING MODES** Page.

## **PRINTER CTRL**

The AFIS DMU has two RS-232 printer interfaces. Users may print messages or weather to either or both printer ports. Automatic printing is also available. Controls for these options, as well as Auto Form Feed control, are accessed on the **PRINTER CONTROL** page. Access the **PRINTER CONTROL** page by line selecting the **PRINT-ER CTRL** field on the **OPERATING MODES** page and pressing **ENTER**.

## *MESSAGE DEST*

The Message Destination field is used to assign the printer port that will be used when messages are printed. Messages can be sent to printer port 1 (**PRT1**), printer port 2 (**PRT2**), or **BOTH**.

- 1. **AFIS** key DEPRESS to display **AFIS MENU** page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**.
- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over the **PRINT-ER CTRL** field. **SEL** will appear in the field.
- 5. **ENTER** Key DEPRESS to access the **PRINTER CONTROL** page.
- 6. Line Select Key DEPRESS to position cursor over **MESSAGE DEST**.
- 7. **BACK** Key DEPRESS to cycle destination field between **PRT1**, **PRT2**, and **BOTH**.
- 8. **ENTER** Key DEPRESS to set Message Destination field to its present value (**PRT1**, **PRT2**, or **BOTH**.)

## *WEATHER DEST*

The Weather Destination field is used to assign the printer port that will be used when weather is printed. Weather can be sent to printer port 1 (**PRT1**), printer port 2 (**PRT2**), or **BOTH**.

- 1. **AFIS** key DEPRESS to display **AFIS MENU** page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**.

- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **SEL** option of **PRINTER CTRL** field.
- 5. **ENTER** Key DEPRESS to access the **PRINTER CONTROL** page.
- 6. Line Select Key DEPRESS to position cursor over **WEATHER DEST**.
- 7. **BACK** Key DEPRESS to cycle destination field between **PRT1**, **PRT2**, and **BOTH**.
- 8. **ENTER** Key DEPRESS to set Message Destination field to its present value (**PRT1**, **PRT2**, or **BOTH**.)

## *AUTO FORM FEED*

The Auto Form Feed option, when set to YES, will cause the printer to Form Feed, or eject the page, after each message or weather report is printed. Setting the Auto Form Feed option to NO will print messages and weather reports on the same page until the page is full, then eject the page.

- 1. **AFIS** key DEPRESS to display **AFIS MENU** page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**.
- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **SEL** option of **PRINTER CTRL** field.
- 5. **ENTER** Key DEPRESS to access the **PRINTER CONTROL** page.
- 6. Line Select Key DEPRESS to position cursor over **AUTO FORM FEED**.
- 7. **BACK** Key DEPRESS to toggle Auto Form Feed option between **YES** and **NO**.
- 8. **ENTER** Key DEPRESS to set Auto Form Feed to its present value (**YES** or **NO**.)

## *AUTO PRINT MSG*

The Auto Print Message field is used to select or deselect the automatic printing of messages. If **AUTO PRINT MSG** is set to **YES**, then messages will automatically be printed upon receipt. If **AUTO PRINT MSG** is set to **NO**, then messages will not be printed upon receipt.

- 1. **AFIS** key DEPRESS to display **AFIS MENU** page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**.
- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **SEL** option of **PRINTER CTRL** field.
- 5. **ENTER** Key DEPRESS to access the **PRINTER CONTROL** page.
- 6. Line Select Key DEPRESS to position cursor over **AUTO PRINT MSG**.
- 7. **BACK** Key DEPRESS to toggle Auto Print Message field between **YES** and **NO**.
- 8. **ENTER** Key DEPRESS to set Auto Print Message field to its present value (**YES** or **NO**.)

## *AUTO PRINT WX*

The Auto Print Weather field is used to select or deselect the automatic printing of weather. If **AUTO PRINT WX** is set to **YES**, then weather will automatically be printed upon receipt. If **AUTO PRINT WX** is set to **NO**, then weather will not be printed upon receipt.

- 1. **AFIS** key DEPRESS to display **AFIS MENU** page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**.
- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **SEL** option of **PRINTER CTRL** field.
- 5. **ENTER** Key DEPRESS to access the **PRINTER CONTROL** page.
- 6. Line Select Key DEPRESS to position cursor over **AUTO PRINT WX**.

- 7. **BACK** Key DEPRESS to toggle Auto Print Weather field between **YES** and **NO**.
- 8. **ENTER** Key DEPRESS to set Auto Print Weather field to its present value (**YES** or **NO**.)

## **PRINTING PROCEDURES**

## *PRINTING FLIGHT PLANS*

Following is a step by step procedure to print a flight plan in the aircraft:

*Note: The aircraft must be specially REGISTERED with the Global Data Center (GDC) for this feature.*

- 1. Enable **AUTO PRINT WX** from the printer control page of the **AFIS OPERATING MODES** page.
- 2. Select **SEND AFIS MSG** from the **AFIS MENU**.
- 3. Leave the **TO** and **FR** fields blank. At the address (#) field, type: **PRFPD1234**, where D1234 is the flight plan number.
- 4. Transmit the request to the GDC.
- 5. When uplinked, the flight plan will be treated like weather and will print automatically.

## *PRINTING MESSAGES*

Messages may be printed automatically as the message is uplinked, and/or individually at any time.

## *To Automatically Print Messages Upon Receipt:*

1. Select **AUTO PRINT MSG** from the AFIS OPERATING MODES, PRINTER CONTROL page, to **YES**. All uplinked messages will print automatically upon receipt.

## *To Manually Print a Message:*

- 1. While reviewing the message, line select one of the white caret symbols at the bottom of the message page.
- 2. The **PRINT MESSAGE?** prompt will display. Press **ENTER** to send the message to the printer currently selected for messages.

## *To Manually Print All Messages:*

- 1. From the **AFIS MENU**, select the **SEND AFIS MSG** page.
- 2. On the send message page, leave the **TO** and **FR** fields blank. At the address (#) field, type ONE of the following commands:

**MSG 1** Send messages to printer one. **MSG 2** Send messages to printer two. **MSG 3** Send messages to both printers.

3. Press **ENTER** until the **SEND MESSAGE?** prompt is displayed. Press **ENTER** again to initiate printing to the specified printer(s).

## *PRINTING WEATHER*

SIGMETS, Winds Aloft, and Terminal Weather may be printed automatically or manually.

## *To Automatically Print SIGMETS, Winds Aloft, and Terminal Weather Upon Receipt:*

1. Select **AUTO PRINT WX** from the AFIS OPERATING MODES, PRINTER CONTROL page. All SIGMETS, Winds Aloft, and Terminal Weather reports will print automatically as they are received.

## *To Manually Print All SIGMETS, Winds Aloft, or Terminal Weather:*

- 1. From the **AFIS MENU**, select the **SEND AFIS MSG** page.
- 2. On the send message page, leave the **TO** and **FR** fields blank. At the address (#) field, type ONE of the following commands (note- there is a space between the command and the numeral, ex. SIG<space>1):

| SIG 1 | Send SIGMETS to printer one.       |
|-------|------------------------------------|
| SIG 2 | Send SIGMETS to printer two.       |
| SIG 3 | Send SIGMETS to both printers.     |
|       |                                    |
| WND 1 | Send Winds Aloft to printer one.   |
| WND 2 | Send Winds Aloft to printer two.   |
| WND 3 | Send Winds Aloft to both printers. |

## **SELECTING OPERATING MODES (FOR AFIS USERS NOT EQUIPPED WITH SATELLITE DATA COMMUNICATIONS SYSTEM)**

## *AUTO REPORTING*

When the system is initialized, the Automatic Reporting and or Auto Wx update function will retain the status at aircraft shutdown. The following procedures allow the function to be turned **OFF** and back **ON**.

*Figure 7-107*

## *TURNING AUTO REPORT OFF*

- 1. **AFIS** Key DEPRESS to display AFIS MENU Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**. (Figure 7-107)
- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **ON** option of **AUTO REPORT** field. (Figure 7-108)
- 5. **BACK** Key DEPRESS. **OFF** appears in the cursor. (Figure 7-109)
- 6. **ENTER** Key DEPRESS to turn **OFF** the **AUTO REPORT** function.

*NOTE: If all ground networks are OFF, then AUTO REPORT will be OFF.*

*Figure 7-108*

*Figure 7-109*

## *RETURNING TO AUTO REPORT*

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**. (Figure 7-110)
- AFIS MENU < 1 AFIS FLT PLAN 2 SIGMETS 3 TERMINAL WX 4 WINDS ALOFT 5 RECALL AFIS FPL 6 SEND AFIS MSG 7 DISPL AFIS MSG 8 OPERATING MODES

*Figure 7-110*

- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **OFF** option of **AUTO REPORT** field. (Figure 7-111)
- 5. **BACK** Key DEPRESS. **ON** appears in the cursor.
- 6. **ENTER** Key DEPRESS to turn **ON** the **AUTO REPORT** function. (Figure 7-112)

*Figure 7-111*

*NOTE: If all ground networks are OFF, then AUTO REPORT will be OFF.*

*Figure 7-112*

## *AUTO WEATHER UPDATE*

When the system is initialized, the Automatic Weather Update function will retain the status at aircraft shutdown. The following procedures allow the function to be turned **OFF** and back **ON**.

## *TURNING AUTO WX UPDT OFF*

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- AFIS MENU < 1 AFIS FLT PLAN 2 SIGMETS 3 TERMINAL WX 4 WINDS ALOFT 5 RECALL AFIS FPL 6 SEND AFIS MSG 7 DISPL AFIS MSG 8 OPERATING MODES

*Figure 7-113*

- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**. (Figure 7-113)
- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **ON** option of **AUTO WX UPDT** field. (Figure 7- 114)

*Figure 7-114*

- 5. **BACK** Key DEPRESS. **OFF** appears in the cursor. (Figure 7-115)
- 6. **ENTER** Key DEPRESS to turn **OFF** the **AUTO WX UPDT** function.

*Figure 7-115*

## *RETURNING TO AUTO WX UPDT*

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**. (Figure 7-116)
- AFIS MENU < 1 AFIS FLT PLAN 2 SIGMETS 3 TERMINAL WX 4 WINDS ALOFT 5 RECALL AFIS FPL 6 SEND AFIS MSG 7 DISPL AFIS MSG 8 OPERATING MODES

3. **ENTER** Key - DEPRESS.

*Figure 7-116*

- 4. Line Select Key DEPRESS to position cursor over **OFF** option of **AUTO WX UPDT** field. (Figure 7-117)
- 5. **BACK** Key DEPRESS. **ON** appears in the cursor. (Figure 7-118)

*Figure 7-117*

6. **ENTER** Key - DEPRESS to turn **ON** the **AUTO WX UPDT** function.

*NOTE: A Weather Update Request must be performed to notify the GDC of the change in status of AUTO WX UPDT.*

*Figure 7-118*

## **GROUND NETWORK OPERATING MODES**

The status of each network is held in non-volatile memory. When the system is initialized, all networks will prefill with the status at system shut-down. The following procedures allow the ground networks to be manually operated, turned **OFF**, or returned to **AUTO**.

*NOTE: SITA/AVICOM are two different ground networks covering different regions. The appropriate network is selected for operation based on current Lat/Lon location of aircraft.*

*Figure 7-119*

# *AUTO TO MAN OR OFF MODE*

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**. (Figure 7-119)

- 4. Line Select Key DEPRESS to position cursor over **AUTO** option of desired ground network field. (Figure 7-120)
- 5. **BACK** Key DEPRESS until **MAN** or **OFF** appears in the cursor.
- 6. **ENTER** Key DEPRESS to select **MAN** or **OFF** mode. (Figure 7-121)

*Figure 7-120*

*Figure 7-121*

*NOTE: If MAN is selected, all other networks will indicate OFF.*

## *RETURNING TO AUTO*

- 1. **AFIS** Key DEPRESS to display **AFIS MENU** Page.
- 2. Line Select Key DEPRESS to position cursor over **OPERATING MODES**. (Figure 7-122)
- 3. **ENTER** Key DEPRESS.
- 4. Line Select Key DEPRESS to position cursor over **MAN** or **OFF** option of ground network field. (Figure 7-123)
- 5. **BACK** Key DEPRESS until **AUTO** appears in the cursor. (Figure 7-124)
- 6. **ENTER** Key DEPRESS to select **AUTO** mode.

*NOTE: AUTO REPORT, AUTO WX UPDT, and OPER-ATING MODE selection status are stored in non-volatile memory. If the operator turns to OFF or MAN, the operator must reselect to turn ON.*

The **ACTIVE LINK** information at the bottom of the page indicates the network that is being serviced at that time. If the system is operating in automatic mode and the network selected by the present position information is turned **OFF** or none are operational, **NONE** will be displayed.

*Figure 7-122*

*Figure 7-123*

*Figure 7-124*

## **UPDATING AFIS FLIGHT PLAN AND WEATHER**

## *UPDATING AFIS FLIGHT PLAN*

- 1. **FPL** Key DEPRESS to display Active Flight Plan Page.
- 2. Active Flight Plan VERIFY the Active Flight Plan route or AMEND as necessary.
- 3. Line Select Key DEPRESS until cursor is positioned over **AFIS UPDATE?** (Figure 7- 125)
- 4. **ENTER** Key DEPRESS. **AFIS FPL UPDATE** Page appears with cursor positioned over **ACTUAL FL** value field. (Figure 7-126)

*NOTE: Values entered are checked against aircraft limitations stored in GDC computers. Invalid entries prevent cursor movement and cause the field to flash. Amend and re-enter to advance cursor.*

*Figure 7-125*

*Figure 7-126*

*NOTE: SIGMETS Winds and Terminal Wx are automatically updated when a AFIS FPL update is received.*

- 5. **ACTUAL FL** value VERIFY or INSERT actual flight level.
- 6. **ENTER** Key DEPRESS.
- 7. **ASSIGNED FL** value VERIFY or INSERT new flight level assignment.
- 8. **ENTER** Key DEPRESS.
- 9. **PAYLOAD** value VERIFY or INSERT amended payload value.
- 10. **ENTER** Key DEPRESS.
- 11. **FUEL REM** value VERIFY or INSERT amended fuel remaining value.
- 12. **ENTER** Key DEPRESS.

- 13. **CRUISE MODE** VERIFY or INSERT an amended cruise mode.
- 14. **ENTER** Key DEPRESS. The cursor positions over **TRANSMIT REQUEST**? field. (Figure 7-127)
- 15. **ENTER** Key DEPRESS to initiate a Flight Plan Update. **ACTIVE FPL** Page will appear.

*Figure 7-127*

*NOTE: For aircraft equipped with the Antenna Switching Unit, if DATA LINK DISABLED message appears DEPRESS momentary AFIS annunciator to enable the air to ground data link. Also enable VHF or satellite network.*

Wait for **DATA CENTER** AK message if sending multiple requests.

## *SELECTING UPDATE AS ACTIVE FLIGHT PLAN*

- 1. **FPL** Key DEPRESS until AFIS FLIGHT PLAN LIST Page appears with Updated Flight Plan (UPDA - XXXX). (Figure 7-128)
- 2. Line Select Key DEPRESS to position cursor over Updated Flight Plan.
- 3. **ENTER** Key DEPRESS. Cursor positions itself over **REPLACE ACTIVE FPL?**
- 4. **ENTER** Key DEPRESS to replace Active Flight Plan with Updated Flight Plan. (Figure 7-129)
- 5. ACTIVE FPL CONFIRM. Updated Flight Plan becomes the Active Flight Plan.

*Figure 7-128*

*Figure 7-129*

## **UPDATING SIGMETS**

- 1. **AFIS** Key DEPRESS to display AFIS MENU Page.
- 2. Line Select Key DEPRESS to position cursor over **SIGMETS**. (Figure 7-130)
- 3. **ENTER** Key DEPRESS to display first **SIGMETS** Page.
- 4. Line Select Key DEPRESS to position cursor over **FROM** field.
- 5. Desired Identifier INSERT.
- 6. **ENTER** Key DEPRESS.

*NOTE: Parentheses appear indicating a request has not yet been sent or received.*

- 7. Line Select Key DEPRESS to position cursor over **TO** field.
- 8. Desired Identifier INSERT.
- 9. **ENTER** Key DEPRESS.
- 10. Line Select Key DEPRESS to position cursor over **TRANSMIT REQUEST**? (Figure 7-131)
- 11. **ENTER** Key DEPRESS to initiate a SIGMET update.

*NOTE: When an updated SIG-MET is received it replaces all previous SIGMETS. If NAT is entered as FR option, a North Atlantic Tracks update is sent. (Figure 7-132)*

Wait for **DATA CENTER AK** if sending multiple requests.

*Figure 7-130*

*Figure 7-131*

*Figure 7-132*

## **UPDATING WEATHER**

- 1. **AFIS** Key DEPRESS to display AFIS MENU Page.
- 2. Line Select Key DEPRESS to position cursor over **TERMINAL WX**. (Figure 7-133)
- 3. **ENTER** Key DEPRESS to display **TERMINAL WX** Menu Page.
- 4. Line Select Key DEPRESS to position cursor in next available field. (Figure 7-134)

*NOTE: If desired, when no field is available, place cursor over an existing identifier.*

- 6. **ENTER** Key DEPRESS. The newly entered ID appears in parentheses on the Menu.
- 7. Repeat Steps (5) and (6) to enter additional requests.
- 8. Line Select Key DEPRESS to position cursor over **TRANSMIT REQUEST**?

*Figure 7-133*

*Figure 7-134*

9. **ENTER** Key - DEPRESS. Identifiers listed on this page will be transmitted to the ground via the data link.

*NOTE: Wait for DATA CENTER AK if sending multiple requests.*

## *TO UPDATE TERMINAL WEATHER DATA PAGES*

10. Access the **TERMINAL WEATHER** Data Page (Figure 7-135) by selecting an Identifier on the **TERMI-NAL WX MENU** Page.

*Figure 7-135*

## *TO INSERT A NEW IDENTIFIER*

- 11. Line Select Key DEPRESS to position the cursor over the identifier field.
- 12. IDENTIFIER INSERT. The data text fields will go blank.
- 13. **ENTER** Key DEPRESS. The **TERMINAL WEATHER** Menu Page appears with the new identifier in place of the original identifier, and the cursor positioned at the location of the original identifier selected. If there is no data available for the new identifier, it will appear in parentheses.

## **UPDATING WINDS ALOFT**

- 1. **AFIS** Key DEPRESS to display AFIS MENU Page.
- 2. Line Select Key DEPRESS to position cursor over **WINDS ALOFT**. (Figure 7-137)
- 3. **ENTER** Key DEPRESS to display **WINDS ALOFT** Menu Page.
- 4. Line Select Key DEPRESS to position cursor in next available field. (Figure 7-138)

*NOTE: If desired, when no field is available, place cursor over existing identifier.*

5. Desired Identifier - INSERT.

*NOTE: Identifier can be VOR, airport, waypoint, Lat/Lon or VORTAC ident.*

6. **ENTER** Key - DEPRESS. The newly entered ID appears in parentheses on the Menu.

*Figure 7-137*

*Figure 7-138*

7. Repeat Steps (5) and (6) to enter additional requests.

- 8. Line Select Key DEPRESS to position cursor over **TRANSMIT REQUEST**?
- 9. **ENTER** Key DEPRESS. Identifiers listed on this page will be transmitted to the ground via the data link.

*NOTE: Wait for DATA CENTER AK if sending multiple requests.*

## *TO UPDATE THE WINDS ALOFT DATA PAGES*

10. Access the **WINDS ALOFT** Data Pages (Figure 7-139) by selecting an identifier on the **WINDS ALOFT** menu Page.

## *TO INSERT A NEW IDENTIFIER*

- 11. Line Select Key DEPRESS to position the cursor over the identifier field.
- 12. IDENTIFIER INSERT. The data text fields will go blank.

*Figure 7-139*

13. **ENTER** Key - DEPRESS. The **WINDS ALOFT** Menu Page appears with the new identifier in place of the original identifier, and the cursor positioned at the location of the original identifier selected. If there is no data available for the new identifier, it will appear in parentheses.

## **AFIS GRAPHICAL WEATHER OPERATIONS**

The AFIS functions described in this section are available only on an AFIS Data Management Unit (DMU) equipped to process graphical weather. If your AFIS DMU has not been equipped to process graphical weather the WX Graphics option will not be listed on the AFIS Main Menu. Contact your nearest Honeywell dealer or the Global Data Center for AFIS DMU upgrade information.

## **INTRODUCTION**

AFIS provides timely aviation oriented graphical weather products, which supplement the variety of AFIS textual weather. Like other AFIS messages, Weather Graphics are transmitted via VHF or satellite data transceivers. In order to provide an additional level of situational awareness, own-ship position and flight plan are overlaid on the graphical weather products. The GNS-XLS and AFIS DMU must be configured to receive and display Weather AFIS Graphical Weather. AFIS Graphical Weather hardware also includes a separate Remote Processing Unit (RPU) and installation kit. The RPU uses an updateable PCMCIA Data Card, which contains the application software, base maps, and an aeronautical database. The Data Card must remain in the RPU during use. Ask your Honeywell dealer for subscription information to ensure your unit is using the most current RPU software.

An optional SRAM PCMCIA card is available for storage of uplinked weather products during power interrupts. Uplinked AFIS Graphical Weather products that are older than 6 hours will delete automatically to prevent unintended use. It is possible to display AFIS Graphical Weather on up to two GNS-XLS units with a single AFIS DMU, however each FMS must be configured with a separate RPU. Contact your Honeywell dealer for details on dual RPU installations.

## **Available Graphical Information Includes:**

Moving map with special use airspace, geographic reference information display.

Airport and FBO directory information.

NEXRAD weather with historical replay and convective 1 hour forecast information.

CATMET/METAR weather.

Winds Aloft.

Significant Weather.

*NOTE: Individual Graphical Weather products may contain upwards of 11,000 characters. In some areas normal per character fees apply when requesting Graphical Weather products through the Satellite network. Refer to your chosen pricing plan for more details.* 

## **WX GRAPHIC IMAGERY**

## **OVERVIEW**

Four types of weather graphic maps are available from the AFIS® Weather Graphics interface: US National Next Generation Radar (NEXRAD) coverage; worldwide representation of aviation weather reports Categorical METARs (CATMET); Winds aloft reports; and Significant Weather reports (selectable options are TURB, NCWF, ICE, MISC). All of the weather graphics are viewed from the **MAP** page, one at a time.

AFIS weather graphics are displayed in the **NORTH UP** display for all regional views. NEXRAD and CATMET may also be viewed in 100 NM and 200 NM scales. The weather graphic display scales are selected from the **WX DISPLAY OPTS** page (press the blue caret line select key (LSK 3L)), or by using the "**+**" and "**-**" options from the **MAP** view.

## *NEXRAD*

The NEXRAD weather graphic displays weather conditions as shaded blocks representing the intensity of the radar returns for the selected region. See Figure 7-140. The NEXRAD is depicted with blocks that are 8km2 (approximately 4.3nm). The USA National (USANATL) and US Regional weather graphic is displayed with 64 km2 (approximately 35nm) blocks. Each

*Figure 7-140*

block is color-coded to represent the precipitation level. The absence of color-coded blocks indicates clear to very light mist. The other colors are coded as follows:

| Color  | Precipitation        | Comments                                  |
|--------|----------------------|-------------------------------------------|
| None   | None to light mist   | None                                      |
| Green  | Light rain           | None                                      |
| Yellow | Moderate rain        | Moderate thunderstorm<br>activity         |
| Red    | Heavy to severe rain | Heavy to severe thunder<br>storm activity |

*NOTE: Missing NEXRAD information is indicated by a white line across the region on the display where the NEXRAD information is missing. Subsequent NEXRAD maps with a complete transmission will overwrite the white line with the correct NEXRAD information. A dashed white line denotes the effective boundary of the NEXRAD data. Diagonal dotted blue lines will be displayed when viewing NEXRAD information on a 100nm or 200nm scale in a region where weather has not yet been received. Until a regional (8Km) NEXRAD product has been received, it is not possible to view the NEXRAD at either the 100nm or 200nm NEXRAD scale. Similarly, until the national (64Km) NEXRAD product has been received, it is not possible to view the NEXRAD at the national scale.* 

## *CATMET*

Categorical METARs (**CATMETs**) are graphical maps of ceiling, visibility and other surface weather information based on indivual METAR reports supplied by the National Weather Service. The coverage area includes airports worldwide. It is possible to slew to a CATMET airport across the display using the crosshair feature. If the aircraft position is within the selected region, the aircraft and route of flight are displayed as well.

CATMETs are graphically displayed as a two-box station-reporting square to the left of the airport identifier at 100 and 200 nautical mile ranges. Each station reporting square is divided into a two-box upper **ceiling** category and lower **visibility** category. On Regional and National scales, the CATMET icon is a one-box consolidation of the most severe level of ceiling **OR** visibility, graphically represented by the lowest level of the ceiling or visibility category. The pilot can tell at a glance airports that are at or below minimums. When selected for display, the ceiling and visibility information from the CATMET reports form a Station Reporting Square, which is placed on the left side of the airport identifier. If no CATMET information is available, no station square will be displayed. A hollow station square means no significant weather is reported at that location.

At Regional or National scale, the CATMET icon may have a small yellow box in its center. At the 100nm or 200nmscale, the CATMET reporting squares may have a red line to the left of the boxes. See Figures 7-141 and 7-142. If this box or line appears, it represents one or more of the following conditions:

Surface Winds are greater than 19 kts.

Surface Winds are greater than 10 kts. with gusts.

Ground Temperature is within +/- 5 degrees of freezing.

Temperature / Dew point spread is within 4 degrees.

Each station square is coded in the following manner:

| Station<br>Square<br>Color | Sky<br>Conditions      | Ceiling<br>(ft) | Visibility<br>(nm) |
|----------------------------|------------------------|-----------------|--------------------|
| None                       | VFR                    | > 3,000         | > 5nm              |
| Green                      | Marginal VFR<br>(MVFR) | 1,000 – 3,000   | 3nm – 5nm          |
| Yellow                     | IFR                    | 500 – 1,000     | 1nm – 3nm          |
| Red                        | Low IFR (LIFR)         | < 500           | < 1nm              |

*Figure 7-141*

*Figure 7-142*

Surface categorical winds are divided into eight magnetic directions and eight wind velocity indications. If winds are "light and variable", the CATMET wind indicator will show "N<10 KNOTS".

| Magnetic<br>Direction | Velocity<br>Indicator |
|-----------------------|-----------------------|
| 338 < D < 022         | V < 10 kts            |
| 023 < D < 067         | 10 < V < 15 kts       |
| 068 < D < 112         | 15 < V < 20 kts       |
| 113 < D < 157         | 20 < V < 25 kts       |
| 158 < D < 202         | 25 < V < 30 kts       |
| 203 < D < 247         | 30 < V < 35 kts       |
| 248 < D < 292         | 35 < V < 40 kts       |
| 293 < D < 337         | V > 40 kts            |
|                       |                       |

The Freezing danger indicator is based on the reported ground temperature and is coded as follows:

**LOW** = surface temperature is not within 5 degrees C of freezing **HIGH** = surface temperature is within ±5 degrees C of freezing

The TEMP/DEW SPREAD display options ar "LESS THAN 4C" or "GREATER THAN 4C", and provides the pilot with an indication of the surface temperature and dewpoint spread. See Figure 7-143.

*Figure 7-143*

## *SIG WX*

The SIG WX weather graphic displays areas of forecast meteorological phenomena such as turbulence, National Convective Weather Forecasts, icing, and miscellaneous (low and high pressure centers, warm and cold fronts, and jet stream location). See Figures 7-144 through 7-147. The **SIG WX** map may be viewed at 100 NM scales or higher in the affected regions. Each SIG WX product must be viewed one at a time. If the aircraft and/or route of flight is located within the specified region, they too will appear.

*Figure 7-144*

*Figure 7-145*

*Figure 7-146*

*Figure 7-147*

## *WINDS*

The WINDS weather graphic provides worldwide wind information, and displays forecast wind direction and speed in a color coded format at the following flight levels and altitudes:

| Altitude / Flight Level | Pressure Level |
|-------------------------|----------------|
| Surface*                | 1000 Mb        |
| 10,000 msl              | 700 Mb         |
| 18,000 msl              | 500 Mb         |
| FL 240                  | 400 Mb         |
| FL 300                  | 300 Mb         |
| FL 340                  | 250 Mb         |
| FL 390                  | 200 Mb         |
| FL 450                  | 150 Mb         |
| FL 510                  | 100 Mb         |

*NOTE: Surface Winds are part of the CATMET and will not be displayed unless that product has been received.*

Wind speed is coded in the following manner for all but surface winds:

| Color  | Wind Speed  |
|--------|-------------|
| Green  | 0 - 30 kts  |
| Yellow | 30 - 60 kts |
| Red    | > 61 kts    |

For surface winds, wind speed is coded in the following manner:

| Color Wind | Speed       |
|------------|-------------|
| Green      | 0 - 10 kts  |
| Yellow     | 10 - 20 kys |
| Red        | > 20 kts    |

*NOTE: Although WIND data is available worldwide, occasionally WIND data is not available at all the listed altitudes in every region of the world due to a lack of source data. When WIND data is not available for a particular altitude or flight level, that map will display the geographic image without the WIND overlay.* 

#### **CONFIGURATION SELECTION FOR WX GRAPHICS**

#### **GENERAL PAGE SELECTION OVERVIEW FOR WX GRAPHICS**

## **GETTING STARTED**

## **FROM THE AFIS MENU**

Access the **WX GRAPHICS** functions by selecting option 1 (LSK 1L) from the **AFIS MENU**. See Figure 7-148. For all other AFIS functions, select options 2 through 9 from the **AFIS MENU**. If **WX GRAPHICS** is not configured or installed, the **AFIS MENU** will not list **WX GRAPH-ICS** as an option.

*Figure 7-148*

## **NORMAL OPERATIONS**

1. For normal operation, access the WX GRAPHICS functions by selecting option 1 (LSK 1L) from the AFIS MENU. The first time AFIS Graphical Weather is accessed after powering the system on, the 50 NM Moving Map page will appear with your position centered on the map. See Figure 7-149. If you exit and

*Figure 7-149*

return to the AFIS Graphical Weather functions, the system will return to the last WX Graphics page accessed.

2. From the 50 NM Moving Map page, select LSK 3L (Blue caret) to access **WX DISPLAY OPTS** page. Select **WX REQT** (LSK 4R) to request AFIS Graphical Weather products. Read on for more detailed procedures on requesting or using AFIS Graphical Weather.

## **GRAPHICAL WEATHER DEMO MODE**

## **OVERVIEW**

For safety reasons, operation of AFIS Graphical Weather should be learned on the ground. To facilitate learning, AFIS Graphical Weather may be configured in a demonstration mode as described in this section. The **DEMO** mode does not transmit, but still provides all button functionality using stored graphical weather examples from the RPU. Entering the demo mode will not affect other AFIS functions.

At power-up the RPU system will default to the normal Weather Graphics operating mode. There is also a Weather Graphics Demonstration mode. Access to the **DEMO** mode is available by selecting LSK 1R from the Weather Graphics **MAIN MENU**.

*WARNING: In DEMO MODE the graphical weather is NOT CUR-RENT WEATHER and should only be used for training or demonstration purposes. Be careful not to leave the weather graphics configuration in a demo mode during flight.*

## **FOR DEMO MODE**

You may place the RPU in a demonstration mode by first accessing the AFIS Wx Graphics function, and then select LSK 1R from the Weather Graphics **MAIN MENU**. The demo mode is used for crew training or demonstration purposes. In demo mode the RPU uses pre-stored (canned) weather images for practice or training.

- 1. Access the demo function by first selecting **WX GRAPHICS** (LSK 1L) from the **AFIS MENU**.
- 2. Go to **MAIN MENU** page by selecting the LSK 1R (unmarked).
- 3. From the **MAIN MENU**, press LSK 1R (unmarked) to access the **DEMO** initialization page. See Figure 7- 150.
- 4. Select **YES** using LSK 3L (green arrow) to highlight your choice, and then select **ACK** (LSK 5L) to acknowledge entering the demo mode.
- 5. At the **WEATHER GRAPH-ICS DEMONSTRATION** page press any LSK key or the **ENTER** key to initialize the demo mode. See Figure 7-151.

*Figure 7-150*

*Figure 7-151*

6. All demo functions are accessed identically to normal operations from this point (see the normal operation procedures).

*NOTE: When in the DEMO mode, access the normal mode of operation by pressing LSK 1R from the MAIN MENU page to access the DEMO initiation page. Once prompted, choose DEMO "OFF" to access the normal mode again.*

## **MAP PAGE**

## **OVERVIEW**

Using position information gained from the FMS, AFIS Graphical Weather automatically tracks your flight plan and displays own-ship position and graphical weather around the aircraft position on a **MAP** page. See Figure 7-152. To access the **MAP** page, select **RETURN** (LSK 5R) from other weather graphics menu pages. You may need to press this key several times depending on which menu level you are on.

*Figure 7-152*

In addition to displaying Graphical Weather, the AFIS Graphical Weather system enables an auxiliary **Moving Map** function which plots and updates own-ship position and displays SUA geometry. The Moving Map feature is available when no graphical weather is displayed on the map. The **MAP** page automatically reverts to the Moving Map mode when no weather is displayed. The Moving Map is available on all scales, although track up is only available at scales of 200 NM and below.

AFIS Graphical Weather provides a variety of different map views including the 5 NM, 10 NM, 15 NM, 25 NM, 50 NM, 100 NM, 200 NM, Regional US, National US, and International views. Some features are not available on all map scales, see table 7-1 following.

## **Map features available on each map scale.**

|             | ATA<br>ET D<br>M<br>AT<br>C | ATA<br>D D<br>A<br>R<br>X<br>E<br>N | ATA<br>WX D<br>CANT<br>NIFI<br>G<br>SI | ATA<br>D D<br>N<br>WI | OS<br>K A/C FPL & P<br>C<br>A<br>R<br>T | AP<br>M<br>RESIZE<br>RT<br>O<br>RP<br>O<br>N AN AI<br>W T<br>SLE<br>O | RT<br>O<br>RP<br>SPLAY AI<br>O<br>NF<br>W & DI<br>TY I<br>CILI<br>SLE<br>FA |
|-------------|-----------------------------|-------------------------------------|----------------------------------------|-----------------------|-----------------------------------------|-----------------------------------------------------------------------|-----------------------------------------------------------------------------|
| NATIONAL US |                             |                                     |                                        |                       |                                         |                                                                       |                                                                             |
| REGIONAL US |                             |                                     |                                        |                       |                                         |                                                                       |                                                                             |
| 100-200 NM  |                             |                                     |                                        |                       |                                         |                                                                       |                                                                             |
| 5-50 NM     |                             |                                     |                                        |                       |                                         |                                                                       |                                                                             |

*Table 7-1*

## **WAYPOINT INFO FEATURE (LSK 1L)**

When viewing the **MAP** page, access **WAYPOINT INFO** page by pressing the icon (LSK 1L).

## **ACCESS WX DISPLAY OPTION PAGE (LSK 3L)**

When viewing any **MAP** page, access the **WX DISPLAY OPTS** page by selecting the blue caret (LSK 3L) on the left side. See Figure 7-153. Once graphical weather has been uplinked to the aircraft, you may select the desired graphical product on the **WX DISPLAY OPTS** page. Only one product may be displayed at a time.

*Figure 7-153*

## **SLEW (LSK 4L)**

With the map scale set to 200 NM or less, access the SLEW function by selecting the slew icon (LSK 4L) from the **MAP** page. The slew function is used to re-center the map on an airport.

## **SCROLL FEATURE (LSK 4L)**

With any graphical weather selected and the map scale set to 100 NM or greater, press the **Scroll** icon (LSK 4L) on the **MAP** page to scroll through all available weather graphic maps. To ascertain the timeliness of the graphical weather, check the effectivity times at the bottom of each individual product. Uplinked AFIS Graphical Weather products that are older than 6 hours will be deleted automatically to prevent unintended use.

## **RE-CENTER MAP (LSK 5L)**

With the map scale set to 200 NM or less, re-center the map by selecting the **RE-CENTER** icon (LSK 5L) from the **MAP** page. The re-center icon only appears when the map is not already centered about own-ship position.

## **ACCESS MAIN MENU (LSK 1R)**

When viewing the **MAP** page, access the **MAIN MENU** page by pressing LSK 1R (unmarked).

## **MAP SCALE INDICATOR AND SELECTION KEYS (LSK 2R AND LSK 3R)**

Map Scale is indicated on the right side of the **MAP** page between the "+" and "-" line select keys. When available, the "+" option (LSK 2R) will cause the map page to redraw with increased map scale, and the "-" option (LSK 3R) will cause the map to redraw to a smaller scale.

## **ACCESS DISPLAY MENU (LSK 4R)**

When viewing the **MAP** page, access the **DISPLAY MENU** page by pressing the **MENU** icon (LSK 4R).

## **MAIN MENU**

## **OVERVIEW**

To access the **MAIN MENU** from any **MAP** Page, select LSK 1R (unmarked), or the **MENU** icon (LSK 4R) from the **MAP** page. See Figure 7-154. Once on the **MAIN MENU**, select the corresponding line select key to choose a desired function, or select **RETURN** to return to the **MAP** page. See Figure 7-155. The **MAIN MENU** provides access to frequently used functions such as **WAYPT INFO** (used to move the map to a selected airport, or display airport facility information), **SLEW** (used to search for identifiers or redirect the screen), and **RECENTER** (used to redraw the map centered on the aircraft icon), and **DISPLAY MENU** (used to change map display settings). Also from the **MAIN MENU**, press LSK 1R (unmarked) to access the **DEMO** initialization page.

*NOTE: The available LSK functions on the MAIN MENU will vary depending on the map scale and your selected graphical weather options, as illustrated in Figures 7-154 and 7-155.*

*Figure 7-154*

## **WAYPT INFO (LSK 1L)**

## *OVERVIEW*

*Figure 7-155*

The WAYPT INFO function is accessed from the **MAIN MENU** when no weather graphics products are selected, or by selecting the Waypoint icon (LSK 1L) from the **MAP** page. The waypoint information function is used to locate airport information for specified airports.

When accessing Waypoint Information from the **MAP** page, you may either use line select keys to scroll through the list of airports, or you may use the FMS alphanumeric keypad to enter the desired airport identifier. Select **NXT** to search alphabetically up the list of airports, or select **PREV** to search alphabetically down the list of airports. When typing in an airport identifier, press **BACK** to move the cursor left one space, or press **SEL** to move the cursor right one space. When the desired identifier is shown on the bottom of the page, press **ACK** to view the airport facility information for that airport.

Airport Facility Information is available for public airports with hard surfaced runways of at least 3000 feet in length. Additionally, AFIS Graphical Weather provides FBO information for many frequented airports. Airport Facility information may include airport name, identifier, location, elevation, traffic pattern altitude, common frequencies, FBO contact numbers, and runway information.

- 1. Select **WAYPT INFO** (LSK 1L) from the **MAIN MENU**, or select the Waypoint Information icon from the **MAP** page. See Figure 7- 156.
- 2. Type the airport identifier, then press **ACK** (LSK 5L) to view the airport facility information for a specific airport. See Figure 7-157.
- 3. Press the **NXT** key to go to the next page of airport information, or press the **PRV** key to return to the previous page. See Figure 7-158 and 7-159.
- 4. Press the **NXT** key again to return to the **MAP** page.

The **WAYPT INFO** page also provides a movable **Crosshair Tool** to select areas of the map while seeking airport facility information. The crosshairs on the **WAYPT INFO** page may be repositioned according to the associated green direction indicators with corresponding line select keys.

- 1. Select **WAYPT INFO** (LSK 1L) from the **MAIN MENU**, or select the Waypoint Information icon from the **MAP** page.
- 2. Use line select keys to position the crosshair near the desired airport on the map, select **ACK** (LSK 5L) to display a list of airports near that location on the map, or **EXIT** (LSK 5R) to exit the function.

*Figure 7-156*

*Figure 7-157*

*Figure 7-158*

*Figure 7-159*

- 3. Select the desired airport from the list with the associated left line select key, then press **ENTER** to display the first page of Airport Facility information for that airport. Select the **NXT** key to go to the next page or the **PRV** key to return to the previous page.
- 4. Select **RETURN** from the airport list page to return to the **MAP** page.

## **MAP SCALE**

## *OVERVIEW*

Change the MAP SCALE directly from the **MAP** page, or through the **WX DISPLAY OPTS** page. Map scales are defined as areas, or listed in nautical miles that refer to the approximate distance from top to bottom of the map window. With no graphical weather products selected, control the map scale with "**+**" and "**-**" (LSK 2R and 3R). When any graphical weather product is selected, control the map scale from the **WX DISPLAY OPTS** page as follows:

- 1. From the **MAP** page, select the blue caret (LSK 3L) to access the **WX DISPLAY OPTS** page. See Figure 7- 160.
- 2. The current scale is shown at the LSK 2R position. To change the map scale, press LSK 2R to cycle through the choices. The choices are USANATL, 100 NM, 200 NM, and regional map scales. Cycling through the map scales will also display the **LOAD**

*Figure 7-160*

*Figure 7-161*

*Figure 7-162*

## **DISPLAY MENU (LSK 4R)**

## **MAP FEATURES**

## *GEOGRAPHY*

Geographical reference features available include country and state lines, major lakes and rivers, coastlines, and large islands. To display Geographical reference information, select "**GEOG ON**" from the **DISPLAY MENU**.

## *SPECIAL USE AIRSPACE (SUA)*

Class B, Class C, Alert, Prohibited, and Restricted areas are included in the Special Use Airspace option. Class D airspace will not display because many class D areas are temporary. The **SUA** setting is located on the **DISPLAY MENU**. See Figure 7-163.

## *TRACK UP*

The GNS-XLS FMS may be configured to display the map either with a **TRACK UP** depiction or a **NORTH UP** depiction. In **TRACK UP** mode the aircraft icon is centered on the map or is centered at the bottom of the map. When the FMS is tracking an active flight plan, in the **TRACK UP** mode the aircraft icon remains stationary relative to the display, while the map

*Figure 7-163*

*Figure 7-164*

moves relative to the aircraft icon. In both **TRACK UP** and **NORTH UP** modes, you may select to view the aircraft icon in either the Center or Edge position. The **TRACK UP** setting is located on the **DISPLAY MENU**. See Figure 7-164.

*NOTE: TRACK UP mode is only available on maps of 5 NM to 200 NM scale.*

## *NORTH UP*

In **NORTH UP** mode the aircraft icon moves across the display and the map image stays relatively fixed. As the aircraft icon nears the map edge, the map will redraw with the aircraft icon at either the opposite map edge or in the map center position. In both **TRACK UP** and **NORTH UP** modes, you may select to view the aircraft icon in either the center or edge position.

*Figure 7-165*

Choosing **A/C EDGE** in the **NORTH UP** mode will give the longest period of time before the map redraws. The **NORTH UP** setting is located on the **DISPLAY MENU**. See Figure 7-165.

*NOTE: When displaying Graphical Weather imagery, only the NORTH UP mode is available for viewing.*

## *A/C EDGE/CENTER*

The **A/C EDGE** or **CENTER** option lets you display the aircraft on the bottom edge, or in the center of the screen.

In the **A/C EDGE** mode, the aircraft icon is at the edge of the map page, thus allowing a majority of the screen to be used to display information in front of the aircraft. See Figure 7-166. If the system is set to **CENTER** mode, the aircraft icon will be in the center of the map page. See Figure 7-167.

In the **TRACK UP** display, **A/C EDGE** mode will place the aircraft on the bottom edge of the screen. In the **NORTH UP** display, **A/C EDGE** mode will display the aircraft on the edge of

*Figure 7-166*

*Figure 7-167*

the screen based on the aircraft's current true course. Both these settings are located on the **DISPLAY MENU**.

## **SLEW (LSK 4L)**

The **SLEW** function provides means to re-center the map on a specific airport by typing in an airport identifier. Access **SLEW** from the **MAIN MENU** (LSK 3L) while displaying graphical weather with the map scale set at 200 NM or less. With no graphical weather selected (map scale 200 NM or less), access **SLEW** by pressing the **SLEW** icon (LSK 4L) on the **MAP** page. When entering an identifier during functions such as slewing, the GNS-XLS FMS utilizes a feature called "ID Completion". As you enter the desired identifier, the system displays the first match for the entered characters.

**PREV** and **NEXT** line select buttons are used to scroll forward and backward through characters. **SEL** is used to select a character or to move the cursor forward. **BACK** is used to backspace a single character on a line. **ACK** is used to acknowledge the entire entry. Once you **ACK** an entry it will automatically return to the map window.

## **IDENTIFIER PROCEDURE**

- 1. With the map scale set to 200 NM or less while displaying graphical weather, select **SLEW** (LSK 4L) from the **MAIN MENU**. See Figure 7-168. The **SELECT POSITION** page will display. See Figure 7-169.
- 2. On the **SELECT POSITION** page type the desired airport identifier then press **ENTER** to re-center the map on that airport.
- 3. Or, use the **NEXT** or **PREV** keys to scroll to the first character of the airport identifier, and then press **SEL** to accept the character. Do not press **ACK** until the desired airport identifier is showing. Pressing **SEL** will also move the cursor one space to the right in preparation for

*Figure 7-168*

*Figure 7-169*

selection of the next character. A solid line cursor appears underneath the character to be entered or changed in the **WPT IDENT** area. Select **NEXT** to scroll to the next character. For example, if '**A**' is displayed, selecting **NEXT** scrolls to '**B**'. Selecting **PREV** will return to the previous character.

- 4. Repeat step 3 above for each character of the airport identification. Select **BACK** to edit any previously accepted character.
- 5. If the aircraft icon is not visible on the map after redrawing the map to different position, the map will display "**OFF MAP**" to indicate that the map does not represent your current position. The **RE-CENTER** icon will re-center the map to own-ship position.

## **CROSSHAIR PROCEDURE**

The Crosshair provides a means to re-center the map on an area of the existing map view with a crosshair pointer.

- 1. With the map scale set to 200 NM or less, select **SLEW** (LSK 3L) from the **MAIN MENU**, or press the **SLEW** icon from the **MAP** page.
- 2. The **MAP** page will display again with the crosshair tool visible on the page. See Figure 7-170. Use the associated line select keys following the arrows to reposition the crosshair tool to the desired point on the map.
- 3. Select **ACK** when the crosshair is at the correct position on the map. The map page will re-center on the chosen point of the map.

*Figure 7-170*

4. If the aircraft icon is not visible on the map after redrawing the map to different position, the map will display "**OFF MAP**" to indicate that the map does not represent your current position. The **RE-CENTER** icon will re-center the map to own-ship position.

## **RECENTER (LSK 5L)**

With the map scale set to 200 NM or less, access **RECENTER** centers the map on the aircraft's position.

## **RE-CENTER PROCEDURE**

1. With the map scale set to 200NM or less (while graphical weather is selected), select **RECENTER** (LSK 5L) from the **MAIN MENU**. See Figure 7-171. Or, when no graphical weather is selected, press the **RE-CENTER** icon from the **MAP** page.

2. The **MAP** page will redraw with the aircraft icon centered on the map.

*Figure 7-171*

## **WX REQUEST PAGE**

## **OVERVIEW**

Access the **WX REQUEST** page from the **WX DISPLAY OPTS** page. This page is used to request real-time **NEXRAD**, **CATMET**, forecast **SIG WX** and forecast **WINDS** aloft weather graphics.

The weather graphic request is transmitted from the aircraft through VHF or SATCOM networks worldwide to the Global Data Center (GDC). The GDC receives the request and verifies that an updated version of the requested weather product is available. If an updated product exists, it is transmitted to the aircraft. If an update is not available an AFIS message indicating that the aircraft already has the most current map is transmitted to the aircraft.

When a weather graphic product has been received, there will be a "**Y**" next to that product on the appropriate **WX REQUEST** page indicating it is available for viewing. If the requested product is not available, the GDC will issue an AFIS message to the aircraft indicating that the requested AFIS Wx graphics product is not currently supported and the letter "**X**" will appear on the appropriate **WX REQUEST** page next to the requested product. Example: **CATMET: X**

## **PROCEDURE OVERVIEW**

To request weather graphics, from the **WX REQUEST** page, press the desired weather graphic product line select key i.e., **NEXRAD**, **CATMET**, **SIG WX**, or **WINDS**. See Figure 7- 172. One or all available WX GRAPHICS products may be requested at the same time. After selecting the desired weather graphic product for example, **NEXRAD**, a page may appear displaying available WX GRAPHICS regions. See Figure 7-173. Press the desired region line select key. The selected region is indicated with a reverse video display highlighted. Press the **RETURN** line select key to return to the **WX REQUEST** page. Next, back on the **WX REQUEST** page press the **SEND WX REQT** line select key to transmit request to the GDC for processing.

*Figure 7-172*

*Figure 7-173*

*NOTE: Be sure to check for currency for each chart after displaying the new or updated chart to ensure you are viewing the most current weather information. The available weather graphic codes on the bottom of the WX DISPLAY OPTS page indicate which products have been uplinked and are available for viewing. Multiple products may be requested simultaneously. Users are advised to be judicious about the number of weather products requested when awaiting other AFIS messages, such as a PDC or flight plan recall.* 

## **REQUEST NEXRAD WEATHER GRAPHIC**

Although NEXRAD is currently available only for the continental U.S., border areas of Canada and Mexico, and limited areas in the Caribbean, NEXRAD maps come in National and Regional (64km2 and 8km2 ) display options. Any region may be selected, however areas not supported will display map information.

- 1. From the **MAP** Page, access the **WX DISPLAY OPTS** page by selecting the **Blue Caret** (LSK 3L) on the left of the screen. See Figure 7-174.
- 2. Press **WX REQT** (LSK 4R) on the **WX DISPLAY OPTS** page to display the **WX REQUEST** page. See Figure 7-175.

*Figure 7-174*

- 3. On the **WX REQUEST** page, press **NEXRAD** (LSK 1L) to display the NEXRAD geographical regions.
- 4. On the **NEXRAD** page, press the line select key corresponding to the desired region, then press **RETURN** (LSK 5R) to display the **WX REQUEST** page. Transmit the request by pressing **SEND WX REQT** (LSK 4R).

*Figure 7-175*

- 5. After pressing the **SEND WX REQT** line select key, **PENDING** displays during the transmission process. When the transmission is complete **PENDING** is replaced with **SEND WX REQT** and the requested item is shown in brackets until the product has been received.
- 6. When the product has been received, the brackets will go away, and there will be a "**Y**" next to the product label on the **WX REQUEST** page indicating that the map is available for viewing. Also, an available weather graphic code indication will display on the bottom of the **WX REQUEST** page.

The weather graphic codes indications are:

**NX** = NEXRAD **CT** = CATMET **FD** = WINDS **SW** = SIG WX

## **HISTORICAL NEXRAD REPLAY FUNCTION**

A **Historical NEXRAD** replay function is available on request, and provides a historical replay of time sequenced NEXRAD products on the **MAP** page when the US REPLAY product is stored in the RPU. The maximum number of maps uplinked in each Historical NEXRAD reply product is limited to five plus the current NEXRAD product, but there may be fewer historical NEXRAD maps available in the event that the file size exceeds the maximum size limit.

1. From the **MAP** page, press the **HISTORY** icon (LSK 5L) with the **NEXRAD** feature displayed. See Figure 7- 176. There must be a sufficient number of NEXRAD images stored in memory to utilize the **Historical NEXRAD** replay feature.

*Figure 7-176*

## **REQUEST CATMET WEATHER GRAPHIC**

**CATMET** (METAR) reports are available for all listed regions of the world.

- 1. From the **MAP** page, access the **WX DISPLAY OPTS** page by selecting the **Blue Caret** (LSK 3L) on the left of the screen.
- 2. Press **WX REQT** (LSK 4R) on the **WX DISPLAY OPTS** page to display the **WX REQUEST** page.

3. On the **WX REQUEST** page, press **CATMET** (LSK 2L) to select the CATMET product. See Figure 7-177. *Figure 7-177*

- 4. Transmit the request by pressing **SEND WX REQT** (LSK 4R).
- 5. After pressing the **SEND WX REQT** line select key, **PENDING** displays during the transmission process. When the transmission is complete **PENDING** is replaced with **SEND WX REQT** and the requested item is shown in brackets until the requested item has been received. See Figure 7-178.

*Figure 7-178*

6. When the product has been received, the brackets will go away, and there will be a "**Y**" next to the product label on the **WX REQUEST** page indicating that the map is available for viewing. Also, a weather graphic code indication will display on the bottom of the **WX REQUEST** page. The weather graphic code indications are as follows:

> **NX** = NEXRAD **CT** = CATMET **FD** = WINDS **SW** = SIG WX

## **REQUEST SIG WX WEATHER GRAPHIC**

Turbulence and icing are currently available only for the continental U.S., border areas of Canada and Mexico, and limited areas in the Caribbean. Other regions will be added in the future. Miscellaneous significant weather information is available worldwide and contains fronts, the jet stream, and events such as hurricanes and convective storms.

- 1. From the **MAP** page, access the **WX DISPLAY OPTS** page by selecting the **Blue Caret** (LSK 3L) on the left of the screen.
- 2. Press **WX REQT** (LSK 4R) on the **WX DISPLAY OPTS** page to display the **WX REQUEST** page. See Figure 7-179.

*Figure 7-179*

- 3. On the **WX REQUEST** page, press **SIG WX** (LSK 3L) to display the SIG WX geographical regions. See Figure 7-180.
- 4. On the **SIG WX** page, press the line select key corresponding to the desired region, then press **RETURN** (LSK 5R) to display the **WX REQUEST** page. Transmit the request by pressing **SEND WX REQT** (LSK 4R).
- 5. After pressing the **SEND WX REQT** line select key, **PENDING** displays during the transmission process. When the transmission is complete **PENDING** is replaced with **SEND WX REQT** and the requested item is shown in brackets

*Figure 7-180*

*Figure 7-181*

until the requested item has been received. See Figure 7-181.

6. When the entire product has been received, the brackets will go away, and there will be a "**Y**" next to the product label on the **WX REQUEST** page indicating that the map is available for viewing. Also, a weather graphic code indication will display on the bottom of the **WX REQUEST** page. The weather graphic code indications are as follows:

> **NX** = NEXRAD **CT** = CATMET **FD** = WINDS **SW** = SIG WX

The following is a list of available SIG WX products:

**TURB** = Turbulence Forecast

**NCWF** = National Convective Weather Forecast

**ICE** = Icing Forecast

**MISC** = Miscellaneous Significant Weather Information

*Note: Significant weather is uplinked as three separate files, one containing turbulence and icing information; the second contains worldwide High Significant weather charts and NEXRAD cell top information for the U.S., and the third file contains the National Convective Weather Forecast. Due to the size of the second file it may require more time to uplink this product.* 

## **REQUEST WINDS WEATHER GRAPHIC**

WINDS Aloft information is available for all displayed regions, from the surface up to FL510 (flight level 510).

- 1. From the **MAP** page, access the **WX DISPLAY OPTS** page by selecting the **Blue Caret** (LSK 3L) on the left of the screen.
- 2. Press **WX REQT** (LSK 4R) on the **WX DISPLAY OPTS** page to display the **WX REQUEST** page. See Figure 7-182.
- 3. On the **WX REQUEST** page, press **WINDS** (LSK 4L) to display the WINDS geographical regions. See Figure 7-183.
- 4. On the **WINDS** page, press the line select key corresponding to the desired region, then press **RETURN** (LSK 5R) to display the **WX REQUEST** page. Transmit the request by pressing **SEND WX REQT** (LSK 4R).
- 5. After pressing the **SEND WX REQT** line select key, **PENDING** displays during the transmission process. When the transmission is

*Figure 7-182*

*Figure 7-183*

complete **PENDING** is replaced with **SEND WX REQT** and the requested item is shown in brackets until the requested item has been received. See Figure 7-184.

6. When the product has been received, the brackets will go away, and there will be a "**Y**" next to the product label

*Figure 7-184*

on the **WX REQUEST** page indicating that the map is available for viewing. Also, a weather graphic code indication will display on the bottom of the **WX REQUEST** page. The weather graphic code indications are as follows:

**NX** = NEXRAD **CT** = CATMET **FD** = WINDS **SW** = SIG WX

The following is a list of available WIND products:

| Altitude / Flight Level | Pressure Level |
|-------------------------|----------------|
| Surface*                | 1000 Mb        |
| 10,000 msl              | 700 Mb         |
| 18,000 msl              | 500 Mb         |
| FL 240                  | 400 Mb         |
| FL 300                  | 300 Mb         |
| FL 340                  | 250 Mb         |
| FL 390                  | 200 Mb         |
| FL 450                  | 150 Mb         |
| FL 510                  | 100 Mb         |

*<sup>\*</sup>Surface Winds are part of the CATMET and will not be displayed unless that product has been received.*

Wind speed is coded in the following manner for all but surface winds:

| Color  | Wind Speed |
|--------|------------|
| Green  | 0 - 30kts  |
| Yellow | 30 - 60kts |
| Red    | > 61kts    |

For surface winds, wind speed is coded in the following manner:

| Color  | Wind Speed |
|--------|------------|
| Green  | 0 - 10kts  |
| Yellow | 10 - 20ks  |
| Red    | > 20kts    |

*NOTE: Although WIND data is available worldwide, occasionally WIND data is not available at all the listed altitudes in every region of the world due to a lack of source data. When WIND data is not available for a particular altitude or flight level, that map will display the geographic image without the WIND overlay.*

## **DISPLAY WX GRAPHICS**

When the initial weather graphic request is received by the RPU, the available weather graphic products are accessed from the **WX DIS-PLAY OPTS** page. Weather graphics received by the aircraft are displayed with an **OFF** just to the right. **OFF** indicates that the weather graphic product is available but is not turned on. By pressing the corresponding line select key next to the received weather graphic product, **OFF** will toggle to **ON**, enabling the weather graphic to be displayed. But, before displaying the weather graphic product, first select the scale of the weather graphic. Only one weather graphics product at a time may be displayed. For example, toggling **WINDS ON** will toggle **NEXRAD OFF**.

With any graphical weather selected and the map scale set to 100 NM or greater, press the **Scroll** icon (LSK 4L) on the **MAP** page to scroll through all the weather graphic products selected **ON**. To ascertain the timeliness of the graphical weather, check the effectivity times at the bottom of each individual product. Uplinked AFIS Graphical Weather products that are older than 6 hours will delete automatically to prevent unintended use.

*NOTE: If the aircraft position or route of flight (depicted from the active flight plan in the GNS-XLS) is located in the selected region it is also displayed in weather graphic page.* 

## **WX DISPLAY OPTIONS**

## **OVERVIEW**

To access the **WX DISPLAY OPTIONS** page, press the line select key (LSK 3L) corresponding to the caret on the left side of the **MAP** page. Prior to requesting a graphical weather product, the initial **WX DISPLAY OPTS** screen has only two line select options **WX REQT** and **RETURN**. When weather graphics are available, the weather graphic code displays on the status line at the bottom left corner of the **MAP** page. The weather graphic codes are as follows: NEXRAD "**NX**"; CATMET "**CT**"; SIG WX "**SW**"; WINDS "**FD**". Also, when a weather graphic product has been received, there will be a "**Y**" next to that product on the appropriate **WX REQUEST** page indicating it is available for viewing. If the requested product is not available, the Global Data Center will issue an AFIS message to the aircraft indicating that the requested product is not currently supported and the letter "**X**" will appear on the appropriate **WX REQUEST** page next to the requested product .

*NOTE: If any weather graphic is selected ON, the moving MAP PAGE will not display.*

## **DISPLAY NEXRAD WX GRAPHIC**

Some NEXRAD data is available when "**NX**" displays on the status line. NEXRAD products are available in a 100 NM scale or higher. From the **MAP** page, press "**+**" or "**-**" (LSK 2R and 3R) to resize the map if desired. The "**NX**" code indicates that a NEXRAD product is available for display, unless an 8km NEXRAD has been requested and received, the 100 and 200 NM products will not be available.

- 1. To display the **WX DISPLAY OPTS** page from the **MAP** page, press the **Blue Caret** (LSK 3L) on the left side of the **MAP** page.
- 2. Press the **NEXRAD** line select key to toggle the NEXRAD from **OFF** to either the **ON**, **NX/CELL TOPS**, or **NX/NCWF** settings, where:

**ON** = NEXRAD Map

**NX/CELL TOPS**= NEXRAD Map with Cell Tops

**NX/NCWF** = NEXRAD Map with National Convective Weather Forecast

3. After selecting a NEXRAD product to display, on the WX DISPLAY OPTS page press REGL DISPLAY (LSK 2R) to change the map scale, or you may change scale later by pressing "+" or "-" from the MAP page. Press RETURN to view the MAP page. See Figure 7-185.

Figure 7-185

NOTE: Cell Tops and Convective Weather Forecast are uplinked as part of the SIG WX product and will not be displayed unless that product has been received. Missing NEXRAD information is indicated by a white line across the region on the display where the NEXRAD information is missing. Subsequent NEXRAD maps with a complete transmission will overwrite the white line with the correct NEXRAD information. A dashed white line denotes the effective boundary of the NEXRAD data. Diagonal dotted blue lines will be displayed when viewing NEXRAD information on a 100nm or 200nm scale in a region where weather has not yet been received. Until a regional (8Km) NEXRAD product has not been received, it is not possible to view the NEXRAD at either the 100nm or 200nm NEXRAD scale. Conversely, until a national (64Km) NEXRAD product has been received, it is not possible to view the NEXRAD at the National or Region scale.

#### HISTORICAL NEXRAD REPLAY

A **Historical NEXRAD** replay function is available on request, and provides a historical replay of time sequenced NEXRAD products on the **MAP** page when a US REPLAY product is stored in the RPU. The maximum number of maps uplinked in each Historical NEXRAD reply product is limited to five plus the current NEXRAD product, but there may be fewer historical NEXRAD products available in the event that the file size exceeds the maximum size limit.