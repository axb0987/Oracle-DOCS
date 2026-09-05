# Listing Vantage Points
- Source: https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-vantage-point.htm
- Fetched: 2026-09-05 02:13 CDT

# Listing Vantage Points

List vantage points in Health Checks.

A vantage point is a geographic location for launching a monitor or on-demand probe. Oracle Cloud Infrastructure maintains vantage points on the infrastructure of cloud providers around the world, including AWS, Azure, and Google.

- [Console](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-vantage-point.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-vantage-point.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-vantage-point.htm#)
- 

You can list vantage points in the Console when[creating](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-vantage-point.htm#unique_1387481542)or[updating a health check](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-vantage-point.htm#unique_1052676947).

## At Creation

- On the Health checks list page, select Create health check . If you need help finding the list page, see[Listing HTTP Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor.htm#top)or[Listing Ping Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-monitor.htm#top).
The Create health check dialog box opens.
- In the Vantage points field, select the vantage points that you want from the list of available vantage points. We recommend selecting three or more vantage points across three different providers.
- Provide values for the remaining fields.
For field descriptions, see[Creating an HTTP Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-monitor.htm#top)or[Creating a Ping Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-ping-monitor.htm#top).
- Select Create health check .
The new health check's details page opens. Results appear after a few moments.

## When Updating

- On the Health checks list page, select the health check that you want to work with. If you need help finding the list page or the health check, see[Listing HTTP Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-http-monitor.htm#top)or[Listing Ping Monitors](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-ping-monitor.htm#top).
The health check's details page opens.
- Select Edit .
- In the Vantage points field, select the vantage points that you want from the list of available vantage points. We recommend selecting three or more vantage points across three different providers.
- Update remaining fields as needed.
For field descriptions, see[Creating an HTTP Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-http-monitor.htm#top)or[Creating a Ping Monitor](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/create-ping-monitor.htm#top).
- Select Save .
- 

Use the[oci health-checks vantage-point list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks/vantage-point/list.html)command and required parameters to list vantage points:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI for Health Checks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/health-checks.html).
- 

Run the[ListHealthChecksVantagePoints](https://docs.oracle.com/iaas/api/#/en/healthchecks/latest/HealthChecksVantagePointSummary/ListHealthChecksVantagePoints)operation to list vantage points.

## Sample List

The following list is a sample of available vantage points for Health Checks. The list of vantage points is dynamic and changes frequently.

To list current vantage points, see[Listing Vantage Points](https://docs.oracle.com/en-us/iaas/Content/HealthChecks/Tasks/list-vantage-point.htm#top).

Provider Location Name
Amazon Ashburn, VA`aws-iad`
Amazon Columbus, OH`aws-cmh`
Amazon Dublin`aws-dub`
Amazon Frankfurt`aws-fra`
Amazon London`aws-lhr`
Amazon Mumbai`aws-bom`
Amazon Paris`aws-cdg`
Amazon Portland, OR`aws-pdx`
Amazon San Francisco`aws-sfo`
Amazon Sao Paolo`aws-gru`
Amazon Seoul`aws-icn`
Amazon Singapore`aws-sin`
Amazon Stockholm`aws-arn`
Amazon Sydney`aws-syd`
Amazon Tokyo`aws-tyo`
Amazon Toronto`aws-yyz`
Azure Ashburn, VA`azr-iad1`
Azure Chicago`azr-ord`
Azure Dublin`azr-dub`
Azure Hong Kong`azr-hkg`
Azure Johannesburg`azr-jnb`
Azure San Antonio, TX`azr-sat`
Azure Sau Paulo`azr-gru`
Azure Singapore`azr-sin`
Google Charleston, SC`goo-chs`
Google Council Bluffs, IA`goo-cbf`
