# **NAV and TFC Composite Display Mode**

**NAV Menu Display Mode** 

### **RMT, PGE, and EMG Display Modes**

Refer to the MFD-85B section for descriptions and operation of the RMT, PGE, and EMG display modes for the MFD-85C. These display modes are the same for both the MFD-85B and -85C.

#### <span id="page-136-0"></span>REVERSIONARY MODES OF OPERATION

EFIS-85C(14)/86C(14) systems have reversionary operating modes for the controls, displays, and display processors in the event of a failure of a system element. Control for selection of normal and reversion operating modes is provided by external, cockpit mounted reversionary switches. The following paragraphs describe the operational and display differences when the system is operated in a reversion mode.

#### NOTE

All external switches for reversion and drive transfer switching are installer supplied items and are not part of the EFIS system. Therefore, not all EFIS installations have reversion switching for all of the reversion capabilities. Also, switch labels and position names may not be the same as those used in the following descriptions. Refer to the appropriate aircraft manuals for specific information on the reversion operation modes specific to your aircraft.

#### Electronic Flight Display (EFD) Failure

EFD failures show in many ways such as:

- blank displays
- · jittery or scrambled displays
- · fading displays
- · unstable size of the display or display elements.

Various reversionary display modes are available for the EFDs on each side of the cockpit. A DISPLAY SELECT switch sets the system to show an EADI on the top EFD and an EHSI on the bottom EFD (normal operation mode) or an EADI on either EFD (top or bottom) with the other EFD turned off or an EADI on both the top and bottom EFDs at the same time. A DISPLAY MODE switch selects either normal operation (EADI and EHSI on individual displays) or the composite display mode which shows an EADI and an EHSI together. These two switches can be operated together such that a composite display can show on either the top or bottom EFD with the other EFD turned off, or on both the top and bottom EFDs. Interconnect wiring straps, connected during installation of the EFIS system, determine the specific switching capabilities used and whether or not the composite display mode is available.

#### EADI Failure (top EFD)

To recover EADI display information select the lower EFD with the display select switch and select the composite display mode with the display mode switch. A composite display of the EADI and EHSI shows on the bottom EFD.

### EHSI Failure (bottom EFD)

To recover EHSI display information select the upper EFD with the display select switch and select the composite display mode with the display mode switch. A composite display of the EADI and EHSI shows on the top EFD.

#### NOTE

In some installations, both the display select and composite mode functions are switched together on one switch. In these installations, the composite mode is selected automatically when the display mode switch is set to other than the normal mode. The switch may be labeled as a "Composite" switch with normal mode as the center position, ADI as the upper position and HSI as the lower position.

In the composite display mode, all flags and annunciators are the same, except that they may be positioned in a different location. Refer to the figure on the following page.

In addition to moving the EADI or combining it with the EHSI in the composite display mode on either EFD, a drive transfer switch can set the MFD to show the display mode selected for the bottom EFD. If the pilot's or both the pilot's and copilot's drive transfer switches are set to the drive transfer mode, the pilot's bottom EFD display mode is shown on the MFD. If only the copilot's drive transfer switch is set to the drive transfer mode, the copilot's bottom EFD display mode is shown on the MFD. When the MFD display is in drive transfer, all MFD functions are disabled, except for the PWR button and the INT knob. Refer to the Display Processor Unit Failure paragraphs for additional information about the drive transfer modes.

**EADI and EHSI Composite Display Mode** 

**Composite Display Mode Flags** 



---

[🡅](./toc.md) ·•⦁•· [🡄 **Composite Display**](./Composite-Display.md) ·•⦁•· [Display Processor Unit (DPU) Failure 🡆](./Display-Processor-Unit-DPU-Failure.md)