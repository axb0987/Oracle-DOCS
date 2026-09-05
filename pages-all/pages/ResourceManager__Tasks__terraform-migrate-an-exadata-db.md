# Migrating an Exadata DB System to the New Resource Model
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/terraform-migrate-an-exadata-db.htm
- Fetched: 2026-09-05 02:56 CDT

# Migrating an Exadata DB System to the New Resource Model

Use Resource Manager and Terraform configurations to migrate an Exadata DB system to the new Exadata resource model.

The X8M generation of Exadata hardware introduces a new resource model that replaces the Exadata DB system. The new resource model uses new APIs to provision and manage its resources. The existing DB system APIs for Exadata will be deprecated by Oracle Cloud Infrastructure for all users following written notification and a transition period allowing you to switch to the new API and Console interfaces.

If you have existing Exadata DB systems in Oracle Cloud Infrastructure, you can use Terraform to switch them to the new resource model and APIs.
Caution  
  
Switching an Exadata DB system to the new resource model and APIs can't be reversed. If you have automation for your system that utilizes the DB system APIs, you might need to update your applications before switching.

Switching to the new resource model:
- Doesn't impact the DB system's existing Exadata databases or client connections
- Doesn't change the underlying hardware or shape family of your Exadata Cloud Service instance
- Won't affect bare metal and virtual DB systems

After converting your DB system, you'll have two new resources in place of the DB system resource: a cloud Exadata infrastructure resource, and a cloud VM cluster resource.

What to expect after switching:
- Your new cloud Exadata infrastructure resource and cloud VM cluster are created in the same compartment as the DB system they replace
- Your new cloud Exadata infrastructure resource and cloud VM cluster use the same networking configuration as the DB system they replace
- After the switch, you can't perform operations on the old Exadata DB system resource
- Switching is permanent, and the change can't be undone
- X6, X7, X8 and Exadata base systems retain their fixed shapes after the switch, and can't be expanded

See[Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/iaas/exadatacloud/index.html)for more information.

## To Migrate an Exadata DB System

These migration steps use the following example, which shows an existing Exadata Cloud Service instance using the old DB system resource model:
```

```

To migrate the system to the new resource model, first create the`oci_database_migration`resource:
```

```

Provisioning the`oci_database_migration`resource creates two new resources:`oci_database_cloud_exadata_infrastructure`and`oci_database_cloud_vm_cluster`.

You can get OCIDs of these two resources from the`oci_database_migration`resource:
```

```

Create a Terraform configuration for the two new resources:
```

```

Then run the Terraform import command:
```

```

Terraform now manages the two new resources. After switching to the new Exadata resource model, remove the old`oci_database_db_system`config.
Tip  
  
After the migration, you can use[resource discovery](https://docs.oracle.com/iaas/Content/dev/terraform/resource-discovery.htm)
