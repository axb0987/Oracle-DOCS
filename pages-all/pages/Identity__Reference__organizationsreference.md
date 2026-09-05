# Details for Organization Management
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm
- Fetched: 2026-09-05 02:15 CDT

# Details for Organization Management

This topic covers details for writing policies to control access to Organization Management.

## Resource-Types

- `organizations-family`
- `organizations-link`
- `organizations-recipient-invitation`
- `organizations-sender-invitation`
- `organizations-invitation`
- `organizations-domain`
- `organizations-domain-governance`
- `organizations-entity`
- `organizations-tenancy`
- `organizations-order`
- `organizations-subscription`
- `organizations-subscription-mapping`
- `organizations-assigned-subscription`
- `organizations-subscription-region`
- `organizations-governance-rules`
- `organizations-enforced-governance-rules`

## Supported Variables

Organization Management supports all the general variables (see[General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)), plus additional ones listed here:

Required variables (supplied by service for every request):

Variable Variable Type Comments
`target.resource.kind`String The resource kind name of the primary resource for the request.

Automatic Variables (supplied by the SDK for every request):

Variable Variable Type Comments
`target.tenant.id`Entity (OCID) The OCID of the target tenant ID.

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

[organizations-family](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_LINK_INSPECT

ORGANIZATIONS_RECIPIENT_INVITATION_INSPECT

ORGANIZATIONS_SENDER_INVITATION_INSPECT

ORGANIZATIONS_DOMAIN_INSPECT

ORGANIZATIONS_DOMAIN_GOVERNANCE_INSPECT

ORGANIZATIONS_TENANCY_INSPECT

ORGANIZATIONS_SUBSCRIPTION_INSPECT

ORGANIZATIONS_SUBSCRIPTION_MAPPING_INSPECT

ORGANIZATIONS_ASSIGNED_SUBSCRIPTION_INSPECT

ORGANIZATIONS_SUBSCRIPTION_REGION_INSPECT

GOVERNANCE_RULE_INSPECT

ORGANIZATIONS_ENTITY_INSPECT

ORGANIZATIONS_TENANCY_INSPECT`ListLinks`

`ListRecipientInvitations`

`ListSenderInvitations`

`ListDomains`

`ListDomainGovernances`

`ListOrganizationTenancies`

`ListSubscriptions`

`ListSubscriptionMappings`

`ListAssignedSubscriptions`  
`ListAvailableRegions`

`ListGovernanceRules`

`ListOrganizations`  
none
READ INSPECT + ORGANIZATIONS_LINK_READ

ORGANIZATIONS_RECIPIENT_INVITATION_READ  

ORGANIZATIONS_SENDER_INVITATION_READ

ORGANIZATIONS_DOMAIN_READ

ORGANIZATIONS_DOMAIN_GOVERNANCE_READ

ORGANIZATIONS_ENTITY_READ

ORGANIZATIONS_TENANCY_READ

ORGANIZATIONS_SUBSCRIPTION_READ

ORGANIZATIONS_SUBSCRIPTION_MAPPING_READ

ORGANIZATIONS_ASSIGNED_SUBSCRIPTION_READ

GOVERNANCE_RULE_READ INSPECT +`GetLink`

`GetRecipientInvitation`

`GetSenderInvitation`

`GetDomain`

`GetDomainGovernance`

`GetOrganizationTenancy`

`GetSubscriptionMapping`

`GetAssignedSubscription`

`GetGovernanceRule`

`ListTenancyAttachments`

`GetTenancyAttachment`none
USE READ + ORGANIZATIONS_RECIPIENT_INVITATION_UPDATE

  
ORGANIZATIONS_DOMAIN_UPDATE  

ORGANIZATIONS_DOMAIN_GOVERNANCE_UPDATE

ORGANIZATIONS_ENTITY_UPDATE

ORGANIZATIONS_SENDER_INVITATION_UPDATE

GOVERNANCE_RULE_UPDATE

GOVERNANCE_RULE_RETRY READ +`AcceptRecipientInvitation`

`IgnoreRecipientInvitation`

`CancelSenderInvitation`

`UpdateSenderInvitation`

`UpdateDomain`

`UpdateDomainGovernance`

`UpdateOrganization``GetGovernanceRule`

`DeleteInclusionCriterion`

`RetryGovernanceRule`

`RetryTenancyAttachment`none
MANAGE USE + ORGANIZATIONS_LINK_PARENT_DELETE

ORGANIZATIONS_LINK_CHILD_DELETE  

ORGANIZATIONS_SUBSCRIPTION_MAPPING_CREATE

ORGANIZATIONS_SENDER_INVITATION_CREATE

ORGANIZATIONS_DOMAIN_CREATE

ORGANIZATIONS_DOMAIN_DELETE

ORGANIZATIONS_ORDER_ACTIVATE

ORGANIZATIONS_DOMAIN_GOVERNANCE_CREATE

ORGANIZATIONS_DOMAIN_GOVERNANCE_DELETE

ORGANIZATIONS_ENTITY_UPDATE

ORGANIZATIONS_TENANCY_CREATE

ORGANIZATIONS_SUBSCRIPTION_MAPPING_DELETE

ORGANIZATIONS_TENANCY_DELETE

ORGANIZATIONS_TENANCY_RESTORE

GOVERNANCE_RULE_CREATE

GOVERNANCE_RULE_DELETE USE +`DeleteLink`

`CreateSenderInvitation`

`CreateDomain`

`DeleteDomain`

`ActivateOrder`

`CreateDomainGovernance`

`DeleteDomainGovernance`

`UpdateOrganization`

`CreateChildTenancy`

`DeleteSubscriptionMapping`

`DeleteOrganizationTenancy`

`RestoreOrganizationTenancy`

`CreateSubscriptionMapping`

`CreateGovernanceRule`

`DeleteGovernanceRule`none

[organizations-link](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_LINK_INSPECT`ListLinks`none
READ, USE INSPECT + ORGANIZATIONS_LINK_READ INSPECT +`GetLink`none
MANAGE USE + ORGANIZATIONS_LINK_PARENT_DELETE

ORGANIZATIONS_LINK_CHILD_DELETE USE +`DeleteLink`none

[organizations-recipient-invitation](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_RECIPIENT_INVITATION_INSPECT`ListRecipientInvitations`none
READ INSPECT + ORGANIZATIONS_RECIPIENT_INVITATION_READ INSPECT +`GetRecipientInvitation`none
USE, MANAGE READ + ORGANIZATIONS_RECIPIENT_INVITATION_UPDATE READ +`AcceptRecipientInvitation`

`IgnoreRecipientInvitation`

`UpdateRecipientInvitation`none

[organizations-sender-invitation](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_SENDER_INVITATION_INSPECT`ListRecipientInvitations`none
READ INSPECT + ORGANIZATIONS_SENDER_INVITATION_READ INSPECT +`GetSenderInvitation`none
USE READ + ORGANIZATIONS_SENDER_INVITATION_UPDATE READ +`UpdateSenderInvitation`

`CancelSenderInvitation`none
MANAGE USE + ORGANIZATIONS_SENDER_INVITATION_CREATE USE +`CreateSenderInvitation`none

[organizations-invitation](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_RECIPIENT_INVITATION_INSPECT

ORGANIZATIONS_SENDER_INVITATION_INSPECT`ListRecipientInvitations`

`ListSenderInvitations`none
READ INSPECT + ORGANIZATIONS_RECIPIENT_INVITATION_READ

ORGANIZATIONS_SENDER_INVITATION_READ INSPECT +`GetRecipientInvitation`

`GetSenderInvitation`none
USE READ + ORGANIZATIONS_RECIPIENT_INVITATION_UPDATE

ORGANIZATIONS_SENDER_INVITATION_UPDATE READ +`AcceptRecipientInvitation`

`UpdateRecipientInvitation`

`UpdateSenderInvitation`

`CancelSenderInvitation`none
MANAGE USE + ORGANIZATIONS_SENDER_INVITATION_CREATE USE +`CreateSenderInvitation`none

[organizations-domain](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_DOMAIN_INSPECT`ListDomains`none
READ INSPECT + ORGANIZATIONS_DOMAIN_READ INSPECT +`GetDomain`none
USE READ + ORGANIZATIONS_DOMAIN_UPDATE READ +`UpdateDomain`none
MANAGE USE + ORGANIZATIONS_DOMAIN_CREATE

ORGANIZATIONS_DOMAIN_DELETE USE +`CreateDomain`

`DeleteDomain`none

[organizations-domain-governance](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_DOMAIN_GOVERNANCE_INSPECT`ListDomainGovernances`none
READ INSPECT + ORGANIZATIONS_DOMAIN_GOVERNANCE_READ INSPECT +`GetDomainGovernance`none
USE READ + ORGANIZATIONS_DOMAIN_GOVERNANCE_UPDATE READ +`UpdateDomainGovernance`none
MANAGE USE + ORGANIZATIONS_DOMAIN_GOVERNANCE_CREATE

ORGANIZATIONS_DOMAIN_GOVERNANCE_DELETE USE +`CreateDomainGovernance`

`DeleteDomainGovernance`none

[organizations-entity](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_ENTITY_INSPECT`ListOrganizations`none
READ INSPECT + ORGANIZATIONS_ENTITY_READ INSPECT +`GetOrganization`none
USE READ + ORGANIZATIONS_ENTITY_UPDATE READ +`UpdateOrganization`none
MANAGE - - none

[organizations-tenancy](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_TENANCY_INSPECT`ListOrganizationTenancies`none
READ, USE INSPECT + ORGANIZATIONS_TENANCY_READ INSPECT +`GetOrganizationTenancy`none
MANAGE USE + ORGANIZATIONS_TENANCY_CREATE

ORGANIZATIONS_TENANCY_DELETE

ORGANIZATIONS_TENANCY_RESTORE USE +`CreateChildTenancy`

`DeleteOrganizationTenancy`

`RestoreOrganizationTenancy`none

[organizations-order](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT - - none
READ - - none
USE - - none
MANAGE ORGANIZATIONS_ORDER_ACTIVATE`ActivateOrder`none

[organizations-subscription](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_SUBSCRIPTION_INSPECT`ListSubscriptions`none
READ INSPECT + ORGANIZATIONS_SUBSCRIPTION_READ INSPECT +`GetSubscription`none
USE, MANAGE USE + ORGANIZATIONS_SUBSCRIPTION_ASSIGN

ORGANIZATIONS_SUBSCRIPTION_DELETE  
ORGANIZATIONS_SUBSCRIPTION_MAPPING_CREATE USE +`AssignTenancySubscription`

`AssignDefaultSubscription`

`CreateSubscriptionMapping`none

[organizations-subscription-mapping](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_SUBSCRIPTION_MAPPING_INSPECT`ListSubscriptionMappings`none
READ INSPECT + ORGANIZATIONS_SUBSCRIPTION_MAPPING_READ INSPECT +`GetSubscriptionMapping`none
USE, MANAGE USE + ORGANIZATIONS_SUBSCRIPTION_MAPPING_DELETE

ORGANIZATIONS_SUBSCRIPTION_MAPPING_CREATE USE +`DeleteSubscriptionMapping`

`CreateSubscriptionMapping`none

[organizations-assigned-subscription](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_ASSIGNED_SUBSCRIPTION_INSPECT`ListAssignedSubscriptions`none
READ INSPECT + ORGANIZATIONS_ASSIGNED_SUBSCRIPTION_READ INSPECT +`GetAssignedSubscription`none
USE - - none
MANAGE - - none

[organizations-subscription-region](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT ORGANIZATIONS_SUBSCRIPTION_REGION_INSPECT`ListAvailableRegions`none
READ - - none
USE - - none
MANAGE - - none

[organizations-governance-rules](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT GOVERNANCE_RULE_INSPECT`ListGovernanceRules`

`ListOrganizations`

`ListOrganizationTenancies`none
READ INSPECT + GOVERNANCE_RULE_READ INSPECT +`GetGovernanceRule`

`ListTenancyAttachments`

`GetTenancyAttachment`none
USE READ + GOVERNANCE_RULE_UPDATE

GOVERNANCE_RULE_RETRY READ +`GetGovernanceRule`

`DeleteInclusionCriterion`

`RetryGovernanceRule`

`RetryTenancyAttachment`none
MANAGE USE + GOVERNANCE_RULE_CREATE

GOVERNANCE_RULE_DELETE USE +`CreateGovernanceRule`

`DeleteGovernanceRule`none

[organizations-enforced-governance-rules](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm#)

Verbs Permissions APIs Fully Covered APIs Partially Covered
INSPECT GOVERNANCE_RULE_ENFORCED_INSPECT`ListEnforcedGovernanceRules`

`ListOrganizations`

`ListOrganizationTenancies`none
READ INSPECT + GOVERNANCE_RULE_ENFORCED_READ INSPECT +`GetEnforcedGovernanceRule`none
USE - - none
MANAGE - - none

## Permissions Required for Each API Operation

The following table lists the API operations in a logical order, grouped by resource type. For information about permissions, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/../Concepts/policyadvancedfeatures.htm#Permissi).

API Operation Permissions Required to Use the Operation
GetLink ORGANIZATIONS_LINK_READ
ListLinks ORGANIZATIONS_LINK_INSPECT
DeleteLink ORGANIZATIONS_LINK_CHILD_DELETE

ORGANIZATIONS_LINK_PARENT_DELETE
GetRecipientInvitation ORGANIZATIONS_RECIPIENT_INVITATION_READ
AcceptRecipientInvitation ORGANIZATIONS_RECIPIENT_INVITATION_UPDATE
IgnoreRecipientInvitation ORGANIZATIONS_RECIPIENT_INVITATION_UPDATE
UpdateRecipientInvitation ORGANIZATIONS_RECIPIENT_INVITATION_UPDATE
ListRecipientInvitations ORGANIZATIONS_RECIPIENT_INVITATION_INSPECT
CreateSenderInvitation ORGANIZATIONS_SENDER_INVITATION_CREATE
GetSenderInvitation ORGANIZATIONS_SENDER_INVITATION_READ
ListSenderInvitations ORGANIZATIONS_SENDER_INVITATION_INSPECT
CancelSenderInvitation ORGANIZATIONS_SENDER_INVITATION_UPDATE
UpdateSenderInvitation ORGANIZATIONS_SENDER_INVITATION_UPDATE
UpdateSenderInvitation ORGANIZATIONS_DOMAIN_READ
ListDomains ORGANIZATIONS_DOMAIN_INSPECT
CreateDomain ORGANIZATIONS_DOMAIN_CREATE
UpdateDomain ORGANIZATIONS_DOMAIN_UPDATE
DeleteDomain ORGANIZATIONS_DOMAIN_DELETE
GetDomainGovernance ORGANIZATIONS_DOMAIN_GOVERNANCE_READ
ListDomainGovernances ORGANIZATIONS_DOMAIN_GOVERNANCE_INSPECT
CreateDomainGovernance ORGANIZATIONS_DOMAIN_GOVERNANCE_CREATE
UpdateDomainGovernance ORGANIZATIONS_DOMAIN_GOVERNANCE_UPDATE
DeleteDomainGovernance ORGANIZATIONS_DOMAIN_GOVERNANCE_DELETE
GetOrganization ORGANIZATIONS_ENTITY_READ
ListOrganizations ORGANIZATIONS_ENTITY_INSPECT
UpdateOrganization ORGANIZATIONS_ENTITY_UPDATE
GetOrganizationTenancy ORGANIZATIONS_TENANCY_READ
ListOrganizationTenancies ORGANIZATIONS_TENANCY_INSPECT
approveForTransfer/unapproveForTransfer ORGANIZATIONS_TENANCY_TRANSFER_APPROVAL_UPDATE
CreateChildTenancy ORGANIZATIONS_TENANCY_CREATE

Note : When the subscriptionId attribute is specified for a created child tenancy, then ORGANIZATIONS_SUBSCRIPTION_MAPPING_CREATE is also required. For more information see[CreateChildTenancyDetails Reference](https://docs.oracle.com/iaas/api/#/en/organizations/latest/datatypes/CreateChildTenancyDetails).
DeleteOrganizationTenancy ORGANIZATIONS_TENANCY_DELETE
RestoreOrganizationTenancy ORGANIZATIONS_TENANCY_RESTORE
ActivateOrder ORGANIZATIONS_ORDER_ACTIVATE
ListSubscriptions ORGANIZATIONS_SUBSCRIPTION_INSPECT
ListSubscriptionMappings ORGANIZATIONS_SUBSCRIPTION_MAPPING_INSPECT
GetSubscription ORGANIZATIONS_SUBSCRIPTION_READ
GetSubscriptionMapping ORGANIZATIONS_SUBSCRIPTION_MAPPING_READ
AssignTenancySubscription ORGANIZATIONS_SUBSCRIPTION_ASSIGN
AssignDefaultSubscription ORGANIZATIONS_SUBSCRIPTION_ASSIGN
DeleteSubscriptionMapping ORGANIZATIONS_SUBSCRIPTION_MAPPING_DELETE
CreateSubscriptionMapping ORGANIZATIONS_SUBSCRIPTION_MAPPING_CREATE
ListAssignedSubscriptions ORGANIZATIONS_ASSIGNED_SUBSCRIPTION_INSPECT
GetAssignedSubscription ORGANIZATIONS_ASSIGNED_SUBSCRIPTION_READ
ListAvailableRegions ORGANIZATIONS_SUBSCRIPTION_REGION_INSPECT
ListGovernanceRules GOVERNANCE_RULE_INSPECT
GetGovernanceRule GOVERNANCE_RULE_READ
CreateGovernanceRule GOVERNANCE_RULE_CREATE
UpdateGovernanceRule GOVERNANCE_RULE_UPDATE
DeleteGovernanceRule GOVERNANCE_RULE_DELETE
RetryGovernanceRule GOVERNANCE_RULE_RETRY
CreateInclusionCriterion GOVERNANCE_RULE_UPDATE
DeleteInclusionCriterion GOVERNANCE_RULE_UPDATE
ListTenancyAttachments GOVERNANCE_RULE_READ
GetTenancyAttachment GOVERNANCE_RULE_READ
RetryTenancyAttachment GOVERNANCE_RULE_RETRY
ListEnforcedGovernanceRules GOVERNANCE_RULE_ENFORCED_INSPECT
