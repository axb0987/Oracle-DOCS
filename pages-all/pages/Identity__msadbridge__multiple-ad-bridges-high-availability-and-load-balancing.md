# About Multiple AD Bridges for High Availability and Load Balancing
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/multiple-ad-bridges-high-availability-and-load-balancing.htm
- Fetched: 2026-09-05 02:24 CDT

# About Multiple AD Bridges for High Availability and Load Balancing

If you only have one Microsoft Active Directory bridge component in one Windows Service connecting to your Microsoft Active Directory domain, it can be a single point of failure in the architecture. To avoid this, IAM supports the installation of multiple AD bridge instances mapping to the same Microsoft Active Directory domain.

The maximum number of AD bridges that an administrator can install per domain must not exceed 5. In addition, the maximum number of domains that an administrator can configure per tenant must not exceed 10. To configure these limits, raise an SR with Oracle Support.

With an AD bridge high availability (HA) deployment of at least two AD bridges per domain, delegated authentication and data synchronization loads can be shared among all the AD bridges. The allocation of requests to a AD bridge is random, depending on the availability of that particular AD bridge. One delegated authentication request is picked up by one AD bridge. An AD bridge can pick delegated authentication and full or incremental synchronization. Both AD bridges have the capability to perform data synchronization and delegated authentication simultaneously. However, only one AD bridge can perform data synchronization of a domain at a time.

[

-
