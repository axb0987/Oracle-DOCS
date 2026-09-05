# Finding the DRG Upgrade Status
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-upgrade-status.htm
- Fetched: 2026-09-05 02:43 CDT

# Finding the DRG Upgrade Status

Find the Dynamic Routing Gateway (DRG) upgrade status.

DRGs created before June 2021 (or possibly April 2021 depending on the region) use legacy software, and can be[upgraded to the most recent version](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions). The status can be not updated , in progress , or updated .

DRGs created after that date always use the upgraded software.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-upgrade-status.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-upgrade-status.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-upgrade-status.htm#)
- 

This information is only seen for DRGs created before May 17, 2021. DRGs created after that date are upgraded by default.

On the Dynamic Routing Gateways list page, select the DRG that you want to work with. If you need help finding the list page or the DRG, see[Listing DRGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-list.htm).
If this DRG is a legacy DRG, the upgrade status displays in the Dynamic routing gateway information details tab. Upgraded DRGs don't have a field indicating the upgrade status.
- 

Use the[network drg get-upgrade-status](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/get-upgrade-status.html)command and required parameters to find the DRG upgrade status:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[GetUpgradeStatus](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/GetUpgradeStatus)
