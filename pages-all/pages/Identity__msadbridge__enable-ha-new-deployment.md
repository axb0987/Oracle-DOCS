# Enable HA for a New Deployment
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/enable-ha-new-deployment.htm
- Fetched: 2026-09-05 02:24 CDT

# Enable HA for a New Deployment

Enabling high availability for an existing AD bridge deployment in an IAM identity domain.

AD Bridge High Availability must be enabled for you. Enter an SR with Oracle Support to enable the feature.

## Limitations
Note the following limitations for AD bridge HA.
- AD bridge HA will not work if any one of the AD bridges installed for a domain is version 19.3.3 and below.
- Only one AD bridge can be configured in one Windows machine. To configure multiple AD bridges you have to use multiple Windows machines in the same domain. Note that without AD bridge HA enabled by Oracle Support, installation of second AD bridge for the domain fails.
- Maximum of 5 AD bridges per domain can be configured by an administrator for HA and load sharing.
Note
