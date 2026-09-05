# IP Address Insights
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ip_inventory.htm
- Fetched: 2026-09-05 02:41 CDT

# IP Address Insights

Use IP Address Insights to get a holistic view of the IP addresses used across a tenancy, potentially spanning multiple compartments.
IP Address Insights provides you with a hierarchical visbility into VCNs, respective subnets, and network resources, enabling you to centrally monitor and manage IP administration for cloud assets with ease. It also provides the data on IP utilization to identify potential issues and resolve them. Using IP Address Insights, you can:
- View IP addresses used across a tenancy
- View IP utilization of network resources in a tenancy
- Review IP conflicts
- Manage alarms when IP utilization crosses a threshold

## Required IAM Policies

To use Oracle Cloud Infrastructure, you must be granted security access in a policy by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which compartment to work in.

For administrators, see[IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Policies).
Create this policy to allow a group to access IP Address Management (IPAM) in the tenancy or a specific compartment.

```

```

```

```

## Limitations

The following limitations have been identified in the CIDR utilization metrics within IP Address Insights:
- Metric Availability : Subnet CIDR utilization metrics are published at fixed intervals, approximately every 30 minutes. In regions with many subnets, publishing metrics might take longer than the typical interval.
- Sampling Interval : Metrics are collected at set intervals. Short-duration changes in CIDR utilization that occur between collection cycles might not appear in the metric graphs.
- Reported Utilization Values : CIDR utilization values are computed through periodic processing. As a result, the percentage returned by the`Get Subnet CIDR Utilization`
