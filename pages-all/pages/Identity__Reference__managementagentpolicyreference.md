# Details for Management Agent
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/managementagentpolicyreference.htm
- Fetched: 2026-09-05 02:15 CDT

# Details for Management Agent

This topic covers details for writing policies to control access to the Management Agent service.

## Resource-Types

`management-agents`

`management-agent-install-keys`

`management-agent-named-credentials`

## Supported Variables

Only the general variables are supported (see[General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)).

## Details for Verb + Resource-Type Combinations

The following tables show the[permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm)and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.

### management-agents

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

MGMT_AGENT_INSPECT

ListManagementAgentPlugins

ListManagementAgents

ListWorkRequestErrors

ListWorkRequestLogs

ListWorkRequests

none
read

INSPECT +

MGMT_AGENT_READ

INSPECT +

GetManagementAgent

GetWorkRequest

none
use

READ +

MGMT_AGENT_UPDATE

READ +

UpdateManagementAgent

none
manage

USE +

MGMT_AGENT_CREATE

MGMT_AGENT_DELETE

MGMT_AGENT_DEPLOY_PLUGIN_CREATE

USE +

DeleteManagementAgent

DeployPlugins

DeleteWorkRequest

none

### management-agent-install-keys

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

MGMT_AGENT_INSTALL_KEY_INSPECT

ListManagementAgentInstallKeys

none
read

INSPECT +

MGMT_AGENT_INSTALL_KEY_READ

INSPECT +

GetManagementAgentInstallKey

GetManagementAgentInstallKeyContent

none
use

READ +

MGMT_AGENT_INSTALL_KEY_UPDATE

READ +

UpdateManagementAgentInstallKey

none
manage

USE +

MGMT_AGENT_INSTALL_KEY_CREATE

MGMT_AGENT_INSTALL_KEY_DELETE

USE +

CreateManagementAgentInstallKey

DeleteManagementAgentInstallKey

none

### management-agents-named-credentials

Verbs Permissions APIs Fully Covered APIs Partially Covered
inspect

MGMT_AGENT_NAMED_CREDENTIAL_INSPECT

ListNamedCredentials

none
read

INSPECT +

MGMT_AGENT_NAMED_CREDENTIAL_READ

MGMT_AGENT_NAMED_CREDENTIAL_APPLY

INSPECT +

GetNamedCredential

GetNamedCredentialsMetadatum

none
use

READ +

MGMT_AGENT_NAMED_CREDENTIAL_APPLY

READ +

UpdateNamedCredential

none
manage

USE +

MGMT_AGENT_NAMED_CREDENTIAL_CREATE

MGMT_AGENT_NAMED_CREDENTIAL_UPDATE

MGMT_AGENT_NAMED_CREDENTIAL_DELETE

USE +

CreateNamedCredential

DeleteNamedCredential

UpdateNamedCredential

none

## Permissions Required for Each API Operation

The following table lists the API operations in alphabetical order.

For information about permissions, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/../Concepts/policyadvancedfeatures.htm#Permissi).

API Operation Permissions Required to Use the Operation
`CreateManagementAgentInstallKey`MGMT_AGENT_INSTALL_KEY_CREATE
`CreateNamedCredential`MGMT_AGENT_NAMED_CREDENTIAL_CREATE
`DeleteManagementAgent`MGMT_AGENT_DELETE
`DeleteManagementAgentInstallKey`MGMT_AGENT_INSTALL_KEY_DELETE
`DeleteNamedCredential`MGMT_AGENT_NAMED_CREDENTIAL_DELETE
`DeleteWorkRequest`MGMT_AGENT_DELETE
`DeployPlugins`MGMT_AGENT_DEPLOY_PLUGIN_CREATE
`GetManagementAgent`MGMT_AGENT_READ
`GetManagementAgentInstallKey`MGMT_AGENT_INSTALL_KEY_READ
`GetManagementAgentInstallKeyContent`MGMT_AGENT_INSTALL_KEY_READ
`GetNamedCredential`MGMT_AGENT_NAMED_CREDENTIAL_READ
`GetNamedCredentialsMetadatum`MGMT_AGENT_NAMED_CREDENTIAL_INSPECT
`GetWorkRequest`MGMT_AGENT_READ
`ListManagementAgentInstallKeys`MGMT_AGENT_INSTALL_KEY_INSPECT
`ListManagementAgentPlugins`MGMT_AGENT_INSPECT
`ListManagementAgents`MGMT_AGENT_INSPECT
`ListNamedCredentials`MGMT_AGENT_NAMED_CREDENTIAL_INSPECT
`ListWorkRequestErrors`MGMT_AGENT_INSPECT
`ListWorkRequestLogs`MGMT_AGENT_INSPECT
`ListWorkRequests`MGMT_AGENT_INSPECT
`UpdateManagementAgent`MGMT_AGENT_UPDATE
`UpdateManagementAgentInstallKey`MGMT_AGENT_INSTALL_KEY_UPDATE
`UpdateNamedCredential`MGMT_AGENT_NAMED_CREDENTIAL_UPDATE

For more details and examples, see[Set Up Oracle Cloud Infrastructure for Management Agents](https://docs.oracle.com/iaas/management-agents/doc/perform-prerequisites-deploying-management-agents.html#OCIAG-GUID-EFD288F4-55C4-4DEF-900D-0DEAA24360A2)
