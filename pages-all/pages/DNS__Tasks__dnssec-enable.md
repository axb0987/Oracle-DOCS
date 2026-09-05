# Enabling DNSSEC on a Zone
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-enable.htm
- Fetched: 2026-09-05 01:58 CDT

# Enabling DNSSEC on a Zone

Enable DNS security extensions (DNSSEC) on a public zone.

Note  
  

You can't enable DNSSEC on a private zone, or on a zone with downstream servers configured.

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-enable.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-enable.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-enable.htm#)
- 

- On the Public zones or Private zones list page, select the zone you want to work with. If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#top).
- In Zone information , under DNSSEC, select Edit .
- Select the DNSSEC switch to Enabled .
- Select Save changes .

Important  
  
Wait for the work request to complete successfully before proceeding.
- For DNSSEC to work correctly, you need to add the key signing key (KSK) information to the parent zone.
The parent zone could be a top-level domain (TLD) such as "com", it could be an OCI zone, or a zone you host with another DNS provider. If the parent zone is a top-level domain, the domain registrar usually has a way for you to set the KSK information for DNSSEC. To obtain the KSK information for the DS record:
- In the zone details page, select the DNSSEC tab.
- In the Promote KSK infoblock, select the data type:

- Structured: Digest fields are copied separately. Select this option if the parent zone DNS provider requires separate input for each field in the DS record.
- Unstructured: Digest fields are copied into a single string. Select this option if the parent zone DNS provider supports presentation format input for the DS record.
- Select Copy to copy the digest information and the recommended TTL (time to live) information.
- Paste the DS record digest information into a DS record for the zone. If the zone is an OCI zone, see[Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm)for instructions. Here is an example of a DS record containing KSK digest information:

```

```

- Select Promote new key-signing key .
- 

Use the[zone create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/create.html)command and required parameters to create a public primary zone. To enable DNSSEC, set the`dnssec-state`option to enabled :

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. For information on adding a record to the zone, see[Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm).
- 

Run the[CreateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/CreateZone)operation to create a public primary zone. Specify the zone type as`PRIMARY`and zone scope as`GLOBAL`. To enable DNSSEC, specify the`dnssecState`as`ENABLED`.

The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. For information on adding a record to the zone, see[Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm)
