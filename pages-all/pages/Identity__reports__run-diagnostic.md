# Running the Diagnostic Data Report
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/reports/run-diagnostic.htm
- Fetched: 2026-09-05 02:27 CDT

# Running the Diagnostic Data Report

Run a diagnostic data report for an IAM identity domain.
Use the[diagnostic data report](https://docs.oracle.com/en-us/iaas/Content/Identity/reports/diagnostic.htm)to view data captured for an identity domain. You perform two separate actions to get diagnostic data:
- Set the diagnostics type, which sets the level at which you capture operational logs. You do this in the Settings area.
- Run the diagnostic data report in the Reports area.

After setting the diagnostics type and running the diagnostic data report, diagnostic data is captured for the next 15 minutes. After 15 minutes, the diagnostics type reverts to None .

- On the Domains list page, select the domain for which you want to run a diagnostic data report. If you need help finding the list page or the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/reports/../domains/to-view-identity-domains.htm).
- On the details page, perform one of the following actions depending on the option that you see:

- Select the Settings tab, and then go to the Diagnostics section on the tab.
- On the left side of the page, select Domain settings , and then select Diagnostics .
- Under Diagnostics , select Edit diagnostics settings (if necessary), and then select the diagnostics type:
- None doesn't collect any activity.
- Activity view captures only high-level logging information only.
- Data view captures mid level and high-level logging information.
- Service view captures detailed logging information.
- Select Identify item in search results to identify the resources returned in the diagnostic log.
- Save your changes to activate data logging in IAM.
- 6. On the domain details page, perform on the following actions depending on the option that you see:

- Select the Reporting tab.
- On the left side of the page, select Reports .
- Under Reports , select View report for the Diagnostics data report .
- On the Diagnostic Report page, enter filter values, such as dates and user names, to search for specific information.
- Select Download report .
