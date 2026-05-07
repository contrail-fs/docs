# Display Processor Unit (DPU) Failure

A DPU failure shows the red boxed "DRV" annunciator in the middle of the EADI and EHSI displays. To restore operation of the displays using the MPU in place of the failed DPU, set the external, cockpit mounted drive transfer switch, on the failed side of the cockpit, to the drive transfer mode. A yellow boxed "CDRV" annunciator (center drive) shows on the EFDs set to the drive transfer mode and on the MFD. See page 133.

External, cockpit mounted drive transfer switches select the EFIS display processors (DPU or MPU) that drive the EFDs. When the switches are set to the normal operation mode, one DPU drives the EFDs on one side of the cockpit, the other DPU drives the EFDs on the other side of the cockpit, and the MPU drives the MFD display. When a DPU failure is indicated ("DRV" annunciator shows on the EADI and EHSI displays), set the drive transfer switch for that side of the cockpit to the drive transfer mode to restore operation of the EFDs. In the drive transfer mode, the MPU drives the MFD and the EFDs on the side in drive transfer mode while the DPU on the other side continues to drive its EFDs. If both sides of the cockpit are set to the drive transfer mode, the MPU drives all four of the EFDs and the MFD.

#### NOTE

Some installations use a single switch to select the drive transfer mode. The switch has a center position for the normal mode with a left and right position for the transfer modes. Dual drive transfer cannot be selected in these installations.

REVERSIONARY MODES OF OPERATION

**DPU Failure Example (EHSI)** 

In the drive transfer mode, the EFDs show a normal EADI on the top display and an EHSI on the bottom display or a composite display on either or both of the EFDs (depends on the EFD reversion switch settings as previously described for an EFD failure). In addition, the MFD changes to show the same display information as the bottom EFD and all normal MFD functions are disabled, except for the PWR button and the INT control. When both sides of the cockpit are in drive transfer mode, the MFD shows the pilot's bottom EFD display information. A yellow boxed "CDRV" annunciator shows on the EFDs on the side set to the drive transfer mode and on the MFD. If both sides are set to the drive transfer mode then a yellow boxed "PDTA" annunciator (pilot's data) shows on all four EFDs and on the MFD.

DCP-85() Display Control Panel sensor selection, EHSI display mode, and other display functions, operate in the same manner through the MPU in drive transfer mode as they do through the DPU in normal operation mode. Therefore, the EADI and EHSI displays show all the same information in the same manner as in the normal operation mode. If only one side of the cockpit is set to the drive transfer mode, the MPU is controlled by that side's DCP and uses that side's sensor data for the display information. If both sides of the cockpit are set to the drive transfer mode, then the pilot's DCP controls the MPU and the pilot's side sensors are used. Therefore, when both sides of the cockpit are in drive transfer, the EADIs and EHSIs or composite displays on both sides of the cockpit show exactly the same information from the pilot's side sensors.

Comparator monitoring is switched from the failed DPU to the MPU when the drive transfer mode is selected. If it is determined that a DPU failure, not a sensor failure, is the cause of comparator warn flags, select the drive transfer mode to disable the DPU comparators and enable the MPU comparators. In some installations, depending on the aircraft wiring, the comparator monitors in the DPU are not disabled when the drive transfer mode is selected, but the MPU monitors are turned on. In these installations, if it is determined that a DPU failure is the cause of comparator warn flags, in addition to selecting the drive transfer mode, open the failed DPU's circuit breaker to disable its comparator monitors. This allows only the MPU comparators to operate on the drive transfer side. When both sides of the cockpit are set to the drive transfer mode, comparator monitoring is disabled.

**Drive Transfer Annunciation** 

#### <span id="page-141-0"></span>Display Control Panel (DCP) Failure

A DCP failure shows the red boxed "CTL" annunciator in place of the decision height read-out on the EADI and the numeric course read-out on the EHSI. To regain control of the displays on the side of the cockpit with the failed DCP, set the external, cockpit mounted DCP control transfer switch for the failed side to the transfer or cross-side position. This transfers control of both the DCP and CHP controls to the working side DCP and CHP. A yellow boxed "XCTL" annunciator shows on the EFDs on the side of the cockpit that has transferred control and on the MFD.

Externally, cockpit mounted DCP transfer or cross-side switches select the DCP that controls the DPU (or MPU in drive transfer mode) and therefore the EFDs. In the normal operation mode the pilot's DCP controls the pilot's side displays and the copilot's DCP controls the copilot's side displays. This is true even when one side of the cockpit is in the drive transfer mode where the MPU replaces the DPU on that side. When the DCP transfer or cross-side switch on the pilot's side is set to the transfer or cross-side mode, the copilot's DCP controls both sides of the cockpit. The opposite is true when the copilot's side is set to the transfer or cross-side position. Also, when both sides of the cockpit are set to the drive transfer mode (MPU driving all four EFDs and the MFD) then the pilot's DCP controls both sides of the cockpit unless the pilot's DCP transfer or cross-side switch is set to the transfer or cross-side position. In that case the copilot's side DCP controls both sides of the cockpit.

When the DCP transfer or cross-side mode is selected, the annunciator "XCTL" shows in yellow in the lower right corner of the cross-controlled EADI and the EHSI displays. All display parameters, except FCS mode annunciation, are controlled by the cross-side DCP and CHP. Decision height set read-out and NAV data elapsed timer functions also show in yellow on the cross-controlled EADI. However, GS and TTG NAV data and sensor annunciations show in the color appropriate for the selected sensor for that side, the same as when in normal operation. TAS from the air data systems and wind data from the LNAV systems do not go to the EFIS system through the DCP. Therefore, they are not affected by control transfers and on-side data shows on each side of the cockpit unless a cross-side system is selected for the respective sensor.

Also, the flight control system (FCS) mode annunciations which are received by the EFIS system through the DCP, are removed from the EADI display on the failed DCP side of the cockpit. However, on-side FCS mode data on the working side DCP shows on the on-side EADI display. If the on-side DCP detects a failure, the FCS mode annunciation is removed from the displays.

#### **NOTE**

Display brightness control functions are not transferred from one DCP to the other in the cross-side DCP modes. The DCP DIM knobs control the on-side EFD brightness in all operating modes.



---

[🡅](./toc.md) ·•⦁•· [🡄 **NAV and TFC Composite Display Mode**](./NAV-and-TFC-Composite-Display-Mode.md) ·•⦁•· [**EADI Cross-Side DCP Annunciation** 🡆](./EADI-Cross-Side-DCP-Annunciation.md)