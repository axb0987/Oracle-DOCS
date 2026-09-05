# Oracle Alloy Security
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm#dcoc-content-body)

# Oracle Alloy Security

Oracle Alloy uses a shared responsibility model. The operator is responsible for the physical security and environmental controls of the hosting data center. Oracle manages security operations for the Oracle Alloy cloud platform and applies the same tested OCI security practices used for cloud-region operations.

Baseline compliance coverage includes SOC 1, SOC 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, and CSA STAR at no additional cost. Baseline compliance reports and certificates are issued every 6 months. Additional compliance requirements must be agreed in advance and reflected in the operating model, responsibilities, and contract structure.

## Physical Security

Physical security is shared between the operator and Oracle. The operator secures the data center facility and provides cameras, two-factor access control, intrusion-detection controls, and environmental protections for power, cooling, and space.

Oracle secures, monitors, and maintains Oracle-owned racks and infrastructure within the Oracle-managed secure area.

Oracle does not have access to tenant user data. Data-processing obligations are defined in the Oracle Alloy order and associated data-processing terms.

Oracle environments in Oracle Alloy regions are physically separated within the hosting facility. Regular third-party assessments validate physical security standards for the Oracle-managed environment.

## Data Security

Data at rest is encrypted by default by using a two-level AES-256 key hierarchy. Encryption cannot be disabled. Workloads can use Oracle-managed keys or customer-managed keys through OCI Key Management, depending on control and compliance requirements.

Customer-managed key models include Virtual Vault for multitenant hardware security module (HSM)-backed keys, Dedicated Key Management Service (KMS) and Private Vault for single-tenant HSM-backed keys, and External KMS for integrations with customer-controlled on-premises HSMs.

Important: When using customer-controlled key management, the customer is solely responsible for operating, securing, backing up, recovering, rotating, and managing the lifecycle of the key-management infrastructure. This model introduces higher customer-managed risk because loss of key availability, misconfiguration, or inadequate operational controls can affect workload access, data availability, and regulatory compliance.

Select a key-management model that aligns with workload sensitivity, the operating model, and regulatory requirements.

## Identity and Access Management

Security boundaries are enforced at the realm, region, and tenancy levels. Each end-customer tenancy remains a separate partition for resource administration unless delegated access is explicitly granted.

Oracle Alloy operator access uses OCI IAM with built-in role-based administrative groups so that job duties can be separated across administration, pricing, billing, branding, orders, subscriptions, customer limits, and security. Supported authentication and federation options include bring-your-own identity provider, OCI passkeys, FIDO2 authenticators, and X.509 certificates.

## Operator Security Access

Operator access is governed through OCI IAM by using least-privilege policies, separated administrative roles, and explicit approval boundaries for platform operations, billing, support, networking, and announcements. End-customer tenancy administration remains separate from the operator's platform-administration model unless delegated access is intentionally granted.

Operators do not have standard access to Oracle-managed primary encryption keys. Workloads that require tenant-controlled key management must use customer-managed keys and customer-defined rotation policies.

OCI provides granular permission controls, just-in-time access mechanisms for Oracle operations, and audit monitoring of operator activities. Operators are responsible for managing realm access, defining[IAM policies](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm)for administrative groups, providing first-line support for security issues, and escalating platform security issues to OCI as needed.

Grant access to security workflows through explicit group and role assignment. Security Dashboard access is intended for operators who are placed in a Security Operations Manager group in the identity domain. Fusion support functions require the applicable support role assignments and data-access configuration before the user can work with support records.

Operator access can be revoked by opening a severity 1 service request.

Operator administrative access is provisioned through the Operator Access tenancy and the built-in Oracle Alloy identity domain. The identity domain can federate with the operator's identity provider and acts as the service-provider boundary for operator sign-in. Enforce multifactor authentication for operator access to strengthen administrative control of the environment.

## Cloud Operations Transparency

Security issue handling uses a dedicated, role-controlled messaging path between the Oracle Alloy operator and OCI security operations. The path is backed by a 24x7 OCI Security Operations response queue.

Operators with the required access can open security tickets, review existing tickets, and provide observations needed for investigation and response.

## Security Incident Collaboration

The Security Dashboard in the Operator Console provides the operator-facing channel for submitting, reviewing, and tracking security issues with OCI Security Operations. The dashboard supports bidirectional communication. Operators can open security issues when abnormal conditions or security events are observed, even when the issue is not fully characterized.

## Oracle Alloy Security Dashboard

The Security Dashboard is the working area for operator-to-Oracle security collaboration. Open the dashboard from My Tools on the Operator Console home page or from Security in the navigation menu. The Overview page surfaces the most recent tickets. Security Support Tickets opens the full ticket list for broader review.

Ticket search supports lookup by issue summary or service request number. Message search helps locate comments by keyword inside an open ticket. These search capabilities help you move between recent activity, full-history review, and active investigations without leaving the dashboard.

When you create a security ticket, specify the affected service, issue type, severity, summary, and description. Include relevant identifiers, such as OCIDs or session IDs, when available. If you are escalating an end-customer service request, include the originating service request number in the security request notes so that the investigation path remains traceable.

For suspicious users or suspicious activity, open a security ticket immediately and use the highest severity unless a more appropriate issue type is already defined for the event.

Attachments can be added during ticket creation or later from the Attachments resource. Uploads are limited to one file at a time. Files must be 10 MB or smaller, and executable file types are not supported.

Operators can reply to Oracle Security Support directly from the ticket by adding comments. Ticket status remains managed by Oracle Security Support. Attachments associated with a resolved or closed security request are deleted after 7 days to meet security compliance requirements, even if the attachment entry remains visible in the console history.

The operator should triage straightforward issues that are limited to one tenancy and can be resolved through tenant remediation or standard support workflows. Escalate issues that affect multiple tenancies, require OCI investigation, or involve higher operational complexity through the Security Dashboard for OCI Security Operations review and response.

Ticket handling is role controlled. Operators with the required access can create tickets, view existing tickets, add comments, and provide supporting observations or attachments. OCI Security Operations curates the queue, can adjust severity based on investigation findings, and remains responsible for ticket disposition and closure.

## Network Perimeter Security

Oracle Alloy requires redundant backbone and internet transit connectivity, with all required circuits active for bandwidth and redundancy. An out-of-band connection is mandatory as a last-resort recovery path.

Operators that provide their own transit circuits can eliminate Oracle egress charges for those circuits, but they must meet Oracle requirements for diversity, resilience, routing, and 24x7 operational support. In this customer-provided transit model, customer firewalls and network access control lists (ACLs) can enforce region-wide traffic restrictions. Oracle management traffic must remain allowlisted and must pass without network address translation (NAT) or other address translation.

Oracle notifies customers of management allowlist changes through OCI Announcements. Apply the updated rules within 72 hours.

Network protection follows a secure-by-design model that combines segmentation, zero-trust principles, granular workload separation, stateful firewalls, security groups, and OCI-managed gateways for internet, service, and NAT access.[IAM policies](https://docs.oracle.com/iaas/Content/Identity/policieshow/Policy_Basics.htm)govern administrative control of networking resources.

## Infrastructure Security

Data is encrypted in Oracle Alloy regions. Interregion communication uses MACsec. VCN traffic inside a region is not automatically encrypted and must be protected at the workload or application layer when encryption is required. API access can be encrypted by using standard OCI service interfaces.

Oracle continuously patches and updates the platform as part of cloud operations. Infrastructure protection also includes TLS 1.3 with forward secrecy on service endpoints and support for confidential computing capabilities, such as AMD Secure Encrypted Virtualization (SEV) and Intel Software Guard Extensions (SGX), for workloads that require stronger protection for data in use.

Oracle operates continuous monitoring and alerting across the cloud foundation.

## Security Operations

OCI security operations use continuous monitoring and alerting, globally distributed analysts, multiple threat-intelligence sources, resilient audit-health monitoring, and retained log data to support long-term investigations.

Vulnerability management aggregates findings from integrated sources and coordinates response actions, automated ticketing, patching, service-level agreement (SLA) monitoring, and approved exception handling through services such as Security Central, Cloud Guard, scan platforms, and configuration security services.

Incident response follows a structured lifecycle that covers planning and preparation, detection and intake, assessment and triage, response, and resolution and closure. The lifecycle includes incident review, root-cause analysis, and implementation planning.

- [Oracle Alloy Security](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm#oracle-alloy-security)
- [Physical Security](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm#physical-security)
- [Data Security](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm#data-security)
- [Identity and Access Management](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm#identity-and-access-management)
- [Operator Security Access](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm#operator-security-access)
- [Cloud Operations Transparency](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm#cloud-operations-transparency)
- [Security Incident Collaboration](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm#security-incident-collaboration)
- [Oracle Alloy Security Dashboard](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm#oracle-alloy-security-dashboard)
- [Network Perimeter Security](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm#network-perimeter-security)
- [Infrastructure Security](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm#infrastructure-security)
- [Security Operations](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/security.htm#security-operations)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
