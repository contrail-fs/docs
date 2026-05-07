## FALCON 50 OPERATING MANUAL **SECTION 4**

#### TABLE OF CONTENTS

- 1 − DC POWER
  - A − General.
  - B − Tying units.
  - C − System components.
  - D − Protection and regulation.
  - E − Controls and indications.
  - F − Operation.
- 2 − AC POWER
  - A − Principle.
  - B − Power to the inverters.
  - C − Controls and indications.
  - D − System components.
- 3 − DISTRIBUTION
- 4 − ABNORMAL OPERATION OF DC POWER SYSTEM

THIS PAGE IS APPLICABLE TO MODEL : ALL

**SYSTEM DESCRIPTION** ELECTRICAL POWER

#### 1 − DC POWER

#### A − General

The 28.5 VDC which is the basic airplane electrical power is produced by three engine−driven generators.

These generators are also used as starters.

The generators deliver voltage in parallel with two 23 A/hour batteries that operate as buffers.

A ground power unit can be used to power the airplane. In such case, it is connected on the airplane GPU receptacle.

The airplane system comprises:

- 1 ) One LH main bus powered by:
  - − Battery 1.
  - − Starter−generators 1 and 2.
  - − Ground power unit (if connected, on the ground).

The LH main bus powers primary bus A and auxiliary bus C.

- 2 ) One RH main bus powered by:
  - − Battery 2.
  - − APU generator.
  - − Generator 3.

The RH main bus powers the primary bus B and auxiliary bus D.

NOTE: The main busses can be coupled by means of a coupling switch.

- 3 ) A start bus powered by:
  - a ) Normally, the two batteries in parallel.
  - b ) The batteries in series, in cold temperature start conditions.
  - c ) The ground power receptacle only in case of starting with a GPU.
  - d ) APU generator and batteries in parallel in case of an APU assist start.
  - e ) The batteries in parallel plus one generator (generator−assist start).

This bus distributes the power necessary for starting the engines.

OPERATING MANUAL **SECTION 4**

#### **SYSTEM DESCRIPTION** ELECTRICAL POWER

THIS PAGE IS APPLICABLE TO MODEL : ALL

**ELECTRICAL POWER** 

#### 4) One battery bus powered by:

- a) The two batteries.
- b) By battery 2 only when the batteries are coupled in series.

The battery bus permanently supplies through circuit breakers:

- The extinguishing system (emergency).
- The fueling power system.
- The APU door closing power system.
- The power system of the following lights:
  - Cockpit dome lights.
  - Entrance lights.
  - Aft and baggage compartment light.
  - Nose compartment portable light.

#### B - Tying units

#### 1) Batteries

Battery 1 is directly tied to the start bus and through a relay to the battery bus. Battery 2 is permanently tied to the battery bus and through a relay to the start bus. The make-and-break switches will trip for a reverse current of 250 A, or if the battery voltage has dropped to below 8 volts (start with unsufficiently charged batteries).

#### 2) Generators

- Each generator (1 and 2) is tied to the LH main bus through a reverse current relay and to the start bus through a start contactor.
- Generator No 3 is tied to the RH main bus through a reverse current relay and to the start bus through a start contactor.
- The generators are automatically tied to the main bus as soon as the generator voltage is higher than the bus voltage of 0.3 thru 0.6 V.

The reverse current relays will trip for a reverse current between 22 and 35 A. Each generator is equipped with a generator control unit for protection and regulation.

## FALCON 50 OPERATING MANUAL **SECTION 4**

**SYSTEM DESCRIPTION** ELECTRICAL POWER

#### 3 ) Ground power unit

A GPU connected to the airplane receptacle powers the start bus and the LH main bus through a GPU contactor (LOW TEMP START − NORMAL − EXT POWER selector in EXT POWER).

In such case the RH main bus will be powered when the main busses are tied together.

An overvoltage protecting unit is provided to cut−off power in the event GPU voltage becomes higher than or equal to 32 Volts.

#### C − System components

#### 1 ) Batteries

#### a ) Characteristics

- − There are two 20−elements cadmium−nickel batteries of 23 A/h each, normally coupled in parallel, and installed in the aft compartment. They are coupled in series for engine low temperature engine start on airplane power (battery voltage: 25 VDC).
- − In normal flight conditions they are connected as buffers on the main bus so as to take temporary overloads, supply the essential systems in emergency. They can be recharged in flight.
- − On the ground, with a GPU connected to the airplane. the batteries cannot be tied to airplane (system) as controlled by battery/GPU tying switch. This is aimed at protecting the batteries against overheat).

#### b ) Limitation

Each battery is equipped with a temperature probe. These probes are connected in parallel to a battery temperature indicator, located on the pilot instrument panel. This indicator includes:

- − A temperature scale for each battery.
- − A amber WARM light which illuminates when the battery temperature is higher than 50 °C (112 °F).
- − A red **HOT** light which illuminates when the battery temperature is higher than 65 °C (150 °F). This light is connected in parallel with the red **HOT BAT** light on the failure warning panel.

A blower ventilates the batteries on the ground when they are connected to the start bus. Ventilation in flight is ensured by natural air flow (due to lower pressure at the fuselage port).

THIS PAGE IS APPLICABLE TO MODEL : ALL

**ELECTRICAL POWER** 

#### 2) Generators

SYSTEM DESCRIPTION

#### a) Characteristics

The three DC generators each have a maximum power rating of 9 kw. They are protected by the generator control units that regulate the output voltage to 28 VDC and limit current to 300 A by generator.

#### b) Operation on the ground

- Airfield altitude from -1,000 ft to 10,000 ft or 14,000 ft if F50-154 SB complied with.
- The generator is self-ventilated.
- In continuous operation, each generator is capable of delivering the following currents, at 28 VDC, with an overload capacity sufficient to recharge the batteries after a start.

| N2                  | Generator RPM         | Generator ambient temperature             | Cooling air temperature                  | Maximum current |
|---------------------|-----------------------|-------------------------------------------|------------------------------------------|-----------------|
| 53 %<br>to<br>63%   | 6,500<br>to<br>7,800  | – 55 °C to + 65 °C<br>+ 65 °C to + 100 °C | – 55 °C to + 45 °C<br>+ 45 °C to + 55 °C | 300 A<br>250 A  |
| 63 %<br>to<br>100 % | 7,800<br>to<br>12,300 | – 55 °C to + 100 °C                       | – 55°C to +55°C                          | 300 A           |

#### c) In-flight operation

- Flight altitude from -1,000 ft to 45,000 ft or 49,000 ft if F50-163 SB complied with.
- Each generator can individually supply the main bus with the following currents at 28 VDC.

| N2         | Generator RPM | Altitude                                              | Maximum authorized current | Duration  |
|------------|---------------|-------------------------------------------------------|----------------------------|-----------|
| 58 %<br>to | 7,200<br>to   | 0 to 39,000 ft                                        | 300 A                      | Unlimited |
| 100%       | 12,300        | 39,000 to 45,000 ft<br>or to 49,000ft<br>(SB F50-163) | 250 A                      | Unlimited |

## FALCON 50 OPERATING MANUAL **SECTION 4**

#### D − Protection and regulation

#### 1 ) Battery make−and−break switches

The battery make−and−break switches located in the electrical center box in the aft compartment, are used to tie the batteries to the main busses (LH and RH). Should a reverse current go through this tying circuit they will trip, after a time delay that depends on the current intensity.

If the batteries are weak (voltage lower than 8 V), they will also trip (during a start for example).

#### 2 ) Generator reverse current relay

- − The reverse current relays are located in the electrical power box in the aft compartment and automatically tie the generators to the main busses when their voltage exceeds the bus voltages of 0.3 thru 0.6 V.
- − They will trip whenever a reverse current between 22 and 35 A goes from the main busses to the generators.
- − They also trip if the generator voltage drops to less than 8 volts.

#### 3 ) Generator control units (GCU)

- − The GCU's are located in the aft compartment and ensure:
  - a) Voltage control at 28.5 VDC.
  - b) Balancing of the generator currents, in parallel.
  - c) Protection against overvoltages.
  - d) Limitation of the maximum current supplied by the generators (375 A).
- − Moreover, it progressively attenuates the field at starting and limits the battery charge current after engine start. When a GPU is connected, it prevents the generators from being coupled to the airplane electrical system.

DASSAULT AVIATION Proprietary Data

### FALCON 50 OPERATING MANUAL

THIS PAGE IS APPLICABLE TO MODEL : ALL

## FALCON 50 OPERATING MANUAL **SECTION 4**

#### E − Controls and indications

The different switches and selectors used to control and check operation of DC power system are located on the "DC SYSTEM" zone of the overhead panel.

#### 1 ) Battery controls and indications

- a ) Two BAT 1 and BAT 2 switches are used to set the batteries into operation through their respective make−and−break switches. These switches are automatically returned to OFF should associated make−and−break switch trip.
- b ) Either make−and−break switch tripping will cause BAT 1 or BAT 2 light to come on warning panel.
- c ) One pushbutton light located above each battery switch is used to check the current delivered by the associated batteries or the charging current as read on one ammeter.

#### 2 ) Generator controls and indications

- a ) Three switchesGEN 1, GEN 2, GEN 3 are used to set the generators into operation through associated excitation relays. They are automatically returned to OFF if the excitation current becomes too high (7 thru 15 A) or if there is an overvoltage (U > 32.5 VDC).
- b ) Whenever the excitation relays are open. the reverse current relay will open and amber lights GEN 1 , GEN 2 or GEN 3 illuminate on warning panel.
- c ) Three pushbutton lights above the generator switches, are used to check the current readings on the ammeters (same as for the battery currents).

NOTE: When the busses are energized the blue pushbutton return automatically to BAT 1 BAT 2 (and AC Bus 1 for the AC system).

THIS PAGE IS APPLICABLE TO MODEL : ALL

**SYSTEM DESCRIPTION** ELECTRICAL POWER

#### 3 ) Main busses tie rotary selector

This is a rotative selector at upper portion of the control unit. It actuates the tying contactor and causes BUS TIED light to illuminate or extinguish on the warning panel. In horizontal position, the green mark on the selector is horizontal and pictures the main busses tying. The vertical position is the normal in−flight position and is identified FLIGHT NORM.

#### 4 ) Voltmeters

There are two voltmeters, on each side of the DC power control panel. They are calibrated from 10 thru 30 volts and display the voltage on main busses A and B.

#### 5 ) Ammeters

There are two ammeters at lower portion of the control panel, which display the "Battery" or "Generator" current.

#### 6 ) Battery temperature indicator

Temperature inside the battery is sensed by a thermistance. The temperature indicator is calibrated between 100 and 190 °F, with three color sectors:

- − 0 − 120 °F (48.9 °C) GREEN (NORMAL)
- − above 120 °F (48.9 °C) AMBER (WARM)
- − above 150 °F (65.5 °C) RED (HOT)

The red **HOT** light is connected to the red **HOT BAT** light of the warning panel.

The "LESS 50" pushbutton can be used to move the scales of reading by adding 50 °F at the battery temperature reading when it is too low to be read on normal scale (EG: 120 °F will be read for a true temperature of 70 °F)

OPERATING MANUAL **SECTION 4**

THIS PAGE IS APPLICABLE TO MODEL : ALL

**SYSTEM DESCRIPTION** ELECTRICAL POWER

#### 7 ) Warning panel

a ) Generator failure warning lights

Either of the three amber lights GEN 1 , GEN 2 , GEN 3 is illuminated when associated generator is not coupled to the airplane system (reverse current relay open).

b ) Battery failure warning lights

Either of the two amber lights BAT 1 and BAT 2 is illuminated when the associated battery is not coupled to the airplane system.

c ) Battery overheat warning light

Red **HOT BAT** light, coupled to **HOT** light of the battery temperature indicator, indicates that either battery has reached a temperature higher than 150°F (65.5°C).

d ) Coupling indicator light

Amber BUS TIED light indicates that the main bus coupling switch is set to coupled position.

#### F − Operation

1 ) Before starting

CAUTION: DO NOT USE THE BATTERIES TO TEST THE AIRPLANE CIRCUITS EXCEPT FOR SHORT DURATION TESTS.

> WHEN NO GROUND POWER UNIT IS CONNECTED, USE THE APU OR ONE ENGINE AT IDLE TO PROVIDE ELECTRICAL POWER.

While entering the airplane, check all circuit breakers are in.

Set start selector to EXT POWER or NORMAL, or LOW TEMP START according to the desired mode of starting.

EXT POWER position is used for GPU assist start.

NORMAL and LOW TEMP START positions are used for battery−assist starts, LOW TEMP START position is reserved to starts at temperatures lower than 0°C and to only the first engine.

Section 4 DTM914 Sub-section 05 REVISION 03 Page 12

## FALCON 50 OPERATING MANUAL **SECTION 4**

Set the battery switches to the on position.

Set bus tie selector to the tied position: BUS TIED light illuminates.

- a ) If power selector is set to NORMAL:
  - − Battery 1 will supply the LH main bus.
  - − Battery 2 will supply the RH main bus.
  - − BAT 1 and BAT 2 lights are out (on failure panel).
  - − RH and LH voltmeters read the voltages on the main busses.
  - − The start bus will be powered by the two batteries in parallel.
  - − GEN 1 − GEN 2 − GEN 3 lights are illuminated on warning panel.
- b ) If power selector is set to LOW TEMP START:
  - − The batteries will be coupled in series to the start bus, during starting of the first engine.
  - − Battery 2 only will power the main busses.
  - − BAT 1 light is illuminated (on warning panel).
  - − GEN 1 − GEN 2 − GEN 3 lights are illuminated (on warning panel).

To start the other engines the power selector should be set to NORMAL (batteries in parallel).

- c ) If power selector is set to EXT POWER:
  - − The ground power unit will power the start bus and the LH and RH main busses.
  - − The batteries are isolated from the airplane electrical system.
  - − BAT 1 and BAT 2 lights are illuminated.
  - − GEN 1 − GEN 2 − GEN 3 lights are illuminated.

#### 2 ) Starting

#### a ) Particularities

The optimum conditions of starting are with the batteries. Starting with a GPU should only be an occasional solution.

It is preferable to start first engine 2 then 3, then 1 since the starting of engine 3 or 1 is assisted by generator 2.

THIS PAGE IS APPLICABLE TO MODEL : ALL

SYSTEM DESCRIPTION

**ELECTRICAL POWER** 

- The first engine (preferably engine 2) can be started:
  - Using the batteries in series, in low temperature conditions (LOW TEMP START).
  - With the batteries in parallel (NORMAL) and possibly with the assistance of the APU generator (375 A in addition).
- The other engines (normally 3 and 1) will be started using the batteries in parallel and with the assistance of engine 2 generator.
   APU assistance is not used.

#### b) Starting instructions

- If the batteries are hot, temperature above 120 °F, and WARM light (amber) illuminated, do not attempt a battery start. Use a ground power unit.
- If the temperature exceeds 120 °F during starting, monitor the temperature during the next few minutes following starting.
- If the temperature exceeds 140 °F during starting, wait for its dropping to 120 °F before taking off.
- If the temperature exceeds 150 °F (illumination of HOT light (red) and HOT BAT (red) on warning panel), the battery must be isolated and monitored for cooling, and bench tested.

NOTE: As an average, the rate of cooling of a battery on the ground is 1 °F per minute.

#### c) Pre-start procedures

- Check that the circuit breakers are engaged.
- Set BAT 1 and BAT 2 switches to on.
- Set power selector to desired position ie,
  - NORMAL
  - LOW TEMP START
  - EXT POWER
- Set start selector to: GRD START.
- Set GEN 1 GEN 2 GEN 3 switches to on.
- Throttles in STOP position.
- Booster pump: on, FUEL.. light out.
- Bus tie rotary selector in tied position (BUS TIED light on).
- Computer (CMPTR) to ON.

## FALCON 50 OPERATING MANUAL **SECTION 4**

#### 3 ) Starting sequence

#### a ) Starting the first engine

Pressing the start pushbutton for two to three seconds will apply a positive voltage to the engine start contactor which closes.

#### This will cause:

- − The starter generator to be powered by the start bus bar.
- − The generator control unit to be powered with 28 VDC and develop the following commands:
  - Self maintaining of the start selector (start pushbutton may then be released).
  - Interdiction for the generator reverse current relay to close.
  - Interdiction for the balance circuit to close.

Advance the throttle to idle when N2 exceeds 10 %.

− IGN.. light comes on (ignition).

The starter generator will drive the engine at an increasing speed. This will more and more decrease the starter drive force. The "field maintaining at starting" function of the generator control unit will maintain an important torque on the drive shaft by controlling the excitation current.

When the engine speed reaches 50 % N2, the engine computer will command the generator unit to:

- Cut−off the start contactor self−maintaining circuit.
- Re−establish the balance circuit.
- Apply a command for arming the generator reverse current relay.
- IGN.. light goes out.

The generator control unit regulation circuit progressively increases the generator voltage to the regulation valve. The reverse current relay will actually close when the generator voltage exceeds the main bus bar voltage of 0.3 to 0.6 volts. The generator will then power the airplane system (associated GEN.. light extinguishes).

THIS PAGE IS APPLICABLE TO MODEL : ALL

**SYSTEM DESCRIPTION** ELECTRICAL POWER

#### **ELECTRICAL POWER**

#### b ) Starting the second engine

Set start selector to "NORMAL".

The procedure is the same but start contactor closing will cause the first engine start contactor to close and therefore couple the generator of this engine to the start bus bar (additional power of 350 A).

The second engine generator can be coupled to the airplane system (in the same conditions as for the first engine started) by closing its balance circuit (which will be in parallel with that of the control unit of the already connected generator).

The balance circuit of the first generator senses a high current (of the connected generator) and acts on the regulation circuit to lower the output power and therefore the voltage on the main bus bar.

The balance circuit of the second generator. senses a low voltage (excitation current) and will react to increase its output power to exceed the main bus bar voltage of 0.3 to 0.6 volts.

The generators are tied, the output currents will be balanced and the power of each generator is at the regulated value.

#### c ) Starting the third engine

Same principle as the second engine.

#### d ) Checking the system after starting

Since the batteries have delivered a high quantity of energy during starting, they will tend to demand a high charging current.

In order to limit this current, the voltage of the generators is lowered of 1 volt during the three minutes following the start.

After three minutes, check the generator voltage for (being again 28.5 VDC). Also check generators 1 and 2 (and 3 if coupled) for delivering the same current.

Set the coupling selector to "uncoupled".

## FALCON 50 OPERATING MANUAL **SECTION 4**

Special instructions for the batteries, in flight.

- − If WARM light comes on, monitor the temperature.
- − If the temperature continues to increase up to 140°F (60°C), the battery must be isolated.
  - At the end of the flight if the temperature drops to below 120°F, the battery may be connected again unless WARM light comes on again.
- − If the temperature reaches 150°F and causes **HOT** light to illuminate, definitively isolate the battery.
- − If after the battery has been isolated, the temperature continues to increase up to the limits, land as soon as possible.

DASSAULT AVIATION Proprietary Data

### FALCON 50 OPERATING MANUAL

THIS PAGE IS APPLICABLE TO MODEL : ALL

**SECTION 4**

Section 4 DTM914 Sub-section 05 REVISION 02 Page 18

THIS PAGE IS APPLICABLE TO MODEL : ALL WITH : M1703 MODIFICATION

Special instructions for the batteries, in flight.

- − If WARM light comes on, monitor the temperature.
- − If the temperature continues to increase up to 140°F (60°C), the battery must be isolated.
  - At the end of the flight if the temperature drops to below 120°F, the battery may be connected again unless WARM light comes on again.
- − If the temperature reaches 150°F and causes **HOT** light to illuminate, definitively isolate the battery.
- − If after the battery has been isolated, the temperature continues to increase up to the limits, land as soon as possible.

THIS PAGE IS APPLICABLE TO MODEL : ALL

WITH : M1703 MODIFICATION

**SYSTEM DESCRIPTION** ELECTRICAL POWER

AC POWER SYSTEM

Section 4 DTM914 Sub-section 05 REVISION 10 Page 18 A

**ELECTRICAL POWER** 

#### 2 - AC POWER

#### A - Principle

AC power is provided by three single-phase static inverters of 750 VA each. delivering 115 VAC – 400 Hz and 26 VAC – 400 Hz voltages. The third inverted is a stand-by inverter.

A fourth inverter identical to others. supplies the inertial navigation system (option 34-40-02).

- The pilot inverter (No 1) powers the "BUS W" and "BUS Y" with 115 VAC 400 Hz and 26 VAC – 400 Hz: this is the No 1 or pilot system.
- The copilot inverter (No 2) powers the "BUS X" and "BUS Z" with 115 VAC 400 Hz and 26 VAC - 400 Hz: this is the No 2 or copilot system.
- Should either of the above inverters fail, the third inverter can be coupled to replace the failed one.

#### B - Inverter energizations

1) Pilot inverter (No 1)

It is energized by 28 VDC primary bus "A".

2) Copilot inverter (No 2)

It is energized by 28 VDC primary bus "B".

3) Stand-by inverter

It is directly energized by the RH main bus but its control is supplied by bus B. It will operate in the following cases:

- To replace a failed pilot or copilot inverter.
- On the ground, during warning-up and alignment of the inertial navigation system.

DASSAULT AVIATION Proprietary Data

### FALCON 50 OPERATING MANUAL

THIS PAGE IS APPLICABLE TO MODEL : ALL

**SYSTEM DESCRIPTION** ELECTRICAL POWER

Section 4 DTM914 Sub-section 05 REVISION 10 Page 20

#### 2 − AC POWER

#### A − Principle

AC power is provided by two single−phase static inverters of 350 VA each, delivering 115 VAC − 400 Hz and 26 VAC − 400 Hz voltage.

- − The pilot inverted (No 1) powers the "BUS W" and "BUS Y" with 115 VAC 400 Hz and 26 VAC − 400 Hz: this is the No 1 or pilot system.
- − The copilot inverter (No 2) powers the "BUS X" and "BUS Z" with 115 VAC − 400 Hz and 26 VAC − 400 Hz: this is the No 2 or copilot system.

#### B − Inverter energizations

1 ) Pilot inverter (No 1)

It is energized by 28 VDC primary bus "A".

2 ) Copilot inverter (No 2)

It is energized by 28 VDC primary bus "B".

THIS PAGE IS APPLICABLE TO MODEL : ALL WITH : M1703 MODIFICATION

## FALCON 50 OPERATING MANUAL **SECTION 4**

#### C − Controls and indications

The control switches and selectors for the AC power system are located on the "INVERTERS" zone of the overhead panel.

#### 1 ) Inverter control switches

Two AC 1 and AC 2 switches are used to energize (AC 1) and (AC 2) inverters through their power and synchronization circuits.

A three−position ST−BY switch can be set to AC 1 or AC 2 to energize the stand−by inverter and couple it to the system whose inverter is failed.

### 2 ) AC BUS 1 AC BUS 2 INS pushbutton lights

They are used to read the pilot, copilot or INS inverter voltage on the 0−125 VAC voltmeter circuit. The light of the switched inverter is illuminated in blue.

#### 3 ) Failure lights

AC 1 and AC 2 amber lights on failure warning panel. are controlled by the inverted frequency monitor unit.

Either light illuminated indicates that associated inverter is failed and that its synchronization circuit is cut−off.

#### D − System components

#### 1 ) Pilot. copilot. stand−by and INS inverters

These four inverters are identical.

They are energized by the airplane system (26 thru 30 VDC) and deliver 115 VAC and 26 VAC − 400 Hz.

Output power may reach 750 VA for the 115 VAC and 150 VA for the 26 VAC. It cannot exceed a total of 750 VA on the two outputs. The inverters have an internal protection against overloads.

The pilot and copilot inverters are synchronized to each other. The stand−by inverter is synchronized to the pilot or copilot inverter when coupled.

#### 2 ) Freguency monitor circuits

Two printed circuits will command the phase synchronization line to close when the frequency of each inverter is 400 Hz ± 30.

THIS PAGE IS APPLICABLE TO MODEL : ALL

**SYSTEM DESCRIPTION** ELECTRICAL POWER

#### 3 − DISTRIBUTION

#### A − DC power distribution

The DC voltage is distributed from the LH and RH main busses located at the lower part of the distribution unit, and are called LH and RH electrical centers. The electrical centers are separated by a compartment contained the coupling contactor.

The LH main bus powers:

- − Non load shed primary bus A.
- − Load shed auxiliary bus C.

The RH main bus powers:

- − Non load shed primary bus B.
- − Load shed auxiliary bus D.

#### B − Load−shedding

- − The bus C and D rotary selectors are located on the overhead panel, next to the DC power indication panel.
- − The LH rotary selector is used to switch off the auxiliary bus C, the cockpit and baggage compartment dome lights.
- − The RH rotary selector is used to switch off the auxiliary bus D and the cockpit dome lights.

#### C − AC Power distribution

The single−phase static inverters that supply the AC system deliver 115 VAC − 400 Hz and 26 VAC − 400 Hz.

System No 1. powered by the pilot or stand−by inverted supplies:

- − Bus W with 115 V − 400 Hz.
- − Bus Y with 26 V − 400 Hz.

System 2. powered by the copilot or stand−by inverter supplies:

- − Bus X with 115 V − 400 Hz.
- − Bus Z with 26 V − 400 Hz.

Section 4 DTM914 Sub-section 05 REVISION 10 Page 22

## FALCON 50 OPERATING MANUAL **SECTION 4**

THIS PAGE IS APPLICABLE TO MODEL : ALL WITH : M1703 MODIFICATION

**SYSTEM DESCRIPTION** ELECTRICAL POWER

#### C − Controls and indications

#### 1 ) Inverter control switches

Two inverter control switches marked AC 1 and AC 2 are used to energize inverters 1 (pilot) or 2 (copilot) by closing their supply circuits.

### 2 ) AC BUS 1 AC BUS 2 pushbutton lights

These pushbutton lights are used to read the voltage of inverters 1 and 2 on the 0−125 VAC voltmeter circuit.

The light of the switched converter is illuminated in blue.

#### 3 ) Failure lights

AC 1 and AC 2 amber lights on failure warning panel, are controlled by the inverted frequency monitor unit.

Either light illuminated indicates that associated inverter is inoperative.

#### D − System components

These two inverters are identical.

They are energized by the airplane system (26 − 30 VDC) and deliver 115 VAC and 26 VAC − 400 Hz.

Output power may reach 350 VAC for the 115 VA and 150 VA for the 26 VAC.

It cannot exceed a total of 350 VA on the two outputs.

The inverters have an internal protection against overloads.

THIS PAGE IS APPLICABLE TO MODEL : ALL WITH : M1703 MODIFICATION

**SYSTEM DESCRIPTION** ELECTRICAL POWER

#### 3 − DISTRIBUTION

#### A − DC power distribution

The DC voltage is distributed from the LH and RH main busses located at the lower part of the distribution unit, and are called LH and RH electrical centers. The electrical centers are separated by a compartment contained the coupling contactor.

The LH main bus powers:

- − Non load shed primary bus A.
- − Load shed auxiliary bus C.

The RH main bus powers:

- − Non load shed primary bus B.
- − Load shed auxiliary bus D.

#### B − Load−shedding

- − The bus C and D rotary selectors are located on the overhead panel, next to the DC power indication panel.
- − The LH rotary selector is used to switch off the auxiliary bus C, the cockpit and baggage compartment dome lights.
- − The RH rotary selector is used to switch off the auxiliary bus D and the cockpit dome lights.

#### C − AC Power distribution

The single−phase static inverters that supply the AC system deliver 115 VAC − 400 Hz and 26 VAC − 400 Hz.

System No 1. powered by inverted 1 (pilot) supplies :

- − Bus W with 115 V − 400 Hz.
- − Bus Y with 26 V − 400 Hz.

System 2. powered by the INVERTER 2 (copilot) supplies:

- − Bus X with 115 V − 400 Hz.
- − Bus Z with 26 V − 400 Hz.

**SYSTEM DESCRIPTION** ELECTRICAL POWER

THIS PAGE IS APPLICABLE TO MODEL : ALL

**SYSTEM DESCRIPTION** ELECTRICAL POWER

Section 4 DTM914 Sub-section 05 REVISION 07 Page 24

THIS PAGE IS APPLICABLE TO MODEL : ALL WITH : M1703 MODIFICATION

**SYSTEM DESCRIPTION** ELECTRICAL POWER

THIS PAGE IS APPLICABLE TO

MODEL : ALL WITH : M1703 MODIFICATION

**SYSTEM DESCRIPTION** ELECTRICAL POWER

AC POWER DISTRIBUTION

## FALCON 50 OPERATING MANUAL **SECTION 4**

**SYSTEM DESCRIPTION** ELECTRICAL POWER

DISTRIBUTION OF THE 28 VDC BUS BAR A AND C CONSUMERS

THIS PAGE IS APPLICABLE TO MODEL : ALL

**SYSTEM DESCRIPTION** ELECTRICAL POWER

DISTRIBUTION OF THE 28 VDC BUS BAR B AND D CONSUMERS

Section 4 DTM914 Sub-section 05 REVISION 07 Page 26

**SYSTEM DESCRIPTION** ELECTRICAL POWER

DISTRIBUTION OF THE 28 VDC BUS BAR A AND C CONSUMERS

THIS PAGE IS APPLICABLE TO MODEL : ALL WITH : M1703 MODIFICATION

**SYSTEM DESCRIPTION** ELECTRICAL POWER

DISTRIBUTION OF THE 28 VDC BUS BAR B AND D CONSUMERS

Sub-section 05 REVISION 10 Page 26 B

Section 4 DTM914

## FALCON 50 OPERATING MANUAL **SECTION 4**

**SYSTEM DESCRIPTION** ELECTRICAL POWER

|             | LIL                                                                           | INCULT DILLAND | IN TABLE                                                         |               |
|-------------|-------------------------------------------------------------------------------|----------------|------------------------------------------------------------------|---------------|
|             | 115 ATT 1 * 115 HDG 1 (W) INS FAN * INS PWR * INS HEAT *                      | RADIO          | 115 ATT 2 * 115 HDG 2 (X) WEATHER RADAR * 115 OMEGA *            |               |
|             | 26 ATT 1 * 26 HDG 1 (Y) 26 INS * 26 RMI 1 (Y)                                 | NAV            | 26 ATT 2 * 26 HDG 2 (Z) VOICE RECORDER * 26 RMI 2 (Z) 26 OMEGA * |               |
| POWER       | HYDR 1 (Y)                                                                    | MISC<br>AC     | SHIELD (X)<br>HYDR 2 (Z)                                         | POWER         |
|             | RH CIRCUIT BREAKER PANEL                                                      |                |                                                                  |               |
| PILOT (AC1) | 115 FLT RECORD * RATE OF TURN * A/P AMPLI * A/P CMPTR * YAW DAMP * 115 FD 1 * | AECC           | 115 FD 2 *                                                       | COPILOT (AC2) |
|             | 26 FLT RECORD * 26 FD 1 *                                                     | AFCS           | 26 FD 2 *                                                        | $\mathbb{H}$  |
| لـا         | BLOWER LH (W) FREQ 1 (Y) FAN DEFOG                                            | MISC<br>AC     | BLOWER RH (X)<br>FREQ 2 (Z)                                      |               |

NOTE: The equipment bearing and asterisk are optional.

#### DISTRIBUTION OF AC 1 AND AC 2 POWER SYSTEM CONSUMERS

THIS PAGE IS APPLICABLE TO MODEL : ALL

**SYSTEM DESCRIPTION** ELECTRICAL POWER

#### 4 − ABNORMAL OPERATION OF DC POWER SYSTEM

#### A − Generator failure

If a generator is not coupled to the main bus of airplane system, GEN.. amber light will be illuminated on the failure panel, indicating that the associated reverse current relay has tripped.

When a GEN.. light illuminates while the generator is operating, the associated GEN.. switch will automatically be tilted to Off position. Attempt to reset the generator by placing its switch in On position (2 attempts maximum).

If attempt is unsuccessful, switch off the airplane system so as to have on the operative generator a current lower than the limits (refer to Airplane Flight Manual section LIMITATIONS).

- − If generator No 3 is failed, switch it to tied position and check the voltages. (If necessary switch off some equipment).
- − Should the three generators be failed simultaneously and attempts to reset them be unsuccessful, switch off a maximum number of equipment to reduce the current delivered by the batteries to less than 80 A.

The batteries, when in good condition, may operate for 20 Minutes for an average output current of 80 A and 35 minutes for 50 A.

#### B − Battery failure

In the event of an inadvertent grounding upstream of a battery protection, return current will cause the reverse current relay to open, associated BAT switch to tilt to Off position. and BAT light to illuminate on failure panel.

Attempt to reset the battery by setting battery switch to On position (two attempts at maximum).

Loss of one or the two batteries has no effect on the electrical load.

Section 4 DTM914 Sub-section 05 REVISION 10 Page 28

## FALCON 50 OPERATING MANUAL **SECTION 4**

NOTE : The equipment bearing and asterisk are optional.

#### DISTRIBUTION OF AC 1 AND AC 2 POWER SYSTEM CONSUMERS

THIS PAGE IS APPLICABLE TO MODEL : ALL WITH : M1703 MODIFICATION

**SYSTEM DESCRIPTION** ELECTRICAL POWER

#### **ELECTRICAL POWER**

#### 1 − ABNORMAL OPERATION OF DC POWER SYSTEM

#### A − Generator failure

If a generator is not coupled to the main bus of airplane system, GEN.. amber light will be illuminated on the failure panel, indicating that the associated reverse current relay has tripped.

When a GEN.. light illuminates while the generator is operating, the associated GEN.. switch will automatically be tilted to Off position. Attempt to reset the generator by placing its switch in On position (2 attempts maximum).

If attempt is unsuccessful, switch off the airplane system so as to have on the operative generator a current lower than the limits (refer to Airplane Flight Manual section LIMITATIONS).

- − If generator No 3 is failed, switch it to tied position and check the voltages. (If necessary switch off some equipment).
- − Should the three generators be failed simultaneously and attempts to reset them be unsuccessful, switch off a maximum number of equipment to reduce the current delivered by the batteries to less than 80 A.

The batteries, when in good condition, may operate for 20 Minutes for an average output current of 80 A and 35 minutes for 50 A.

#### B − Battery failure

In the event of an inadvertent grounding upstream of a battery protection, return current will cause the reverse current relay to open, associated BAT switch to tilt to Off position. and BAT light to illuminate on failure panel.

Attempt to reset the battery by setting battery switch to On position (two attempts at maximum).

Loss of one or the two batteries has no effect on the electrical load.

## FALCON 50 OPERATING MANUAL **SECTION 4**

THIS PAGE IS APPLICABLE TO MODEL : ALL

#### C − Weak batteries during start

If during a battery start, the batteries are too weak, their voltages may drop to 8 volts during the high current drain at the beginning of the cycle. As a result one of the battery circuit breakers would trip, causing start contactor to open and start cycle to be discontinued.

If attempt to start was made with the batteries in parallel (ignition selector on NORMAL), it is useless to attempt to start with the batteries in series (ignition selector in LOW TEMP START).

#### D − Simultaneous failures

#### 1 ) Failure of one generator and both batteries

This is indicated by illumination of one generator warning light and the battery warning lights.

After unsuccessful attempts to reset the generator or batteries, switch off services so that remaining generator loads do not exceed the limits.

#### 2 ) Failure of the three generators and one battery

The three generator warning lights and one battery warning light are illuminated. Press the pushbutton light to switch the ammeter to operative battery. Switch off as many services as necessary to continue the flight with one battery. Monitor ammeter and voltmeter readings and land as soon as possible.

#### 3 ) Total electrical power failure

There is no current at all in the airplane. All flags come into view on the radio navigation instruments.

If the emergency lighting switch was in ARMED, emergency lighting comes on automatically.

NOTE: The stand−by horizon remains usable.

#### Procedure:

Attempt to reset the batteries and generators. If unsuccessful

- − Immediately switch off the three generators and the two batteries.
- − Check battery conditions by switching on cockpit dome lights (directly powered by the batteries).

THIS PAGE IS APPLICABLE TO MODEL : ALL

**SYSTEM DESCRIPTION** ELECTRICAL POWER