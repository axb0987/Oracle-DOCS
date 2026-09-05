# Exporting Users and Groups for Oracle Application Roles
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/datatransfer/export-users-and-groups-oracle-application-roles.htm
- Fetched: 2026-09-05 02:20 CDT

# Exporting Users and Groups for Oracle Application Roles

Export users and groups assigned to Oracle application roles of Oracle applications to a comma-separated values (CSV) file.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains . Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click Integrated applications .
- In the Applications page, select the Oracle application that has application roles with users and groups assigned to them.
- Select Application roles .
- Select the checkbox for application role that you want to export and select Export .
- Select Confirm .
- After the job completes, review the job results.
- If the job can be processed immediately, then a dialog box appears with the Job ID and a link for your import job. Select the link and review the details on the Jobs page.
- If the job cannot be processed immediately, then a message appears with a Schedule ID in it. Copy that Schedule ID , and use it to search for the job on the Jobs page. The job appears when processing completes.
- If needed, go to the Jobs page, locate, and open the job that you want to view.
This page shows how many application roles that you attempted to export, how many application roles exported successfully, and how many application roles can't be exported because of a system error.
- Select Download exported file .
See[Export Job Errors](https://docs.oracle.com/en-us/iaas/Content/Identity/datatransfer/../jobs/export-job-errors.htm)
