# Generate Event-based Access Reviews Report
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/generate-event-based-access-reviews-report.htm
- Fetched: 2026-09-05 03:14 CDT

# Generate Event-based Access Reviews Report

As an Administrator of Oracle Access Governance, you can analyze information on event-based access reviews by generating reports using the Event-Based Report capability of Oracle Access Governance.

## Navigate to the Event-Based Access Reviews Report Service

You can run, view, and save the event-based access review report.

You must have Administrator rights to view and run this service. Find out more about application roles in the[Understanding Application Roles](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm#predefined-application-roles-reference)topic

Here's how you can open the event-based access review report service on Oracle Access Governance Console:

- From the browser, go to Oracle Access Governance. On the OCI console, you can open it using the Service Home Page link.
- In the Username field, enter either the Administrator user name.
- In the Password field, enter the password and select Sign In .
You will be navigated to the home page of the Oracle Access Governance Console.
- Select icon on the top, on the left side of the application page to display the navigation menu .
- Select Access Reviews , then Event-Based Setup .
The Event-Based Setup landing page is displayed.
- Select the View access review report button
The Event-Based Access Reviews Report landing page is displayed.

## Run Event-Based Access Reviews Report

As an Administrator, you can generate a monthly report on event-based access reviews by selecting appropriate reporting criteria.

You can generate the report based on date range and event types (predefined identity changes to perform access reviews). For example, you can generate a report on the access reviews initiated or implemented for all the new identities added or removed in your organization in the last month. Here's how you can run an event-based access reviews report by selecting the appropriate report selection criteria:

- In the From field, select the start date from which you want to run a report.
- In the To field, select the end date up to which you want to run a report.
To generate a report, you must take care of the following date range rules:
- You can select only the first day of the month.
- You can generate a report only for a maximum of a 12-month period, i.e. the difference between the From date and the To date can't be more than 12 months.
If you started implementing event-based access reviews from the 10th of this month and want to generate report till the present day, then in the From field, select the first day of this month, and in the To field, select the first day of the next month. However, the results will include records only from the date of implementation of the event-based access reviews up to the current day.
- Select the event type. Available options are:
- Change
- Timeline
- Unmatched accounts
- Select the Event Name for which you want to generate the access review report.
The Enabled and Disabled event-types displayed are based on whether the specific event is disabled or enabled in the Event-Based Setup screen.
- If you selected Timeline or Unmatched accounts event type then select the Event Name you want to include in the report.
- Select Apply .
According to the selected criteria, you can view the graphical charts on the same application page.

## View Event-Based Access Reviews Report Results

After you generate an event-based access review report, you can see a set of graphical charts (donut charts, stacked bar charts, and chart legends) displaying the report details on the same application page.

The donut charts display the following information:
- User accounts review decision : Shows the number of impacted user accounts after running the event-based access reviews. The decision statuses are categorized based on Pending , Approved , or Revoked access reviews.
- Role membership review decision : Shows the number of impacted user roles and group roles after running the event-based access reviews. The decision statuses are categorized based on Pending , Approved , or Revoked access reviews.
- Permission assignments review decision : Shows the number of impacted user permissions or entitlements after running the event-based access reviews. The decision statuses are categorized based on Pending , Approved , or Revoked access reviews.
- Unmatched accounts review decision : Shows the number of unnmatched accounts after running the event-based access reviews. The decision statuses are categorized based on Pending , Approved , or Revoked access reviews.
- Auto action of low risk : Shows the number of approved low-risk review tasks after running the event-based access review. These low-risks review tasks are categorized based on Auto , which are automatically approved by Oracle Access Governance, or Manual , which are manually approved by the assigned reviewer.

The stacked bar charts display the following group information:
- Group by user organization - Top 5 : Shows which top five organizations are affected after the running the event-based access reviews. The decision statuses are categorized based on Pending , Approved , or Revoked access reviews.
- Group by applications - Top 5 : Shows which top five applications are affected after the running the event-based access reviews. The decision statuses are categorized based on Pending , Approved , or Revoked access reviews.
- Group by Roles - Top 5 : Shows which top five roles are affected after the running the event-based access reviews. The decision statuses are categorized based on Pending , Approved , or Revoked access reviews.
- Group by system - Top 5 : Shows which top 5 integrations or orchestrated systems are affected after the running the event-based access reviews. The decision statuses are categorized based on Pending , Approved , or Revoked access reviews.
- Group by insights : Shows, for unmatched accounts, the distribution of reason for flagging as unmatched based on the following options:
- No match
- Multi-match
- User deleted

## Additional Actions

In addition to viewing report, you can also save the event-based access reviews report offline in the PDF format or download the CSV data for further analysis, audit, or anything else you usually do with offline reports.

Download PDF : Select the Download PDF button, which is available at the top, right corner of the application page, to save the report results offline in PDF format. Your PDF file will be saved to your downloads directory.
