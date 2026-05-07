# **EADI Cross-Side DCP Annunciation**

**EHSI Cross-Side DCP Annunciation** 

<span id="page-143-0"></span>If the DCP failure is such that data from the DPU (or MPU in drive transfer mode) to the DCP is not being received, several operating functions are not available. The following table lists these functions:

| FUNCTION       | EFFECT / ALTERNATE ACTION                                                                                                                       |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Direct to      | Course deviation must be zeroed with the CRS knob.                                                                                              |
| HDG sync       | Heading cursor must be zeroed with the HDG knob.                                                                                                |
| CAT II Request | CAT II request can only be reset by pushing the CAT II request button instead of being reset automatically by autopilot disengage acknowledge.  |
| Auto BRG Menu  | The bearing pointer menu is not reconfigured to exclude localizer selections. Therefore, Blank BRG pointer displays occur for these selections. |

### Multifunction Processor Unit (MPU) Failure

A detected MPU failure shows the annunciator "DRV" in red in the middle of the MFD and on the EFDs when the MPU is driving the displays in a drive transfer mode. When the MPU fails, the MFD and all it's functions are lost (including TCAS and weather radar) as well as the drive transfer capabilities for the EFDs. However, navigation and weather radar information are available for display on the EHSIs.

#### Multifunction Display (MFD) Failure

When the MFD fails, all it's functions are lost and there is no backup capability for the display. However, navigation and weather radar information are available for display on the EHSIs.

## **SELF-TEST**

EFIS-85C(14)/86C(14) systems use internal self-test routines to verify proper operation of the EFIS systems. In addition, the displays shows flags or other self-test information from the remote sensors that provide data to the system.

#### **EFIS Self-Test**

EFIS self-test is initiated by actuating an external installer supplied switch or button ("EFIS TEST" or similar). When the EFIS self-test is first initiated the following occurs:

- pilot's EADI shows a 10-degree pitch up from the current pitch attitude and a 10-degree right roll from the current roll attitude
- pilot's EHSI shows a 20-degree heading change to the right from the current heading
- copilot's EADI shows a 10-degree pitch down from the current pitch attitude and a 10-degree left roll from the current roll attitude
- · copilot's EHSI shows a 20-degree heading change to the left from the current heading
- the annunciator "TEST" shows in red on the EADIs and the MFD while the test is in process.

During the EFIS self-test the various comparator monitors are tested. The 10-degree attitude and 20-degree heading changes create a compare error for the comparator monitors to detect. Properly operating attitude and heading comparator monitors show the yellow boxed "ATT" (attitude) comparator warning flag on the EADIs and the yellow boxed "HDG" (heading) comparator warning flag on the EHSIs. In addition to the EFIS comparator warn flags, if installed, remote mounted master warn and comparator warn annunciators turn on. If CAT II approach mode is selected when the EFIS self-test is initiated, the CAT II comparator monitors are also tested. Properly operating CAT II comparators show the yellow boxed "LOC", "GS", "IAS", and "RA" comparator warn flags on the EADIs and yellow boxed "LOC" and "GS" comparator warn flags on the EHSIs and, if installed, remote mounted CAT II comparator warn annunciators turn on.

Also tested when the CAT II approach mode is selected, are the CAT II lateral, vertical, (red triangle pointers) and IAS (yellow flashing arrows) excessive deviation monitors. Refer to the EADI and EHSI Category II Excessive Deviation Warnings sections of this pilot's guide for detailed explanations of the excessive deviation warning annunciations.

Push and hold the "EFIS TEST" switch/button for longer than 4 seconds to turn on the flags test portion of the self-test. During the flags test, pitch, roll, and heading information are removed from view and all active display flags show on the displays. When the self-test switch/button is released, the displays return to normal operation, except that comparator warn flags do not turn off. To turn off the comparator warn flags, push and release the remote mounted comparator warn reset switch/button.

A copyright message shows on the displays during all portions of the EFIS self-test in installations with -001 version DPU/MPU. Installations with all other versions of DPU/MPU show the copyright message only in the flags test portion of the EFIS self-test.



---

[🡅](./toc.md) ·•⦁•· [🡄 Display Processor Unit (DPU) Failure](./Display-Processor-Unit-DPU-Failure.md) ·•⦁•· [**Sensor Self-Test** 🡆](./Sensor-Self-Test.md)