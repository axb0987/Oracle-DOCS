# Business Reporting
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/business-reporting.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/business-reporting.htm#dcoc-content-body)

# Business Reporting

Use this section to learn how operators use Business Reporting dashboards and reporting data to monitor consumption, onboarding, support, and update activity for a Dedicated Region environment.

Use the Business Reporting dashboards in the Operator Console to review Cost and Usage, Order Status, Customer Support Metrics, and Update Activity. Refresh report data before reviewing or exporting dashboard results so operational decisions use the latest available dashboard data.

## Access Business Reporting Dashboards

Open the Operator Console and access Business Reporting from My Reports, or use the navigation menu and select Governance and Administration, then Business Reporting Dashboards.

After opening a dashboard, use the report tabs at the bottom of the screen to move between available views. Use the filter bar to add, change, or remove filters, and verify active filter values before exporting or sharing results.

## Business Reporting Dashboard Areas

Use the following dashboard areas to support executive reporting, operational review, and customer onboarding decisions.

Dashboard Use Primary Review Areas
Cost and Usage Review consumption, cost, service usage, usage date, region, tenancy, and subscription data. Filter by service, tenancy OCID, subscription OCID, region, and usage date. The daily view includes usage date, currency, cost, unit of measure, usage, product description, product SKU, service, region, tenancy OCID, and subscription OCID. Organization subscription OCIDs represent operator usage; Oracle Cloud subscription OCIDs represent end-customer usage.
Order Status Track activation orders and provisioning status for customer onboarding. Review order state, admin email, activation email status, customer details, order creation period, and activation status. Use this dashboard to find customers with sent activation emails, identify pending activation, track orders without an order number, and review order processing over a selected duration.
Customer Support Metrics Review open, escalated, and resolved Service Requests and trends that support customer support operations. Use Open SRs, Resolved SRs, and SR Details tabs. Review open SRs by severity, tenancy, escalation status, and status; resolved SRs by timeframe, tenancy, status, and severity; and SR details by SR type, SR number, resolved month, tenancy, escalation status, status, severity, and creator. Data refreshes once per day.
Update Activity Review scheduled and completed changes to OCI services, including emergency, mitigating, normal, and routine changes. Use Scheduled and Completed tabs to review known disruptive changes, services, change type, region, update schedule details, completion status, and updates completed in the last 24 hours, 7 days, or 30 days.

## Order States and Change Types

Use order states to identify where an activation order is in the onboarding flow. Creating means the order was created and the activation email was sent. Pending Activation means the customer has not yet activated the subscription. Activating means provisioning is in progress. Active means ordering and provisioning are complete. Needs Attention indicates an activation error that may require resending the activation email or working with the customer.

Use change type definitions to interpret update activity. Emergency changes are required during a change freeze or within the next 24 hours. Mitigating changes address active incidents or potential customer-impacting events. Normal changes require 24 hours between approval and deployment and often introduce new or custom payloads. Routine changes have been implemented at least four times with the same implementation steps.

## Dashboard Controls and Export

Use dashboard controls to keep views current, preserve context, and share filtered results.

Control Use
Export Data Download the dashboard or report with the current filters applied. Export options include PowerPoint, Acrobat, CSV, image, or print, depending on the dashboard context.
Undo and Redo Reverse or repeat the previous dashboard edit when interacting with the report view.
Refresh Data Refresh the dashboard with the latest available data. This is especially important before reviewing Order Status and other operational dashboards.
Filter Bar Add filters, verify active filter values, deselect individual filters, or remove all filters when the dashboard needs to return to an unfiltered view.

## Direct Data Warehouse Access

Use direct data warehouse access when an approved business intelligence tool must build custom reporting views beyond the Operator Console dashboards. Oracle updates the reporting data warehouse every 24 hours, and BI tools connect by using read-only access to published data warehouse views.

Before connecting a BI tool, allowlist the BI server IP address or CIDR range, download the Autonomous Database wallet, and obtain the current read-only credentials from Vault. Treat the wallet, wallet password, database credentials, and extracted reporting data as restricted operational data.

Setup Area Operational Guidance
Allowlist BI server access In the Customer Console, override to the Oracle defined tenancy, open the Oracle Provided Autonomous Database that is within the production compartment, update network access, allow public access, and add approved access control values by IP address, CIDR block, VCN, or VCN OCID.
Download the database wallet Download client credentials from the database connection pane. Use a wallet password that is 8 to 60 characters and includes at least one alphabetic and one numeric character.
Acquire credentials Retrieve the latest decoded secret from Vault in the adw_clone_prod compartment. The read-only username is dw_reader. When using SQL Developer, select the public_low connection service.
Review refresh timing Open ADW_Clone and review Clone information for the last refresh point timestamp and upcoming refresh value before reconciling BI reports with dashboard data.

### Data Warehouse Views

Use the following published views when modeling custom BI reports. View definitions can change; update the BI semantic model when Oracle communicates revised definitions.

Reporting Area Schema and View Key Data
Cost and Usage REVENUE OCI_COST_AND_USAGE _DASHBOARD_V Usage date, tenant ID, subscription OCID, service, usage, unit of measure, region, product SKU, product description, cost, and currency.
Customer Support Metrics SUPPORT CUSTOMER_SUPPORT _METRIC_V Critical flag, days since updated, deleted flag, problem description, severity, SR number, status, timestamps, time to resolution, resolution target flag, owner count, and day, week, and month rollups.
Order Status SPMR ORDER_STATUS_V Admin email, order identifiers, order OCID, created and updated timestamps, state, customer, tenancy home region, activating account name, subscription ID, subscription dates, and activation email timestamp.
Update Activity OPERATIONS UPDATE_ACTIVITY_V Change identifiers, locations, issue type, emergency and routine flags, change type, service owner, change driver, outage type, known disruptive change flag, status, planned start and finish, closure code, completion status, orphaned flag, and audit timestamps.
Windows Instance Cores Summary CDI WINDOWS_INSTANCE _CORES_SUMMARY_V Physical host ID, total CPU cores per physical server, and virtual machine OCID for Windows Server tracking.

- [Business Reporting](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/business-reporting.htm#business-reporting)
- [Access Business Reporting Dashboards](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/business-reporting.htm#access-business-reporting-dashboards)
- [Business Reporting Dashboard Areas](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/business-reporting.htm#business-reporting-dashboard-areas)
- [Order States and Change Types](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/business-reporting.htm#order-states-and-change-types)
- [Dashboard Controls and Export](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/business-reporting.htm#dashboard-controls-and-export)
- [Direct Data Warehouse Access](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/business-reporting.htm#direct-data-warehouse-access)
- [Data Warehouse Views](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/business-reporting.htm#data-warehouse-views)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
