# Locations
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/location.htm
- Fetched: 2026-09-05 02:27 CDT

# Locations

Compartments are created by tenancy administrators in IAM. You can specify compartments by name or OCID.

The policy statement's compartment element specifies the scope of access to a compartment or tenancy. For example, use`tenancy`as a location to grant access to the specified resources across an entire tenancy.
Note  
  

To create a policy that gives access to a specific region or availability domain, use the`request.region`or`request.ad`attribute with a condition. For more information, see[Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/conditions.htm).

The location is required in policy statements.

Syntax:`[ tenancy | compartment <compartment_name> | compartment id <compartment_ocid>`]
Note  
  

By default, the policy statement's compartment is assumed to be a direct child of the compartment where you create the policy. To specify a different parent compartment, use the compartment path, with a colon between the two compartments.

Example

```

```

Examples :
- 

Single compartment by name
```

```

- 

Single compartment by OCID

```

```

- 

Many compartments by name

```

```

- 

Many compartments by OCID

```

```
