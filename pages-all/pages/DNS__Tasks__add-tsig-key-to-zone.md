# Adding a TSIG Key to a Secondary DNS Zone
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-tsig-key-to-zone.htm
- Fetched: 2026-09-05 01:58 CDT

# Adding a TSIG Key to a Secondary DNS Zone

You can add a TSIG key directly to a secondary domain name service (DNS) zone. A TSIG key lets DNS authenticate updates to secondary zones.

See[Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm)for information about TSIG keys and how they're used in zones.

For information about the service, see the[DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/../Concepts/dnszonemanagement.htm).

## Using the Console

- On the Public zones list page, select the secondary zone you want to work with. If you need help finding the list page, see[Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#top).
- Select the Upstream servers tab.
- Select Manage upstream servers .
- Find the existing upstream server that you want to associate the TSIG key with, or select Add additional server IP to add a new one.
- Select an existing key or select Create a new TSIG key and provide the following details:

- Name: The name of the key used in domain name syntax. We recommend that the name reflect the names of the hosts and uniquely identify the key among a set of keys these two hosts might share at any particular time.
- Algorithm: Select the public key's algorithm used to encrypt or decrypt data. Applicable algorithms include hmac-md5, hmac-sha1, hmac-sha224, hmac-sha256, hmac-h384, and hmac-sha512.
- Secret: The base64 string encoding the binary shared secret that corresponds to the key. A maximum value of 255 characters is allowed.
- Show Advanced Options: Optionally, you can apply tags. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- If you created a key, select Create TSIG key .
-
