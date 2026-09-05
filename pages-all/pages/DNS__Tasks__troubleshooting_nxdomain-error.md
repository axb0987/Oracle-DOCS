# Querying For a Private Zone After Creation Returns an NXDOMAIN Error Message or Public IP Address
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/troubleshooting_nxdomain-error.htm
- Fetched: 2026-09-05 01:59 CDT

# Querying For a Private Zone After Creation Returns an NXDOMAIN Error Message or Public IP Address

Querying a private zone returns an NXDOMAIN error message or a public IP address.

- If a query is sent before the private zone is published, the query recurses to the internet. An error message stating that the domain doesn't exist or a public name response is returned for the query.
-
