# User Types and Permissions
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/dedicated_kms_user_mgmt_user_roles_types.htm
- Fetched: 2026-09-05 02:34 CDT

# User Types and Permissions

Configure Dedicated KMS user types and define permissions to the HSM partition.

The following table lists the operations that each user role can perform on an HSM partition:

Operations Mode Crypto Officer(CO) Crypto User (CU)
`loginHSM`Global, Server Yes Yes
`createUser`Global, Server Yes No
`syncUser`Global, Server Yes No
`listUsers`Global, Server Yes Yes
`deleteUser`Global, Server Yes No
`changePswd`Global, Server No Yes
`getUserInfo`Global, Server Yes Yes
`getKeyDiffMap`Global, Server Yes No
`getUserDiffMap`Server Yes Yes
`storeFixedKey`Server Yes No
syncKey Server Yes No
`modifyKeyOwner`Server Yes No
`FindAllKeys`Global, Server Yes No
`getKeyInfo`Global, Server No Yes
`setUserAttributes`Global, Server Yes No
`setAttribute`Global, Server Yes Yes
`getAttribute`Global, Server No Yes
`listAttributes`Global, Server Yes Yes
`registerUserAuthPubKey`Global, Server Yes No
`deregisterUserAuthPubKey`Global, Server Yes No
`setUserAuthPubKey`Global, Server Yes No

`listUserAuthPubKeys`Global, Server Yes Yes
`updateUserAuthPubKey`Global, Server Yes No
`resetUserAuthPubKey`Global, Server Yes No
`getCert`Server Yes Yes
`unlockUser`Global, Server Yes No
`unlockCO`Global, Server Yes No
`logoutHSM`Global, Server Yes Yes
`backupPartition`Server Yes No

`getPartitionInfo`Server Yes No
`restorePartition`Server Yes No
`Reconnect`Server Yes Yes
`server`Global, Server Yes Yes
`Info`Global Yes Yes
`Help`Global, Server Yes Yes
`Quit`Global Yes Yes
`Exit`
