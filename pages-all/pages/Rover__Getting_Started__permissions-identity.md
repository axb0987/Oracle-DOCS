# Identity and Access Management Permissions for Roving Edge Infrastructure
- Source: https://docs.oracle.com/en-us/iaas/Content/Rover/Getting_Started/permissions-identity.htm
- Fetched: 2026-09-05 02:59 CDT

# Identity and Access Management Permissions for Roving Edge Infrastructure

Describes the details for writing user IAM policies that control access to rules for the Identity and Access Management service for a Roving Edge Infrastructure device.

## Resource-Types

`groups`

`policies`

`users`

`lockout-policies`

## Details for Verb + Resource-Type Combinations

The following tables show the permissions and API operations covered by each verb. The level of access is cumulative as you go from`inspect`&gt;`read`&gt;`use`&gt;`manage`.

### groups

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

GROUP_INSPECT

ListGroups

GetGroups

ListUserGroupMembership (also needs USER_INSPECT)

GetUserGroupMembership (also needs USER_INSPECT)

read

GROUP_INSPECT

ListGroups

GetGroups

None

use

GROUP_INSPECT

GROUP_UPDATE

ListGroups

GetGroups

UpdateGroup

AddUserToGroup (also needs USER_UPDATE)

RemoveUserFromGroup (also needs USER_UPDATE)

manage

GROUP_INSPECT

GROUP_UPDATE

GROUP_CREATE

GROUP_DELETE

ListGroups

GetGroups

UpdateGroup

CreateGroup

DeleteGroup

None

### policies

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

POLICY_READ

ListPolicies

GetPolicies

None

read

POLICY_READ

ListPolicies

GetPolicies

None

use

POLICY_READ

ListPolicies

GetPolicies

None

manage

POLICY_READ

POLICY_UPDATE

POLICY_CREATE

POLICY_DELETE

ListPolicies

GetPolicies

UpdatePolicy

CreatePolicy

DeletePolicy

None

### users

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

USER_INSPECT

ListUsers

GetUser

ListUserGroupMembership (also needs GROUP_INSPECT)

GetUserGroupMembership (also needs GROUP_INSPECT)

read

USER_INSPECT

USER_READ

ListUsers

GetUser

ListApiKeys

ListAuthTokens

ListOauth2ClientCredentials

ListCustomerSecretKeys

None

use

USER_INSPECT

USER_READ

USER_UPDATE

ListUsers

GetUser

ListApiKeys

ListAuthTokens

ListOauth2ClientCredentials

ListCustomerSecretKeys

UpdateUser

AddUserToGroup (also needs GROUP_UPDATE)

RemoveUserFromGroup (also needs GROUP_UPDATE)

manage

USER_APIKEY_ADD

USER_APIKEY_REMOVE

USER_AUTHTOKEN_REMOVE

USER_AUTHTOKEN_RESET

USER_AUTHTOKEN_SET

USER_CAPABILITIES_UPDATE

USER_CREATE

USER_DELETE

USER_INSPECT

USER_OAUTH2_CLIENT_CRED_CREATE

USER_OAUTH2_CLIENT_CRED_UPDATE

USER_OAUTH2_CLIENT_CRED_REMOVE

USER_READ

USER_SECRETKEY_ADD

USER_SECRETKEY_REMOVE

USER_SECRETKEY_UPDATE

USER_UNBLOCK

USER_UPDATE

ListUsers

GetUser

ListApiKeys

ListAuthTokens

ListOauth2ClientCredentials

ListCustomerSecretKeys

UpdateUser

UploadApiKey

DeleteApiKey

DeleteAuthToken

UpdateAuthToken

CreateAuthToken

UpdateUserCapabilities

CreateUser

DeleteUser

CreateOauth2ClientCredential

UpdateOauth2ClientCredential

DeleteOauth2ClientCredential

CreateCustomerSecretKey

DeleteCustomerSecretKey

UpdateCustomerSecretKey

UpdateUserState

None

### lockout-policies

Verbs Permissions APIs Fully Covered APIs Partially Covered

inspect

LOCKOUT_POLICY_INSPECT

ListLockoutPolicies

None

read

LOCKOUT_POLICY_INSPECT

LOCKOUT_POLICY_READ

ListLockoutPolicies

GetLockoutPolicy

None

use

LOCKOUT_POLICY_INSPECT

LOCKOUT_POLICY_READ

LOCKOUT_POLICY_UPDATE

ListLockoutPolicies

GetLockoutPolicy

UpdateLockoutPolicy

None

manage

LOCKOUT_POLICY_INSPECT

LOCKOUT_POLICY_READ

LOCKOUT_POLICY_UPDATE

ListLockoutPolicies

GetLockoutPolicy

UpdateLockoutPolicy
