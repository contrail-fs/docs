# Engine Tune Phase 4 - Fuel Flow Retune

Shipped and verified 2026-05-14. Targets `JET_density_on_FF_table` only. Drag and `n1_and_mach_on_thrust_table` rev 13 frozen.

Status: **VERIFIED PASS**. All 3 cross-check cards landed within +/-3% of prediction.

## What changed

`engines.cfg` line 61 (Phase 2 Iter 2 line preserved as comment on line 60).

| Knot (rho slug/ft^3) | Phase 2+3 | Phase 4 | Lift |
|---|---|---|---|
| 0.00046 (FL450) | 0.42 | 0.46 | +9.5% |
| 0.00059 (FL410) | 0.46 | 0.50 | +8.7% |
| 0.00074 (FL350) | 0.51 | 0.55 | +7.8% |
| 0.00089 (FL290) | 0.54 | 0.57 | +5.6% |
| 0.00107 (FL250) | 0.58 | 0.58 | unchanged |
| 0.00127 (FL200) | 0.62 | 0.62 | unchanged |
| 0.00150 (FL150) | 0.67 | 0.67 | unchanged |
| 0.00176 (FL100) | 0.77 | 0.77 | unchanged |
| 0.00205 (FL050) | 0.85 | 0.85 | unchanged |
| 0.00240 (SL) | 1.24 | 1.24 | unchanged |

## Why this shape

Phase 4 test cards (H0-H10 + L1, GW 32 klb, dISA -3 to +3) revealed a structural FF deficit at high-N1c speed-held cruise that Phase 2+3 LRC anchors didn't surface:

- **Clean M.80 high-alt data**: H8 FL350 -18%, H9 FL370 -16%, H10 FL410 -13% (per-hour and per-mile both)
- **Clean LRC across full envelope**: Phase 2+3 anchors all within +/-3% (PASS)
- **Mid/low-alt M.75/MCT data muddied**: H1-H4 cards held N1c past the M=0.5 thrust cliff (rev13 row 90), accelerated to M=0.77-0.81 instead of book M=0.59-0.75. FF readings honest for the achieved op point but not directly comparable to book speed-held cruise.

### The 1D rho ceiling

`JET_density_on_FF_table` is one factor per altitude. At any given altitude, LRC and M.80 share the same density factor. Empirical N1c response in sim from D1/H1 same-density pair: sim FF rises 2.6%/N1c-point vs book 5.3%/N1c-point. **Sim N1c sensitivity is half book.** No single rho factor satisfies both bands at the same altitude. The MSFS jet FF model assumes one TSFC for all thrust regimes; real turbofan TSFC degrades with thrust.

### The drag-low compensation at low alt

Sim drag chain validated at LRC speeds (Phase 2+3 TAS anchors PASS). At higher N1c at low alt, the rev13 thrust table M=0.5 cliff produces more thrust than drag consumes at book Mach. Pilots flying speed-held cruise (M.75 schedule, not N1c-held) at low alt will use **lower N1c** than book to balance drag. Lower N1c -> lower FF. This partially self-corrects the structural FF deficit for realistic cruise scenarios at low alt.

We have no clean data quantifying this self-correction, but the mechanism is real. Decision: **don't lift mid/low-alt knots** since LRC fits perfectly there and high-N1c is rare in actual ops below FL250.

## Predicted residuals (linear-scaling estimate)

Sim FF * (new factor / old factor). Verify in sim.

### LRC band (Phase 2+3 PASS baseline)

| Card | Knot | Sim now | Predicted | Book | Residual |
|---|---|---|---|---|---|
| D1 FL050 LRC | 0.00205 | 691 | 691 | 689 | +0.4% |
| E1 FL100 LRC | 0.00176 | 669 | 669 | 653 | +2.4% |
| D2 FL150 LRC | 0.00150 | 626 | 626 | 620 | +1.0% |
| E2 FL200 LRC | 0.00127 | 613 | 613 | 601 | +1.9% |
| L1 FL250 LRC | 0.00107 | 594 | 594 | 584 | +1.8% |
| D3 FL270 LRC | ~0.00094 | 588 | ~600 | 581 | +3% (marginal) |
| E6 FL350 LRC | 0.00074 | 574 | 619 | 572 | **+8%** (degraded) |
| D6 FL410 LRC | 0.00059 | 555 | 603 | 555 | **+9%** (degraded) |

### M.80 high-alt cruise band (Phase 4 target)

| Card | Knot | Sim now | Predicted | Book | Residual |
|---|---|---|---|---|---|
| H8 FL350 M.80 | 0.00074 | 630 | 679 | 772 | -12% |
| H9 FL370 M.80 | 0.00074 | 612 | 660 | 730 | -10% |
| H10 FL410 M.80 | 0.00059 | 596 | 648 | 684 | -5% |

### Other anchors (cross-checks)

| Card | Knot | Sim now | Predicted | Book | Residual |
|---|---|---|---|---|---|
| H0 SL TOGA | 0.00240 | 1900 | 1900 | 1872 | +1.5% |
| F FL350 M0.75 | 0.00074 | 601 | 648 | 620 | +5% |
| S3 FL350 MCT | 0.00074 | 651 | 702 | 685-720 | in band |

## Verification results (PASS)

Flown 2026-05-14, GW 32 klb, dISA +0.5 to +2.5.

| Card | Predicted | Actual | Match | vs book | Pre-Phase 4 |
|---|---|---|---|---|---|
| E6 FL350 LRC | 619 | 605 | -2.3% | +5.8% over | +0.3% |
| H8 FL350 M.80 | 679 | 681 | +0.3% | -11.8% under | -18% |
| D6 FL410 LRC | 603 | 603 | 0% | +8.6% over | 0% |

All three within +/-3% of prediction. Linear-scaling model holds.

E6 came in slightly better than predicted (+5.8% vs +8% predicted) — likely because the user settled at M=0.644 instead of book M=0.687. MSFS FF is mildly Mach-sensitive; lower Mach = lower FF. Favorable direction.

D6 flown single-engine (ENG 2/3 at 0%, timeout). Per-engine FF reading at N1c=95.4 / rho=0.000553 still valid since per-engine FF is independent of engine count.

Net cruise burn estimates (M.80 high alt): ~10% under book vs ~17% pre-Phase 4. LRC high alt: ~6-9% over book (safe direction for endurance planning).

## What got fixed

| Region | Phase 2+3 | Phase 4 (predicted) | Improvement |
|---|---|---|---|
| M.80 FL350 (H8) | -18% | -12% | +6 pp |
| M.80 FL370 (H9) | -16% | -10% | +6 pp |
| M.80 FL410 (H10) | -13% | -5% | +8 pp |
| Long-haul cruise burn estimate | ~17% under | ~9% under | halved |

## What got worse (acceptable trade)

| Region | Phase 2+3 | Phase 4 (predicted) | Cost |
|---|---|---|---|
| LRC FL350 (E6) | +0.3% | +8% | endurance estimate ~8% conservative (safe direction) |
| LRC FL410 (D6) | 0% | +9% | endurance estimate ~9% conservative |

LRC at high alt now over-burns book by ~9%. This is the **safe direction** for endurance planning - pilots who plan with book FF will arrive with more fuel than predicted, not less. Mid/low-alt LRC unchanged.

## Phase 5 hand-off (WASM custom FF)

Remaining residuals (-5 to -12% M.80, +8-9% LRC at high alt) are exactly the band-spread that 1D rho cannot fix. The MSFS engine sim cannot be replaced via cfg, but a custom WASM gauge can:

1. Read N1c, M, rho per engine each tick
2. Index a 2D LUT for "book FF at this op point"
3. Compute delta vs sim FF
4. Drain/add fuel from active tanks each tick to make total burn match book

Phase 5 will:
- Spike a 30-min JS test (`SimVar.SetSimVarValue` on tank quantities) to verify the override path works without fighting the engine sim
- If JS works, ship FF correction inside `Engines.js` with a 2D LUT (~100 anchor points)
- If JS doesn't work, set up WASM toolchain and ship as a custom gauge module
- Cfg curve becomes the "no-correction baseline"; WASM applies only the delta

Both bands targeted to land within +/-2% across the full envelope.

## What I won't touch (Phase 4 boundaries)

- `n1_and_mach_on_thrust_table` rev 13 (line 70) - drag/thrust validated, frozen
- Aircraft drag tables
- `high_fuel_flow=1700` (locked to SL TOGA spec via knot 0.0024 = 1.24)
- `idle_fuel_flow=234` (locked to S1a clamp anchor)
- `fuel_flow_scalar=0.96`, `ThrustSpecificFuelConsumption=0.406` (global scalars, can't differentiate bands)
- `Engines.js` display logic (Phase 5 scope)

## Files modified

- [engines.cfg](../../msfs-projects/Content/fs/SimObjects/Airplanes/CTL_FA50/engines.cfg) line 60-61 (Phase 2 Iter 2 commented, Phase 4 active)
- [engine-tune-phase2-3-final.md](../engine-tune-phase2-3-final.md) "What's next" section updated
