# Editing VN Encryption
- Source: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_vn_encryption.htm
- Fetched: 2026-09-05 02:44 CDT

# Editing VN Encryption

Turn VN encryption on or off for a VCN.

This feature is only available in the US Government Cloud. Before you change the settings for VN encryption, be sure you understand the full impacts of doing so, as explained in[VN Encryption](https://docs.oracle.com/iaas/Content/gov-cloud/govinfo.htm#govinfo_topic_LAN-encryption).

Turning this feature on or off isn't immediate. Expect a 10 minute delay between enabling or disabling this feature and full implementation of that change.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_vn_encryption.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_vn_encryption.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/edit_vn_encryption.htm#)
- 

- On the Virtual Cloud Networks list page, select the VCN that you want to work with. If you need help finding the list page or the VCN, see[Listing VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-vcn.htm).
- In the VCN information tab for the VCN, select Edit next to the VN Encryption status, which is either "Enabled" or "Disabled."
- Select or unselect the Enable VN Encryption checkbox.
- Select Save Changes .
- 

Use the[network vcn update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/vcn/update.html)command and parameters shown to turn VN Encryption on:

```

```

To turn VN Encryption off:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[UpdateVcn](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Vcn/UpdateVcn)
