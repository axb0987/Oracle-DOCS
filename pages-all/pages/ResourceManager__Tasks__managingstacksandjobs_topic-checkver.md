# Checking the OCI Terraform Provider Version
- Source: https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingstacksandjobs_topic-checkver.htm
- Fetched: 2026-09-05 02:56 CDT

# Checking the OCI Terraform Provider Version

Verify the version of the OCI Terraform provider used by Resource Manager in the current region.

Note  
  
You can also check this version using a Terraform command. For instructions, see[Checking the Terraform and OCI Terraform Provider Versions](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#basics__provider-version).

The OCI Terraform provider documentation reflects the[latest version](https://github.com/oracle/terraform-provider-oci/releases). You can view documentation for earlier provider versions by visiting the[Terraform Registry](https://registry.terraform.io/providers/oracle/oci/latest/docs)and selecting a specific version.

- On the Stacks list page, select the stack that you want to work with. If you need help finding the list page or the stack, see[Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/../Tasks/list-stacks.htm).
- On the stack's details page, select Plan .

The plan job automatically includes the version of OCI Terraform provider in its log.

You can alternatively run an apply job, which also includes this version information in its log.
The Plan panel opens.
- (Optional) Update the job name.
- Select Plan .
A plan job starts. The new plan job is listed under Jobs . When the job is complete, the Job details page opens, with the log listed.
- On the Job details page, view the provider version listed in the job log.

To access the job log from this page, select Logs under Resources .

Example provider version:
```

```
