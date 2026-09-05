# Viewing the Custom Logs Acceptance Rate
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/viewing_custom_logs_acceptance_rate.htm
- Fetched: 2026-09-05 02:36 CDT

# Viewing the Custom Logs Acceptance Rate

You can use the Oracle Cloud Infrastructure Monitoring service Service Metrics page to track the custom logs acceptance rate in your tenancy.

To view the rate of custom log throughput that the system is ingesting, open the navigation menu and click Observability &amp; Management . Under Monitoring , click Service Metrics . The Service Metrics page opens.

From the Metric namespace list, select oci_logging . The Logging charts are then displayed, along with time-based filtering controls.

The Custom Log Acceptance Rate chart shows the throttling rate for custom logs. The X-axis indicates the time, while the X-axis represents the percentage. For example, a value of 1 in the chart corresponds to 100%, which means all data is being received and ingested based on the throttling limit. A value less than 1 means that not all data is being accepted.

For example, assuming there is throughput of 10 GB, but 12 GB has been received, then the additional 2 GB gets added to the queue to be ingested later. Until the 10 GB is processed, the additional 2 GB is not forwarded. This scenario translates to an acceptance rate that decreases from 1 to 0.8, or 80%. Less data is being accepted and the remainder goes into the queue (80% accepted, 20% in the queue).

As a result, you can use this metric to determine if OCI Logging is receiving your data. If your data volume is large, then the Custom Log Acceptance Rate metric helps highlight whether the system is burdened, and you can therefore potentially stop sending more data and instead try again later.

For more information on Monitoring, see[Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm)and[Logging Metrics](https://docs.oracle.com/en-us/iaas/Content/Logging/Concepts/../metrics.htm)
