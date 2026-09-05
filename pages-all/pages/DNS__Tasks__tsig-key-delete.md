# Deleting a TSIG Key
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-delete.htm
- Fetched: 2026-09-05 01:59 CDT

# Deleting a TSIG Key

Delete a TSIG key.

Note  
  

A TSIG key attached to a zone must be removed from the zone using DNS Zone Management. See[Managing DNS Service Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/managingdnszones.htm)for more information.

See[Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm)for more information about TSIG keys and how they're used in zones.

For general service information, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm).

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-delete.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-delete.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-delete.htm#)
- 

- On the TSIG keys list page, select the key you want to delete. If you need help finding the list page, see[Listing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig-key-list.htm#top).
- From the Actions menu (three dots) for the TSIG key you want to delete, select Delete .
- When prompted, confirm the deletion.
- 

Use the[tsig delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/tsig-key/delete.html)command and required parameters to delete a TSIG key:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[DeleteTsigKey](https://docs.oracle.com/iaas/api/#/en/dns/latest/TsigKey/DeleteTsigKey)
