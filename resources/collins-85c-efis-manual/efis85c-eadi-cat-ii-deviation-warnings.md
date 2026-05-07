# **EADI Category II Excessive Deviation Warnings**

The EFIS-86C system provides special visual cues to indicate excessive deviation of the ILS localizer and ILS glideslope, and excessive indicated airspeed deviation during a Category II approach.

#### <span id="page-52-0"></span>**Excessive ILS Localizer Deviation**

Enable Logic—The on-side localizer deviation is compared to the CAT II limit when all of the following conditions are met:

- On-side CAT II A or B request received
- VOR/LOC is the active course from the on-side DCP
- On-side radio altitude is less than 600 feet
- On-side localizer is tuned and valid
- On-side back course is not detected
- · Go around is not selected on either side
- On-side DCP is valid and cross-side DCP is not selected

Monitor Limits—An excessive deviation warning occurs when the enable conditions are met and the localizer deviation exceeds 25 microamperes for a CAT IIA request, or 20 microamperes for a CAT IIB request.

The on-side excessive deviation warning is also displayed when the cross-side system detects an excessive deviation condition, cross-side data is valid, and a localizer scale is in view.

Annunciation—When an excessive deviation warning occurs, a red triangular-shaped pointer appears to the right or left of the aircraft symbol. The apex of the triangle points in the direction of appropriate correction (fly right if the triangle is to the left of the aircraft symbol, and fly left if the triangle is to the right of the aircraft symbol).

Neither the external master warn or ILS comparator warn annunciators are turned on for the excessive deviation condition.

#### **Excessive ILS Glideslope Deviation**

**Enable Logic**—The on-side glideslope deviation is compared to the CAT II limit when all of the following conditions are met:

- · On-side CAT II A or B request received
- VOB/LOC is the active course from the on-side DCP
- On-side radio altitude is between 90 and 600 feet
- · On-side glideslope is valid
- · On-side localizer is tuned and valid for 15 seconds
- On-side back course is not detected
- · Go around is not selected on either side
- On-side DCP is valid and cross-side DCP is not selected

Monitor Limits—An excessive deviation warning occurs when the enable conditions are met and the glideslope deviation exceeds 75 microamperes for a CAT IIA request, or 65 microamperes for a CAT IIB request. The on-side excessive deviation warning is also displayed when the cross-side system detects an excessive deviation condition, cross-side data is valid, and a glideslope scale is in view.

Annunciation—When an excessive deviation warning occurs, a red triangular-shaped pointer appears above or below the aircraft symbol. The apex of the triangle points in the direction of appropriate correction (fly down if the triangle is above the aircraft symbol, and fly up if the triangle is below the aircraft symbol).

Neither the external master warn or ILS comparator warn annunciators are turned on for the excessive deviation condition.

#### **Excessive Indicated Airspeed Deviation**

Enable Logic—The on-side IAS deviation is compared to the CAT II limit when all of the following conditions are met:

- On-side CAT II request received
- VOR/LOC is the active course from the on-side DCP
- On-side radio altitude is between 15 and 1000 feet
- · On-side glideslope is valid
- On-side localizer is tuned and valid for 15 seconds
- On-side back course is not detected
- · Go around is not selected on either side
- On-side DCP is valid and cross-side DCP is not selected
- · Excessive IAS deviation is enabled

Monitor Limits—An excessive deviation warning occurs when the enable conditions are met and the IAS deviates from the IAS reference by more than +10 knots or -5 knots.

The on-side excessive deviation warning is also displayed when the cross-side system detects an excessive deviation condition, cross-side data is valid, and a glideslope scale is in view.

Annunciation—When an excessive deviation warning occurs, a yellow arrow appears above or below the green rectangular IAS marker pointing in the direction of appropriate correction (lower IAS if the arrow is above the IAS marker, and increase IAS if the arrow is below the IAS marker).

The external master warn annunciator is not turned on for the excessive deviation condition.



---

[🡅](./toc.md) ·•⦁•· [🡄 Radio Altitude Comparator](./Radio-Altitude-Comparator.md) ·•⦁•· [**Category II Outputs** 🡆](./Category-II-Outputs.md)