# Multitenancy Support Model
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/multitenancy-support-model.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/multitenancy-support-model.htm#dcoc-content-body)

# Multitenancy Support Model

Use this section to learn how support changes when the Dedicated Region customer operates multiple internal tenancies.

In a multitenancy Dedicated Region, support becomes a two-tier model. Internal users work with the Dedicated Region operator for Tier 1 support through the in-realm console. The operator manages those SRs, resolves issues when possible, and opens an Oracle-facing support request when OCI support is required.

Support Design Area Implementation Guidance
Tier 1 ownership The Dedicated Region operator defines and staffs the Tier 1 support model for internal tenants, including support hours, internal service-level agreements (SLAs) or service-level objectives (SLOs), severity handling, and routing.
Tier 2 escalation The operator escalates to OCI support when Oracle help is required. Oracle Tier 2 support has response SLOs for critical issues, while OCI service SLAs continue to apply to the performance, availability, and manageability of eligible services.
Ticket isolation Internal tenant SRs are visible to the internal tenant and operator. Oracle-facing operator SRs are visible to the operator and Oracle. Internal tenants do not access operator SRs.
Data minimization Operators must include only the information that Oracle needs in the Oracle-facing SR and avoid forwarding unnecessary internal tenant data.
Support tooling Internal users can create, update, and close SRs through the in-realm support experience. Operators manage internal SRs and escalations from the Operator Console and support interface.
Support metrics Operators must monitor open, submitted, and resolved SR trends and filter metrics by severity, status, and channel to improve support operations.
Staffing readiness Estimate internal tenant volume, identify support personnel before onboarding, evaluate support skills, and implement a 24x7 rotation when the business requires around-the-clock support.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
