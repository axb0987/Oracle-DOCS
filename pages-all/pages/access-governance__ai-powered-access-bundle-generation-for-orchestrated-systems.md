# AI-Powered Access Bundle Generation for Orchestrated Systems
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/ai-powered-access-bundle-generation-for-orchestrated-systems.htm
- Fetched: 2026-09-05 03:13 CDT

# AI-Powered Access Bundle Generation for Orchestrated Systems

Oracle Access Governance offers AI-powered access bundle recommendations through its Auto-generated access bundles capability. This streamlines application onboarding by discovering source configuration and automatically generating access bundle recommendations for managed applications, including Generative AI-generated naming conventions and descriptions.

## Overview

Onboarding a new orchestrated system into Oracle Access Governance involves importing users and their associated permissions, such as entitlements, groups, and roles from the managed system. However, requesting access to these permissions then requires configuring access bundles within Oracle Access Governance and assigning the permissions to them, even if they are already defined in the managed system.

The Auto-generated access bundles recommendation capability addresses this challenge. It leverages Artificial Intelligence (AI) to intelligently discover existing relationship mappings between users and permissions within a managed system. It then automatically generates access bundle recommendations for managed applications, complete with Generative AI-generated naming conventions and descriptions. This approach significantly reduces administrative effort, eliminates duplicate modeling, and enables seamless use within Oracle Access Governance.

Additionally, Oracle Access Governance introduces Account profiles , which standardize and simplify the creation of new user accounts in managed systems by pre-defining and storing their essential attributes. This simplifies permission management by eliminating the need to repeatedly enter account details for provisioning in each access bundle.

This integrated solution provides the following benefits:
- Ensures consistency in provisioning.
- Reduces administrative effort.
- Minimizes manual tasks.
- Simplifies onboarding through pre-configured account profile template experience.
- Provides faster governance.

## Authorization for AI-Powered Access Bundle Generation

Users can access the AI-powered access bundle recommendation framework in Oracle Access Governance, if they have the following authorizations.
- `AG_Administrator`
- `AG_AppOwner_Admin`
- `AG_AppOwner_Admin_Restricted`

For more details, see[Application Roles and Responsibilities Reference](https://docs.oracle.com/en-us/iaas/Content/access-governance/application-roles-and-responsibilities-reference.htm).

## Before You Begin

Before using the AI-powered access bundle recommendations, you must ensure some key prerequisites are met.

- Orchestrated System Integration : The managed system must be successfully configured and integrated as an orchestrated system within Oracle Access Governance.
- Identity Data Synchronization : A successful and complete data load from the managed system into Oracle Access Governance is mandatory. This includes user accounts within the managed system and all the relevant permissions, such as roles, entitlements, and groups. Oracle Access Governance uses this data to understand existing assignments.
- Account Profiles Creation : The account profile containing the account attribute values must exist for the managed system. See[Setting Up Account Profiles in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-setting-up-account-profiles-in-oracle-access-governance).
Note  
  
Some managed systems don't require additional details for an account to be created. Therefore, the account profile is not required and will not be displayed. Examples of such managed systems are Oracle Cloud Infrastructure, Flat File, and Fusion Applications.

## Process Flow for AI-Powered Access Bundle Generation

Let's look at the high-level steps involved in the AI-powered access bundle generation process in Oracle Access Governance.

- Create Account Profiles: First, set up the Account profiles required for provisioning users from Oracle Access Governance to the managed system. See[Setting Up Account Profiles in Oracle Access Governance](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-settings-for-an-orchestrated-system.htm#configure-setting-up-account-profiles-in-oracle-access-governance).
- Generate AI-Powered Access Bundle Recommendations: To retrieve intelligent access bundle recommendations, use the Build new recommendations feature on the Auto-generated access bundles page for your orchestrated system in the Oracle Access Governance Console. This triggers a Machine Learning (ML) job that mines existing users-permissions relationships from a managed system and then automatically generates access bundle recommendations including Generative AI-generated naming conventions and descriptions. See[Create Auto-Generated Access Bundle Recommendations](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-ai-powered-access-bundle-generation.htm#create-auto-generated-access-bundle-recommendations).
- Convert AI-Powered Recommendations into Access Bundles: Finally, an administrator manually converts these recommendations into actual access bundles. See[Finalize Auto-Generated Access Bundle Recommendations](https://docs.oracle.com/en-us/iaas/Content/access-governance/manage-ai-powered-access-bundle-generation.htm#finalize-auto-generated-access-bundle-recommendations).
