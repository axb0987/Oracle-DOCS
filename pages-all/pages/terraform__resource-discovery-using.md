# Using Resource Discovery
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/resource-discovery-using.htm
- Fetched: 2026-09-05 19:20 CDT

# Using Resource Discovery

Discover deployed OCI resources using the Terraform provider.

The OCI Terraform provider's resource discovery feature uses HashiCorp's[terraform-exec](https://github.com/hashicorp/terraform-exec/)to import the discovered OCI resources into Terraform configuration and state files.

## Prerequisites

Terraform-exec requires the Terraform CLI to be present on your system. See[Download and Install Terraform](https://docs.oracle.com/iaas/Content/dev/terraform/installing.htm#download-terraform)for installation details.
Note  
  

If you are using Terraform version v0.11, this tool cannot generate a state file. Only configurations are supported in v0.11. By default the configurations are generated in v0.12.

If you use v0.13.* of the Terraform CLI, make sure that the version is compatible with v0.12 syntax.

Additionally, you must have the OCI Terraform provider downloaded and installed. See[Download and Install the Provider](https://docs.oracle.com/iaas/Content/dev/terraform/installing.htm#download-provider)for download instructions.

### Adding the Tools to Your Path

To run the OCI Terraform provider as an executable and[use resource discovery](https://docs.oracle.com/iaas/Content/dev/terraform/resource-discovery-using.htm), you can:
- Add`terraform-provider-oci`to your system path.
- Run the provider from the directory where it is located.
- Specify the full path to the provider when you run resource discovery commands.

Because resource discovery commands use terraform-exec to call Terraform on your behalf, your system must specify the location of the Terraform CLI using either of the following methods:
- Provide the full path including name for the Terraform CLI using the`terraform_bin_path`environment variable. See[Environment Variables](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#environment-variables)for more information on setting variables.
- Add the Terraform CLI to your system path.

### Authentication

To discover resources in your compartment, the OCI Terraform provider needs authentication information about the user, tenancy, and region with which to discover the resources. It is recommended that you specify a user that has access to inspect and read the resources to discover.

You can use[API Key Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#api-key-auth)and[Environment Variables](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#environment-variables)or[Instance Principal Authorization](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#instance-principal-auth)to provide the required information.

## Exporting Resources

After you have specified the location of the Terraform CLI and authentication settings, either of the following commands can be used to export a compartment's resources:

```

```

```

```

These commands discover all supported resources within the compartment and generate Terraform configuration files in the provided`output_path`. The generated`.tf`files contain the Terraform configuration with the resources that the command has discovered.
Caution  
  
Ensure that the`output_path`is empty before running resource discovery.
Note  
  
The`compartment_id`parameter is required if using[Instance Principal Authorization](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#instance-principal-auth).

The following common parameter combinations export the resources described:
- `compartment_id= <empty_or_tenancy_OCID> services= <empty_or_not_specified>`- All tenancy and compartment scope resources.
- `compartment_id= <empty_or_tenancy_OCID> services= <comma_seperated_list>`- Tenancy and compartment scope resources for the services specified.
- `compartment_id= <non-root_OCID> services= <empty_or_not_specified>`- All compartment scope resources.
- `compartment_id= <non-root_OCID> services= <comma_seperated_list>`- Compartment scope resources for the services specified. Tenancy scope resources aren't discovered even if services with such resources are specified.
Note  
  
Export of compartment resources supports only the target compartment. Resources in child compartments aren't discovered.

### Parameters

You can use the following parameters to control the behavior of the resource discovery tool.

Parameter Details
`command`The command to run. Supported commands include:
- `export`- discovers OCI resources within the compartment and generates Terraform configuration files for them
- `list_export_resources`- lists the Terraform OCI resource types that are discovered by the`export`command
- `list_export_services`- lists the allowed values for services arguments along with scope in JSON format
`compartment_id`The OCID of the compartment to export. If`compartment_id`or`compartment_name`isn't specified, the root compartment is used. Required if using[Instance Principal Authorization](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#instance-principal-auth).
`compartmet_name`The name of a compartment to export. If`compartment_id`or`compartment_name`isn't specified, the root compartment is used.
`exclude_services`A comma-separated list of service resources to exclude from the export. Any service present in both`services`and`exclude_services`argument is excluded.
`filter`Filter discovered resources by specified criteria. For more information, see[Filtering Resources](https://docs.oracle.com/iaas/Content/dev/terraform/resource-discovery-using.htm#filter).
`generate_state`Provide this flag to[import the discovered resources into a state file](https://docs.oracle.com/iaas/Content/dev/terraform/resource-discovery-using.htm#state)in addition to the Terraform configuration files.
`ids`A comma-separated list of tuples`< resource_type : resource_ID >`(for example,`oci_core_instance:ocid.....`) for resources to export. The ID could either be an OCID or a Terraform import ID. By default, all resources are exported.
`list_export_services_path`The full path, including the filename, to use as the output for list of supported services, in JSON format.
`output_path`The absolute path to output the generated configurations and state files of the exported compartment.
`parallelism`The number of threads to discover resources in parallel. The default value is`1`.
`retry_timeout`The time duration in seconds for which API calls wait and retry the operation in case of API errors. By default, the retry timeout duration is 15 seconds.
`services`A comma-separated list of service resources to export. If not specified, all resources within the provided compartment (excluding IAM resources) are exported.

See[Supported Services](https://docs.oracle.com/iaas/Content/dev/terraform/resource-discovery.htm#supported-services)for accepted values and[Exporting Identity Resources](https://docs.oracle.com/iaas/Content/dev/terraform/resource-discovery-using.htm#identity-export)for related information.
`tf_version`The version of Terraform syntax to use when generating configuration files. The default is v0.12. The allowed values are:
- `0.11`
- `0.12`

If you specify`0.11`as the syntax version, use v0.11 of the Terraform CLI to discover resources.

If you use Terraform CLI v0.13 and greater to discover resources, ensure that the version is compatible with v0.12 syntax. State files are generated in Terraform syntax matching the[version of the Terraform CLI](https://docs.oracle.com/iaas/Content/dev/terraform/resource-discovery-using.htm#prerequisites)used to discover resources. The`tf_version`parameter doesn't apply to state files.
`variables_global_level`

List top-level attributes to export as variables, following the format`attribute1,attribute2`. Resource-level attributes (`variables_resource_level`) are excluded from this list.
`variables_resource_level`

List resource-level attributes to export as variables, following the format`resourceType.attribute`. Top-level attributes (`variables_global_level`) are excluded from this list.

### Filtering Resources

Filter discovered resources by specified criteria:
- 

Resource type filter:`Type <operator> <provider-resource-type>`

&lt;operator&gt; is either`=`(equal to) or`!=`(not equal to)
- Attribute filter:`AttrName= <attribute-name> ;Value <operator> <value>`Find all resources with matching attribute and value
- Up to 10 filters (resources must satisfy all) Resource type filter: VCN only
```

```
Resource type filter: Anything but VCN
```

```
Attribute filter: Defined tag value
```

```
Multiple filters: VCN only, must have dns_label attribute set to test
```

```

For more information about filtering discovered resources, see[Filtering Resources discovered via Resource Discovery](https://registry.terraform.io/providers/oracle/oci/latest/docs/guides/resource_discovery#filtering-resources-discovered-via-resource-discovery).

### Verbose Logging

To get verbose console output when the provider is running, precede the resource discovery command with the`TF_LOG`or`OCI_TF_LOG`flags. For example:

```

```

```

```

The[`TF_LOG`](https://www.terraform.io/docs/internals/debugging.html)level and`OCI_TF_LOG`flags can also be set as environment variables.

To redirect verbose console output to a log file, set the`OCI_TF_LOG_PATH`environment variable and provide the path.

### Exit Status

For any error related to the OCI APIs or service unavailability while discovering resources, the tool moves on to find next resource. All errors encountered are displayed after the discovery is complete.
- Exit code`0`- Success.
- Exit code`1`- Failure because of errors such as incorrect environment variables, arguments, or configuration.
- Exit code`64`- Partial success. Resource discovery was not able to find all the resources because of service failures.

## Exporting Identity Resources

Some resources, such as identity resources, exist only at the tenancy level and cannot be discovered within a specific compartment. To discover such resources, use the following command, which omits any compartment parameter:

```

```

Note  
  
When exporting identity resources, the`compartment_id`value, if provided, is ignored.

## Exporting Resources to Another Compartment

Once you have reviewed the generated Terraform configuration files and made any necessary changes, the configuration can be used with Terraform. One such use case is the re-deploying of those resources in a new compartment or tenancy, using Terraform.

To do so, specify the following environment variables:

```

```

Then run the following command:
```

```

## Generating a Terraform State File

Caution  
  
The state file contains all resource attributes that are specified as part of configuration files. If you manage any sensitive data with Terraform, such as database or user passwords or instance private keys, treat the state file itself as sensitive data. See[Storing Sensitive Data](https://docs.oracle.com/iaas/Content/dev/terraform/storing-sensitive-data.htm)for more information.

It is also possible to generate a Terraform state file to manage the discovered resources. To do so, run the following command, which includes the`-generate_state`flag:

```

```

The results of this command are both the`.tf`files representing the Terraform configuration and a`terraform.tfstate`file representing the state. See[State](https://www.terraform.io/docs/state/index.html)for more information.
Note
