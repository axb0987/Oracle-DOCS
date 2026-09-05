# Troubleshooting DNSSEC Issues
- Source: https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-troubleshooting.htm
- Fetched: 2026-09-05 01:58 CDT

# Troubleshooting DNSSEC Issues

Troubleshoot common issues with DNSSEC.

- Useful tools people can use to verify their DNSSEC configuration are BIND's[Dig tool](https://www.isc.org/downloads/),[DNSViz](https://dnsviz.net/), or[DNS Analyzer](https://dnssec-analyzer.verisignlabs.com/).
- When reaching out to support, it's helpful to indicate if the zone is DNSSEC enabled, what parent/child DS records exist, dig results using`+dnssec`, and the results of using[DNSViz](https://dnsviz.net/).
- Maintaining a valid chain of trust is important because broken chains of trust result in data being marked as invalid, which can cause domains and subdomains to become invisible to verifying clients. Security lameness is when a parent zone has a DS record pointing to a nonexistent DNSKEY. If all DS records point to nonexistent DNSKEYs, then the child zone is marked as invalid.
-
