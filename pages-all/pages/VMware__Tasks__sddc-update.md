# Editing an VMware Solution SDDC
- Source: https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-update.htm
- Fetched: 2026-09-05 03:09 CDT

# Editing an VMware Solution SDDC

Edit an SDDC in VMware Solution. You can update SDDC properties such as display name, SSH key, VMware software version, and the VLANs that the SDDC uses.

If you change the VMware software version after provisioning an SDDC, the new version is used only on ESXi hosts that you add to the SDDC. The software version of existing hosts isn't changed.

Changes that you make to the SDDC by using the OCI Console, API, or CLI aren't automatically made in vCenter. For example, if you change the software version or the SSH keys, the change applies only to ESXi hosts that you add to the SDDC. To change these properties for existing hosts, you must make the applicable updates in vCenter manually.

- [Console](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-update.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-update.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/sddc-update.htm#)
- 

Information in the Console might be shown in a different order than is presented in this topic. Regardless of the order presented, all required and optional fields are the same.

- On the Software-Defined Data Centers list page, select the SDDC that you want to work with. If you need help finding the list page or the SDDC, see[Listing SDDCs](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/../Tasks/sddc-list.htm).
The SDDC's details page opens with the SDDC information tab selected.
- On the details page, select Edit SDDC .
- In the Edit SDDC panel, update the settings that you want to change:

- SDDC name: Enter a descriptive name for the SDDC. This name must be unique among all SDDCs in the creating, active, or updating state across all compartments in the region. The SDDC name must be 1 to 16 characters, start with a letter, and contain only non-accented letters, numbers, and hyphens (`-`). Hyphens can't be next to each other. The name is not case-sensitive. For example,`test`and`Test`are treated as the same name. Avoid entering confidential information.
- Optional: Configure any available add-ons:
- VMware Avi Load Balancer License allocation compartment: Select the target compartment.
- VMware Avi Load Balancer License allocation: Select the license allocation.
- Instances: Number of assigned instances.

For more information on license allocations see[Listing VMware Solution License Allocations](https://docs.oracle.com/en-us/iaas/Content/VMware/Tasks/license-allocation-list.htm).
- Tags: Edit or add tags.
- SSH key: Provide the public key part of the SSH key. This key is required for remote connections to the ESXi hosts.
- Perform one of the following actions depending on the option that you see:

- Select Update .
- Select Save Changes .
- (Recommended) Select the vSphere client link to go to vCenter, and make the appropriate updates for the SDDC properties that you changed in the Console. You can do this task now or after you save your changes.
- 

Use the[sddc update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ocvs/sddc/update.html)command and required parameters to update the SDDC:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateSddc](https://docs.oracle.com/iaas/api/#/en/vmware/latest/Sddc/UpdateSddc)
