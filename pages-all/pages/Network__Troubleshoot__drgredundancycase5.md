# Redundancy Remedy: Case 5
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/drgredundancycase5.htm
- Fetched: 2026-09-05 02:48 CDT

# Redundancy Remedy: Case 5

This topic describes one of several redundancy issues that you might be alerted to in the Console.

## Summary of the Issue

You use Site-to-Site VPN to connect your on-premises network to a VCN. Although Oracle provisions two IPSec tunnels for the connection, only one of them is up/active. Your connection to Oracle is at risk when routine maintenance is performed on the Oracle router.

## How to Fix the Issue

The following diagram illustrates the issue.

Before the fix:
[

Notice that a Site-to-Site VPN consists of two IPSec tunnels, and Oracle automatically provisions each on a different Oracle router.

After the fix:
[

If your CPE supports having two active IPSec tunnels, you need to bring up the second tunnel. This avoids having the single tunnel as a point of failure. Oracle recommends configuring both tunnels to use BGP dynamic routing.
Note  
  
How to bring up the tunnel depends on which CPE device you use. See the instructions for your CPE device. Devices are listed at[CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/../Tasks/configuringCPE.htm)
