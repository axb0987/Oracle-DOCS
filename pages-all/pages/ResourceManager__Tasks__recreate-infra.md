# Recreating Infrastructure from an Existing Compartment
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/recreate-infra.htm
- Fetched: 2026-09-05 02:56 CDT

# Recreating Infrastructure from an Existing Compartment

Using resource discovery in Resource Manager, re-create existing infrastructure from an existing compartment.

For more information about resource discovery, see[Resource Discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/resource-discovery.htm).

The following high-level instructions show how to re-create infrastructure from an existing compartment. To access detailed steps, select the provided links.

- [Create a stack from the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm)that contains the resources you want to re-create.
- [Download](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm)the generated Terraform configuration file.
- Edit the`vars.tf`file (variables in the downloaded Terraform configuration file) to specify the destination`compartment_ocid`and`region`.

Example:

```

```

- If the destination region has more or fewer availability domains than the source region, then edit the`vars.tf`file to specify the correct number of[availability domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).

For example, if you cloned from a region that has 3 availability domains and you want to re-create the infrastructure in a region that has only 1 availability domain, then remove the references to the second and third availability domains.

Example showing 3 availability domains:
```

```

Example showing 1 availability domain:
```

```

- Store the edited configuration file in the location that you want to reference when creating the second stack.
You can store a configuration file in a zip file, folder, Git repository, or other location supported by Resource Manager for creating stacks. See[Where to Store Your Terraform Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Concepts/terraformconfigresourcemanager.htm#sources).
- [Create](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack.htm)a second stack using the edited configuration file.
- (Optional) Run a[plan job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm)on the new stack.
- Run an[apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)on the new stack.
