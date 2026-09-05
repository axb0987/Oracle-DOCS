# Upgrading a DRG
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-upgrade.htm
- Fetched: 2026-09-05 02:44 CDT

# Upgrading a DRG

Upgrade a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.

A legacy DRG created before June 2021 (or possibly April 2021 depending on the region) must be upgraded before you can connect it to more than one VCN, use it in cross-tenancy peering scenarios, or change the internal routing policies. This upgrade process doesn't change the DRG's OCID. For details, see[Before you Upgrade a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__before_upgrade).
Note  
  
You can't roll back this change to the DRG. Upgrading the DRG resets existing BGP sessions for both Site-to-Site VPN and FastConnect.

To monitor the upgrade process or decide whether you might need to upgrade a DRG, follow the steps in[Finding the DRG Upgrade Status](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-upgrade-status.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-upgrade.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-upgrade.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-upgrade.htm#)
- 

- On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
- Select the name of the DRG.
- Select Upgrade DRG .
This option is available only for legacy DRGs that can be upgraded.

A message appears reminding you the action can't be reversed.
- Select Upgrade DRG .
- The upgrade occurs in the background. You can continue to make configuration settings while the upgrade is occurring. You're notified when the upgrade is complete.
- When the upgrade finishes, select Refresh page to gain access to the new DRG capabilities.
- 

Use the[network drg upgrade](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/upgrade.html)command and required parameters to upgrade a legacy DRG:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpgradeDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/UpgradeDrg)
