# Updating an OAuth Setting
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/oauth/update-oauth-settings.htm
- Fetched: 2026-09-05 02:25 CDT

# Updating an OAuth Setting

Configure the default token issuance policy in an identity domain in IAM.

- Open the navigation menu and select Identity &amp; Security . Under Identity , select Domains .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
- On the domain details page, select Security .
- On the Security page, select OAuth .
- Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select Security and then OAuth .
- Under Default token issuance policy , select Allow all resources .
This setting allows the client to access any resource within the tenant regardless of the trust scope settings at the application level.
- (Optional) In the Issuer field, enter a custom issuer value. This issuer value is used in the newly issued tokens.

If you don't specify a custom issuer, the default IDCS issuer is used:
```

```

Note  
  
Allowed issuer values are either the default IDCS issuer (`https://identity.oraclecloud.com`) or an issuer with the same prefix as the current domain value (for example,`https://idcs-abcdefghijklmnopqrstuvwxyz.identity.oraclecloud.com`).

Caution  
  

Only one previous issuer value is stored. If you make frequent changes in the issuer value, the old token validation might fail.

After changing the issuer value at the domain level, the issuer might be different on the client side based on the tenancy configuration. Validate the issuer value logic on the client side to use the new issuer value.
-
