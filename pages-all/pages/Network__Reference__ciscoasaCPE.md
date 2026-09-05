# Cisco ASA Configuration Options
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPE.htm
- Fetched: 2026-09-05 02:42 CDT

# Cisco ASA Configuration Options

Select the configuration based on the ASA software version:
- 9.7.1 or newer:[Route-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm)
- 8.5 to 9.7.0:[Policy-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEpolicybased.htm)
- Older than 8.5: Not supported by the Oracle configuration instructions. Consider upgrading to a newer version.
Important  
  

We recommend using a[route-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/../Reference/ciscoasaCPEroutebased.htm)to avoid interoperability issues and to achieve tunnel redundancy with a single Cisco ASA device.

The Cisco ASA doesn't support route-based configuration for software versions older than 9.7.1. For the best results, if the device allows it, we recommend that you upgrade to a software version that supports route-based configuration.
