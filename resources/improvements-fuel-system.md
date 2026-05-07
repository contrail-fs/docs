1. LO FUEL warning — Doc source: Training manual
Training (Ch.5, ~line 247):
“Low fuel level in a feeder tank is indicated by the amber LO FUEL light … The light indicates that the fuel remaining in at least one of the feeder tanks is less than 300 pounds. The warning circuit is delayed (15 seconds) to eliminate false indications caused by waves or fuel movement inside the tanks.”
OMB: Does not describe LO FUEL or 300 lb / 15 s.
Current: Threshold 250 lb, no delay (Fuel.js ~577–588).
Verdict: Gap. Per Training: use 300 lb and 15 s delay before illuminating LO FUEL.
2. Refuel stop levels (REAR LO / HI) — Both docs
OMB: HI 15,513 lb total; LO 13,195 lb (4,348 / 4,499 per side/center).
Training: HI 15,513 lb (2,315.5 gal); LO 13,213 lb (1,971 U.S. gal); table also gives 609 lb regulation, 1,750 lb center feeder LO.
Current: Stops at 1860 gal (HI) and 1585 gal (LO) → ~12,462 lb and ~10,620 lb.
Verdict: Gap. Align with docs: HI ≈ 2,315 gal, LO ≈ 1,971 gal (Training) or ~1,972 if using 13,195 lb.
3. Center feeder two-step (REAR LO) — Both docs
OMB: REAR LO → center feeder stops at 600 lb until center wing full, then continues to 1,750 lb (float/solenoid closes).
Training: Same: “center feeder tank can be fed up to approximately 600 pounds … at which point fueling is interrupted until the center wing tank is full. Once the center wing tank has filled, the center feeder tank can be filled to 1,750 pounds.”
Verdict: Gap. Optional enhancement: implement 600 lb pause until center wing full, then allow center feeder to 1,750 lb when REAR is LO.
4. Pressure fueling / VALVE TEST — Both docs
OMB: Test cock above panel; open with coupling connected and truck delivering; fueling must stop automatically after a few seconds.
Training: “The test is accomplished during refueling by placing the VALVE TEST handle on the fueling panel to the TEST position. A successful test is indicated when fueling automatically stops after a few seconds.”
Verdict: Gap. Optional: add VALVE TEST that simulates “full” to test STOP FUELING / FUELING OK.
5. Defuel valve — Both docs
OMB: “Electrically-activated valve controlled by DEFUELING switch … connects the pressure fueling system to the booster pump interconnect duct.”
Training: “Solenoid valve controlled by the defueling switch … connects the pressure refueling system to the LP crossfeed line. Fuel suction from the feeder tanks is performed through LP booster pumps.”
Verdict: Gap. Add defuel valve in fuel model and tie it to DEFUEL switch (no doc conflict; OMB “interconnect duct” and Training “LP crossfeed line” both mean a path to booster/suction).
6. Gravity fueling and vent valves — Both docs
OMB: GRAVITY FUELING switch (test panel); when ON, three air vent valves open in sequence, FUELING light on.
Training: Same: GRAVITY FUELING switch on test panel; when ON, “three air vent valves of the feeder tank and center wing tank open in sequence; FUELING light illuminates.”
Verdict: Gap. Optional: add switch and vent/gravity path if desired.
7. Regulation level and capacities — Both docs
Training: Regulation 609 lb (~90 gal); side feeders max ~1,400 lb (209 gal); center feeder max 2,460 lb (367 gal); center feeder LO refuel 1,750 lb. Wing 3,748 lb (~560 gal) each; center wing 2,749 lb (410 gal).
Current: feederHoldTargetGalPerFeeder = 91 (~609 lb); tank capacities in config are in the right ballpark.
Verdict: Aligned. No change needed for regulation or capacities.
8. Shutoff valves vs “booster shutoff” and N2 — Training only (no delay)
Training:
“Each feeder tank is equipped with a fuel shutoff valve … downstream of the booster pump. … The shutoff valves are cable-actuated by means of the FIRE PULL handles.”
So the documented shutoff is the fire shutoff (FIRE PULL), not a valve that closes when the booster switch is turned off.
Training Q6: “After landing, when are the fuel booster pumps turned off?” One option: “They are turned off at 30% N2 rpm.” That refers to when to turn off the booster pump switch, not a valve delay.
Neither doc describes:
a “booster shutoff valve” that closes when the booster is switched off, or
a 30 second delay before closing any valve based on N2.
Verdict: Not doc-driven. The 30 s delay when N2 ≥ 50% for valves 14/15/16 is a design choice for the sim (e.g. to avoid instant engine stumble when switching boosters). Keep or tune (e.g. 30 vs 300 s) as desired; no doc requirement to add or remove it.
9. Drainage — OMB only (Training mentions sump drains)
OMB: Separate/simultaneous drainage; center wing isolation valve; drain valves and procedures.
Training: Sump drains (eight), drain valves in feeder manifolds and transfer manifold; defuel via pressure receptacle with truck suction; tanks must be depressurized/vented first.
Verdict: Gap if you want full drainage simulation; optional.
10. Pressure fueling limits — Training only
Training: Max feed pressure 50 psi, minimum 30 psi; max flow 1,800 lb/min.
Verdict: Optional: use 50 psi / 1,800 lb/min as limits in refuel logic if you model pressure/flow.
11. FUELING light causes — Training only
Training: FUELING light may indicate: vent valves open, defuel valve open, refuel door open, gravity fueling switch not off, vent lever VENT OPEN, or auxiliary bus D off.
Verdict: Optional: drive FUELING light from these conditions for consistency.
Summary table (OMB + Training)
#	Topic	OMB	Training	Current	Action
1	LO FUEL (300 lb, 15 s delay)	—	✓ 300 lb, 15 s	250 lb, no delay	Fix: 300 lb + 15 s delay
2	Refuel stop HI/LO (15,513 / 13,213 lb)	✓ 13,195	✓ 13,213, 1,971 gal	Wrong gal	Fix: ~2,315 gal (HI), ~1,971 gal (LO)
3	Center feeder 600 → 1,750 lb (REAR LO)	✓	✓	Not impl.	Optional
4	VALVE TEST / test cock	✓	✓	Not impl.	Optional
5	Defuel valve	✓	✓ (solenoid, LP crossfeed)	No valve	Add valve + DEFUEL switch
6	Gravity fueling / vent valves	✓	✓	Not impl.	Optional
7	Regulation 609 lb (91 gal)	✓	✓	✓ 91 gal	OK
8	Booster shutoff delay (30 s, N2 ≥ 50%)	—	—	300 s in code	Not in either doc; design choice only
9	Drainage / isolation valve	✓	partial	Not impl.	Optional
10	Pressure limits (50 psi, 1,800 lb/min)	—	✓	—	Optional
11	FUELING light conditions	—	✓	—	Optional
Bottom line: With both docs: implement LO FUEL at 300 lb with 15 s delay (Training) and refuel stop at doc values (HI ~2,315 gal, LO ~1,971 gal). Defuel valve is in both; center two-step, valve test, gravity/vent, and drainage are in one or both and are optional. The booster shutoff delay (30 s when N2 ≥ 50%) is not mentioned in either document; it stays a sim design choice, not a doc requirement.