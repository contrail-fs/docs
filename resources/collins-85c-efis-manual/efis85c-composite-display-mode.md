# **Composite Display**

In the NAV and RDR display modes, the respective line key menus show the annunciator "TFC>" in green next to the third line key from the top. Push this line key to turn on or off the traffic display mode while in the NAV and/or RDR display modes. In this way, the MFD can show a composite display of any combination of the RDR, NAV, and TFC display modes.

When the TFC display mode shows as part of a composite display mode with the RDR and/or NAV modes, the TFC line key menu does not show on the display and no changes can be made to the currently selected traffic display options. However, the currently selected traffic display options (TA-ONLY, 0-OFF, ABOVE, and BELOW) are still annunciated in the upper leR of the display below the green display mode annunciators. To change the traffic display options, push the TFC button to turn on the dedicated traffic display then select the desired traffic display options.

**RDR, NAV, and TFC Composite Display Mode** 

#### <span id="page-128-0"></span>TCAS System Diagnostic Display

A TCAS diagnostic data page shows a list of the TCAS related systems monitored by the TCAS computer and tested during the TCAS self-test routine. Valid systems show in green followed by the word "PASS". Invalid systems show in yellow followed by the word "FAIL".

If a TCAS problem is suspected and you are going to use the MFDs TCAS diagnostic data page to verify the suspected problem, it is suggested that you operate the TCAS self-test first. This is suggested, because although the COLLINS TCAS-94 system waits approximately 10 seconds before running its initialization self-test, some aircraft systems (such as heading systems) may take longer than 10 seconds to become valid at initial power-up. The TCAS computer's internal self-test monitors identify these systems as failed if they are not valid by the time the self-test operates. TCAS internal self-test monitors also indicate failures for some TCAS-related systems that are re-initialized or self-tested while in flight. TCAS computers retain self-test diagnostic information until the self-test operates again. The MFD TCAS diagnostic data page shows the TCAS system status as reported by the TCAS computer during the most recent operation of the self-test. Operating the TCAS self-test resets the TCAS diagnostics data. If TCAS-related system(s) have indeed failed, operating the TCAS self-test allows the TCAS computer to identify the failed system(s). In addition, it clears any failures recorded for TCAS-related systems that are working properly, but require longer than 10 seconds for a power-up valid or require a long initialization.

To turn on the TCAS diagnostic data page, select the TFC display mode, push and hold the CLR button, then push and hold the third line key from the top. The TCAS diagnostic data page shows on the MFD only while the buttons are pushed. Release the CLR button and the line key to turn off the diagnostic data page.

The TCAS diagnostic data page makes it easier to prepare a TCAS squawk report when a failure occurs. When preparing a TCAS squawk report, operate the TCAS self-test and then select the diagnostic data page. Include all failures shown in the list in your squawk report.

**TCAS Diagnostic Data Page** 

#### Controls

Controls on the MFD-85C operate in the same manner as the controls on the MFD-85B except that the TFC button has been added, the RDR and NAV modes are controlled from the same button, and a line key menu for the TFC display mode is added. The following paragraphs describe the controls that affect the information shown in the TFC display mode.

TFC Button—Push the TFC button on the top left side to turn on the TCAS traffic display mode and the TCAS line key menu along the right side of the display. The TCAS menu turns off after approximately 5 seconds of no selection activity. With the MFD in the TCAS display mode, push the TFC button or any line key at any time to again turn on the TCAS menu.

Line Keys—In the TFC display mode a line key menu on the right side of the display, when turned on, shows the traffic display options for selection. To turn on the line key menu push any line key or the TFC button. The menu stays on for approximately 5 seconds then turns off. While the menu shows on the display, push the line key for the desired display option to select, set or turn on and off that traffic display option. Selected options show in green and unselected show in white. The following describes the operation of the EFIS system's line key traffic display options.

The top line key, with the TCAS menu identifier  $\lozenge$ -OFF>, turns on and off the display of "other traffic". With other traffic turned off, the annunciator " $\lozenge$ -OFF" shows in the upper left corner of the display, the line key menu identifier shows in green, and TCAS does not show "other traffic" on the display. With other traffic turned on, TCAS shows a cyan open diamond traffic symbol on the display for detected "other traffic", the " $\lozenge$ -OFF" annunciator turns off, and the line key menu identifier shows in white.

The second line key from the top, with the TCAS menu identifier A↑/B↓>, sets the altitude volume (relative to your own aircraft) for which TCAS shows "other traffic" on the display. PT, TA and RA traffic are not affected by the ABOVE and BELOW modes and always show on the display regardless of the selected altitude volume. (Except RA traffic does not show on the display in the TA-ONLY mode). Successive pushes of the button cycles through the available altitude volumes. The line key menu identifier shows selected modes in green and unselected modes in white. The ranges of the altitude modes are:

- NORMAL (2700 ft above to 2700 ft below, no annunciation on the display)
- ABOVE (9900 ft above to 2700 ft below)
- BELOW (2700 ft above to 9900 ft below)
- ABOVE and BELOW (9900 ft above to 9900 ft below).

The "ABOVE" and "BELOW" annunciators show in white in the upper left corner of the display. In the "normal" mode neither annunciator shows.

The third line key from the top, with the TCAS menu identifier ALT>, selects the type of altitude data, relative or absolute, that shows with the traffic symbols. In the relative mode, the altitude data (if available) shows as a two number read-out preceded by a "+" or "-" sign. In the absolute mode, the altitude data shows as a three number read-out. Also, in the absolute altitude mode, an annunciator at the lower left end of the full-range arc shows your own aircraft's altitude. If the altitude data is baro corrected, the annunciator shows as a three number read-out preceded by ALT (i.e. ALT240.) If the altitude data is not baro corrected or the TCAS system is in TEST mode, it shows as a three number read-out preceded by FL (i.e. FL240.)

Line Advance (▲) and Reverse (▼) Buttons (Range Selection)—The line advance and reverse buttons on the left side at the bottom of the MFD, select the traffic display range. The advance button (▲) increases the range and the reverse button (▼) decreases the range. Selected range is annunciator in the upper right corner of the TFC display. If the TFC display mode shows as part of a composite display with the RDR display mode, then range is controlled by the WXP and the line advance reverse buttons are disabled.

#### Radar (RDR) and Navigation (NAV) Display Modes

The MFD-85C uses essentially the same RDR and NAV display mode formats as the MFD-85B. Only the variations from the MFD-85B are described in this section. Refer to the MFD-85B Weather Radar Display Mode and Navigation Display Mode sections of the MFD-85B chapter for descriptions and operation of MFD-85C annunciators, flags, and display elements not described here.

The RDR NAV button turns on and off both the RDR and NAV display modes. Each push of the button cycles through a sequence of display mode selections. The first push turns on the RDR mode. A second push turns on the NAV mode with the RDR mode to form a composite display of radar and navigation information. A third push turns off the RDR mode and leaves the NAV mode on. A fourth push turns off the NAV mode and turns on the RDR mode. At the end of the sequence, the selection cycle repeats as the button is pushed. Selection of a display mode with any other mode button (i.e., TFC, RMT, etc...) saves the currently selected RDR/NAV display mode(s) and selected display options in memory in the MFD. When the RDR button is pushed the last selected RDR and/or NAV display mode(s) are recalled from the memory and shown on the display.

The third line key in the line key menus for both the RDR and NAV display modes shows the annunciator "TFC" and is used to turn on and off the TFC display mode. With the RDR hutton and the TFC line key, the MFD-85C can show a composite display of any combination of the TFC, RDR, and NAV display modes. All of the annunciators, flags, and display elements for each mode, show on the display in essentially the same manner and locations as in the respective dedicated display modes. The exceptions are described in the following paragraphs.

#### NOTE

TCAS display options such as ABOVE, BELOW and "Other Traffic" on or off, cannot be selected or changed when the TFC mode shows as part of a composite display with the RDR and/or NAV display mode(s). Push the TFC mode button to turn on the dedicated TFC mode, to make changes to the TCAS display options.

#### **RDR Display**

The MFD-85C RDR display mode format is the same as the MFD-85B RDR mode with the following differences:

- In the RDR mode, the line key menu shows the annunciator "TFC" on the third line key from the top.
  A composite display of the RDR and TFC modes shows on the MFD-85C when the TFC mode is selected with this line key.
- An additional display mode annunciator ("TFC") shows in green in the upper left corner of the display below the RDR and NAV mode annunciators, when the TFC mode is selected to show on the MFD.

In the RDR and TFC composite display mode, all of the annunciators, flags, and display elements show on the display in the same manner and locations as in the respective dedicated display modes with the following exceptions.

• TCAS mode annunciators, "TCAS-0FF" and "TA-ONLY", show below the display mode annunciators and above the TCAS display options annunciators.

- The TFC display line key menu is not available and does not show in the RDR display mode or in the composite TFC and RDR and/or NAV display modes.
- TCAS no bearing annunciators do not show in the TFC and RDR and/or NAV composite modes.
- The annunciator "TRAFFIC" shows in yellow (TA) or red (RA) in the middle of the display when TCAS detects TA or RA traffic even if the TFC mode shows as a part of a composite display with the RDR and/or NAV modes.
- Display range and range rings show in the RDR display format.
- The "TCAS FAIL" and "TD-FAIL" annunciators show in the upper left corner in place of the TFC annunciator for TCAS computer failures and TCAS display failures respectively.
- In the composite display mode of TFC, RDR and/or NAV, the TCAS display option annunciators show
  in the middle of the left side of the display below the MFD display mode annunciators ("RDR", "NAV",
  and "TFC").

**RDR and TFC Composite Display Mode** 

#### **NAV Display**

The MFD-85C NAV display mode format is the same as the MFD-85B NAV mode with the following differences:

- In the line key menu the annunciator TFC shows on the third line key from the top in place of the ENTER annunciator unless the joystick is in use. A composite display of the NAV and TFC modes shows on the MFD-85C when the TFC mode is selected with this line key.
- An additional display mode annunciator ("TFC") shows in green in the upper left corner of the display below the RDR and NAV mode annunciators, when the TFC mode is selected to show on the MFD.

In the NAV and TFC composite display mode, all of the annunciators, flags, and display elements show on the display in the same manner and locations as in the respective dedicated display modes with the following exceptions.

- The TCAS mode annunciators "TCAS-0FF" and "TA-ONLY" show below the display mode annunciators and above the TCAS display options annunciators.
- The TFC display line key menu is not available and does not show in the NAV display mode or in the composite display mode of TFC and NAV and/or RDR.
- The TCAS no bearing annunciators do not show in the composite display mode of TFC and NAV and/or RDR.
- The annunciator "TRAFFIC" shows in yellow or red in the middle of the display when TCAS detects
  TA or RA traffic, even if the TFC display shows as a part of a composite display with the NAV and/or
  RDR displays.
- In the composite display mode of TFC and NAV the display range and range rings show in the NAV
  display format. Also, Any time the RDR display mode shows as part of a composite NAV display with
  or without the TFC display, the display range and range rings show in the RDR display format.
- The "TCAS-FAIL" and "TD-FAIL" annunciators show in the upper left corner in place of the TFC annunciator for TCAS computer failures and TCAS display failures respectively.
- In the composite display mode of TFC, NAV and/or RDR, the TCAS display option annunciators show
  in the middle of the left side of the display below the MFD display mode annunciators ("RDR", "NAV",
  and "TFC").

#### NOTE

If the joystick is moved while in a NAV display mode or a composite NAV and RDR display mode, the TFC line key annunciator changes to ENTER and the line key is used to enter a waypoint into the MFD memory for transfer to a compatible LNV system.

#### **NAV MENU Display**

Operation of the MFD-85C NAV menu is the same as the MFD-85B, except for the TFC and RDR NAV buttons. Push the TFC button, with the display mode annunciator "<TCAS" to show the dedicated TCAS traffic display mode. Push the RDR button, with the annunciator "<RDR/HDG UP" annunciator to show the radar and/or NAV and/or TFC display modes. From the NAV menu the RDR button changes the display to show the mode(s) (RDR and/or NAV and/or TFC) that were selected prior to selection of the NAV menu display mode.



---

[🡅](./toc.md) ·•⦁•· [🡄 Traffic (TFC) Display Mode](./Traffic-TFC-Display-Mode.md) ·•⦁•· [**NAV and TFC Composite Display Mode** 🡆](./NAV-and-TFC-Composite-Display-Mode.md)