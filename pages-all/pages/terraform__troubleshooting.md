# Troubleshooting the Terraform Provider
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm
- Fetched: 2026-09-05 19:21 CDT

# Troubleshooting the Terraform Provider

Troubleshoot common OCI Terraform provider issues.
Tip  
  
See also[Known Issues for Terraform Provider](https://docs.oracle.com/iaas/Content/dev/terraform/known-issues.htm).

Start with[Troubleshooting Basics](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#basics)and then see the following guidance:
- [Common Issues](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#common_issues)
- [Terraform CLI Issues](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#terraform-cli-issues)
- [Terraform Provider Issues](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#terraform-provider-issues)
- [Service API Errors](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#terraformtroubleshooting_topic_Service_Errors)

## Troubleshooting Basics

When troubleshooting or getting support for the OCI Terraform provider, it's often useful to first check the status of the OCI services, the version of Terraform and the provider, and enable and collect verbose logging.
Tip  
  
Checking service status and verbose log output can help you determine whether an issue is related to the Terraform provider or the OCI service the provider is using.

See the[list of common issues](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#common_issues)after you start with the basics.

### Checking OCI Service Status and Outages

To check on the latest status and whether there are any outages in OCI, see[OCI Status](https://ocistatus.oraclecloud.com/).

### Checking the Terraform and OCI Terraform Provider Versions

To verify the version of Terraform and the OCI Terraform provider, initialize Terraform from a directory with your configurations and then run the`-version`command. For example:

```

```

```

```

The versions are displayed:
```

```

Tip  
  
Newer versions of the OCI Terraform provider include the version of the provider in error messages.

The OCI Terraform provider documentation reflects the[latest version](https://github.com/oracle/terraform-provider-oci/releases). You can also[download and install a specific version of the provider](https://docs.oracle.com/iaas/Content/dev/terraform/installing.htm#download-provider).

### Verbose Logging for OCI Terraform Provider

To get verbose console output when the provider is running, precede your Terraform command with the`TF_LOG`and`OCI_GO_SDK_DEBUG`flags. For example:

```

```

The[`TF_LOG`](https://www.terraform.io/docs/internals/debugging.html)level and`OCI_GO_SDK_DEBUG`flags can also be set as environment variables.

## Automatic Retries

While applying, refreshing, or destroying a plan, Terraform might encounter some intermittent OCI errors (such as 409, 429 or 500 errors) that could succeed on retry. By default, the OCI Terraform provider automatically retries such operations for up to 2 minutes or 10 minutes but with a maximum of 9 retries.
Note  
  

- We recommend[using the`retries_config_file`option](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#retries-config-file)for better retry control, including individual error code configuration and the`first_retry_sleep_duration`parameter for a delayed first retry.
- [`retries_config_file`](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#retries-config-file)takes precedence over`disable_auto_retries`or`retry_duration_seconds`.
- Limit use of[`retry_duration_seconds`](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#retry-duration-seconds)to errors that succeed after retry only, such as 409, 429, and 500. Don't use`retry_duration_seconds`for errors that are unlikely to succeed after retry, such as 400, 401, 403, 404, 412, and 413.

Retry configuration options:
- [Using retries_config_file](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#retries-config-file)(recommended)
- [Using retry_duration_seconds](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#retry-duration-seconds)

### Using retries_config_file

Use this retry configuration option to individually configure retriable errors, such as 409, 429, and 500.

The following field can be specified in the`provider`block to further configure the retry behavior:

`retries_config_file`- A JSON file path with an individual retry configuration for each recoverable error code in the following format:
```

```

Parameter descriptions:
- `retry_max_duration`- Maximum duration for retries, in seconds. The maximum number of retries is 9.

For example, the value`120`allows retries only until 120 seconds have passed from the first attempt (assuming that the maximum number of retries hasn't been exceeded).

If you expect the error code to exceed the maximum number of retries (9) within the specified duration, then also configure`first_retry_sleep_duration`.

To disable retries for an error code, set the value to`0`(zero).
- `first_retry_sleep_duration`- Time to wait for the first retry, in seconds.

The first retry is the second attempt. (The first attempt in this case is expected to return the specified error code.)

For example, the value`60`waits 60 seconds after the first attempt to retry.

Example configuration:
```

```

In this example, the error`409`is expected to exceed the maximum number of retries (9), so its configuration includes both`retry_max_duration`(120 seconds maximum duration) and`first_retry_sleep_duration`(60 seconds before next retry). This configuration delays the first retry, helping to avoid exceeding the maximum within the specified duration.

### Using retry_duration_seconds

Use this retry configuration option for 429 and 500 errors only.

The following fields can be specified in the`provider`block to further configure the retry behavior:
- `disable_auto_retries`- Disable automatic retries for retriable errors.
- `retry_duration_seconds`- The minimum duration (in seconds) to retry a resource operation in response to HTTP 429 and HTTP 500 errors. The actual retry duration might be slightly longer because of jittering of retry operations. This value is ignored if the`disable_auto_retries`field is set to`true`.

## Concurrency Control Using Retry Backoff and Jitter

To alleviate contention between parallel operations against OCI services; the OCI Terraform provider schedules retry attempts using quadratic backoff and full jitter. Quadratic backoff increases the maximum interval between subsequent retry attempts, while full jitter randomly selects a retry interval within the backoff range.

For example, the wait time between the first and second retry attempts is chosen randomly between 1 and 8 seconds. The wait time between the second and third retry attempts is chosen randomly between 1 and 18 seconds. Regardless of the number of retry attempts, the retry interval time is capped after the 12th attempt at 288 seconds.

## Common Issues

Note  
  
See[Known Issues for Tagging](https://docs.oracle.com/iaas/Content/Tagging/Tasks/knownissues_tagging.htm)for a known issue with tags related to Terraform.

### Resources Are Destroyed When Applying Changes

Existing OCI resources might be destroyed and re-created when Terraform configurations attempt to update a resource property that is not updatable. Terraform warns you when changes will destroy a resource. Always run`terraform plan`before applying changes to see what resources will be affected. See[Destructive Changes](https://docs.oracle.com/iaas/Content/dev/terraform/applying.htm#destructive-changes)for more information.

### Dependent Resource Cannot Be Updated

Sometimes, an update to an OCI resource should force the resource to be destroyed and re-created, but another resource's dependency on the resource disallows the operation.

For example, you might want to make an update to an`oci_core_instance_configuration`resource, but an instance pool uses that instance configuration. The instance configuration cannot be deleted because the instance pool references it in a required argument.

To work around this type of behavior, you can use the`lifecycle`and`create_before_destroy`meta-arguments in the resource block.

In this example, Terraform creates a second`oci_core_instance_configuration`resource that includes your updates, then assigns the new instance configuration to the related instance pool. Finally, Terraform destroys the original instance configuration. For example:
```

```

See[The`lifecycle`Meta-Argument](https://www.terraform.io/docs/language/meta-arguments/lifecycle.html)and[Destructive Changes](https://docs.oracle.com/iaas/Content/dev/terraform/applying.htm#destructive-changes)for more information.

### Resource Cannot Be Destroyed or Updated

You can prevent an OCI resource from being destroyed by including the`lifecycle`and`prevent_destroy = true`meta-arguments in the resource block of your Terraform configuration file. The following configuration, for example, results in an Object Storage bucket that cannot be destroyed:
```

```

This meta-argument prevents the use of`terraform destroy`. Because certain configuration updates require resources to be destroyed before they can be applied, this setting can make some updates impossible to apply as well. In this example,`name`is a property that cannot be updated without destroying and re-creating the resource. Therefore, you cannot update the name of the bucket without removing or changing the`lifecycle`meta-argument.

See[The`lifecycle`Meta-Argument](https://www.terraform.io/docs/language/meta-arguments/lifecycle.html)for more information.

### Resource Argument Cannot Be Unset

Many Oracle Cloud Infrastructure resources managed by the OCI Terraform provider accept configuration arguments that are optional. Once set, whether during resource creation or a subsequent update, these arguments cannot be unset by passing an empty string or removing the argument from the configuration. Attempts to unset these arguments are ignored by Terraform.

The full reference of the OCI Terraform provider's supported resources and data sources contains usage, argument, and attribute details. The full reference is available at[docs.oracle.com](https://docs.oracle.com/iaas/tools/terraform-provider-oci/latest/)and[Terraform Registry](https://registry.terraform.io/providers/oracle/oci/latest/docs). For releases of the OCI Terraform Provider, see[oracle/terraform-provider-oci](https://github.com/oracle/terraform-provider-oci/releases).

Data sources and resources are grouped by service within the reference.

### Referencing Triggers in Lifecycle Meta-arguments

Terraform v0.14 and later might require that you replace global variables in your configuration files with a combination of local variables and triggers. To reference a trigger in`lifecycle`and`ignore_changes`meta-arguments and avoid executing the configuration on subsequent Terraform apply operations, reference the trigger as follows:
```

```

### Cannot Delete Compartment

By default, the Terraform provider does not delete a compartment when using the`destroy`command.

You must set the`enable_delete`argument to`true`for the provider to attempt to delete the compartment. For example:
```

```

Note  
  
To destroy a compartment, the compartment must also be empty. Use the`depends_on`argument to ensure that any hidden dependencies are defined. See[Resources](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm#resources)for more information.

### "Operation Timeout" Error

If the Terraform CLI returns an error message like the following:
```

```

Then the specified OCI service is indicating that the resource has not yet reached the expected state after polling for some time.

You may need to increase the operation timeout for your resource to continue polling for longer. See[Operation Timeouts](https://www.terraform.io/docs/configuration/blocks/resources/syntax.html#operation-timeouts)for details on how to do this.

### "Unexpected LifeCycle state" Error

If the Terraform CLI returns an error message like the following:
```

```

Then the specified OCI service encountered an unknown error. Retry, or contact support regarding that service.

## Terraform CLI Issues

This section contains information dealing with the installation and configuration of the Terraform CLI.

### "No such file" Error After Upgrading the OCI Terraform Provider

If the Terraform CLI returns an error message like the following:
```

```

You are likely using a version of the OCI Terraform provider that is not compatible with the Terraform binary you have installed. For OCI Provider versions v3.x.x and above, a minimum Terraform version of v.0.10.1 is required.

### "TCP...i/o timeout" Message When Connecting Via Proxy

If the Terraform CLI returns an error message like the following:
```

```

Then you may not have properly configured your proxy settings. The OCI Terraform provider supports`http_proxy`,`https_proxy`and`no_proxy`variables where the inclusion or exclusion lists can be defined as follows:
```

```

### "x509: certificate signed by unknown authority" Error Message

If the Terraform CLI returns an error message like the following:
```

```

Ensure that Terraform is using trusted TLS certificates and the certificate chain is valid. For more information, see["x509: certificate signed by unknown authority" from Terraform CLI with a Terraform Enterprise remote](https://support.hashicorp.com/hc/en-us/articles/4415187888019--x509-certificate-signed-by-unknown-authority-from-Terraform-CLI-with-a-Terraform-Enterprise-remote).

### "Outdated GPG key...unable to verify new provider releases" Error Message

If the Terraform CLI returns an error message like the following:
```

```

This message means that the Terraform registry is omitting the Terraform provider versions signed by a new GPG key. The Terraform CLI will install the last version of the OCI Terraform provider that it can successfully verify, which might not be the latest version.

To remove this message and ensure you can use the latest version of the OCI Terraform provider,[upgrade the Terraform CLI](https://docs.oracle.com/iaas/Content/dev/terraform/installing.htm)to the latest maintenance release available for the major Terraform version you are using. For example, if you are using Terraform v0.12.21, upgrade to the lastest available version of v0.12.

## Terraform Provider Issues

This section contains information related to the installation and configuration of the OCI Terraform provider.

### "NotAuthenticated" Error When Using Modules

If you are using modules and the Terraform CLI returns an error message like the following:
```

```

Verify that each module declares its own provider requirements. For more information, see[Providers Within Modules](https://developer.hashicorp.com/terraform/language/modules/develop/providers).

### "NotAuthenticated" Error When Using Terraform

Symptom: The Terraform CLI returns an error message such as the following:
```

```

Possible causes: Incorrect configuration.

Resolution: Verify the following.
- Correctly configured attributes:
- `user_ocid`
- `tenancy_ocid`
- `fingerprint`
- `private_key_path`- verify that it's pointing to a private key, and not the corresponding public key.
- The public key corresponding to`private_key_path`was added to the user account specified as`user_ocid`.
- The public and private key pairs use the correct format. For details, and for steps to generate keys, see[Required Keys and OCIDs](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm).
- The user account is part of a group with the appropriate permissions to perform the actions in the plan you're executing.
- The tenancy is subscribed to the region targeted in the plan.
- If you're using modules, verify that each module declares its own provider requirements. For more information, see[Providers Within Modules](https://developer.hashicorp.com/terraform/language/modules/develop/providers).

### "Can not create client, bad configuration: did not find a proper configuration for tenancy" Message When Using Aliases

If the Terraform CLI returns a message like this, it might indicate an issue with your environment:
```

```

If your provider configuration includes an alias, your resources should explicitly specify the provider alias using`provider = "oci.alias_name"`. If a resource does not use the alias to specify the provider, Terraform creates a default provider to use with such resources. The default provider loads configuration values from environment variables or the`~/.oci/config`file. These values may differ from those used by your aliased provider and cause the configuration error.

Either remove the alias in your provider configuration, or ensure that every resource specifies the provider by the proper alias. Read more about using`alias`in the[official Terraform documentation](https://www.terraform.io/docs/configuration/providers.html), and see[Configuring the Provider](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm)for more information about how Terraform uses environment variables and the OCI config file.

### "Field cannot be set" Error Message

If the Terraform CLI returns an error message like the following:
```

```

You are likely using an older version of the OCI Terraform provider and the field you are trying to set was released in a later version. Use the following command to check your Terraform provider version.
```

```

The OCI Terraform provider documentation reflects the[latest version](https://github.com/oracle/terraform-provider-oci/releases).

### "Could not get info about the first DbHome in the dbSystem" Error Message When Importing db_home

If the`oci_database_db_system`being imported is missing a primary`db_home`, an empty placeholder for`db_home`is set in the Terraform state file. To keep configurations consistent with the imported state, add an empty placeholder for`db_home`to your configuration. For example:
```

```

The full reference of the OCI Terraform provider's supported resources and data sources contains usage, argument, and attribute details. The full reference is available at[docs.oracle.com](https://docs.oracle.com/iaas/tools/terraform-provider-oci/latest/)and[Terraform Registry](https://registry.terraform.io/providers/oracle/oci/latest/docs). For releases of the OCI Terraform Provider, see[oracle/terraform-provider-oci](https://github.com/oracle/terraform-provider-oci/releases).

Data sources and resources are grouped by service within the reference.

### "Failed to query available provider packages" Error Message When Running Resource Discovery

If the Terraform CLI returns an error message like the following when[using resource discovery](https://docs.oracle.com/iaas/Content/dev/terraform/resource-discovery-using.htm):
```

```

Then you can ensure that Terraform uses an existing local provider binary by specifying its location using the`provider_bin_path`environment variable. For example:
```

```

Terraform attempts to download the latest version of the OCI Terraform provider when you use resource discovery.

### Default Tags Deleted on Apply

Sometimes, the OCI Terraform provider can unexpectedly delete existing[tag defaults](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagdefaults.htm)from a resource when running`terraform apply`. This issue affects the`Oracle-Tags`automatic tag defaults in particular.

To work around this issue, you can add the`ignore_defined_tags`attribute to your provider block.

The`ignore_defined_tags`attribute allows you to list out the keys of the defined tags that Terraform will ignore as part of plan or apply. The`ignore_defined_tags`attribute can only be specified at the provider level, and has a maximum allowed size of 100. The tags provided in this attribute are ignored for all the resources in that Terraform file.

In the following example, "Oracle-Tags.CreatedOn" and "Oracle-Tags.CreatedBy" are the keys in the`defined_tags`map associated with a remote resource:
```

```

For more information, see[Provider Definitions](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm#provider-definitions)and refer to the[related GitHub issue](https://github.com/oracle/terraform-provider-oci/issues/1283).

## Service API Errors

Because the Terraform provider interacts with OCI services on your behalf, many error messages surfaced by the Terraform provider come directly from OCI services. The[API Errors](https://docs.oracle.com//iaas/Content/API/References/apierrors.htm)reference lists common errors returned by all services.

Service error messages returned by the OCI Terraform provider include the following information:
- Error - the HTTP status code and error code (see[API Errors](https://docs.oracle.com//iaas/Content/API/References/apierrors.htm))
- Provider version - the version of the OCI Terraform provider used to make the request
- Service - the OCI service responding with the error
- Error message - details regarding the error returned by the service
- OPC request ID - the request ID
- Suggestion - suggested next steps

For example:
```

```

This section details a few of the more commonly returned service errors.

### "400-InvalidParameter" Error

If the Terraform CLI returns an error message like the following:
```

```

Update the parameter specified in the error message in the Terrform configuration for the resource.

The full reference of the OCI Terraform provider's supported resources and data sources contains usage, argument, and attribute details. The full reference is available at[docs.oracle.com](https://docs.oracle.com/iaas/tools/terraform-provider-oci/latest/)and[Terraform Registry](https://registry.terraform.io/providers/oracle/oci/latest/docs). For releases of the OCI Terraform Provider, see[oracle/terraform-provider-oci](https://github.com/oracle/terraform-provider-oci/releases).

Data sources and resources are grouped by service within the reference.

### "400-LimitExceeded" Error

While using Terraform, you might encounter errors indicating that you have reached or exceeded the service limits for a resource. For example:
```

```

To understand more about OCI service limits and how to request a limit increase, see[Limits by Service](https://docs.oracle.com/iaas/Content/General/service-limits/default.htm)

### "404-NotAuthorized" Error

If the Terraform CLI returns an error message like the following:
```

```

Verify the user account is part of a group with the appropriate permissions to perform the actions in the plan you are executing. Refer to the policy reference for your service for more information.

### "500-InternalError" Error

If the Terraform CLI returns an error message like the following:
```

```

The service responded to the request from the Terraform provider with an internal error. If you[contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)
