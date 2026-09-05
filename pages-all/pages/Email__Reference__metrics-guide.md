# Email Metrics Querying
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/metrics-guide.htm
- Fetched: 2026-09-05 02:01 CDT

# Email Metrics Querying

You can access and analyze email metrics using the web console, API, or command line interface (CLI).

The core of this process is creating a metrics query. The easiest way to build these queries is with the[Metrics Explorer in the OCI web console. The Metrics Explorer lets you select filters, constructs the query syntax for you, and allows you to use that syntax in the API or CLI to search for metrics.

Metrics queries use Oracle Monitoring Query Language (MQL) to specify:
- Metric(s) to retrieve
- Interval for data aggregation
- Dimension(s) to limit the data
- Grouping criteria
- Statistic function to apply to each interval's data
- Predicate to filter results by threshold or absence of data

For more information, see the[Email Delivery Metrics Reference](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/metricsalarms_topic-Available_Metrics_oci_emaildelivery.htm), which lists all available Email Delivery metrics and their dimensions.

## Building a Query in Metrics Explorer

- From the compartment list, select the compartment or choose root for all tenancies.
- From the metric namespace options, select oci_emaildelivery for Email Delivery metrics.
- Choose a metric name, such as accepted , relayed , bounced , complaints , open , or another available metric. Only metrics with data are shown.
- Select a time interval (default is 1 minute). You can select whole-hour , whole-day , or set a custom interval in minutes or hours.
- Choose a statistic (default is mean ; other options include percentiles such as Pxx ).
- Select one or more dimensions:

- Choose a dimension name, such as resourceDomain (email sending domain) or resourceId (approved sender).
- Based on your choice, select a dimension value (domain or sender) from the displayed list.
- Select Update Chart . The MQL query appears in the left panel. The chart above displays the resulting data.
- To create an alarm based on the query, select Create Alarm . You can use Notification or Streaming services to send alerts.

## Example Metrics Queries

Data Needed Query (time range separate from query)
All emails submitted by the service, per minute`EmailsAccepted[1m].count()`
All emails submitted by the service, per hour`EmailsAccepted[1h].count()`
Emails relayed (that is, successfully relayed to recipient email provider) by all`sales.mydomain.com`senders, per day`EmailsRelayed[1d]{resourceDomain = "mydomain.com"}.count()`
Hard bounce count, per day`EmailsHardBounced[1d].count()`
Count of the daily number of emails sent by the sender marketing@mydomain.com that are suppressed (blocked) because the recipient is on the suppression list.`EmailsSuppressed[1d]{resourceId = "<sender-ocid>"}.count()`

Note: The`resourceId`dimension requires the OCID of the approved sender, not the email address. You can get the sender OCID from the[Approved Senders](https://www.oracle.com/cloud/sign-in.html?redirect_uri=https%3A%2F%2Fcloud.oracle.com%2Fmessaging%2Femail%2Fsenders)page.
Emails opened for mydomain.com senders, per day`EmailsOpened[1d].count()`
Note  
  

Metrics cannot be grouped by a custom header dimension. If you need this capability, use the Logging integration. For instructions, see[Email Log Searching](https://docs.oracle.com/en-us/iaas/Content/Email/Reference/log-guide.htm).

## Querying Email Delivery Metrics Using the API

To access email delivery metrics using the API, use the Monitoring service's[`SummarizeMetricsData`](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/MetricData/SummarizeMetricsData)method. Like Metrics Explorer, this method requires a compartment OCID and a[`SummarizeMetricsDataDetails`](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/datatypes/SummarizeMetricsDataDetails)object containing the date range, namespace (use`oci_emaildelivery`for Email Delivery metrics), and an MQL query.
Note  
  
When filtering by metric dimensions, such as`resourceDomain`or`resourceId`, MQL requires double quotes. If you use Python or a similar language, enclose the MQL string in single quotes in your code so you can keep the required double quotes around values inside the MQL. See the code samples below.

The following table lists sample python metrics list and data queries. Replace`<compartment_ocid>`with your compartment OCID, or your tenancy OCID when querying within the root compartment.

Data Needed Code Sample (Python)

List of available metrics for the "oci_emaildelivery" namespace, sorted by name in ascending order
```

```

Double quotes surround all parameter values because there is no query that contains double quotes.

Count of emails accepted per minute within a one-hour window (12:00-13:00 on 2 March 2023) across all senders and sending domains
```

```

Double quotes surround all parameter values because there is no query that contains double quotes.

Count of opens per day for a 14-day period for all emails sent by a particular approved sender
```

```

Single quotes used around arguments in Python strings so you can use double quotes as required by MQL query for`resourceDomain`values.

Count of opens per day for a 14-day period for all emails sent by a particular approved sender
```

```

Single quotes used around arguments in Python strings so you can use double quotes as required by MQL query for`resourceDomain`
