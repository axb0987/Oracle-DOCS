# Customer Support
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/customer-support.htm
- Fetched: 2026-09-05 03:30 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/customer-support.htm#dcoc-content-body)

# Customer Support

Oracle Alloy support is structured in tiers. The Oracle Alloy operator provides Tier 1 support to end customers and owns the customer interaction through resolution. Oracle provides Tier 2 and Tier 3 support to the operator, engages engineering and service teams when required, and works on the escalated issue to mitigation and closure.

End customers can create and manage support requests through the partner-branded Support Center. Operators can manage those requests through the Operator Console or through an external support system of their choice. When the operator escalates an issue to Oracle, Oracle handles a separate support record. Data and metadata from the original end-customer request are not automatically transferred.

Oracle does not provide support SLAs. Service availability commitments follow OCI service-level agreements, and support response objectives follow Oracle cloud hosting and delivery policies. Incident handling uses standard severity levels, from critical outage through general guidance, and includes triage, mitigation, resolution, and root-cause follow-up for high-severity events.

## Support Tooling and Customer-Facing Workflows

When you use the built-in support experience, support tooling spans the Customer Console, Operator Console, and Fusion Console. End customers create technical, billing, and service limit requests from the Help menu in the Customer Console. Operators review those requests through support workflows. Oracle-facing escalations are handled separately in Fusion Console.

This separation keeps customer-facing and Oracle-facing records independent while preserving the operator as the system of engagement.

To enable the customer-facing support workflow, configure customer support users with the required access in the customer identity domain. Configure operator support representatives with the required customer support roles and data access in Fusion Console. Customer-facing support users need permissions to read and manage tickets in the tenancy. The support service must be allowed to inspect domains so that ticket workflows can function correctly.

The built-in support workflow supports the full request lifecycle for technical, billing, and service limit requests. End customers can view active or closed requests, add comments, and track status transitions, such as Pending with Support, Pending with Customer, and Close Requested.

Technical support requests can include attachments such as logs or screenshots. Uploads are limited to one file at a time. Each file must be 10 MB or smaller. Executable formats are not supported. Attachments associated with resolved or closed requests are deleted after 7 days to meet security compliance requirements. Closed requests cannot be reopened.

For direct assistance and self-service, the Customer Console also includes the Alloy Realms Support Chatbot for OCI service questions. When management escalation or service-request status verification is required, operators can use OCI phone support and must be prepared to provide the service request number, business effect, current contact details, and the applicable Customer Support Identifier (CSI).

## Third-Party Tooling and Knowledge Discovery

Partners can continue to use an external support platform for end-customer interactions when that operating model is preferred. In that configuration, the built-in end-customer Support Center can be disabled so that end customers interact only with the partner-selected platform. Escalations to Oracle must still be submitted through the Oracle Alloy support workflow used for partner-to-Oracle requests.

Support operations can also be augmented with knowledge-discovery tooling. Document-retrieval chat is supported today within Alloy realms.

## Service Objectives and Operating Model

Tier 1 service-level agreements and service-level objectives remain the operator's responsibility because the operator owns the end-customer support relationship. Oracle provides response-time targets for Tier 2 support, while OCI service-level agreements govern service performance, availability, and manageability for the underlying cloud services.

Operational readiness planning must account for expected end-customer volume, required support coverage, and staff skill depth before region onboarding. We recommend a 24x7 rotation when the support model includes production workloads that require continuous response.

The operator-facing Customer Support Metrics dashboard provides centralized visibility into open, submitted, and resolved service requests. Dashboard filters by severity, status, and communication channel help identify backlog trends, response bottlenecks, and areas for support-process improvement.

## Escalation and Case Quality

When escalation to Oracle is required, the operator creates a separate Oracle support request from the partner workflow. Some fields can be prepopulated from the original request, but the operator can review and edit the new request before submission so that only the information required for diagnosis and resolution is shared.

Escalated requests should capture the affected service or product area, business effect, relevant OCIDs or service instance identifiers, observed error messages, troubleshooting steps already performed, supporting screenshots or logs, and the requested severity. For 24x7 engagement, the request should identify primary and secondary contacts so that Oracle can maintain continuous communication during mitigation and recovery.

Management escalation is available when an issue is not progressing quickly enough, when project timelines or upgrade schedules are at risk, or when a direct discussion with Oracle support management is required. Operators can use phone support channels for this escalation path and must be prepared to provide the service request identifier, business effect, and current contact details.

## Support Workflow and Separation of Records

The support workflow uses two independent and secure service-request streams. End-customer requests are created, viewed, updated, and closed in the partner-branded End Customer Console. Operator escalations to Oracle are created and managed in a separate partner-to-Oracle support flow.

Oracle does not have access to end-customer service requests, and end customers do not have access to the operator's Oracle-facing requests.

Operators manage end-customer service requests from the Operator Console and can work those requests directly or escalate them to Oracle when Tier 2 assistance is required. If the issue requires deeper service investigation, Oracle can open a further internal request with the appropriate service team or engineer while the operator continues to own communication with the end customer.

- [Customer Support](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/customer-support.htm#customer-support)
- [Support Tooling and Customer-Facing Workflows](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/customer-support.htm#support-tooling-and-customer-facing-workflows)
- [Third-Party Tooling and Knowledge Discovery](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/customer-support.htm#third-party-tooling-and-knowledge-discovery)
- [Service Objectives and Operating Model](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/customer-support.htm#service-objectives-and-operating-model)
- [Escalation and Case Quality](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/customer-support.htm#escalation-and-case-quality)
- [Support Workflow and Separation of Records](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/customer-support.htm#support-workflow-and-separation-of-records)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
