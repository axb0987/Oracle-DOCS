# Migrating Kubernetes Secrets to KMS v2
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmigratingsecretstokmsv2.htm
- Fetched: 2026-09-05 01:55 CDT

# Migrating Kubernetes Secrets to KMS v2

Find out how to re-encrypt existing Kubernetes secret objects using Key Management Service (KMS) provider version 2 in a cluster you've created using Kubernetes Engine (OKE).

The Kubernetes cluster control plane stores sensitive configuration data (such as authentication tokens, certificates, and credentials) as Kubernetes secret objects in etcd. When you create a cluster using Kubernetes Engine, you can specify a master encryption key in the Oracle Cloud Infrastructure Vault service to encrypt the data encryption keys that protect Kubernetes secrets at rest. For more information, see[Encrypting Kubernetes Secrets at Rest in Etcd](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengencryptingdata.htm).

Kubernetes uses a KMS provider to communicate between the Kubernetes API server and the Kubernetes Engine KMS plugin. The KMS provider version is separate from the version of the master encryption key in Vault. Migrating from KMS provider version 1 to KMS provider version 2 does not require you to create a new master encryption key or change the key associated with the cluster. For more information about Kubernetes KMS providers, see[Using a KMS provider for data encryption](https://kubernetes.io/docs/tasks/administer-cluster/kms-provider/)in the Kubernetes documentation.

The KMS provider version used to encrypt Kubernetes secret objects depends on the Kubernetes version running on the cluster control plane:
- Clusters that use a master encryption key you manage and run Kubernetes versions earlier than 1.36.1 use KMS provider version 1 to encrypt Kubernetes secret objects.
- New clusters created with Kubernetes version 1.36.1 or later and a master encryption key that you manage use KMS provider version 2 from the time the cluster is created.
- When you upgrade an existing cluster to Kubernetes version 1.36.1 or later, Kubernetes Engine starts using KMS provider version 2. New Kubernetes secret objects use KMS provider version 2, as do existing secret objects that are subsequently updated.

Upgrading the cluster control plane does not automatically rewrite all existing Kubernetes secret objects. Secret objects that were encrypted using KMS provider version 1 before the upgrade can remain encrypted using KMS provider version 1 until Kubernetes writes them again.

Kubernetes Engine retains KMS provider version 1 as a read fallback, so existing secret objects remain readable after the control plane upgrade and during migration. You do not have to migrate existing secret objects immediately to keep applications running.

Use the procedure in this topic to rewrite all existing Kubernetes secret objects in one operation. When Kubernetes rewrites each secret object, the Kubernetes API server encrypts it using KMS provider version 2. After the migration succeeds, secret objects that were previously encrypted using KMS provider version 1 have been re-encrypted using KMS provider version 2.

Note the following:
- You do not normally need to perform this migration for a new cluster created with Kubernetes version 1.36.1 or later, because the cluster uses KMS provider version 2 from the time the cluster is created.
- You cannot perform the migration while the cluster control plane is running a Kubernetes version earlier than 1.36.1.
- Kubernetes Engine does not automatically start a bulk migration when you upgrade the cluster control plane. You decide when to start the migration.
- A manual migration is only required when you want to re-encrypt all existing, unchanged Kubernetes secret objects in one operation.
Note  
  

This procedure only applies to clusters that use a master encryption key that you manage to encrypt Kubernetes secret objects at rest in etcd. It does not apply to clusters that only use the default encryption of the block storage volumes containing etcd.

## Before You Begin

Before migrating Kubernetes secret objects to KMS provider version 2:
- Confirm that the cluster uses a master encryption key in the Oracle Cloud Infrastructure Vault service that you manage to encrypt Kubernetes secrets at rest. See[Encrypting Kubernetes Secrets at Rest in Etcd](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengencryptingdata.htm).
- Upgrade the cluster control plane to Kubernetes version 1.36.1 or later. See[Upgrading the Kubernetes Version on Control Plane Nodes in a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8smasternode.htm).
- Configure`kubectl`to access the cluster. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm).
- Ensure that your Kubernetes identity has permission to create, get, watch, and delete the cluster-scoped`storageversionmigrations.storagemigration.k8s.io`resource. A cluster administrator typically has these permissions.
- If you use a backup solution such as Velero, take a current backup that includes all Kubernetes secret objects, and confirm that the backup completed successfully. Protect the backup according to your organization's security requirements because it contains sensitive data.
- Plan to monitor the migration until it succeeds. The migration reads and rewrites every Kubernetes secret object in the cluster and can generate additional Kubernetes API activity. Larger clusters can take longer to migrate.

## Confirming That the Cluster Is Ready

You cannot view the internal Kubernetes Engine KMS provider configuration. Instead, use the Kubernetes control plane version and Kubernetes API discovery to confirm that the cluster is ready for migration:
- 

Check the Kubernetes client and server versions, by entering:

```

```

Confirm that the`Server Version`is`v1.36.1`or later.

The server version is the Kubernetes version running on the cluster control plane. The Kubernetes versions running on worker nodes do not determine whether KMS provider version 2 migration is available.
- 

Check that the Storage Version Migration API is available, by entering:

```

```

Verify that the output includes the`storageversionmigrations`resource, similar to the following:
```

```

- 

Confirm that your Kubernetes identity can create, monitor, and delete a migration, by entering:

```

```

```

```

```

```

```

```

Each command must return`yes`.

If a command returns`no`, ask a cluster administrator to perform the migration or grant the required Kubernetes RBAC permissions.

You can start the migration when all of the following are true:
- The cluster uses a master encryption key that you manage to encrypt Kubernetes secret objects.
- The cluster control plane is running Kubernetes version 1.36.1 or later.
- The Storage Version Migration API is available.
- Your Kubernetes identity has the required permissions.

If the Storage Version Migration API is not available, do not attempt to use a different bulk-rewrite procedure. Confirm that`kubectl`is connected to the intended cluster and that the control plane upgrade has completed. If the API remains unavailable, contact Oracle Support.

## Migrating Existing Kubernetes Secret Objects

For more information about using the Kubernetes Storage Version Migration API to migrate stored objects, see[Migrate Kubernetes Objects Using Storage Version Migration](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/storage-version-migration/)in the Kubernetes documentation.

To re-encrypt all existing Kubernetes secret objects using KMS provider version 2:
- 

Create a file named`migrate-secrets-to-kms-v2.yaml`with the following contents:

```

```

The empty`group`value identifies the Kubernetes core API group. The`resource: secrets`value limits the migration to Kubernetes secret objects.

A`StorageVersionMigration`resource is cluster-scoped. The migration therefore includes Kubernetes secret objects in all namespaces.
- 

Create the migration:

```

```

Creating the resource instructs the Kubernetes storage version migrator to read and rewrite the Kubernetes secret objects. The operation does not intentionally change secret values. When each object is written, the Kubernetes API server encrypts it using the active KMS provider version 2 configuration.
- 

Monitor the migration and wait for it to succeed:

```

```

A successful command returns output similar to the following:
```

```

The timeout controls how long`kubectl`waits for the condition. Reaching the timeout does not cancel a migration that is still running.

## Verifying the Migration

To confirm that the migration completed successfully:
- 

Get the migration status:

```

```

- 

In the`status.conditions`list, confirm that the`Succeeded`condition has a value of`True`, similar to the following:
```

```

The successful status confirms that Kubernetes rewrote the secret objects. For a cluster that uses a master encryption key you manage and is running Kubernetes version 1.36.1 or later, the rewritten objects are encrypted using KMS provider version 2.

After confirming that the migration succeeded, you can delete the completed migration resource:

```

```

You can also delete the local`migrate-secrets-to-kms-v2.yaml`file.

Deleting the`StorageVersionMigration`resource does not undo the migration and does not delete any Kubernetes secret objects.

## Troubleshooting KMS v2 Migration

### The Storage Version Migration API Is Not Listed

If the`kubectl api-resources`command does not list the`storageversionmigrations`resource, confirm that:
- `kubectl`is using the context for the intended cluster.
- The`Server Version`reported by`kubectl version`is`v1.36.1`or later.
- The control plane upgrade completed successfully.

The Kubernetes versions running on worker nodes do not determine whether the migration API is available.

If all these conditions are met and the API remains unavailable, contact Oracle Support. Do not attempt to use a different bulk-rewrite procedure.

### The Migration Cannot Be Created

If the`kubectl create`command returns a`Forbidden`error, confirm that your Kubernetes identity can create the migration resource:

```

```

If the command returns`no`, ask a cluster administrator to perform the migration or grant the required Kubernetes RBAC permissions.

If the`kubectl create`command returns an`AlreadyExists`error, inspect the existing migration:

```

```

If the existing migration completed successfully and you want to run a new migration, delete the completed`StorageVersionMigration`resource before creating it again.

### The Migration Does Not Succeed

Inspect the migration status and associated events:

```

```

If the`Failed`condition is`True`, or if the migration remains incomplete, retain the command output and contact Oracle Support.
