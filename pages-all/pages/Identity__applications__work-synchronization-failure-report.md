# Accessing the Synchronization Failure Report
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/applications/work-synchronization-failure-report.htm
- Fetched: 2026-09-05 02:20 CDT

# Accessing the Synchronization Failure Report

You can view the synchronization failure report of a provisioning application from the Import tab. The report contains the sync failures for the selected application. This report is useful in finding out the reason behind sync failures that occurred during account and object sync of an application.

- On the Domains list page, select the domain in which you want to make changes. If you need help finding the list page for the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/../domains/to-view-identity-domains.htm).
- On the details page, select Integrated applications . A list of applications in the domain is displayed.
- Select the name of the app that you want to configure.
- Depending on the options you see, do one of the following:

- Select the Actions menu (three dots) and then select Synchronization failure .
- Select Import and select Synchronization failure .
- In the Synchronization Failure Report page, you can use the filters to narrow down the result based on the following criteria:
- Application

The Application filter is case-sensitive.
- Dates range

Choose the number of days for which you need the failure report. Preconfigured values are: Past 30 Days , Past 60 Days , Past 90 Days . Alternatively, enter the Start date and the End date in the text box or select them from the calendar.
- Object type

To narrow down the result based on Application or Object type , choose a value from the menu and enter a corresponding value in the text box. The available values are: Equals , Contains , Starts with and Ends with .
Tip  
  
If you select Equals and enter Google App in the text box, the filter displays entries only for Google App. If you select Starts with and enter G in the text box, the filter displays entries for applications starting with the letter G.
- After you have set the filter, select Run to display the search result.

The following table describes the various columns in the search filter:

Filter Columns

Description

Application

Displays the name of the Application.

Object type

Displays the type of the Object, for example, Account, Group, Organization, Printer, and so on.

Object identifier

Displays the unique ID of the object from which sync is performed.

Name

Displays the name of the object on which sync is performed.

Date

Displays the time when the sync was performed on the object.

ECID

Displays the value of the Event Correlation Identifier (ECID).

Failure reason

Displays the reason behind the synchronization failure.
-
