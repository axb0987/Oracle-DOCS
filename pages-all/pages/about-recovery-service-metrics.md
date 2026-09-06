# About Recovery Service Metrics
- Source: https://docs.oracle.com/iaas/recovery-service/doc/about-recovery-service-metrics.html
- Fetched: 2026-09-05 18:57 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/recovery-service/doc/about-recovery-service-metrics.html#dcoc-content-body)

# About Recovery Service Metrics

Learn about the metrics emitted by the metric namespace:`oci_recovery_service`( Oracle Database Autonomous Recovery Service ).

A protected database is an Oracle Database that uses Recovery Service for backups and data protection.

Use Recovery Service metrics to monitor the backup performance of your protected databases. For example, you can use metrics to monitor the protection status or health of your database, the amount of backup storage space utilized to meet the recovery window goal, etc.

In the OCI Console , use the Protected database details page to view the default metric charts for a single protected database. Use the Oracle Cloud Infrastructure Monitoring service to view metrics for multiple protected databases.

You can also use the Oracle Cloud Infrastructure Monitoring service to build metric queries and create alarms to be notified when the metrics meet alarm-specified triggers.
The following terms are helpful for understanding metrics:
- Namespace : A container for Recovery Service metrics.`oci_recovery_service`is the Recovery Service namespace.
- Metrics : The fundamental concept in telemetry and monitoring. Metrics define a time-series set of datapoints. Each metric is uniquely defined by namespace, metric name, compartment identifier, a set of one or more dimensions, and a unit of measure. Each datapoint has a timestamp, a value, and a count associated with it.
- Dimensions : A key-value pair that defines the characteristics associated with the metric. For example,`resourceId`, which is the protected database OCID.
- Statistics : Metric data aggregations over specified periods of time. Aggregations are done using the namespace, metric name, dimensions, and the datapoint unit of measure within the time period specified.
- Alarms : Used to automate operations monitoring and performance. An alarm keeps track of changes that occur over a specific period of time. It also performs one or more defined actions, based on the rules defined for the metric.

To monitor resources, you must have the required type of access to Recovery Service resources in a policy written by an administrator.

Parent topic:[Recovery Service Metrics](https://docs.oracle.com/iaas/recovery-service/doc/recovery-service-metrics.html#GUID-E1EBF5BD-8BDE-413F-B8C4-EE059180342B)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
