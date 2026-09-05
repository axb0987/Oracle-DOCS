# Information for Design Review
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/build-readiness-guide/information-for-design-review.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/build-readiness-guide/information-for-design-review.htm#dcoc-content-body)

# Information for Design Review

Prepare the following information for Oracle design review.

Document Set What to Include Purpose
Floor plans and layouts Scaled floor plans in AutoCAD and PDF format that show walls, columns, doors, rack locations, row identifiers, remote power panel (RPP) or busway locations, electrical branch circuits, and row load information. Confirms the physical layout, service clearances, rack placement, and power distribution design.
Mechanical design package Mechanical one-line diagrams, cubic feet per minute (CFM) information, computational fluid dynamics (CFD) analysis, and failure analysis for the cooling infrastructure. Confirms that cooling systems support the planned rack load and failure scenarios.
Electrical design package Electrical one-line diagrams, load calculations, breaker coordination study, failure matrix, power distribution unit (PDU) details, panel details, naming conventions, and rack-to-breaker mapping. Confirms that power systems provide the required capacity and redundancy.
Handoff and emergency information Updated as-built drawings, panel schedules, power mapping to UPS systems, emergency escalation procedures, escape routes, and fire system information. Supports safe operations, incident response, and service continuity.

## General Facility Specifications

Start with the base building capabilities. The site must meet the following minimum environmental, electrical, and safety conditions before detailed rack design is approved.

Category Requirement Planning Details
Power architecture Use AC 3-phase service and provide separate A and B power paths backed by independent UPS systems. Hybrid AC and DC systems are not acceptable. Size each UPS path for 100% of the total IT load.
Generator and backup power Size emergency generation for IT, mechanical, and emergency loads. Ensure that the plant can run at full load without interruption. Fuel storage must support full-load operation long enough to permit scheduled fuel delivery without interrupting generator output.
Distribution Provide two active power paths supported by separate UPS systems. If the site uses busbar, top boxes must accept IEC60309 plug sets without modifications to original equipment manufacturer (OEM) hardware or extension leads.
Environmental envelope Maintain the room within the supported operating range. Supply air 18 degrees C to 27 degrees C; dew point -9 degrees C to 15 degrees C; 8% to 50% RH baseline and up to 70% RH where air-quality validation supports the range.
Airflow planning Size airflow to maintain supported IT inlet conditions across the rack row. Use 150 CFM per kW as the baseline planning value. Denser footprints might require about 160 CFM per kW.
Floor loading Design the raised floor and supporting structure for the maximum approved rack weight. Support rack weights up to 900 kg or 1,150 kg, depending on footprint. The live load rating must be at least 1,361 kg, or 3,000 lb.
Fire and leak detection Provide data hall fire detection, fire protection, and water or condensation leak monitoring. Single-zone fire detection and dry-pipe pre-action protection are the baseline planning assumptions. Leak detection must alert building operations and security.

- [Information for Design Review](https://docs.oracle.com/en-us/iaas/Content/dedicated/build-readiness-guide/information-for-design-review.htm#information-for-design-review)
- [General Facility Specifications](https://docs.oracle.com/en-us/iaas/Content/dedicated/build-readiness-guide/information-for-design-review.htm#general-facility-specifications)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
