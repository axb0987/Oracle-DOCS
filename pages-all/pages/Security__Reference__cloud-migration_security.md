# Securing Oracle Cloud Migrations
- Source: https://docs.oracle.com/en-us/iaas/Content/Security/Reference/cloud-migration_security.htm
- Fetched: 2026-09-05 03:04 CDT

# Securing Oracle Cloud Migrations

This topic provides security information and recommendations for using Oracle Cloud Migrations.

To collect the metadata of virtual machines (VMs) from an on-premises environment, the Oracle Cloud Migrations service uses a remote agent appliance (virtual appliance) on your on-premises environment. The remote agent appliance runs outside of Oracle Cloud Infrastructure (OCI) as part of your on-premises environment.

Although the appliance is distributed as a sealed virtual machine and is more hardened compared to a regular VM, the appliance is less secure than all the service components that are running within an OCI-controlled environment.

The Oracle Cloud Migrations service uses other core OCI tenancy resources (services) to perform a migration and therefore it needs explicit permissions to interact with these resources.
In the following sections, you'll find information on how you can:
- Secure access to migration secrets using a compartment and Identity and Access Management (IAM) policies.
- Secure communication between the migration service components and other core OCI services by using a compartment and IAM policies.

## Security Recommendations

The remote agent appliance runs a few plugins such as discovery or replication. These plugins need credentials to access your on-premises environment assets and be able to perform desired operations.

The credentials of the plugins are stored as secrets in OCI Vault. Here are the recommendations for securing access to migration secrets and providing privileges for other core OCI services.

- Understand and follow the best practices to organize and store secrets in OCI Vault by practicing the principle of least privilege. Create a dedicated compartment to store migration secrets, which is a separate compartment from any other secrets stored in OCI Vault.
- Create identity policies statements that only allow the discovery and replication plugins to access the secrets in the migration secrets compartment.
- Create identity policies statements that allow minimal access to the other core OCI services that are needed to perform migration tasks.

## Security Policy Examples

The following are the examples for creating policies for accessing secrets in migration compartments.

### Organize Compartments with Secrets and Let Discovery Plugin Access Secrets

- Create a designated compartment for the migration secrets such as,`migration_secrets`.

See[Recommendations for Working with Compartments](http://docs.oracle.com/iaas/Content/cloud-migration/cloud-migration-get-started.htm#cloud-migration-recommendations-compartments).
- [Create Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm)using the`migration_secrets`compartment.
- [Managing Keys](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm)for the vault.
- 

Create a policy that allows the discovery plugin to access the`migration_secrets`that you created.

For example, the discovery plugin is provided a read access for`migration_secrets`.

```

```

For more information about Discovery plugin policies, see[Oracle Cloud Migration Service Policies](https://docs.oracle.com/iaas/Content/cloud-migration/cloud-migration-servicepolicies.htm).

### Organize Compartments with Secrets and Let Replication Plugin Access Secrets

- Create a designated compartment for the migration secrets such as,`migration_secrets`.
- [Creating a Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults_topic-To_create_a_new_vault.htm)using the`migration_secrets`compartment.
- [Create master encryption key](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingkeys.htm)for the vault.
- 

Create a policy that allows the replication plugin to access the`migration_secrets`that you created.

For example, the replication plugin is provided a read access for`migration_secrets`.

```

```

For more information about Replication plugin policies, see[Oracle Cloud Migration Service Policies](https://docs.oracle.com/iaas/Content/cloud-migration/cloud-migration-servicepolicies.htm).

### Let Hydration Agent Access Snapshot Objects from the Replication Bucket

```

```

For more information about Hydration Agent policies, see[Oracle Cloud Migration Service Policies](https://docs.oracle.com/iaas/Content/cloud-migration/cloud-migration-servicepolicies.htm)
