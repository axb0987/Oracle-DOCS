# Supporting Social JIT Provisioning with Group Membership Support
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/implicitJitGroupMembership.htm
- Fetched: 2026-09-05 02:17 CDT

# Supporting Social JIT Provisioning with Group Membership Support

Use the API to manage new identity domain users with social Just-In-Time (JIT) user provisioning for first-time users.

OCI REST API now supports social JIT Provisioning, to automate user account creation when the user first tries to access identity domains when the user doesn't exist in the identity domain. Social JIT provisioning also supports granting group membership as part of user provisioning.

## Attribute Definitions

- socialJitProvisioningEnabled : You can enable/disable social JIT by controlling this social attribute.
- jitProvGroupStaticListEnabled : When JIT is enabled, you can set this attribute to true to indicate social JIT user provisioning groups should be assigned from a static list.
- jitProvAssignedGroups : This attribute contains a list of groups to be assigned to each social JIT-provisioned user. JIT user-provisioning applies this static list when jitProvGroupStaticListEnabled is set to true.

## Examples

Toggle Social JIT GroupMembership support:`PATCH /admin/v1/SocialIdentityProviders/{idpID}`
Sample request body:
```

```

Sample response:
```

```

Fetch Group Membership for JIT enabled IDP:`GET /admin/v1/SocialIdentityProviders/{idpId}?attributes=jitProvAssignedGroups`
Sample response:
```

```

Remove particular group GUID from JIT enabled IDP membership list:`PATCH /admin/v1/SocialIdentityProviders/{idpId}`
Sample request body:
```

```

Sample response body:
```

```

Remove Group Membership list for IDP enabled IDP:`PATCH /admin/v1/SocialIdentityProviders/{idpId}`
Sample request body:
```

```

Sample response body:
```

```
