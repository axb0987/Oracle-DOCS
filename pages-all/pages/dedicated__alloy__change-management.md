# Change Management
- Source: https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/change-management.htm
- Fetched: 2026-09-05 03:29 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/change-management.htm#dcoc-content-body)

# Change Management

Oracle Alloy follows the same established OCI change-management model used across Oracle cloud regions. Most changes are designed to roll out without customer-visible disruption. For known disruptive changes, the operator designates at least one 12-hour maintenance window each month in coordination with Oracle so that validation, implementation, and post-change checks can be completed in a controlled way.

Operators can review change status through the Update Activity dashboard. Operators can request a temporary change freeze by submitting a technical service request with start and end times in UTC and a business justification. We recommend 6 weeks of notice. Keep freeze periods short because they delay security fixes, software enhancements, and backlog clearance.

When the operator provides the internet transit layer, Oracle uses OCI Announcements to communicate management allowlist policy changes. Apply the updated allowlist rules within 72 hours.

Known disruptive changes have historically remained infrequent. Manual announcements from Oracle can be reviewed, edited, approved, blocked, and targeted by authorized operator roles before release to end customers. Automated service notifications are not customizable and are delivered directly as service-generated events.

If the operator plans maintenance that could interrupt Oracle Alloy or OCI Dedicated Region connectivity, the operator must notify Oracle by opening a service request before the work is performed.

Oracle provides 15-day notice for known disruptive changes. Non-disruptive changes are communicated through OCI Announcements. Customers can subscribe to announcements through email, SMS, and other supported delivery protocols.

## Change Categories

OCI change management classifies changes as normal, routine, emergency, or mitigating changes based on urgency, repeatability, and risk.
- 

Normal changes: New or spontaneous implementations that require the full review and approval path and at least 24 hours between approval and deployment.
- 

Routine changes: Prevalidated implementations that have been run at least four times with the same implementation steps, such as credential rotation or capacity allocation.
- 

Emergency changes: Changes that must be run within the next 24 hours or during an approved freeze period, such as urgent security patching or software upgrade or downgrade.
- 

Mitigating changes: Changes that reduce risk during an active incident or a potential customer-impacting event, such as changes triggered by Network Operations Center (NOC) or alarm conditions.

## Rollout Progression

Changes progress through OCI development and validation before they are introduced into production Oracle Alloy regions. After deployment to the first Oracle Alloy region, Oracle can delay rollout to the second region for up to 15 days. A similar interval can be applied before rollout to more regions so that validation can complete before the next deployment wave. The operator can select the deployment sequence across its regions.

## Update Activity Dashboard

The Update Activity dashboard provides a detailed operational view of change status. The dashboard includes updates completed in the last 24 hours, updates scheduled for the next 24 hours, updates completed in the past week, and updates scheduled for the next 7 days.

The dashboard also surfaces completed update details and scheduled update details so that recent activity and near-term deployments can be reviewed from one operator view.

## Rollback and Corrective Action

If an approved deployment does not validate successfully, the change is rolled back immediately. Unsuccessful changes then enter an internal corrective action and preventive action process to capture root cause, define the remediation required, and reduce the likelihood of recurrence in future deployments.

## Oracle Software Security Assurance

Oracle Software Security Assurance provides the secure development methodology that supports change introduction across the service lifecycle. It embeds security into design, build, testing, and maintenance activities and is intended to reduce the incidence and effect of security weaknesses.

- [Change Management](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/change-management.htm#change-management)
- [Change Categories](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/change-management.htm#change-categories)
- [Rollout Progression](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/change-management.htm#rollout-progression)
- [Update Activity Dashboard](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/change-management.htm#update-activity-dashboard)
- [Rollback and Corrective Action](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/change-management.htm#rollback-and-corrective-action)
- [Oracle Software Security Assurance](https://docs.oracle.com/en-us/iaas/Content/dedicated/alloy/change-management.htm#oracle-software-security-assurance)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
