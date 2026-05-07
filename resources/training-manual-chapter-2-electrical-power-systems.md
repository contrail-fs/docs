# CHAPTER 2 ELECTRICAL POWER SYSTEMS

## **CONTENTS**

| F                                              | Page |
|------------------------------------------------|------|
| INTRODUCTION                                   | 2-1  |
| GENERAL                                        | 2-1  |
| DC System                                      | 2-2  |
| AC System                                      | 2-2  |
| DC POWER SYSTEM                                | 2-3  |
| Distribution                                   | 2-3  |
| BAT (1 or 2)                                   | 2-6  |
| AC POWER SYSTEM                                | 2-23 |
| Normal Inverters (Pilot, Copilot, and Standby) | 2-23 |
| Two-Inverter System                            | 2-24 |
| INS Inverter                                   | 2-26 |
| LIMITATIONS                                    | 2-29 |
| DC Power Limitations                           | 2-29 |
| AC Power Limitations                           | 2-29 |
| Starter Limitations                            | 2-29 |
| TROUBLESHOOTING                                | 2-30 |
| CIRCUIT-BREAKER LISTING                        | 2-34 |
| OUESTIONS                                      | 2-36 |

## ILLUSTRATIONS

| Figure | Title<br>Page                                     |      |
|--------|---------------------------------------------------|------|
| 2-1    | Electrical Component Locations                    | 2-2  |
| 2-2    | Electrical Control Panel                          | 2-3  |
| 2-3    | Circuit-Breaker Panels                            | 2-4  |
| 2-4    | Bus Tie Relay Circuit Breakers (Rear Compartment) | 2-5  |
| 2-5    | Battery Indications                               | 2-7  |
| 2-6    | Battery Temperature Indicator<br>                 | 2-7  |
| 2-7    | Hot Battery Bus Circuitâ€”After S/B 318<br>         | 2-8  |
| 2-8    | DC Operation                                      | 2-9  |
| 2-9    | Starter-Generator and APU Generator               | 2-9  |
| 2-10   | Generator Indications<br>                         | 2-11 |
| 2-11   | DC Electrical Systemâ€”Configuration No. 1          | 2-12 |
| 2-12   | DC Electrical Systemâ€”Configuration No. 2          | 2-13 |
| 2-13   | DC Electrical Systemâ€”Configuration No. 3          | 2-14 |
| 2-14   | DC Electrical Systemâ€”Configuration No. 4          | 2-15 |
| 2-15   | DC Electrical Systemâ€”Configuration No. 5          | 2-16 |
| 2-16   | DC Electrical Systemâ€”Configuration No. 6          | 2-17 |
| 2-17   | DC Electrical Systemâ€”Configuration No. 7          | 2-18 |
| 2-18   | DC Electrical Systemâ€”Configuration No. 8          | 2-19 |
| 2-19   | DC Electrical Systemâ€”Configuration No. 9          | 2-20 |
| 2-20   | DC Electrical Systemâ€”Configuration No. 10         | 2-21 |
| 2-21   | DC Electrical Systemâ€”Configuration No. 11         | 2-22 |
| 2-22   | Ground Power<br>                                  | 2-23 |
| 2-23   | Inverter Control and Indication<br>               | 2-25 |

|       | FALCON 50 PILOT TRAINING MANUAL        |      |
|-------|----------------------------------------|------|
|       |                                        |      |
| 2-24  | AC Power System<br>                    | 2-26 |
| 2-25  | Simplified AC Power System<br>         | 2-27 |
| 2-26  | Total Electrical System                | 2-28 |
| 2-27  | Start and Dry Motoring Sequence        | 2-29 |
| 2-28  | Trouble Situations                     | 2-30 |
|       | TABLES                                 |      |
| Table | Title                                  | Page |
| 2-1   | Nicad Battery Specifications           | 2-6  |
| 2-2   | Ground Power Functions and Indications | 2-24 |
| 2-3   | Circuit-Breaker Listing                | 2-34 |

## CHAPTER 2 ELECTRICAL POWER SYSTEMS

## INTRODUCTION

The electrical system for the Falcon 50 consists of the DC system, the AC system, and their distribution. For aircrafts with an auxiliary power unit (APU) installed, a discussion on APU operation is included. The electrical chapter concludes with a section on specific limitations.

## GENERAL

Electrical power is provided by a 28.5-volt DC supply system and by a 115-volt, 400-Hz and a 26-volt, 400-Hz power supply system. The DC system supplies 28.5 volts to the battery, start, main, and secondary buses which,

in turn, supply 28.5-volt power for inverter conversion. Since DC power must be available before AC power is possible, this chapter begins with the DC power system.

## DC SYSTEM

The DC power system is supplied by the three engine-driven, 9-kw, 300-ampere starter-generators, as shown in Figure 2-1. For aircrafts with an APU installed, a fourth generator, driven by the APU, is provided.

Two 23-ampere-hour batteries are used. They provide a backup source of DC power and a means of starting the engines on the ground or in the air. Ground power may be connected to the aircraft via a ground power receptacle; it can be used to start the engines, APU, or to power the electrical system. It cannot be used to charge aircraft batteries.

The DC power is distributed by two independent subsystems which may be interconnected for safety reasonsâ€”and to minimize the effect of a distribution failure. The various aircraft components to be supplied are divided between the two systems. In addition, within each system, the services to be supplied are again divided between two distribution buses. One directly supplies a components bus through a cockpit-controlled relay. These controlled buses are called load-shed buses.

## AC SYSTEM

Aircraft not equipped with modification M1703 will have a three-inverter system consisting of inverter No. 1, inverter No. 2, and a standby inverter. This will include aircraft from SN 003 through SN 224. When the inverter switches are selected to on, DC power is applied to the 750-VA solid-state statictype inverters which, in turn, produce AC power and distribute it to the AC power buses. If either of these inverters fail, a third inverter

Figure 2-1. Electrical Component Locations

(standby inverter) may be selected to provide AC power in place of the failed inverter. If an inertial navigation system (INS) is installed, a fourth inverter is provided to power the INS exclusively.

Most of the aircraft SN 225 through SN 252 will be equipped with just two 350-VA solidstate static-type inverters. There is no standby inverter in this system. If an inverter fails, that inverter's bus system will be without power with no way to supply it from any other source. This is called the "simplified power AC generation system."

## DC POWER SYSTEM

## DISTRIBUTION

## DC Buses

The distribution of DC power is through the left-hand (LH) and right-hand (RH) main buses. These buses are located in the lower section of the DC main power center in the rear compartment. They are isolated to ensure separation of the LH and RH distribution center circuits.

The LH main bus supplies the primary A bus and auxiliary C bus which may be load shed (Figure 2-2).

Figure 2-2. Electrical Control Panel

The RH main bus supplies the primary B bus and the auxiliary D bus, which also may be load shed.

## Circuit Breakers

For circuit protection, there are three circuitbreaker panels (Figure 2-3) that collectively control DC power distribution. The LH panel contains some of the breakers for buses A and C. The center circuit breaker panel contains most of the breakers for buses A, B, C, and D. The RH panel, however, contains breakers for buses A, B, and D. All breakers are color coded to indicate either primary circuit (white), secondary circuit (green), both primary buses (red), or AC (gray) association.

Figure 2-3. Circuit-Breaker Panels

Load shedding, a means of quickly reducing the overall DC load, is provided through two switches on the electrical control panel. The LH switch sheds the C bus, and the RH switch sheds the D bus. Either switch will cause shedding of the flight compartment dome lights, entrance lighting, rear compartment light, nose area light, and baggage compartment lighting.

## Current Limits

The generators are operationally limited to a continuous current of 300 amperes and load limiting of 350 amperes for 1 minute. Each generator can supply maximum current at an operating speed of 6,200-12,000 rpm up to an altitude of 39,000 feet. Above 39,000 feet, the amperage load is limited to 250 amperes. Each battery has a continuous initial charge current rating of 220 amperes. Above 250 amperes, the BAT switch trips, in 50 seconds (time proportional to charge current).

## Bus Tie System

A bus tie switch is provided to interconnect buses when No. 3 generator fails or any two generators fail without a bus short. This switch controls a relay which connects the LH and RH main buses in the main power center.

Figure 2-4 shows the circuit for the bus tie relay. The circuit breakers are located in the rear compartment. Circuit breaker 51p2 provides continuity for the 3-minute time delay associated with generator output reduction during engine start.

The bus tie relay can be energized from either bus. If either circuit breaker is popped, the other provides continuity. To determine which is popped, both voltmeters must be read.

Figure 2-4. Bus Tie Relay Circuit Breakers (Rear Compartment)

## Batteries

There are two 20-cell, nickel-cadmium batteries located in the rear compartment. The nominal voltage is 24-26 volts with an output capacity of 23 ampere-hours in parallel (Table 2-1).

Individually or in series, these batteries can be used to start the engines or to provide power to other aircraft services. The APU cannot be started in series.

Battery control is incorporated into the DC SYS-TEM panel in the form of individual switches, one switch for each battery. The battery switches will automatically trip in the event of a reverse flow to the battery of 250 amperes or more.

To indicate battery functioning and provide for current monitoring, pushbutton switchlights are provided on the DC SYSTEM panel, as shown in Figure 2-3. The switchlights illuminate blue when depressed, thus indicating that they are operating properly and, at the same time, that the ammeter is connected to the corresponding battery circuit.

## BAT (1 OR 2)

A light on the master warning panel (Figure 2-5) is provided to indicate the disconnection of the batteries from the main bus, and a HOT BAT light indicates battery overtemperature. Two temperature probes are connected in parallel to a HOT BAT light on the master

### Table 2-1. NICAD BATTERY SPECIFICATIONS

### CAPACITY

- 23 amps/hour
- 20 cells
- 24 to 26 volts
- 22 volts minimum start limitations for engine start/23 volts minimum for APU start
- If generators fail, 20 minutes in load shed, 10 minutes if EFIS-equipped

### PROTECTION

### RCR:

- 18 volts minimum to close
- 8 to 11 volts to hold closed (RCR opens no trip)
- Opens with a reverse current of 250 amps, switches trip (50 sec.)

### INDICATION

- Volts and amps
- Temperature indication, American planesâ€”Less 50Â°
- Warning lights

### MISC.

- Blower cooled on ground (No. 2 battery switch), venturi air-cooled in fight
- Aircraft will draw:
- Left main busâ€”50 amps\*
- Right main busâ€”30 amps\*

<sup>\*</sup> Upper-limit values

Figure 2-5. Battery Indications

warning panel. The light comes on if the internal temperature of either battery reaches 150Â°F. Each probe is also connected to a battery temperature indicator on the copilot instrument panel. The indicator is provided with a temperature scale for each battery (Figure 2-6). In addition, an amber WARM light on the temperature indicator comes on when the temperature of either battery exceeds 120Â°F; a HOT light for either battery comes on at 150Â°F. There is a LESS 50Â°F pushbutton which provides a means of reading an off-scale value. When the button is depressed, 50Â°F must be subtracted from the indicated value for a true temperature reading.

Figure 2-6. Battery Temperature Indicator

## Operation

As soon as the batteries are connected, the No. 1 battery supplies power for the battery bus and the start bus. The No. 2 battery supplies power directly to the battery bus only.

Figure 2-7 shows the hot battery bus circuit.

## NOTE

Certain items of equipment are directly supplied from the battery bus. They are:

â€¢ Lighting system

- Pressure refueling system
- Fire extinguishers
- APU door-closing circuit (early aircrafts only; later aircrafts supplied from B bus)

The power-up sequence is described below. Position BAT 1 switch to ON (Figure 2-8).

In this mode, the No. 1 battery supplies power to the LH main bus. The LH main bus then energizes the A and C buses. Power is applied to some master warning panel lights, and the BAT 1 indicator light is out.

Figure 2-7. Hot Battery Bus Circuitâ€”After S/B 318

### NOTE

The battery switches will automatically trip in the event of an excessive charge rate.

As soon as power is on the A bus, the blue BAT 1 light comes on, and the LH main bus voltage will be indicated on the LH voltmeter. The LH ammeter indicates current being supplied by the No. 1 battery.

### NOTE

It is not necessary to depress the battery blue light unless a generator is selected first.

The BAT 2 switchlight performs a similar function for the RH side.

Figure 2-8. DC Operation

## Generators

The three engine-driven starter-generators are identical (Figure 2-9).

Figure 2-9. Starter-Generator and APU Generator

Generator characteristics are as follows:

- Maximum nominal voltage adjusted to 28.5 VDC
- Maximum authorized outputâ€”300 amperes maximum continuous and 250 amperes above FL 390
- Operating speedâ€”6,200 to 12,000 rpm

The starter-generators are self-cooled and have a starting amperage draw of 900 amperes. The APU generator has a starting amperage draw of 600 amperes.

Each starter-generator operates in conjunction with a control unit (GCU) and performs the following functions:

- Regulates voltage to 28.5 VDC
- Load-shares between generators
- Provides 32-VDC overvoltage protection
- Provides generator load limitation of 375 amperes
- Reduces generator output to 27.5 VDC for 3 minutes if any engine or the APU is started

In addition, the GCU progressively weakens the field of the corresponding starter-generator during engine starting and limits battery charging current following engine starting.

Each starter-generator is connected to one of the main buses through a reverse-current relay.

Connection is made when the starter-generator output voltage exceeds the bus voltage by 0.3 to 0.8 VDC.

The connecting circuit is broken for a reversecurrent. This occurs when the respective generator is being overpowered by a supply on the bus or, the respective generator cannot maintain the required potential matching the other generators on line with it.

The engine-driven starter-generators are mounted on the underside of each engine within the cowling. The APU generator is located in the aft compartment within the APU shroud.

To facilitate generator control, there are guarded isolation switches located on the main power center. When closed, they apply 28.5 VDC to close the generator load-sharing relays. They are also used to isolate individual generators from the main bus by opening the generator RCR for adjustment and test when the aircraft is on the ground. These switches are normally used for maintenance applications.

The generator-control switches located on the overhead control panel are mechanically latched and serve to control generator excitation. If a generator fails because of overvoltage or overcurrent, the corresponding switch automatically returns to the OFF position. Returning the switch to the ON position should accomplish normal reset.

Generator operation can be verified by depressing the blue GEN switchlight shown in Figure 2-10. When depressed, the light illuminates and the corresponding generator's current is displayed on the ammeter.

If for any reason the starter-generator becomes isolated from the system it normally supplies, the corresponding amber GEN light on the annunciator panel illuminates.

The starter-generators provide power for the main DC buses and, in certain cases, the start bus.

ILLUMINATE BLUE WHEN DEPRESSED AND DISPLAY CORRESPONDING GENERATOR CURRENT ON THE AMMETER

SUPPLIES

Figure 2-10. Generator Indications

During start, voltage from the batteries and the APU or one operating generator (Figure 2-10) energizes the engine starter-generator. The generator function of the starter-generator can be connected to the aircraft power supply only if the starter function is concluded. When the start is complete, the generator failure warning light on the master warning panel goes out. Simultaneously, this voltage is applied to the regulating and equalizing circuits. With the bus tie switch in flight NORMAL, the generators supply power as follows:

- Engine No. 1 starter-generator (S/G 1) supplies power for the LH main DC bus.
- Engine No. 2 starter-generator (S/G 2) supplies power for the LH main DC bus.
- Engine No. 3 starter-generator (S/G 3) supplies power to the RH main DC bus.
- The APU generator supplies power for the RH main DC bus.

Note that the APU starter-generator is identical with the other engine-driven units. When the APU reaches 95%, the generator function produces electrical power and ties it to the aircraft electrical system.

Eleven different configurations of the DC electrical system are shown in Figures 2-11 through 2-21.

Figure 2-11. DC Electrical Systemâ€”Configuration No. 1

Figure 2-12. DC Electrical Systemâ€”Configuration No. 2

Figure 2-13. DC Electrical Systemâ€”Configuration No. 3

Figure 2-14. DC Electrical Systemâ€”Configuration No. 4

Figure 2-15. DC Electrical Systemâ€”Configuration No. 5

Figure 2-16. DC Electrical System â€” Configuration No. 6

Figure 2-17. DC Electrical Systemâ€”Configuration No. 7

Figure 2-18. DC Electrical Systemâ€”Configuration No. 8

Figure 2-19. DC Electrical Systemâ€”Configuration No. 9

Figure 2-20. DC Electrical Systemâ€”Configuration No. 10

Figure 2-21. DC Electrical Systemâ€”Configuration No. 11

## Ground DC Power

A GPU can be used to start the engines, and the APU to power the electrical system.

The ground power receptacle (Figure 2-22) is located on the rear, RH side of the fuselage. A corresponding circuit is provided for overvoltage protection. Whenever the external power receptacle is used, the batteries' APU and engine generators are isolated from the system.

The voltage from a GPU must be 28 volts DC. The external power system includes a protection circuit that cuts off voltage at the receptacle if it increases to 32 volts. In addition, external power automatically drops off if voltage decreases to below 8 volts.

To apply external power, the DC power selector switch must be moved to the EXT POWER position. This applies power to the LH main bus but can be routed to the RH main bus through the bus tie relay. The bus tie switch placed in the tied position will cause the BUS TIED light to illuminate.

When external power is supplied to the aircraft, the BAT 1, BAT 2, GEN 1, GEN 2, and GEN 3 lights on the master warning panel will be illuminated.

Table 2-2 lists ground power functions and indications.

## AC POWER SYSTEM

## NORMAL INVERTERS (PILOT, COPILOT, AND STANDBY)

The AC power system is supplied by three single-phase, 750-va static inverters, each producing outputs of 115-volt, 400-Hz power and 26-volt, 400-Hz power.

For operation, all three inverters require 28 Â±2 volts DC. The pilot inverter receives power from the A bus, the copilot inverter from B bus and the standby inverter control power from B bus with operating power from the RH main.

Figure 2-22. Ground Power

Table 2-2. GROUND POWER FUNCTIONS AND INDICATIONS

| GPU POWER ON                                                                                                                                                 | GPU POWER OFF                                                                                                                        |  |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|--|
| DC Power Selectorâ€”Normal                                                                                                                                     | DC Power Selectorâ€”Normal                                                                                                             |  |
| â€¢<br>Battery switchesâ€”On<br>Result: Battery power to main buses<br>OR<br>â€¢<br>Battery switchesâ€”Off<br>Result: Main buses not powered                         | â€¢<br>Battery switchesâ€”On<br>Result: Battery power to main buses<br>OR<br>â€¢<br>Battery switchesâ€”Off<br>Result: Main buses not powered |  |
| DC Power Selectorâ€”External Power                                                                                                                             | DC Power Selectorâ€”External Power                                                                                                     |  |
| â€¢<br>Battery switchesâ€”On or off<br>Result: Batteries isolate from main<br>buses, No. 1 battery blue amp light on,<br>No. 1 and No. 2 amber battery lights on | â€¢<br>Battery switchesâ€”On<br>Result: Main buses not powered<br>OR<br>â€¢<br>Battery switchesâ€”Off<br>Result: Main buses not powered      |  |

Inverter control is accomplished by the use of switches located on the overhead panel. The switches for the pilot and copilot inverters are two-position switches. In the ON position, the auxiliary loop used to supply control power for the inverter is closed. The OFF position removes power from the inverter.

The standby inverter (Figure 2-23) is controlled by a three-position switch located between the other inverter switches. In the center position, when on the ground, the inverter is used in parallel with the INS inverter to warm up the INS. When in the LH position, the inverter replaces the pilot inverter. In the RH position, it replaces the copilot inverter.

For operation indications, a voltmeter and AC bus 1 and AC bus 2 switchlights are used. The voltmeter is used for both of the 115-volt AC circuits and also for INS power displays. The switchlightsâ€”AC bus 1, AC bus 2, and INS when depressed, connect the voltmeter to the corresponding circuit.

Amber AC 1 and AC 2 indicator lights on the master warning panel illuminate for zero inverter output or a frequency drift of Â±30 Hz, from 400 Hz (SB 214 also includes voltage drops of 5% from 26V). These lights sense only the 26-vac buses.

The operating sequence is to power the DC buses and set the inverter circuit breakers. Movement of the pilot or copilot inverter control switches to ON will activate the corresponding inverter. If either pilot or copilot inverter fails, moving the standby inverter's control switch to the LH or RH position provides power to the failed inverter's circuits with priority.

## TWO-INVERTER SYSTEM

On the aircraft equipped with the two-inverter system, the inverters are single-phase, solid state, static-type which are rated at 350 VA and producing 115 volts at 400-Hz and 26 volts at 400-Hz power.

During normal operation, the two-inverter switches are placed in the ON position which will supply 28 volts to the inverters. The pilot inverter receives power from the A bus and the copilot inverter receives power from the B bus. Even though these inverters produce 115 volts and 26-volts AC power, only the 115-volt output is used on the aircraft equipped with this system.

The inverters are controlled with switches located on the overhead panel, same as the

Figure 2-23. Inverter Control and Indication

three-inverter system. However, this system does not have a voltmeter to display the 115-volt output. The only monitoring device is the AC 1 and AC 2 light in the warning panel. This light monitors a fault signal from the inverter itself. When the inverter voltage drops excessively low, or its frequency varies from 400 Hz by more than Â±30 Hz, the AC warning light will illuminate to indicate an inverter failure.

### **INS INVERTER**

The INS inverter, located in the baggage compartment, has characteristics identical with those of the normal inverters. It requires an input of  $28 \pm 2$  volts DC to produce 115 volts

AC for the INS bus. It also has a 26-volt AC output that is not used.

Distribution of the 115 volts AC is through the INS bus to the INS. Whenever the RH main bus is powered, the inverter is activated through a 50-amp fuse. When the INS is in alignment or in standby mode, the standby inverter is put in parallel with the INS inverter to warm up the INS to 70Â°F when it is cold.

Two supply systems distribute power: system 1, or pilot AC system, which feeds the 115-vac and 26-vac buses; and system 2, or copilot AC system, which feeds the 115-vac and 26-vac buses (Figure 2-24 and 2-25).

Figure 2-24. AC Power System

The total electrical system is shown in Figure 2-26.

Figure 2-25. Simplified AC Power System

Figure 2-26. Total Electrical System

## **LIMITATIONS**

### DC POWER LIMITATIONS

Generators are operationally limited to a maximum output of 350 amperes for one minute. Up to 39,000 feet, they are limited to a steady maximum of 300 amperes. Above 39,000 feet, a steady maximum of 250 amperes is the limit.

The maximum bus load voltage for which the DC system has been designed is 32 volts.

### **AC POWER LIMITATIONS**

Inverter input voltage must be a positive  $28 \pm 2$  volts DC.

Current consumption under a full load is 39 amperes; under zero load, it is 1.5 amperes. Total output power should not exceed 115 volts AC, 600 va, nor 26 volts AC, 150 va. The output frequency is limited to 400 Hz  $\pm$  30 Hz.

## STARTER DUTY RECOMMENDATIONS

Table 2-3 shows starter sequence limitations, and Figure 2-27 shows start and dry motoring sequence.

Figure 2-27. Start and Dry Motoring Sequence

## **TROUBLESHOOTING**

The trouble situations shown in Figure 2-28 are a visual sequence depiction to ease understanding of the electrical abnormal checklist.

### **TROUBLE SITUATION NO. 1**

CONDITIONS: LEFT VOLTMETERâ€”28.5 VOLTS BOTH GEN SWITCHESâ€”ON

CAUSE: LOW VOLTAGE FROM NO. 2 GEN

Figure 2-28. Trouble Situations (Sheet 1 of 4)

### **TROUBLE SITUATION NO. 2**

CONDITIONS: LEFT VOLTMETERâ€”INDICATES VOLTAGE INCREASING GEN 1 LIGHTâ€”ON, GEN 1 SWITCHâ€”ON

THEN

CONDITIONS:

GEN 2 SWITCHâ€”OFF
GEN 2 LIGHTâ€”ON
GEN 1 LIGHTâ€”OUT
LEFT VOLTMETERâ€”28.5 VOLTS

CAUSE: SLOW VOLTAGE FROM NO. 2 GEN

Figure 2-28. Trouble Situations (Sheet 2 of 4)

#### **TROUBLE SITUATION NO. 3**

CONDITIONS: LEFT VOLTMETERâ€”30 VOLTS BOTH GEN SWITCHES-ON

CAUSE: REVERSE CURRENT FROM NO. 2 GEN

#### **TROUBLE SITUATION NO. 4**

CONDITIONS: RIGHT VOLTMETER-24 TO 26 VOLTS AMMETER + 120 AMPS
GEN SWITCH - TRIPPED OFF

CAUSE: NO. 3 GEN HAS OVERVOLTS OR OVERAMPS

Figure 2-28. Trouble Situations (Sheet 3 of 4)

### **TROUBLE SITUATION NO. 5**

CONDITIONS: LEFT VOLTMETERâ€”VOLTAGE DROPPING AMMETERâ€”INDICATES MAXIMUM BOTH GEN SWITCHESâ€”TRIPPED OFF

CAUSE: LEFT MAIN BUS SHORTED

Figure 2-28. Trouble Situations (Sheet 4 of 4)

## CIRCUIT-BREAKER LISTING

### Table 2-3. CIRCUIT-BREAKER LISTING

BUS A

DG 1-PILOT HEADING REFERENCE SYSTEM LH GROUND/FLIGHT SWITCHES

ICS 1â€”INTERPHONE AND PUBLIC ADDRESS SYSTEM HEATING CIRCUIT FOR LH STATIC PORT

LIGHTING OF INSTRUMENTS AND CENTER PANEL NO. 1 ENGINE ANTI-ICING SYSTEM

 ANTI-COLLISION LIGHT ON VERTICAL STABILIZER PRESSURIZATION CONTROL CIRCUIT FOR LH LANDING LIGHT DUMP

 PILOT MAP LIGHT NO. 1 AND NO. 2 ENGINE HP BLEED LIGHTING OF THE PILOT DIGITAL DISPLAY SEGMENTS NO. 2 ENGINE PRV VALVE

NAVIGATION LIGHTS DEFOGGING OF SLIDING WINDOW

LIGHTING OF LH SIDE OF CONTROL PEDESTAL AIRBRAKE CONTROL SYSTEM

AUTOMATIC IGNITION CONTROL SYSTEM NO. 1 CONTROL CIRCUIT FOR SLATS

NO. 1 ENGINE INTERTURBINE TEMPERATURE AUX

N1 AND N2 ENGINE MONOPOLE SPEED SENSORS EXT TEMPâ€”ANTI-ICING OF OUTSIDE

NO. 1 ENGINE STARTING CIRCUIT FLIGHT RECORDâ€”FLIGHT RECORDER

NO. 2 ENGINE INTERTURBINE TEMPERATURE AP-RUD-YAW DAMPER

NO. 2 ENGINE N1 AND N2 MONOPOLE SPEED SENSORS AP-ELEVâ€”ELEVATOR POWER SERVO UNIT

NO. 1 ENGINE FLOWMETER INSTR 1â€”INSTRUMENTS CONNECTED TO

NO. 2 ENGINE FLOWMETER COMPARâ€”COMPARATOR

FUEL GAUGING UNITS FOR CENTER FUEL TANKS FD1â€”PILOT FLIGHT DIRECTOR

LANDING GEAR CONTROL CIRCUITS

LANDING GEAR AURAL WARNING ANNUNCIATOR

ADF 1 ELECTRICALLY-DRIVEN PUMP CONTROL CIRCUIT

DME 1 HEATING CONTROL CIRCUIT FOR PILOT WINDSHIELD

VOR 1 HEATING CIRCUIT FOR LH PITOT PROBE

VHF 1 HEATING CIRCUIT FOR LH ANGLE OF ATTACK SENSOR

ATC 1 PILOT WINDSHIELD WIPER

LH LANDING LIGHT POWER SUPPLY CONTROL CIRCUIT FOR FLIGHT COMPARTMENT AIR-CONDITIONING

READINGâ€”LIGHTING OF CIRCUIT BREAKER PANEL NO. 2 ENGINE ANTI-ICING SYSTEM

LIGHTING OF OVERHEAD INSTRUMENT PANEL ARTHUR Q UNIT MONITORING

NO. 1 INVERTER NORMAL HORIZONTAL STABILIZER CONTROL SYSTEM

THRUST REVERSER CONTROL SYSTEM INDICATION SYSTEM FOR SLATS

REVERSE CONTROL WARN AIR DATA COMPUTER

NO. 2 ENGINE COMPUTER TEMPERATURE PROBE

 NO. 2 ENGINE COMPUTER AP-AILâ€”AILERONS POWER SERVO UNIT NO. 1 ENGINE LP BOOSTER PUMP AP-CMPTRâ€”AUTOPILOT COMPUTER NO. 2 ENGINE LP BOOSTER PUMP HRZN-ST-BY PWR-STANDBY HORIZON

FUEL GAUGING UNITS OR LH TANKS THE AIR DATA COMPUTER

### BUS B

AUXILIARY POWER UNIT NO. 3 ENGINE FIRE DETECTION SYSTEM

NO. 3 ENGINE FLOWMETER CIRCUIT NO. 3 ENGINE FIRE EXTINGUISHER SYSTEM FUEL GAUGING UNITS FOR RH TANKS OMEGA NAVIGATION SYSTEM NO. 3 ENGINE LP BOOSTER PUMP HF CONTROL SYSTEM

PASSENGER CABIN AIR-CONDITIONING LIGHTING OF COPILOT SEGMENTS

BAGGAGE COMPARTMENT PRESSURIZATION NO. 3 ENGINE N1 AND N2 MONOPOLE SPEED SENSORS

BAGGAGE COMPARTMENT ISOLATION NO. 3 ENGINE STARTING CIRCUIT

NO. 2 CONTROL CIRCUIT FOR SLAT HEATING OF RH STATIC PORTS

RH POWER SUPPLY FOR MASTER WARNING PANEL FLAP INDICATOR

FUEL TRANSFER INTERCONNECTION HF POWER SYSTEM

LANDING GEAR INDICATION PASSENGER CABIN LOUDSPEAKERS

RH GROUND/FLIGHT SWITCH INTERPHONE AND PUBLIC ADDRESS CIRCUITS ANTI-SKID CIRCUIT COPILOT HEADING REFERENCE SYSTEM

BRAKE INDICATION INVERTERS IN COPILOT CIRCUIT

NO. 3 ENGINE ANTI-ICING SYSTEM ST-BY-CONTROL OF INVERTER POWER TRANSFER

NO. 3 ENGINE HP BLEED CONTROL AND SYNCHRONIZATION CIRCUIT

SHUTOFF VALVE CONTROL CABIN INDIRECTâ€”LIGHTING OF SECTIONS OF THE COPILOT

WING ANTI-ICING INSTRUMENT PANEL SEGMENTS

VALVE CONTROL NO. 3 ENGINE INTERTURBINE TEMPERATURE

INLET VALVE NO. 3 ENGINE COMPUTER

SHUTOFF VALVE RH PITOT HEATâ€”HEATING OF RH PITOT PROBE

FLAP POSITION INDICATION HEATING OF RH ANGLE OF ATTACK SENSOR

AIRBRAKES POSITION INDICATION WIPER RHâ€”COPILOT WINDSHIELD WIPER EMERGENCY HORIZONTAL STABILIZER CONTROL ROLL EMERâ€”EMERGENCY ROLL TRIM

FLIGHT CONTROL TRIM RUDDERâ€”RUDDER TRIM

RH POWER SUPPLY FOR AURAL WARNING INSTR 2â€”VIBRATOR FOR COPILOT ALTIMETER ANNUNCIATOR ANNUNC RHâ€”COPILOT WARNING ANNUNCIATOR

EMERGENCY LIGHTING SYSTEM FD2â€”COPILOT FLIGHT DIRECTOR

### Table 2-3. CIRCUIT-BREAKER LISTING (Cont)

### BUS C

CONTROL CIRCUIT FOR BAR EQUIPMENT DEFOGGING OF AFT SIDE WINDOWS

CONTROL CIRCUIT FOR PILOT AND COPILOT SEATS CABIN TEMP

STROBOSCOPIC WING LIGHTS NOSE CONE BLOWER

PRESSURE-TEMPERATURE OF OIL OF NO. 1 ENGINE A/A IND IC

NO. 1 TRANSFER PUMP POSITION INDICATOR

INERTIAL NAVIGATION SYSTEM LP 1 CROSSFEED CONTROL

RADIO ALTIMETER STEERING CIRCUIT

WEATHER RADAR MONITORING OF NO. 1 HYDRAULIC SYSTEM TAPE RECORDER EMERGENCY WING ANTI-ICING SYSTEM

PASSENGER READING LIGHTS FLIGHT COMPARTMENT TEMPERATURE REGULATION

TAXIING LIGHT HEATING CARPET IN FLIGHT COMPARTMENT

PRESSURE-TEMPERATURE OF OIL OF NO. 2 ENGINE ROLL TRIM, YAW TRIM, HORIZONTAL STABILIZER

NO. 2 TRANSFER PUMP ROLL TRIM CONTROL CIRCUIT

### BUS D

FLITE FONE COPILOT MAP LIGHT

ENGINE MONITORING AND COPILOT'S ENGINE SYNCHRONIZATION INSTRUMENT PANEL LIGHTING NO. 3 TRANSFER PUMP

COLLISION LIGHT AND RH LANDING LP 2â€“3 CROSSFEED CONTROL SYSTEM

BELTS-NO SMK'G-PASSENGER INSTRUCTIONS CABIN TEMPERATURE REGULATION

ADF 2 LIGHTING OF RH SIDE CONTROL PEDESTAL DME 2 TOILET LIGHTING SYSTEMâ€”RAZOR OUTLET

VOR 2 CABIN DISPLAY

VHF 2 POWER SUPPLY FOR RH LANDING LIGHT ATC 2 PRESSURE-TEMPERATURE OF NO. 3 ENGINE

CONTROL CIRCUITS OF BELLY ANTI- PRESSURE FUELINGâ€”REFUELING CIRCUIT

LIGHT MONITORING CIRCUIT OF NO. 2 HYDRAULIC SYSTEM

TOILET COMPARTMENT LIGHTING COPILOT WINDSHIELD ANTI-ICING CIRCUIT

FLAP CONTROL

### BATTERY BUS

EXTINGUISHER POWER SUPPLY

APU AIR INTAKE DOOR

PILOT AND COPILOT DOME LIGHTS

ENTRANCE LIGHTS

BAGGAGE COMPARTMENT, REAR COMPARTMENT

AND NOSE CONE LIGHTS

 PRESSURE REFUELING GEN 1â€“2 ENERGIZING GEN 3 ENERGIZING

## QUESTIONS

- **1.** What is the primary source of DC power when on the ground and the engines are not running?
  - A. 115-volt batteries
  - B. 26-28 volt inverters
  - C. 24-26 volt batteries
  - D. 28-30 volt generators
- **2.** Placing both BAT switches to ON causes illumination of the blue:
  - A. GEN 1 and BAT 1 lights
  - B. GEN 1 and GEN 3 lights
  - C. BAT 1 and BAT 2 lights
  - D. GEN 3 and BAT 2 lights
- **3.** Illumination of the blue BAT 1 light prompts reading of the:
  - A. Left battery voltage and ampere indicator
  - B. Left battery ampere indicator
  - C. Left battery voltmeter
  - D. None of the above
- **4.** Pushing the GEN 3 light causes the:
  - A. Blue BAT 1 light to extinguish
  - B. Blue BAT 2 light to extinguish
  - C. GEN 1 and BAT 2 lights to illuminate
  - D. Blue GEN 3 light to extinguish
- **5.** The battery reverse current relay opens if there is a:
  - A. 25-ampere continuous reverse current
  - B. Difference of 100 amperes between generators
  - C. 250-ampere continuous reverse current
  - D. Difference of 50 amperes between generators

- **6.** When the battery reverse current relay opens due to a reverse current of 250 amperes, it causes the associated:
  - A. BAT light to extinguish
  - B. BAT switch to trip
  - C. BAT light to illuminate
  - D. Both B and C
- **7.** Where are the batteries located?
  - A. Nose compartment
  - B. Rear compartment
  - C. Baggage compartment
  - D. Passenger compartment
- **8.** The HOT BAT light comes on when the battery internal temperature reaches what level?
  - A. 212Â° F
  - B. 194Â° F
  - C. 176Â° F
  - D. 150Â° F
- **9.** What preliminary warning is given to indicate that the battery is getting hot?
  - A. A buzzer sounds
  - B. An amber WARM light illuminates.
  - C. A red HOT light illuminates.
  - D. The lights on the annunciator panel flash.
- **10.** How is it possible to indicate a low battery temperature on the battery temperature indicator?
  - A. Depress the BAT 1 switchlight.
  - B. Turn the BAT switch off.
  - C. Turn the LESS 25 switch.
  - D. Depress the LESS 50 pushbutton switch.

- **11.** As soon as the batteries are connected, which battery supplies power to the start bus?
  - A. No. 1
  - B. No. 2
  - C. Emergency
  - D. Both No. 1 and No. 2
- **12.** What systems are directly supplied from the battery bus?
  - A. Lighting, hydraulic pumps, air conditioning, and APU warning light
  - B. APU door closing, hydraulic pumps, altitude warning, and lighting
  - C. Annunciator panel, oxygen system, electronic cooling, and pilot seat adjust
  - D. Lighting, pressure refueling, fire-extinguishing, and APU door closing
- **13.** When the start selector switch is in the EXT PWR position:
  - A. No. 1 battery is isolated.
  - B. No. 2 battery is isolated.
  - C. Both No. 1 and No. 2 batteries are isolated.
  - D. Neither battery is isolated.
- **14.** If a generator switch trips, what action is required to reset its output?
  - A. Move the generator switch to OFF and then to ON.
  - B. Move the generator switch to ON.
  - C. Extinguish the indicator and switch the generator to ON.
  - D. Push the reset button.
- **15.** Which engine generators supply electrical power to the main LH DC bus?
  - A. Nos. 1 and 3
  - B. Nos. 2 and 3
  - C. Nos. 1 and 2
  - D. Nos. 1, 2, and 3

- **16.** Which generators supply power to the main RH DC bus?
  - A. Nos. 1 and 3
  - B. Nos. 2 and 3
  - C. Nos. 1, 2, and 3
  - D. No. 3 and APU
- **17.** Where is the ground power receptacle?
  - A. On the left aft of the fuselage
  - B. In the nose wheel well
  - C. In the right wheel well
  - D. On the right, aft side of the fuselage
- **18.** What voltage is required from a ground power unit?
  - A. 115 volts AC
  - B. 28 volts DC
  - C. 240 volts AC
  - D. 12 volts DC
- **19.** How is ground power applied to the aircraft distribution system?
  - A. By turning the BAT switch to EXT
  - B. By selecting the DC power selector switch to EXT PWR
  - C. Automatically
  - D. By shutting off all electrical switches
- **20.** When ground power is connected and selected which lights will be illuminated?
  - A. BAT 1, GEN 1, GEN 3
  - B. BAT 2, GEN 2, GEN 3
  - C. BAT 1, BAT 2, GEN 1
  - D. BAT 1, BAT 2, GEN 1, GEN 2 GEN 3

- **21.** What voltage/Hz do the inverters produce?
  - A. 28 volts DC and 26 volts AC, 400 Hz
  - B. 115 volts AC, 400 Hz and 26 volts AC, 400 Hz
  - C. 115 volts AC, 400 Hz and 28 volts DC
  - D. 115 volts AC, 400 Hz and 26 volts DC
- **22.** If the AC 1 switch is set to ON and the standby inverter switch is full left, which inverter is supplying power to the 115- and 26-vac buses?
  - A. The INS inverter, if power is on
  - B. The pilot inverter
  - C. The standby inverter
  - D. The copilot inverter, if it is turned on
- **23.** By what means is the pilot inverter information displayed on the AC voltmeter?
  - A. Depressing the INS switchlight
  - B. Depressing the AC BUS 2 switchlight
  - C. Depressing the AC BUS 1 switchlight
  - D. Depressing the AC BUS 1 and AC BUS 2 switchlights

- **24.** If the pilot inverter frequency drifts beyond tolerance, what indication is shown?
  - A. Illumination of the AC 2 master fault light
  - B. Extinguishing of the AC 2 master fault light
  - C. Illumination of the AC 1 master fault light
  - D. Extinguishing of the AC 1 master fault light
- **25.** Which inverter(s) are in parallel with the INS inverter during warm up?
  - A. Pilot
  - B. Copilot
  - C. Pilot and copilot
  - D. Standby

