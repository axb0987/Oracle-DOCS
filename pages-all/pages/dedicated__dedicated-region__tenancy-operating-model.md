# Tenancy Operating Model
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/tenancy-operating-model.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/tenancy-operating-model.htm#dcoc-content-body)

# Tenancy Operating Model

This section describes when to use Dedicated Region single tenancy or multi-tenancy and what operators must plan before enabling multiple independent internal tenancies.

Dedicated Region single tenancy is intended for organizations that need a dedicated OCI cloud region for their exclusive use in a customer-selected location. Common drivers include data residency, sovereignty, regulatory compliance, security control, low-latency access to on-premises systems, and access to OCI public cloud services in a dedicated environment.

Dedicated Region multitenancy is intended for large organizations that need hard isolation across internal departments, agencies, or business units while operating a single Dedicated Region realm. Common drivers include departmental resource isolation, spend and usage limits, consumption visibility, isolated support requests, and Tier 1 support from an internal operator team.

Dedicated Region multitenancy is intended for large organizations that need hard isolation across internal departments or business units while operating a single Dedicated Region realm. Common drivers include departmental resource isolation, spend and usage limits, consumption visibility, isolated support requests, and Tier 1 support from an internal operator team.

Design Decision Single-Tenancy Dedicated Region Multitenancy Dedicated Region
Department isolation Use OCI Organizations and child tenancies when departmental isolation can share the same customer subscription and centralized support model. Use multiple independent top-level tenancies when departments require stronger tenancy isolation and separately managed internal subscriptions.
Subscription and chargeback Child tenancies share the same subscription and pricing model. Each internal tenancy can map to an internal subscription by using the same rate card. Consumption is summarized for operator reporting and cross-charging.
Support flow Customer administrators submit SRs through My Oracle Support, and Oracle Global Support services those requests. Internal users submit SRs in the in-realm console. The Dedicated Region operator provides Tier 1 support and escalates to OCI support when needed.
Support isolation Administrator group assignment governs support visibility. Support tickets are isolated between tenancies and stored within the Dedicated Region realm.
Conversion planning Use this model when the customer does not need an operator-led internal cloud provider model. Select this model during contracting and product approval. Single-tenancy and multitenancy models are not designed for direct conversion after deployment.

## Eligibility and Guardrails

Dedicated Region multitenancy requests must be reviewed and approved by Oracle Dedicated Cloud Product Management. Customers must demonstrate the need for multitenancy, require two or more regions, agree to deliver Tier 1 support for internal tenants, and not resell OCI services.

## Operator Console and Internal Tenancy Operations

This section summarizes the operational capabilities that the Dedicated Region operator uses to manage internal tenancies, subscriptions, limits, reporting, and training.

Operator Capability Implementation Use
Internal orders and subscriptions Create and manage internal orders for departments or business units, view subscription status, and activate internal tenancies from the Operator Console.
Internal order workflow Place an internal order, create the subscription, send the department administrator activation email, make the tenancy available, and trigger costing through consumption.
Billing administration Manage internal billing accounts, billing cycles, bill-to details, currency, payment details, and billing schedules for internal chargeback or showback.
Limits management Set limits to control resource usage and spend by tenancy. Internal customers can request limit increases, and operators approve or deny those requests.
Business reporting Track internal consumption, resource trends, order status, and support metrics to manage the region as a shared enterprise cloud platform.
Capacity reporting Monitor compute, block storage, file storage, object storage, and Exadata consumption at the tenancy and region levels. Use current and 30-day historical usage data for expansion planning with Oracle.
Notices and enablement Post notices to internal tenancies and access playbooks, onboarding training, documentation, and role-based training for administrators, business users, and operators.

- [Tenancy Operating Model](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/tenancy-operating-model.htm#tenancy-operating-model)
- [Eligibility and Guardrails](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/tenancy-operating-model.htm#eligibility-and-guardrails)
- [Operator Console and Internal Tenancy Operations](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/tenancy-operating-model.htm#operator-console-and-internal-tenancy-operations)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
