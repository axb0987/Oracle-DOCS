# Available Metrics: oci_emaildelivery
- Source: https://docs.oracle.com/en-us/iaas/Content/Email/Reference/metricsalarms_topic-Available_Metrics_oci_emaildelivery.htm
- Fetched: 2026-09-05 02:01 CDT

# Available Metrics: oci_emaildelivery

Learn about the metrics applicable for the policies you create.

The metrics listed in the following table are automatically available for any policies you create. You do not need to enable monitoring on the resource to get these metrics. However, your tenancy must have Email Delivery configured and must send mail to make the`oci_emaildelivery`metric space available in the Metrics Explorer feature.

Each metric includes the following dimensions: RESOURCEID The OCID of the policy to which the metric applies.

Metric Metric Display Name Unit Description Dimensions
`EmailsAccepted`Emails Accepted count The number of unique emails accepted by the Email Delivery service.`resourceID`(The OCID of the approved sender to which the metric applies.)

`resourceDomain`(The domain name of the approved sender email address to which the metric applies.)
`EmailsBlocklist`Emails Blocklist count The number of email blocked by blocklist.
`EmailComplaints`Email Complaints count The number of email complaints for a sender by the Email Delivery service.
`EmailsHardBounced`Emails Hard Bounced count The number of emails hard bounced (permanent failure) for a sender by the recipient domain's email service.
`EmailsSoftBounced`Emails Soft Bounced count The number of emails soft bounced (persistent transient failure) by the recipient domain's email service or due to an inability to reach that service.
`EmailsSuppressed`Emails Suppressed count The number of email suppressed for a tenant by the Email Delivery service.
`EmailsRelayed`
