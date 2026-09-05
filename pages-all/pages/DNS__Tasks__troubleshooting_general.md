# Common Private DNS Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/troubleshooting_general.htm
- Fetched: 2026-09-05 01:59 CDT

# Common Private DNS Issues

Troubleshoot common issues with private DNS.

- If a resolver rule matches the set conditions then the action is applied regardless of result. Later rules aren't applied. For example, if the target destination of a forward rule is unreachable, the traffic is forwarded and no further rule actions are taken.
- When creating a resolver endpoint, ensure the subnet has enough available IP addresses. Listening resolver endpoints require one. Forwarding resolver endpoints require two.
- If Compute instances want to resolve private DNS views and rules using the 169.254.169.254 resolver and they're using custom DHCP settings, 169.254.169.254 must appear in the DHCP nameserver list, otherwise 169.254.169.254 only resolves queries to the internet.
- 

If DNS responses for internet DNS names return`SERVFAIL`, validate that the target DNS names don't fail DNSSEC validation.

For more information on Troubleshooting DNSSEC, see[Troubleshooting DNSSEC Issues](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-troubleshooting.htm).
- 

The private DNS system evaluates DNS requests in the following sequence:

- Private views ( zones )
- Rules
- Internet Attached views are evaluated first in the order configured. The default view is evaluated next, unless it was included in the list of attached views. A match in the sequence ends the resolution, even if the match results in an NXDOMAIN .

For example, if there were a rule to forward any name matching`onprem.example.com`to an on-premises system, but there was a zone in a private view defined as`example.com`. The private view would answer the lookup for`onprem.example.com`and the forwarding rule would never be reached.

## Serving Stale Data to Improve DNS Resiliency

-
