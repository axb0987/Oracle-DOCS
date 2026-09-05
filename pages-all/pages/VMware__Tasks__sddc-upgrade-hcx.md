# Upgrading a VMware Solution SDDC's HCX License
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-upgrade-hcx.htm
- Fetched: 2026-09-05 03:09 CDT

# Upgrading a VMware Solution SDDC's HCX License

Learn how to upgrade the SDDC's HCX license from Advanced to Enterprise.

Updgrading an SDDC's HCX license to Enterprise increases the number of on-premises connection keys issued from 3 to 10.
Important  
  

- SDDCs that use standard shapes already include the Enterprise license at no cost.
- The Advanced license is the default, unbilled option for dense shapes. Upgrading the HCX license is a billed option.
- The upgrade work request is started immediately. The Enterprise billing cycle begins as soon as the work request is complete.

For more information, see[HCX License Types](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Concepts/ocvsoverview.htm#HCX-license-types).

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-upgrade-hcx.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-upgrade-hcx.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-upgrade-hcx.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
- On the SDDC's details page, select the Change link on the right side of HCX license type .
- Select I consent to upgrade to the Enterprise license (Billed Upgrade).
- Select Save Changes .

Important  
  
Charges for the Enterprise license upgrade appear in the next billing cycle.
- 

Use the[sddc upgrade-hcx](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/sddc/upgrade-hcx.html)command and required parameters to upgrade the HCX license to Enterprise (Billed Upgrade) :

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpgradeHcx](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Sddc/UpgradeHcx)
