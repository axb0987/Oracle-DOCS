# Capacity Management
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/capacity-management.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/capacity-management.htm#dcoc-content-body)

# Capacity Management

Use this section to learn how operators monitor capacity consumption, export capacity data, create demand plans, and work with Oracle Capacity Management through the region lifecycle.

Capacity management dashboards show current and historical usage and available capacity for Compute, Block Storage, Object Storage, File Storage, and Exadata resources. Usage types include OCI usage, customer usage, and overhead usage for Compute.

## Access and View Capacity Dashboards

Open Capacity management from My Reports on the Operator Console home page, or use the navigation menu and select Governance and administration, then Capacity management. Select the dashboard, select the compartment under List Scope, and review the dashboard data.

Dashboard Area Use
Current Snapshot Review the current day usage and available capacity by usage type.
Usage Breakdown Review usage by tenancy. For Compute, also review usage by shape.
Historical Data Review usage over the selected time period. The default range is 30 days; available ranges include 60 days, 90 days, and a custom date range.
Compute shape tabs For Compute dashboards, use processor type tabs, such as Intel Standard or AMD Dense, to review current and historical data for each processor type.

## Export Capacity Data

Export capacity data when local analysis, reporting, or capacity review preparation requires a saved file. Open Capacity management, select the dashboard, select the compartment under List Scope, and, for Compute, select the applicable Compute shape tab. Select Export at the top right of the dashboard, select the file type, and confirm the download. Capacity dashboard exports can be saved as CSV, Excel, or PowerPoint files.

## Demand Planning

Use demand plans to track projected capacity changes over a defined time period. In Capacity management, select Demand Planning, select the compartment under List Scope, and create a demand plan with a plan name, active status, start date, end date, resource type, and monthly increase or decrease values.

Monthly demand values are cumulative. For example, if the plan adds 1,000 cores in October, 2,000 cores in November, and 1,000 cores in December, December reflects 4,000 additional cores compared with September because it inherits the increases from October and November. Add additional resource type changes to the same plan when the forecast must cover multiple resource types, then save the completed plan.

## Partner with Oracle to Manage Capacity

Work with the OCI Capacity Manager throughout the contract lifecycle to align demand forecasts, consumption trends, and expansion decisions. Provide quarterly demand forecasts for expected workloads that support customer resale and internal needs, and confirm that space and power are available for approved rack expansions.

Capacity Management Activity Operator Role Oracle Role
Demand signal and forecasting Provide quarterly demand forecasts and communicate expected workload changes. Monitor consumption, compare forecasts with actual usage, and review demand in regular capacity review meetings.
Expansion decision Review and approve expansion recommendations, and confirm space and power readiness. Determine whether expansion is required based on consumption, forecasted demand, and expansion lead time.
Expansion run Validate site readiness for new racks, including space and power. Initiate and oversee rack procurement, ordering, arrival, ingestion, and activation.
Ongoing lifecycle management Continue to provide demand updates and participate in capacity reviews during the contract term. Repeat the review and expansion process as needed to support future capacity needs.

- [Capacity Management](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/capacity-management.htm#capacity-management)
- [Access and View Capacity Dashboards](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/capacity-management.htm#access-and-view-capacity-dashboards)
- [Export Capacity Data](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/capacity-management.htm#export-capacity-data)
- [Demand Planning](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/capacity-management.htm#demand-planning)
- [Partner with Oracle to Manage Capacity](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/capacity-management.htm#partner-with-oracle-to-manage-capacity)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
