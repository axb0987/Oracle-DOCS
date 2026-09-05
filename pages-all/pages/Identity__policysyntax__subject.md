# Subjects
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/subject.htm
- Fetched: 2026-09-05 02:27 CDT

# Subjects

The subject of an IAM policy specifies the groups or principals that the policy grants permission to.

Syntax:
```

```

Note  
  
The subject &lt;any-group&gt; includes all groups and all dynamic groups.

The subject of an IAM policy to specify the principals that the policy grants permission to.
Syntax:
```

```

A policy statement can include only one type of principal, but you can include many instances of that principal.
Note  
  

If the policy is for the default identity domain, you can omit &lt;identity_domain_name&gt; . The policy processes and interprets the policy statement as though it was written as`Default / <group_name>`.

Examples:
- Single group by name in the default identity domain:
```

```

- Several groups by name in the default identity domain (a space after the comma is optional):
```

```

- Single group by OCID in the default identity domain:
```

```

- Several groups by OCID in the default identity domain:
```

```

- Any user in the default identity domain tenancy:
```

```

- Service in the in the default identity domain tenancy:
```

```

- Single group in a secondary identity domain by name:
```

```
