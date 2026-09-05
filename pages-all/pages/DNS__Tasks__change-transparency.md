# Change the Transparency Mode of a Private Zone
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/change-transparency.htm
- Fetched: 2026-09-05 01:58 CDT

# Change the Transparency Mode of a Private Zone

Update the transparency mode used by a private DNS zone.

## Using the Console

- On the Private zones list page, select the zone you want to work with. If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#top).
- On the right side of the Resolution Mode information, select Edit . The Edit resolution mode screen appears.
- Select a different resolution mode. See[DNS resolution mode](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns-zone-transparency)for details on resolution mode behaviors.
- Select Update .

## Using the CLI

Use the[zone update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/update.html)command and required parameters to update the transparency mode used by a private DNS zone to transparent:

```

```

For a complete list of flags and variable options for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).

## Using the API

Run the[UpdateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/UpdateZone)
