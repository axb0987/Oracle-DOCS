# Dangling DNS Delegation
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dangling-dns-delegation.htm
- Fetched: 2026-09-05 01:58 CDT

# Dangling DNS Delegation

Learn about dangling DNS delegation, which can occur when name server records continue to delegate a domain or subdomain to DNS name servers for a DNS zone that no longer exists.

This situation can occur when you delete the OCI DNS zone but don't update name server records at the domain registrar or in the parent DNS zone.

## DNS Resolution and Delegation Risk

Stale registrar or parent-zone name server records can remain after public zone deletion. These stale records can cause DNS resolution issues and might create a potential DNS or security risk.

You are responsible for updating or removing registrar or parent-zone name server records, if required. Cleanup depends on how the domain or subdomain is delegated.

## Deleting a Public DNS Zone

To delete a public DNS zone, follow these steps:

- Identify where the domain or subdomain is delegated.
- If required, update or remove those name server records.
- Delete the public DNS zone in OCI DNS when it is no longer needed.
- After deletion, check whether registrar or parent-zone name server records still point to the OCI name servers for the deleted zone.
- Verify DNS resolution after delegation changes propagate.
After cleanup, the domain or subdomain should no longer delegate to name servers for the deleted OCI DNS zone, unless that delegation is still required for your configuration.

The OCI Console reminder uses the phrase "if required" because cleanup depends on how the domain is delegated:
- For an apex domain, you might need to update registrar name server records.
- For a child zone or subdomain, you might need to update name server records in the parent DNS zone.
-
