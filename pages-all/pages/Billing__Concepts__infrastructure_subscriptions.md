# Infrastructure Subscriptions
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/infrastructure_subscriptions.htm
- Fetched: 2026-09-05 01:43 CDT

# Infrastructure Subscriptions

For Infrastructure subscriptions, you can review your usage, billing schedule, and rate card information.

The Subscription information page for Infrastructure subscriptions displays subscription details, and lists:
- Subscription ID
- Type
- CSI number
- Original start date
- Start date
- End date
- Total contract value
- Currency

From the Subscription information page for Infrastructure subscriptions, you can view the associated[Usage](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/infrastructure_subscriptions.htm#account_management_usage), the[Billing Schedule](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/infrastructure_subscriptions.htm#subscription_billing_schedule), and[Rate Card](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/infrastructure_subscriptions.htm#subscriptions_available_services)details.

## Usage

Usage is a visualization tool on the Subscription information page that helps you track your annual universal credits usage. Charts are available that show visualization of usage data over time. An in-depth tabular list allows viewing usage either in terms of time (the default Timeframe View ), or in terms of the product ( Services View ).

For example, you can:
- Show universal credits usage for a commitment period or custom date range.
- 

Show hourly, daily, or monthly usage of a particular service based on the period duration.

Usage is organized in terms of the following sections:
- Filters are available globally under Resources .
- A cost usage summary that shows the following, but varies based on the subscription:
- Commit amount (only visible for commitment subscriptions)
- Available (only visible for commitment subscriptions)
- Consumption
- Overage (only visible for commitment subscriptions)
- SKUs used
- Regions used
- Usage chart.
- Timeframe view or Services view table of used services, with the ability to download the table as a CSV file.

### Filtering Subscription Usage Data

Under Filters , subscription usage data can be filtered on the following parameters:
- Subscription phase : To show usage, select a subscription phase. Each of these phases has its own duration, and can be of the Pay As You Go, Commitment, or Promotion/Trial type. For the commitment phase, all commitments are shown in the chart and in the detailed usage section. Similarly, the entire commitment amount is shown in the summary of the usage. For promotions, details of the promotion phase are shown in the summary, such as remaining days of the promotion. For Pay As You Go, given there's no commitment or duration, it goes until the subscription is terminated.
Note  
  
For the Funded Allocation public sector plan, this field changes to Allocation period , rather than Commitment period .
- Start date : Specify the custom start date for filtering.
- End date : Specify the custom end date for filtering.
Note  
  
A message is displayed if there is no associated usage for the selected date range.
- Region : Optionally, select a region.

When viewing usage, you can select either a start/end date range, or a subscription phase, but not both. In addition, when selecting a date range, both the Usage chart and Timeframe view/Services view table granularity changes according to the following:
- If you select the same start and end date, then the time interval is hourly .
- If you select a time period less than or equal to 31 days, then the time interval is daily .
- If you select a time period less than or equal to 36 months, then the time interval is monthly .
- Otherwise, a yearly interval is displayed.

### Usage Summary Data

After Filters , usage information is summarized for the selected order and time period, in terms of the Commitment amount , Available , and Amount used . Percentage values under Available and Amount used also signify how much is available, and how much of the commitment amount has been used. An Overage field can also appear but only when an overage has occurred.

When viewing the commitment period for a monthly/annual commit plan, the committed amount, amount already used, and any overages are displayed. A Total usage amount is displayed for Commit plans.

For a custom date range or Pay As You Go plans, the amount used during the chosen time period is displayed.

### Usage Chart

The Usage chart has two modes: Cumulative line chart and Trend bar chart, available in the Chart type list.

A Cumulative line chart presents a visual representation of usage over time. It shows the actual usage until the current day, and then subsequent projected usage for the remainder of the duration. For a commitment period, the chart shows when the projected or actual usage crossed the committed amount. For a commitment phase, two lines are displayed. The black line indicates the committed amount, versus the blue line that indicates the actual usage amount. For a Pay As You Go customer, actual usage and projected usage are displayed until the end of the selected time period.

A Trend bar chart presents the usage that is metered per each unit of time (per day, month, year) based on the subscription phase length. For commitment phases, the usage below the commitment amount is shown as blue bars, while the overage is shown in yellow. This chart helps to analyze the consumption of credits per day, month, and year, and allows a side-by-side comparison.

In both cases, the Y-axis represents the currency in which an order was booked, while the X-axis corresponds to time. For example, if an annual commitment period is being viewed, the chart is divided up into months. You can hover the mouse over a particular data point to view more detail about it. The chart updates dynamically according to the chosen date range or commitment period.

### Viewing Detailed Usage by Timeframe or Service

When viewing usage by Timeframe view (the default), the table lists the usage by time, with the associated services that were consumed for the particular time-based entry.

When viewing usage by Services view , the table lists the services that were consumed during the time period corresponding to the chosen date range or commitment period.

The views are displayed according to the following fields:

Column Name Description
Date UTC ( Timeframe View only) The date the usage occurred, according to the UTC time zone.
Part number and service name The Oracle assigned product number (SKU) and description.
Region Region where the service was consumed.
Quantity used Quantity consumed during the time period.
Metric Unit of measure for the service.
Date range UTC ( Services View only) Date range for the service.
Net unit price Contracted net unit price.
Amount used The amount billed.
Overage The overage amount billed.

The Timeframe View/Product View table updates dynamically according to the chosen date range or commitment period. Selecting Show exact values displays extended decimal values in the Quantity , Net Unit Price , and Amount Used fields.

Each product in Services View can be expanded to view daily usage details for the service. You can also download the table as a CSV file by clicking Download as CSV .

## Billing Schedule

For monthly/annual commit plans, Billing schedule shows the list of service invoices that are generated. Invoices that have been already generated can be accessed from here as well. If you're Pay As You Go, there's no billing schedule (you get charged for what you use). If your plan is monthly/annual commit, Billing schedule shows the schedule in terms of which lines have and have not been invoiced. Billing schedule is organized in terms of the following fields:

Field Description
Status The invoice status:
- Invoiced
- Not Invoiced

Click Invoice to go to the Invoices page and review invoice information. See[Invoices](https://docs.oracle.com/en-us/iaas/Content/Billing/Concepts/invoices.htm)for more information.
Invoice date (UTC) Invoice generation date according to the UTC time zone.
Start date (UTC) Billing period start date according to the UTC time zone.
End date (UTC) Billing period end date according to the UTC time zone.
Frequency Frequency at which service invoices are generated (typically quarterly or annually).
Quantity The amount billed during the time period.
Net unit price Contracted net unit price.
Line net amount

Amount for which the invoice will be generated, or was generated in the past.

You can also download the table as a CSV file by clicking Download as CSV .

## Rate Card

Rate card shows the list of services that are part of the annual universal credits subscription, along with their rate card over time. Rate card is organized in terms of the following:

Field Description
Service The Oracle assigned product number (SKU) and description. You can also search the Rate Card table by this field, by entering it in the search field at the top of the table.
Metric Unit of measure for the service.
Net unit price Contracted net unit price.

Some entries can have a Multiple link, which opens a Tiers panel that shows tier units and price change information.
