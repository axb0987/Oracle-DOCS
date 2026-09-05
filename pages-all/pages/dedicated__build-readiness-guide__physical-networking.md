# Physical Networking
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/build-readiness-guide/physical-networking.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/build-readiness-guide/physical-networking.htm#dcoc-content-body)

# Physical Networking

Physical networking readiness focuses on how carriers and fiber enter the site, how those paths remain secure and diverse, and how cabling is routed from the carrier demarcation point to Oracle space.

Design Principle Requirement Planning Value
Carrier diversity Plan separate interconnection points or equivalent secure rooms so provider connectivity remains resilient. Two MMRs or equivalent secure alternatives are the baseline expectation.
Secure pathways Route carrier and peer cabling through protected pathways to Oracle space. Use tamper-resistant secure pathways with separation between diverse routes.
Cable distance control Plan rack placement around actual cable run length, not straight-line distance. 70 m is the general maximum planning value. Exadata is limited to 40 m.
Optical media Install SMF on diverse A and B paths from the carrier demarcation point to Oracle space. Minimum 48 strands per path.
Approval artifacts Be ready to share circuit and path-diversity information when required. Oracle may request path drawings, service orders, circuit IDs, or other technical responses during review.

Planning note: In non-contiguous deployments, actual cable length matters more than distance between rack faces. Oracle confirms final rack placement and approved pathway routing during design and expansion review.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
