# Manage Access Guardrails in Oracle Access Governance
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-access-guardrails.htm
- Fetched: 2026-09-05 03:15 CDT

# Manage Access Guardrails in Oracle Access Governance

Manage and enforce security constraints or conditions in Oracle Access Governance using the Access Guardrails feature to ensure only authorized and compliant identities can gain access to specific permissions.

## Navigate to Access Guardrails

Access Guardrails are defined from the Access Controls section of the Oracle Access Governance Console. Follow the steps to go to the Access Guardrails page.

- Sign in to the Oracle Access Governance Console.
- You can select one of the following options to navigate to the Access Guardrails page:
- Select the navigation menu icon, and select Access Controls &gt; Access Guardrails .
- On the Console home page, select the Access Controls tab and then select the Select button on the Manage Access Guardrails tile.
Whichever option you choose, you will be navigated to the Access Guardrails page, where you can create, view and manage access guardrails.

## Create an Access Guardrail

To create a new access guardrail, select the Create an access guardrail button. The Create a new access guardrail page is displayed.

### Add Details

In the Add Details task, you can enter general settings about the access guardrail. You're also able to add user friendly tags that can be used in a search for this access guardrail.

- Name : Enter a name for your access guardrail.
- Description : Enter description for access guardrail.
- Tags : Enter one or more tags for this access guardrail.
- Select one to select the event when you want to enforce this guardrail
- New access requests only : This enforces guardrails only if an identity requests a new access using the self-service module.
- New access requests and existing access : This enforces guardrails for existing accesses and for new accesses also.
Depending on the configuration settings, existing accesses would be blocked or a grace period would be allowed if a violation is triggered for this rule.
- After you're happy with the settings, select Next to go to the Define Rules task or select Cancel to cancel the current process.

### Define Rules for Access Guardrails

In the Define rule task, define one or more conditions that an identity must pass in order to gain access.

- Select the + Add condition button.
The Add condition panel is displayed.
- In the What type of condition? drop-down list, select the type of condition you want to define and enforce:

Option Description
Identity has a permission Select this if an identity must have this permission. In this instance, access guardrail will be violated if an identity doesn't have access to the defined permission.

For example, use this before assigning elevated privileges, you can check if an identity has default permissions for performing general functions.
Identity must not have a permission Select this if an identity must not have this permission. In this instance, access guardrail are violated if an identity has access to the defined permission.

For example, for Entra ID orchestrated system,use this to prevent users to request Privileged Access Group , if they are part of External Collaborators group.
Identity matches an attribute Select this if an identity must match the defined attribute.

For example, use this to restrict identities only in the IT Security Corp department to request IAM Administrator role.
Identity has an account for a system

Select this if an identity must have an account in a specific system before an access is granted.
- For Identity has a permission or Identity must not have a permission , select the permission conditions, as follows:
- Which system? : Select the orchestrated system managed by Oracle Access Governance.
- For Oracle Identity Governance systems, available permissions are those provided by an application or resource:

- Which application? : Select the application or resource for the orchestrated system selected.
- Which permission? : Select the permission provided by the application that you want to enforce.
- For other types of systems, available permissions are based on permission type:

- Which granted permission type? : Select the permission type, such as role, groups, privilege, schema, or so on for the orchestrated system selected.
- Which permission? : Select the permission that you want to define or enforce.
- (Optional) Depending on the orchestrated system and permission selected, you can set additional attributes, such as security context values, to achieve detailed control over the defined condition.
- Select Add .
- For Identity has an account for a system , select the conditions, as follows:
- Which system? : Select the orchestrated system for which an identity account must exist. If no violation is found, the approver might decide accept or reject an access request.
- (Optional) Which domain : For OCI orchestrated systems, select the domain to ensure an identity has an account in the selected system domain.
- Select Add .
- For Identity matches an attribute , select the attribute conditions, as follows:
- Which attribute? : Select the identity attribute that must match before an access is granted.
- Select Add .
- Continue adding more conditions, if required.
- Select Any if any one of the set conditions must be satisfied, or select All if all the set conditions must be satisfied.
Test for an Identity
- Select the Test for an identity link to verify the defined conditions against an identity.
- Select identity of your choice to run the test in the Which identity do you want to test? field.
- Select Test .
If the condition fails, the test would display Failed with appropriate details on failure.
- Select Next .

### Action on Failure of Access Guardrail Conditions

In this Action on Failure task, you need to define the action or operation that Oracle Access Governance must perform when an Access Guardrail violation is triggered. You can select to block the access immediately or allow a grace period for a few days to meets the mandatory requirements mentioned in the conditions.

- In the What should happen when the access guardrail fails? field, select one of the following depending on the access-risk level.

Option Description
High risk - Block the access immediately For new access requests, the request would not be raised and the violation is triggered with status - Blocked. For existing accesses (if chosen in the previous task), the access would be removed along with the Blocked status violation.
Low Risk - Accept the risk for a number of days For new or existing accesses, if approved, the access would be granted or retained conditionally for a defined of number of days to complete the mandatory requirements. The violation is raised with the status - Snoozed.
- For Low Risk - Accept the risk for a number of days option, enter the number of days (less than or equal to 90) for which you want to retain access.
- Select the Include the identity’s manager in notifications checkbox to include identity's manager in the notification on access guardrail violation.
- Select Next .
- (Optional) You may select one of the additional actions:
- Cancel : To cancel the current process
- Back : To go back to the previous step.

### Add Primary and Additional Owners

You can associate resource ownership by adding primary and additional owners. This drives self-service as these owners can then manage (read, update or delete) the resources that they own. By default, the resource creator is designated as the resource owner. You can assign one primary owner and up to 20 additional owners for the resources.
Note  
  
When setting up the first Orchestrated System for your service instance, you can assign owners only after you enable the identities from the[Manage Identities](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-identities.htm)section. To add owners:
- Select an Oracle Access Governance active user as the primary owner in the Who is the primary owner? field.
- Select one or more additional owners in the Who else owns it? list. You can add up to 20 additional owners for the resource. You can view the Primary Owner in the list. All the owners can view and manage the resources that they own.

### Review and Submit

In the Review and submit task, review the access guardrail details and create the access guardrail.

Review the access guardrail details and select Create . The access guardrail is successfully created.

## Test for Identity

You can verify the defined conditions against an identity while creating an access guardrail or post its creation through Actions menu (three dots).

- On the Access Guardrails page, select Actions icon, and then select Test for an identity .
- Select identity to run the test in the Which identity do you want to test? field.
- Select Test .
If the condition fails, then Failed status is displayed with appropriate failure details.

## Enforce Access Guardrails in Oracle Access Governance

After creating an access guardrail, you'll need to associate it with one or more access bundle for a system. Alternatively, you can associate an access guardrail with an identity collection, ensuring that only authorized and compliant identities, meeting predefined criteria, are members of an Identity Collection.
You can associate access guardrails cross systems to enforce constraints. For example, grant OCI Security Group only if the identity department matches Corporate Security in Active Directory. Implement Access Guardrails, as explained:

- Create Access Guardrail.
- Associate an access guardrail while change or creating an access bundle.
- Identity raises a self-service access request for an access bundle.
- Guardrail checks are triggered.
If no violation is found, the approver might decide to accept or reject an access request.
If a high-risk violation is identified, the access request fails and resolution status is set as Blocked.
In cases of low-risk violations, the approver can see the violation details and might decide whether to approve or reject the access request. In this case, the violation is set to Snoozed status. If approved, access is granted for a defined, limited number of days. If the violation hasn't been resolved during that time, the permission is revoked.

## Search Access Guardrails and View Details

Search to get specific and relevant results. You can use a basic keyword search for anything that you want to find, scope the search using the suggested filters.
After you have narrowed-down the search, select the access guardrail link under the Name column to view the details. You can also select the Actions menu (three dots) and select View details .

## Edit an Access Guardrail

You can edit an access guardrail to include additional conditions, change enforcement criteria, change failure actions, or update general details. If you have selected enforcement criteria as New access requests and existing access , then the existing accesses would be reassessed based on the change details.

- Go to the Access Guardrails page.
- For a guardrail that you wish to edit, select the Actions menu (three dots), and then select Edit .
- Modify according to the requirement.
The Edit access guardrail page provides the same guided workflow as creating a guardrail.
- On the Review and submit step, select Update .

## View Access Guardrail Violations Report

Generate a report on access guardrail violations by selecting the View access guardrail report button. You can generate a report based on the date range, access guardrail name, violation status, or remediation status.
You can view violations by remediation, violations by risk, and top 5 guardrail violations that were triggered. You can also save the screenshot of the report in the PDF format.
Here are the report filter parameters:
- By Date Range : Use From and To fields to select dates.
- By access guardrail name : View the report for a specific access guardrail.
- By Violation Status : Violations are either opened, with the request status still marked as blocked, or closed, where a previous violation has now been resolved.
- By Violation Remediation : Violation resolution status can be:
- Cleared : A previous violation has now been resolved and closed.
- Blocked : A violation still exists and access request status is blocked.
- Snoozed : A violation that exists for low-risk access guardrails. The approver can accept the risk and approve the access for the defined number of days.

## Delete an Access Guardrail

You can delete an access guardrail and remove its association from an access bundle. After deleted, the access guardrail check would no longer be enforced. Additionally, any open or blocked violations related to the access guardrail would also be removed.

- Go to the Access Guardrails page.
- For a guardrail that you want to delete, select the Actions menu (three dots), and then select Delete .
-
