# VMware Solution Billing Options
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Concepts/billing-options.htm
- Fetched: 2026-09-05 03:07 CDT

# VMware Solution Billing Options

Learn about VMware solution's flexible billing options.

When you provision an SDDC and define its initial clusters, you select a pricing interval for each cluster. The pricing interval for a cluster applies to all hosts in the cluster. Different clusters can have different pricing intervals. Any clusters you add to the SDDC after initial provisioning can also have its own selected pricing interval.

## Pricing Intervals
Each pricing interval requires a minimum host runtime commitment and offers different pricing advantages. For full pricing information for each option, see[Oracle Compute Pricing](https://www.oracle.com/cloud/compute/pricing.html)and[Oracle Cost Estimator](https://www.oracle.com/cloud/cost-estimator.html).

Pricing Interval Required Commitment Notes

Hourly

Hourly pricing requires a minimum of 8 hours of committed host runtime

Use this interval for test projects or short-term high utilization events where extra capacity is required for a limited time. This is the default selection for standard shape hosts.

Monthly

Monthly pricing requires a minimum of 1 month of committed host runtime.

This interval is a common option, and is the default selection for dense shapes.

Yearly

One year pricing requires a minimum of 1 year of committed host runtime.

Use this interval for long-term projects such as workload or application migration to Oracle Cloud Infrastructure.

Every Three Years

Three year pricing requires a minimum of 3 years of committed host runtime.

Use this interval for very long-term projects or mission-critical workloads that aren't easily migrated.

You select an initial pricing interval for each cluster that you define when you create an SDDC. Any hosts that are created during the SDDC provisioning are subject to the selected interval commitment for the cluster it resides in. After the SDDC is provisioned, you can create more hosts in the SDDC cluster with longer or shorter pricing intervals at any time. Hosts don't all have to use the same pricing interval, so you can select a pricing interval that best suits the purpose of the host.

You can change a pricing interval for individual hosts. When you change the pricing interval for a host, the new pricing interval doesn't take effect until the date and time that the old interval ends.
For example, let's say you create a host and choose the pricing interval of Every Three Years. If you later decide the host should have a Monthly pricing interval, the new Monthly pricing interval won't take effect for three years. If you cancel the commitment before the end of the selected pricing interval, billing continues until the interval ends.
Important
