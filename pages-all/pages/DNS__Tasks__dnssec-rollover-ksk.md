# Rolling Over a Key-Signing Key (KSK)
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-rollover-ksk.htm
- Fetched: 2026-09-05 01:58 CDT

# Rolling Over a Key-Signing Key (KSK)

DNSSEC key-signing keys (KSKs) require annual rollover and key promotion.
KSK rollover begins annually when a replacement DNSSEC key version is automatically created. You need to complete the rollover process manually. You're notified that the new key version requires promotion in the Console. To avoid a service disruption, we also recommend that you set up alarms to ensure that you perform all required key rollovers on time. See[DNSSEC](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnssec.htm)for more information.

- [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-rollover-ksk.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-rollover-ksk.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-rollover-ksk.htm#)
- 

- On the Public zones or Private zones list page, select the zone you want to work with. If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#top).
- Select the DNSSEC tab.
- Verify that the KSK for the zone has a status of Needs Promotion .

Note  
  
You can rollover a KSK sooner than the default 1 year period. Select the key's Actions menu (three dots) and then select Stage replacement key version . A new KSK is created.
- Add a new[DS record](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm#types__dlentry_ds)containing the new (KSK) information to the parent zone.
The parent zone could be a top-level domain (TLD) such as "com", it could be an OCI zone, or a zone you host with another DNS provider. If the parent zone is a top-level domain, the domain registrar usually has a way for you to provide the KSK information for DNSSEC. To obtain the KSK information for the DS record:
- In the zone details, select the DNSSEC tab.
- In the Promote KSK infoblock, select the data type:

- Structured: Digest fields are copied separately. Select this option if the parent zone DNS provider requires separate input for each field in the DS record.
- Unstructured: Digest fields are copied into a single string. Select this option if the parent zone DNS provider supports presentation format input for the DS record.
- Select Copy to copy the digest information and the recommended TTL (time to live) information.
- Paste the DS record digest information into a DS record for the zone. If the zone is an OCI zone, see[Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm)for instructions.
- Select Promote new key-signing key .
- Remove the old[DS record](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Reference/supporteddnsresource.htm#types__dlentry_ds)containing the old (KSK) information from the parent zone.

Important  
  
To avoid service disruptions, after the new DNSKEY record is created you must wait until the DNSKEY record's TTL expires before removing the old DS record .
- 

Use the[oci dns zone stage-dnssec-key-version](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/stage-zone-dnssec-key-version.html)command and its required parameters to stage a new key:

```

```

Use the[oci dns zone promote-dnssec-key-version](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/promote-zone-dnssec-key-version.html)command and its required parameters to promote the staged key:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

Run the[stageDnssecKeyVersion](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/StageZoneDnssecKeyVersion)operation to stage a new key. Run the[promoteDnssecKeyVersion](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/PromoteZoneDnssecKeyVersion)
