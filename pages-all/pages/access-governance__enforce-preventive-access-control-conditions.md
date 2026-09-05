# Access Guardrails - Enforcing Preventive Access Control Constraints
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/enforce-preventive-access-control-conditions.htm
- Fetched: 2026-09-05 03:14 CDT

# Access Guardrails - Enforcing Preventive Access Control Constraints

Access Guardrails in Oracle Access Governance are security constraints to define and enforce conditions to regulate and restrict access to sensitive resources. Access Guardrails ensure only authorized identities meeting predefined criteria can gain access. If these conditions are not met, a violation is triggered, allowing you to either block access immediately or provide a grace period for compliance.

## Overview

Implementing Access Guardrails require identities to meet a predefined condition, such as owning a prerequisite permission or an identity attribute, before granting an elevated permission. Such a layered model ensures permissions are granted in a controlled sequence, making access management secure and compliant.

Access Guardrails are NOT applicable when provisioning is done by using Oracle Access Governance policies. Use the self-service, Request Access functionality of Oracle Access Governance to trigger Access Guardrails.

Access Guardrails help security administrators block unauthorized access by ensuring that access requests meet predefined criteria before submission. They also give approvers important context, enabling them to make more informed decisions during the approval process.

Access Guardrails can also be used with Identity Collections. This allows Access Control Administrators to establish preventive access control measures, ensuring that only authorized and compliant identities, those meeting predefined criteria, are members of an Identity Collection. If these conditions are not met, a violation is raised, and you can select to block access immediately or allow a grace period for compliance.

### Key Features of Access Guardrails
- Tiered Permission Model : Access Guardrails help to structure access in tiers—starting with basic roles, such as DB Reader , and progressing to higher privilege roles only when predefined conditions are met. Using this approach, you can ensure that only the minimum necessary rights are granted at each tier.
- Prevents Segregation of Duties Violation : Security constraints in Access Guardrails acts as a pre-check to block access that could conflict with existing roles or responsibilities. For example, in Entra ID, a user assigned both the User Administrator role and the Privileged Role Administrator can independently create new users and elevate their own permissions, posing a risk.
- Conditional Access Enforcement : Access Guardrails require users to satisfy specific conditions, such as role, group membership, location and so on, and continuously monitor change in these attributes to allow or block access.

## Access Guardrails Flow Framework

Here's how Access Guardrails work in Oracle Access Governance.  

  

- Access Control administrator associates access guardrail and approval workflow with an access bundle.
- Identity raises a request for an access bundle using the Request Access functionality.
- The request is validated against the access guardrail. Here's what can happen based on guardrails configurations:
- No Violation : The approver takes decision based on the approval workflow.
- High Risk Violations : The request fails and isn't raised, raising the violation with the Blocked status.
- Low Risk Violation : The request is raised to the approver with violations in the Snoozed status. The approver takes decision to either approve or reject the request, If approved, the request is granted for the defined number of days.

## Access Guardrails Implementation Example

Scenario : For Oracle Unified Directory (OUD) orchestrated system, let's assume that before you grant AccessControlAdmins group access, you want to pre-check the following conditions:
- Restrict granting access to identities belonging to conflicting groups such as DirectoryUserAdmins group.
- Granting access only for identity department belonging to the CorpIT department.

Here's how you can define access guardrails for the specific scenario:

Add Details Name :`oud-access-admin-check`

Select New access requests only
Define rules for Access Guardrails Add two conditions, as follows:
- Select Identity must not have a permission and select the following:
- Which system:`oracle-unified-directory`
- Which granted permission -`Group`
- Which permission:`DirectoryUserAdmins`
- Select Identity matches an attribute and select the following
- Which attribute:`Department`Equals`CorpIT`
Action on Failure Select High Risk - Block the access immediately

After an access guardrail is attached to the access bundle, the request would be validated for these conditions. If a user already belongs to`DirectoryUserAdmins`group or isn't part of`CorpIT`
