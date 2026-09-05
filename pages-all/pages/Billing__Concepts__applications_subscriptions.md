# Applications Subscriptions
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/applications_subscriptions.htm
- Fetched: 2026-09-05 01:42 CDT

# Applications Subscriptions

You can view service details and usage metrics specific to Applications subscriptions on the Subscriptions page. Services shows a list of the different products that the customer has bought as part of their subscription (non-metered or metered SaaS). Usage shows a list of report documents associated with the customer SaaS environment, and can show different details, depending on the type of SaaS subscription (whether non-metered, metered SaaS, or infrastructure-like metered SaaS services).

The Subscription information page for Applications subscriptions displays subscription details, and lists:
- Subscription ID
- Type
- CSI number
- Original start date
- Start date
- End date
- Total contract value
- Currency
- Environment (name of the SaaS currency environment related to the subscription)

The following types of SaaS subscriptions can be viewed:
- Non-metered SaaS provides usage metrics PDFs and Excel files on the Subscriptions information page Usage resource.
- Metered SaaS , such as Oracle Data Cloud and Commerce Cloud, where you can view part number quantities and fulfilled values under Services , and view usage, billable usage, and billable costs by SKU with stacked bar charts under Usage .
- Infrastructure-like metered SaaS services that allow you to view[Usage](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/infrastructure_subscriptions.htm#account_management_usage)and[Rate Card](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/infrastructure_subscriptions.htm#subscriptions_available_services)information, similar to Universal Credits type accounts.
- Other SaaS subscriptions can be viewed that use the same interface and show the same details as[Infrastructure Subscriptions](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/infrastructure_subscriptions.htm).

From the Subscription information page for Applications subscriptions, you can view the associated[Services](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/applications_subscriptions.htm#subscription_appservices)and[Usage](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/applications_subscriptions.htm#subscription_appusage).

## Services

Services have a start date, renewal date (order end date), metric (unit of measure), quantity, and fulfillment value. The services list can be downloaded as a CSV file, and you can sort and search for keywords to help filter the table.

Sometimes, the quantity of the service has a link that opens an Order details panel that shows the different orders that the customer bought, and which totals up the entire quantity of the service.

The banner at the top of the Order details panel shows the same service information as the Services page table.

Each order is presented in a table with the following:
- The effective date range for the period the order covers.
- The order number.
- Status of the service period.
- Quantity that was bought.
- Net unit price.
- Fulfilled value ( Quantity multiplied by the Net unit price ).

## Usage

The following are instructions on how to view usage for usage for non-metered, metered SaaS, and infrastructure-like metered SaaS subscriptions.

### Non-Metered SaaS
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Subscriptions .
- On the Subscriptions page, click the Usage resource.

The Usage table of documents has File Name , Report Date (UTC) , and Size fields. Each document in the table contains the corresponding usage metrics for the services being used from the subscription in the particular environment. Two file types are available: PDF and XLS.

The PDF file contains a usage metrics summary. The XLS file allows drilling down through the data at a much more granular level, which provides a foundation for creating your own reports from the spreadsheet.

Under Resources , you can filter the documents list by report type (PDF and XLS), or a report date range.

### Metered SaaS
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Subscriptions .
- On the Subscriptions page, click the Usage resource.

You can filter Usage by Start date , End date , and then optionally, choose a Granularity (such as Monthly ).

Usage is listed for each associated SKU:
- SKU ID
- Service Name
- Order Start Date (UTC)
- Order End Date (UTC)
- Entitlements : Quantity in the service line's metric (shown in the Service Name field).
- Utilized : How much of the entitlement or quantity was used (same metric as Quantity on the[Services](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/applications_subscriptions.htm#subscription_appservices)resource).
- Utilization % : The usage percentage calculation (Utilized/Quantity x 100).
- Billable Usage : Utilized - Quantity, if Utilized is greater than Quantity (same metric as Quantity on the[Services](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/applications_subscriptions.htm#subscription_appservices)resource).
- Billable Cost : Billable Usage x the price listed on the[Services](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/applications_subscriptions.htm#subscription_appservices)resource (in the subscription's currency).

Click the down arrow ( ) to expand the usage entry, and view the associated stacked bar chart related to the SKU's usage. The chart heading shows the selected Usage time period , and Usage to date in the service line's metric, along with its percentage of billable usage.

The bar chart X-axis shows time in UTC, while the Y-axis is the service line's metric. You can hover the mouse over a particular data point in the chart to view more detail about it. Above the chart, select Cumulative to get a representation of usage over time. The Legend indicates your Usage (which corresponds to Entitlements in the table) compared to your actual Billable Usage .

You can also download the Usage table as a CSV file by clicking Download as CSV .

### Infrastructure-like Metered SaaS
- Open the navigation menu and click Billing &amp; Cost Management . Under Billing , click Subscriptions .
- On the Subscriptions page, click the Usage resource.

Usage for such services shows the following:
- Filters are available globally under Resources . Filter based on the Subscription phase , or Start date and End date .
- A cost usage summary that shows:
- Consumption
- SKUs used
- Regions used
- Usage chart.
- Timeframe view or Services view table of used services, with the ability to download the table as a CSV file.

The Usage chart has only a Trend bar chart option, but otherwise functions the same as that described in[Usage](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/infrastructure_subscriptions.htm#account_management_usage). You can also view[Rate Card](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/infrastructure_subscriptions.htm#subscriptions_available_services)
