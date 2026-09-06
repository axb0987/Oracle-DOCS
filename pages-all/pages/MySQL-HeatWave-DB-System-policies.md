# Policies for MySQL HeatWave DB System
- Source: https://docs.oracle.com/iaas/disaster-recovery/doc/MySQL-HeatWave-DB-System-policies.html
- Fetched: 2026-09-05 18:57 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/disaster-recovery/doc/MySQL-HeatWave-DB-System-policies.html#dcoc-content-body)

# Policies for MySQL HeatWave DB System

Shows how to allow Disaster Recovery (DR) to manage MySQL DB System that is part of the application stack.

Policies to configure using resource principal

```

```

Policies to configure using user authentication:

Policies for MySQL DB System
Configure policies to allow Disaster Recovery (DR) to manage MySQL resource family.
```

```
Policies for Vault-Secret

Configure IAM policies to grant read access to the vault secret used in MySQL DB System disaster recovery (DR) operations, enabling authorized resource principals to retrieve the secret as needed.

Create a Dynamic Group

Before creating the policy, ensure that you have defined a dynamic group for the resources that require access to the Vault secret. For example, to grant all instances within a specific compartment access to the secret, you can use the following policy syntax:

```

```

Replace`<compartment_ocid>`with the actual OCID of your compartment.

Policies for Object Storage

Define the Policy

Create a policy that grants the dynamic group permission to`read`secrets from the Vault and upload logs to Object Storage Bucket during execution. Use the`read`verb with the`secret-family`resource type. The policy syntax is:

```

```

```

```

In the above example:
```

```

Example Policy

If your dynamic group is named`InstanceSecretReaders`and your secrets are stored in the compartment`MySecretsCompartment`then the policy statement would be:

```

```

This policy allows any resource that is a member of the`InstanceSecretReaders`dynamic group to read the secrets stored in the`MySecretsCompartment`compartment through OCI Vault.

Related Topics
- [Policy Configuration for Cluster Creation and Deployment](https://docs.oracle.com/iaas/Content/ContEng/Concepts/contengpolicyconfig.htm)

Parent topic:[Policies for Other Services Managed by Full Stack Disaster Recovery](https://docs.oracle.com/iaas/disaster-recovery/doc/dr-managed-services-policies.html#GUID-CD390A24-EB73-45FB-A770-7E286AD663E4)

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
