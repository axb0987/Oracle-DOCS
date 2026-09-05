# Dedicated Region Security
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#dcoc-content-body)

# Dedicated Region Security

Dedicated Region inherits the defense-in-depth approach that OCI uses and adds the customer facility boundary as an explicit design responsibility. Security planning must cover the data center, caged Oracle equipment area, management network isolation, tenant isolation, IAM, network edge controls, service endpoints, encryption, monitoring, and incident response integration.

Security Layer Controls to Account for in the Design
Data center physical security Restricted access, visitor controls, cameras, two-factor access controls, intrusion detection, and environmental controls that the customer facility program owns.
Infrastructure security Isolated management network, tenant and compartment isolation, segmented private networks, restricted host access, and hardened service hosts.
Application security IAM policies, federation, multifactor authentication, Web Application Firewall, Vault, Cloud Guard, Security Zones, logging, and security lists or network security groups.
Data security Encryption at rest and in transit, key management controls, database encryption options, and protected access to object, block, file, and database services.
Operational security Time-bound bastion access, hardware multifactor authentication (MFA), Oracle-managed device posture, monitoring, audit logging, security information and event management (SIEM) integration, and defined SR workflows.

## Physical Security

Physical security is shared. The customer is responsible for the data center facility, floor space, power, cooling, physical access program, and environmental controls. Oracle is responsible for Oracle-managed cloud racks, hardware maintenance, firmware and software updates, and operational work inside the Oracle Secure Area or approved cage.

Customers must implement and attest to facility controls, such as controlled entry, visitor logging, camera coverage, two-factor access control, intrusion detection, and personnel access reviews.

Oracle provides whitespace, power, cooling, and space specifications for the deployment and works with the customer to restrict access to cages and equipment.

Noncontiguous rack placement can be supported when the data center design meets Oracle requirements. Validate power, cooling, cable diversity, and physical access procedures during design.

## Network Perimeter Security

The network edge security controls that protect tenant traffic, OCI service endpoints, and Oracle operational access paths.

The Dedicated Region network edge bridges public IP addresses, OCI service endpoints, regional bastions, and tenant VCN overlay networks. Most regional services and hardware operate in private networks behind the edge. Service hosts and load balancers are hardened, protected by intrusion prevention system (IPS) and intrusion detection system (IDS) controls, and continuously monitored.

Use OCI-native controls for tenant VCN security, such as route tables, security lists, network security groups, load balancers, Web Application Firewall, NAT gateways, service gateways,[DRGs](https://docs.oracle.com/iaas/Content/Network/Tasks/managingDRGs.htm), and logging.

OCI IAM protects all OCI APIs. Architects can use federation, MFA, least-privilege policies,[compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/Working_with_Compartments.htm), and network sources to restrict who can call APIs and where those calls can originate.

The Oracle Services Network edge provides access to service endpoints while keeping core service infrastructure in private network segments. Document public and private access patterns for each workload.

Use the customer Internet transit model when the enterprise requires a segregated network control layer in addition to OCI tenancy controls. IAM,[compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/Working_with_Compartments.htm), network sources, and workload-level controls remain required.

For circuit speeds,[FastConnect](https://docs.oracle.com/iaas/Content/Network/Concepts/fastconnectoverview.htm)connectivity models, and detailed firewall routing requirements, use the Dedicated Cloud Architecture section. This section focuses on the Dedicated Region security posture that consumes those connectivity patterns.

## Customer Firewall

This section captures Dedicated Region design decisions for a customer-provided Internet transit and firewall model without repeating the core routing and redundancy requirements in the Dedicated Cloud Architecture section.

Use this section to record ownership, validation steps, maintenance procedures, and routing variants for the customer-controlled Internet perimeter. The architecture section remains the source of truth for required Oracle management access, full routing table behavior, redundancy, no-NAT requirements, and the 72-hour allowlist update window.

Design Area Add to the Dedicated Region Design Record
Internet availability ownership If the customer provides Internet transit for the region, the customer assumes responsibility for regional Internet availability and must define operational coverage, escalation paths, and maintenance blackout handling.
Vendor and topology selection Oracle does not mandate a specific firewall vendor, router vendor, or topology. The design must still be reviewed and validated against Oracle connectivity, routing, resiliency, and management-access requirements.
BGP model Document whether the Dedicated Region gateways peer with the customer ASN and the customer advertises Oracle-assigned prefixes to transit providers, or whether an approved multihop BGP model peers the region directly with transit providers.
External point-to-point addressing Document public IPv4 and IPv6 addressing outside the region for router interconnects. Oracle guidance typically uses a public IPv4 /29 and IPv6 /126 per Oracle router from customer address space.
Transit capabilities Confirm that the design provides dual-transit-provider-equivalent capabilities, appropriate physical media, such as 10G, 40G, or 100G Base-LR where applicable, BGP community support, and no single point of failure between region gateways and Internet providers.
Customer policy discretion Customer-defined permit or deny rules for Dedicated Region addresses, ports, or protocols are allowed outside the required Oracle management allowlist, as long as Oracle management and operational traffic is not altered or blocked.
Maintenance coordination If customer network maintenance could interrupt Dedicated Region Internet connectivity, open an SR with Oracle Support before the work. Oracle communicates reciprocal change and allowlist notifications through OCI Announcements.
Allowlist implementation Translate Oracle allowlist policy intent into the native firewall, router, or ACL syntax for the customer platform. Treat sample configurations as illustrative. The Oracle-provided allowlist for the deployment is authoritative.

For eBGP, full Internet routing table, Oracle public prefix routing, no-NAT, redundancy, and allowlist timing requirements, use the Firewall and Sample Firewall Topology Requirements sections.

## Infrastructure Security

The controls that protect Dedicated Region infrastructure services, tenant isolation boundaries, and management planes.

Infrastructure security relies on segmentation, hardened components, controlled management access, and tenant isolation. The management network is isolated from customer workload networks. OCI tenancy, compartment, policy, and VCN controls maintain separation between administrative and workload boundaries.

Private network segments separate core services, overlay networks, and hardware management interfaces. Hardware management paths are restricted and cannot be used as general-purpose workload paths.

Overlay VCN networking is implemented outside the customer guest OS and provides another containment layer between host, hypervisor, and tenant networking functions.

Top-of-rack ACLs, narrow overlay-to-core access controls, hardened service hosts, hardware root-of-trust controls, and code supply chain practices contribute to defense in depth.

Data protection controls must include encryption at rest and in transit, key storage controls, Vault usage, database encryption, logging, and policy-based access to storage and database resources.

## Operations Security

Use this section to learn how Oracle operational access is controlled, monitored, and limited when Oracle personnel operate the Dedicated Region.

Oracle operates and monitors Dedicated Region infrastructure 24x7x365. Operational access is restricted to authorized Oracle personnel, approved devices, and time-bound workflows. Customers must integrate Oracle operational processes with their own incident, access, and change review programs.

Oracle personnel access is integrated with Oracle corporate identity controls and limited to authorized roles.

Access from Oracle-managed devices uses controlled network access paths with hardware MFA and device security posture requirements.

Bastion access is restricted by origin, requires hardware MFA, is time-bound, and limits personnel to the service hosts required for the operational task.

Audit logs, monitoring, reporting, SIEM monitoring, and SR records support operational assurance and investigation workflows.

In a multitenancy deployment, use the operator security dashboard to submit and track security-related tickets, view OCI Security Operations tickets for the operator, and confirm whether high-severity issues are present.

## Security Operations

Use this section to learn how operators use the Security Dashboard to submit, review, update, and track security-related support tickets for a Dedicated Region environment.

Use the Security Dashboard when a security issue requires Oracle Security Support review, when suspicious user activity must be escalated, or when an operator needs to review security ticket status, messages, and supporting attachments.

Security Operations Area Use Primary Operator Actions
Security Dashboard access Open the security operations workspace from the Operator Console. Open Security dashboard from My tools or from the navigation menu under Security. Bookmark the validated Security Dashboard URL only when direct future access is required.
Security ticket monitoring Review the most recent or full list of security support tickets. Use Overview for the most recent tickets, or open Security support tickets to review all tickets. Search by issue summary or SR number when the ticket is not visible in the recent list.
Security ticket creation Submit security service requests to Oracle Security Support. Create a ticket, select the affected service, issue type, and severity, then provide a clear summary and description before submitting.
Suspicious user or activity response Escalate a suspected suspicious user or security activity. Use Default Security Ticket unless another issue type is more appropriate, set the severity to Highest, and include useful identifiers such as user OCID, resource OCID, session ID, or related SR number.
Messages with Oracle Security Support Respond when Oracle Security Support requests information or sends an update. Open the ticket, review the message history, search comments by keyword when needed, and use Add comment to send the response.
Attachments and evidence handling Attach diagnostic files, screenshots, or supporting evidence to a security ticket. Upload one file at a time, keep each file at or below 10 MB, avoid unsupported file types, acknowledge the personal and protected information statement, and account for post-closure attachment deletion.

### Access the Security Dashboard

Access the Security Dashboard when security ticket review or escalation work is required.
- 

Open the Operator Console.
- 

On the Operator Console home page, under My tools, select Security dashboard. Alternatively, open the navigation menu, select Security, and then select Security dashboard.
- 

Verify that the Security Dashboard appears.
- 

Bookmark the Security Dashboard URL only after the initial access path is validated and direct future access is required.

### View Security Support Tickets

Use the Security Dashboard to review recent tickets, inspect all security-related tickets, and confirm the current ticket status.
- 

Open the Security Dashboard from My tools or from the navigation menu under Security.
- 

To view the most recent security-related tickets, select Overview and review the Most recent tickets list.
- 

To view all security-related tickets, select Security support tickets and review the full ticket list.
- 

Use Search to locate a ticket by issue summary name or SR number when the ticket is not visible in the current view.
- 

Treat the ticket status as Oracle-managed and verify status changes in the Security Dashboard before updating internal incident records.

### Create a Security Support Ticket

Create a security support ticket when a security issue requires Oracle Security Support review or action.
- 

Open the Security Dashboard from My tools or from the navigation menu under Security.
- 

Under Security Dashboard, select Security support tickets.
- 

Select Create ticket.
- 

Select the affected service and the issue type.
- 

Select the appropriate severity: Highest, High, Medium, or Low.
- 

Enter a concise Summary and a complete Description with the details required for security triage.
- 

If the ticket escalates a customer service request, enter the SR number in the security service request notes field.
- 

Add an attachment when supporting evidence is required. Upload one file at a time, keep each file at or below 10 MB, and do not upload unsupported file types such as.exe,.bat,.aspx, or.com.
- 

Select Create.

### Create a Ticket to Remove a Suspicious User or Activity

Create a highest-severity security ticket when a suspicious user or suspicious activity requires urgent review and removal action.
- 

Open the Security Dashboard from My tools or from the navigation menu under Security.
- 

Under Security Dashboard, select Security support tickets, then select Create ticket.
- 

Select the affected service.
- 

Select Default Security Ticket unless another issue type more accurately describes the issue.
- 

Set the severity level to Highest.
- 

Use the Summary field to identify the urgent issue or suspicious user activity.
- 

Use the Description field to include helpful triage details, such as a user OCID, resource OCID, session ID, timeline, observed behavior, and related SR number when the ticket escalates a customer service request.
- 

Attach supporting evidence when available, following the file size, file type, and one-file-at-a-time upload requirements.
- 

Select Create.

### Send a Message to Oracle Security Support

Send a message from the Security Dashboard when Oracle Security Support requests more information or when the operator needs to add an update to a security ticket.
- 

Open the Security Dashboard from My tools or from the navigation menu under Security.
- 

Under Security Dashboard, select Security support tickets.
- 

Open the ticket from Most recent tickets or from the full Security support tickets list.
- 

Use Search to locate an SR by issue summary name or SR number when needed.
- 

Review messages to and from Oracle Security Support. Use keyword search when the message history is long.
- 

Select Add comment, enter the response in the Comment field, and select Add comment to send the message.

### Add Attachments to an Existing Security Support Ticket

Add attachments only when diagnostic files, screenshots, logs, or other evidence are required for security triage.
- 

Open the Security Dashboard from My tools or from the navigation menu under Security.
- 

Under Security Dashboard, select Security support tickets.
- 

Use Search to locate the ticket by issue summary name or SR number when needed.
- 

Open the ticket and, in the Resources menu, select Attachments.
- 

Select Add attachment.
- 

Drop the file onto the dialog box or select select it here, select the file, and select Open.
- 

After reading the statement about personal and protected information, select the acknowledgement checkbox.
- 

Select Add attachment.

### Security Operations Guardrails

Keep security ticket handling aligned with incident response, data minimization, and evidence retention requirements.

Guardrail Implementation Guidance
Severity selection Use Highest severity for suspected suspicious user activity or urgent security issues. Use High, Medium, or Low only when the operational impact supports a lower severity.
Triage details Include the affected service, issue type, clear summary, complete description, relevant OCIDs, session ID, observed behavior, timeline, and related SR number when available.
Customer SR linkage When escalating from a customer service request, record the customer SR number in the security service request notes field so the security ticket can be traced back to the originating request.
Attachment controls Upload one file at a time, keep files at or below 10 MB, and do not upload unsupported executable or web application file types such as.exe,.bat,.aspx, or.com.
Sensitive information handling Review all descriptions, comments, and attachments before submission. Include only the information required for security triage and acknowledge the personal and protected information statement when adding attachments.
Retention awareness SR-specific attachments are deleted 7 days after the SR is closed or resolved, even if the attachment reference still appears in the Operator Console or Fusion Console.
Status ownership Oracle Security Support manages security SR status. Verify status in the Security Dashboard before updating incident records or communicating status externally.

- [Dedicated Region Security](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#dedicated-region-security)
- [Physical Security](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#physical-security)
- [Network Perimeter Security](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#network-perimeter-security)
- [Customer Firewall](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#customer-firewall)
- [Infrastructure Security](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#infrastructure-security)
- [Operations Security](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#operations-security)
- [Security Operations](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#security-operations)
- [Access the Security Dashboard](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#access-the-security-dashboard)
- [View Security Support Tickets](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#view-security-support-tickets)
- [Create a Security Support Ticket](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#create-a-security-support-ticket)
- [Create a Ticket to Remove a Suspicious User or Activity](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#create-a-ticket-to-remove-a-suspicious-user-or-activity)
- [Send a Message to Oracle Security Support](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#send-a-message-to-oracle-security-support)
- [Add Attachments to an Existing Security Support Ticket](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#add-attachments-to-an-existing-security-support-ticket)
- [Security Operations Guardrails](https://docs.oracle.com/en-us/iaas/Content/dedicated/dedicated-region/dedicated-region-security.htm#security-operations-guardrails)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
