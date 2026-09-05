# Exporting Groups
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/datatransfer/export-groups.htm
- Fetched: 2026-09-05 02:20 CDT

# Exporting Groups

Export groups to a comma-separated values (CSV) file.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains . Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then depending on what you see, select either the User management tab or under Identity domain , select Groups .
- Select the checkbox for each group that you want to export.
- From the More actions menu, select Export groups .
- In the Export groups window, select Export .
- After the job completes, review the job results.
- If the job can be processed immediately, then a dialog box appears with the Job ID and a link for your import job. Select the link and review the details on the Jobs page.
- If the job cannot be processed immediately, then a message appears with a Schedule ID in it. Copy that Schedule ID , and use it to search for the job on the Jobs page. The job appears when processing completes.
- If needed, go to the Jobs page, locate, and open the job that you want to view.
A page shows how many groups you exported, how many groups exported successfully, and how many groups can't be exported because of a system error.
- Select Download exported file .
- Save your file in a UTF-8 format. Saving the file in UTF-8 format ensures that non-English characters display properly.
- Open the CSV file with a text editor, such as Notepad.
- Save the file with UTF-8 for encoding.
- (Optional) In addition to saving the file in UTF-8 format, if you're using Microsoft Excel to open and save the file, perform the additional steps to ensure that non-English characters display properly.
- In Microsoft Excel, open a new workbook, select the Data tab, and then choose From Text/CSV .
- On the Import Data window, choose your CSV file, and then select Import .
- For File Origin , select 65001: Unicode (UTF-8) .
- For Delimiters , select Comma .
- For Data Type Detection , select Based on first 200 rows , and then select Transform Data .
- Select Close and Load .
- Save the file.
See[Export Job Errors](https://docs.oracle.com/en-us/iaas/Content/Identity/datatransfer/../jobs/export-job-errors.htm)
