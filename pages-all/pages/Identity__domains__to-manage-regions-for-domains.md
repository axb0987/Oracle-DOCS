# Replicating an Identity Domain to Multiple Regions
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm
- Fetched: 2026-09-05 02:21 CDT

# Replicating an Identity Domain to Multiple Regions

You can replicate an identity domain in IAM to additional regions to enable users in that domain to interact with OCI resources in those regions.

Replication is always enabled for the Default identity domain. The Default identity domain always replicates to all regions to which the tenant is subscribed. When an administrator subscribes to another region, the Default identity domain automatically replicates to that region. Additional identity domains are created in a home region that's specified at creation time. They don't replicate to other regions unless replication is specifically enabled.

You should enable replication if users in an identity domain need to interact with OCI resources in regions beyond that domain's home region. For example, if the domain was created with Germany Central (Frankfurt) as its home region, replication to France Central (Paris) lets users in the domain interact with OCI resources in Frankfurt or Paris, but not US East (Ashburn), even if the tenancy is subscribed to that region.
Note  
  
Enabling or disabling replication doesn't affect[disaster recovery](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/disaster_recovery_and_domains.htm).

Before you begin: Ensure that the tenancy is subscribed to the regions to which you want to replicate the identity domain. For more information about the home regions and the basics of managing your region subscriptions, see[Managing Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../regions/managingregions.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm#)
- 

Ensure that the tenancy is subscribed to the regions to which you want to replicate the identity domain. For more information about the home regions and the basics of managing region subscriptions, see[Managing Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/../regions/managingregions.htm).

- On the Domains list page, select the domain that you want to work with. If you need help finding the list page or the domain, see[Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm).
- Perform one of the following actions depending on what you see:
- From the Actions menu, select Manage regions .
- Select More actions , and then select Manage regions .
The Manage regions panel displays a list of regions that the tenancy is subscribed to.
- Perform one of the following actions depending on what you see:
- From the Actions menu (three dots) for the region that you want to replicate to, select Enable replication .
- For the region that you want to replicate to, select Enable replication .
- Confirm the replication.
- 

Use the[oci iam domain enable-replication-to-region](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/domain/enable-replication-to-region.html)command and required parameters to replicate an identity domain to multiple regions:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[EnableReplicationToRegion](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/EnableReplicationToRegion)
