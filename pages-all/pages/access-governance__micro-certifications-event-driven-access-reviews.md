# Micro-Certifications in Oracle Access Governance: Event Driven Access Reviews
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/micro-certifications-event-driven-access-reviews.htm
- Fetched: 2026-09-05 03:15 CDT

# Micro-Certifications in Oracle Access Governance: Event Driven Access Reviews

Micro-certifications are automatically launched by Oracle Access Governance whenever an event, such as change event, timeline event, or unmatched account event, is detected. Oracle Access Governance continuously monitors identity profile and whenever a pre-defined event is detected, it launches access reviews related to that event. These generate near real-time access reviews so that prompt actions can be taken whenever these pre-defined events are detected. It also helps to reduce the certification fatigue as reviewers have to make a decision only for the affected identities.

As an Administrator , you can set up these micro-certifications from the Access Reviews → Event-Based Setup page. Enable or disable an event, auto approve low-risk items, auto-remove unmatched accounts from the system, or add an approval workflow. Reviewers can review or reassign the review tasks from the My Access Review page. Event-based access reviews have the Event - &lt;Identity Attribute Change&gt; identifier.

Note  
  
The Event-Based Setup menu option is not available when you have not activated any identities containing data for identity attributes. To view this option, you must activate at least one identity from the Manage Identities page. See[Select Included Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm#select-identities-for-activation)for details on how to enable identities in Oracle Access Governance.

## Change Event

Change Events are triggered whenever changes are detected in an identity profile. Oracle Access Governance begins real-time, focused access reviews based on occurrence of the events, such as job-code change, location change, manager change.

Change Events support value-based filtering (for Non-Boolean and non-date-time based identity attributes) where you can configure specific values to trigger event-based reviews. You can also set scope of access reviews for particular applications or permissions.
You can enable event-based access reviews for core attributes (for example, Job Code, Organization, Location, and so on) and custom attributes (for example, Cost Center, Project Code, and so on).
Note  
  
If you don't see the option for selecting custom attributes, contact the Oracle Access Governance Administrator. You first need to enable it from the System Administration settings within Oracle Access Governance Console. See[View and Configure Identity Attributes](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identity-attributes.htm#manageattributes-settings).
Change Event is associated with joiner-mover-leaver (JML) actions.
- Joiner refers to action taken by the system when an identity joins the company, such as assigning some birth-right access privileges.
- Mover refers to action taken by the system when an identity moves within the same organization. For example, changes in access privileges due to internal job transfers or location change.
- Leaver refers to action taken by the system when an identity leaves the company, such as revoking access over all corporate applications and systems.

Scenario : Ema , an employee at Acme corporation, has moved to a different project, reporting to a different manager within the same department. From an identity viewpoint, Ema no longer requires access privileges required by direct reports of her previous manager and project but now requires new access privileges.
Note  
  
In this scenario, we are assuming Manager is the core attribute in your data schema and Project Code is one of the custom attributes in your data schema.

For this, you need to enable event-based access reviews for the core attribute Manager Change and a custom attribute Project Code . Whenever the latest data synchronization happens from the orchestrated system with these updates, Oracle Access Governance automatically raise multiple event-based access reviews associated with this single identity.

## Timeline Event

Timeline event access reviews are triggered annually on a given date. Oracle Access Governance automatically launches access reviews on the same day each year for that identity. This may refer to a specific event, for example an anniversary event such as an employee's organization joining date, or a software application license renewal date.

If configured, Access Reviews are generated on the specific date, to determine if permission associated with the event are still appropriate. Alternatively, you can configure a number of days prior to the event date on which to generate the review task.

Scenario : Bill , an employee at Acme corporation, uses the CorporateLDAPdirectory application. Bill's access to this application needs to be reviewed on an annual basis, based on the ActiveStartDate attribute. When Bill is first granted access to CorporateLDAPdirectory the ActiveStartDate is recorded. If you enable a timeline event on this application/attribute combination, then on the anniversary of Bill's first grant of the application, an access review will be generated, which allows a reviewer to revoke Bill's access to the application, or accept and allow Bill access to the application for another 12 months.

## Unmatched Accounts Event

Unmatched Accounts events are triggered whenever Oracle Access Governance detects an orphan account, which cannot be associated with any identity.

You can select the orchestrated system for which you want to configure this event type. You can configure to auto-remove unmatched accounts.
