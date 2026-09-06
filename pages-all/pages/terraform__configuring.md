# Configuring the Provider
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm
- Fetched: 2026-09-05 19:20 CDT

# Configuring the Provider

Configure the OCI Terraform provider with the required authentication and optional environment variables.
Note  
  
For examples of Terraform configuration files for creating specific resources, see[Terraform Oracle Cloud Infrastructure Provider Examples](https://github.com/oracle/terraform-provider-oci/tree/master/examples).

## Authentication

To interact with the Oracle Cloud Infrastructure (OCI) services and supported resources, configure the OCI Terraform provider with authentication credentials for an OCI account.

The OCI Terraform provider supports four authentication methods:
- [API Key Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#api-key-auth)(default)
- [Instance Principal Authorization](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#instance-principal-auth)
- [Resource Principal Authorization](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#resource-principal-auth)
- [Security Token Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#security-token-auth)
- [OKE Workload Identity Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#oke-auth)

### API Key Authentication

By default, the Terraform provider uses API Key authentication, but you can specify this explicitly by setting the`auth`attribute to "APIKey" in the provider definition. Calls to OCI using API Key authentication require that you provide the following credentials:
- `tenancy_ocid`- OCID of the tenancy. To get the value, see[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).
- `user_ocid`- OCID of the user calling the API. To get the value, see[Where to Get the Tenancy's OCID and User's OCID](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#five).
- `private_key`- The contents of the private key file. Required if`private_key_path`isn't defined, and takes precedence over`private_key_path`if both are defined. For details on how to create and configure keys see[How to Generate an API Signing Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#two)and[How to Upload the Public Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#three).
- `private_key_path`- The path (including filename) of the private key stored on the computer. Required if`private_key`isn't defined. For details on how to create and configure keys see[How to Generate an API Signing Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#two)and[How to Upload the Public Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#three).
- `private_key_password`- (Optional) Passphrase used for the key, if it's encrypted.
- `fingerprint`- Fingerprint for the key pair being used. To get the value, see[How to Get the Key's Fingerprint](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#four).
- `region`- An OCI region. See[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
- `config_file_profile`- The profile name if you would like to use a custom profile in the OCI config file to provide the authentication credentials. See[Using the SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#sdk-cli-config-file)for more information.

For example, provide these values as either[environment variables](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#environment-variables)or inside[Terraform configuration variables](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm#provider-definitions).

### Instance Principal Authorization

Note  
  
Instance principal authorization applies only to instances that are running in Oracle Cloud Infrastructure.

Use instance principal authorization to remove requirements for the following attributes in the provider definition:
- `tenancy_ocid`
- `user_ocid`
- `private_key_path`
- `fingerprint`

When instance principal authorization is enabled, the provider can make API calls from a compute instance without these attributes.

To enable instance principal authorization for OCI Terraform providers, set the`auth`attribute to "InstancePrincipal" in the provider definition, as shown in the following example:
```

```

For more information, see[Calling Services from an Instance](https://docs.oracle.com/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm).

### Resource Principal Authorization

Resource principal authorization, such as instance principal authorization, allows the provider to make API calls without needing to provide credentials within the provider definition. Resource principal authorization is used to allow resources such as a running function to access other Oracle Cloud Infrastructure resources. For more information, see[Accessing Other Oracle Cloud Infrastructure Resources from Running Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm).

To enable resource principal authorization for OCI Terraform providers:
- Create the dynamic group and policies required for the running function to manage other OCI resources. Follow the instructions in Using the Console under[Accessing Other Oracle Cloud Infrastructure Resources from Running Functions](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsaccessingociresources.htm)and ensure that the policy allows management of other resources.
- 

Set the following[environment variables](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#environment-variables):
- 

`OCI_RESOURCE_PRINCIPAL_VERSION`, containing the value`2.2`.

When the value is`1`, region override isn't supported.
- 

`OCI_RESOURCE_PRINCIPAL_RPST`, containing the raw contents of the`rpst`file or the absolute path to the`rpst`file, including the filename.
- 

`OCI_RESOURCE_PRINCIPAL_PRIVATE_PEM`, containing the absolute path to the`private.pem`file (including the filename).
- 

`OCI_RESOURCE_PRINCIPAL_REGION`, containing the region identifier in which the provider is deployed (for example,`us-phoenix-1`).
- 

Set the`auth`attribute to "ResourcePrincipal" in the provider definition.
Note  
  

The value for`region`in the provider block overrides the region value set by the environment variable`OCI_RESOURCE_PRINCIPAL_REGION`. This change, introduced in Terraform Provider version 5.0.0, isn't downward-compatible.

When the value of the`OCI_RESOURCE_PRINCIPAL_VERSION`environment variable is`1`, region override isn't supported.

Example:
```

```

### Security Token Authentication

Run Terraform using a token generated with[Token-based Authentication for the CLI](https://docs.oracle.com/iaas/Content/API/SDKDocs/clitoken.htm). To enable Security Token authentication, update the provider definition as follows:

- Set the`auth`attribute to`SecurityToken`.
- Provide a value for`config_file_profile`.
- Set the`region`.

For example:
```

```

Important  
  
This token expires after one hour. Avoid using this authentication method when provisioning of resources takes longer than one hour. For more information, see[Refreshing a Token](https://docs.oracle.com/iaas/Content/API/SDKDocs/clitoken.htm#Refreshing_a_Token).

### OKE Workload Identity Authentication

In Kubernetes, a workload is an application running on a Kubernetes cluster. A workload can be one application component running inside a single pod, or several application components running inside a set of pods that work together. All the pods in the workload run in the same namespace.

In Oracle Cloud Infrastructure, a workload running on a Kubernetes cluster managed by Kubernetes Engine (also known as OKE) is considered a resource in its own right. A workload resource is identified by the unique combination of Kubernetes cluster, namespace, and service account. This unique combination is referred to as the workload identity.

OKE Workload Identity Authentication allows workloads running on Kubernetes clusters managed by Kubernetes Engine to access other Oracle Cloud Infrastructure resources. For more information, see[Granting Workloads Access to OCI Resources](https://docs.oracle.com/iaas/Content/ContEng/Tasks/contenggrantingworkloadaccesstoresources.htm).

To enable OKE Workload Identity Authentication for OCI Terraform providers, set the`auth`attribute to "OKEWorkloadIdentity" in your provider definition, as shown in the following example:
```

```

## Environment Variables

The following environment variables are available for configuring the provider.

Environment variable Description and comments
`OCI_DEFAULT_CERTS_PATH`

Certificate path.

Note: Use only one certificate path variable at a time.
`OCI_SDK_APPEND_USER_AGENT`[Custom user agent](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#custom-user-agents).
`realm_specific_service_endpoint_template_enabled`Dedicated endpoint to securely access storage buckets.
`TF_APPEND_USER_AGENT`[Custom user agent](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#custom-user-agents).
`TF_VAR_auth`or`OCI_AUTH`By default, the OCI Terraform provider uses API key authentication but can be changed using this environment variable. Possible values are mentioned in the different sections in this page.
`TF_VAR_compartment_ocid`Compartment OCID authentication value.
`TF_VAR_config_file_profile`or`OCI_CONFIG_FILE_PROFILE`The profile name if you would like to use a custom profile in the OCI config file to provide the authentication credentials. See[Using the SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#sdk-cli-config-file)for more information.
`TF_VAR_fingerprint`or`OCI_FINGERPRINT`Key fingerprint authentication value.
`TF_VAR_private_key_password`or`OCI_PRIVATE_KEY_PASSWORD`(Optional) Passphrase used for the key, if it's encrypted.
`TF_VAR_private_key_path`or`OCI_PRIVATE_KEY_PATH`Private key path authentication value.
`TF_VAR_private_key`or`OCI_PRIVATE_KEY`The contents of the private key file. Required if`private_key_path`isn't defined, and takes precedence over`private_key_path`if both are defined. For details on how to create and configure keys see[How to Generate an API Signing Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#two)and[How to Upload the Public Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#three).
`TF_VAR_region`or`OCI_REGION`Region value. Example:`us-ashburn-1`
`TF_VAR_tenancy_ocid`or`OCI_TENANCY_OCID`Tenancy OCID authentication value.
`TF_VAR_user_ocid`or`OCI_USER_OCID`User OCID authentication value.
`USER_AGENT_PROVIDER_NAME`[Custom user agent](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#custom-user-agents).

### Exporting and Sourcing Environment Variables

You can either export the[required authentication values](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#api-key-auth)as environment variables, or source them in different bash profiles when executing Terraform commands.

If you primarily work in a single compartment, consider exporting the compartment OCID as an environment variable. The tenancy OCID is also the OCID of the root compartment, and can be used where any compartment OCID is required.
Tip  
  
You can remove Terraform configuration file[provider blocks](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm#provider-definitions)if all[API Key Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#api-key-auth)required values are provided as environment variables or are set in a`*.tfvars`file. UNIX and Linux Export Example The following UNIX and Linux`bash_profile`example applies when the Terraform configuration is limited to a single compartment or user.
```

```
After setting these values, open a new terminal or source the profile changes:
```

```
For more complex environments, consider maintaining multiple sets of environment variables. Windows Export Example
Note  
  
Ensure PEM format for keys. For more information, see[How to Generate an API Signing Key](https://docs.oracle.com/iaas/Content/API/Concepts/apisigningkey.htm#two). The following Windows example applies when the Terraform configuration is limited to a single compartment or user.
```

```
After setting these values, exit and reopen the terminal. (The variables aren't set for the current session.)

### Using Custom User Agents

To use a custom user agent,[export](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#env-export-source)one of the following environment variables. Only one environment variable is considered at a time, following this priority order:
- `USER_AGENT_PROVIDER_NAME`
- `OCI_SDK_APPEND_USER_AGENT`
- `TF_APPEND_USER_AGENT`

### Enabling and Disabling Dual-Stack Endpoints

Some Oracle Cloud Infrastructure (OCI) services are designed to support connectivity using both IPv6 and IPv4 (dual-stack endpoints). This means that users can access OCI resources over either protocol, ensuring compatibility with modern and legacy network environments. OCI services that support dual-stack endpoints facilitate seamless communication and accessibility for clients using IPv6, IPv4, or both.

To enable dual-stack endpoints while using OCI Terraform Provider, set one of the following parameters.
- provider block parameter`dual_stack_endpoint_enabled`to`true`

Example:
```

```

- environment variable`OCI_DUAL_STACK_ENDPOINT_ENABLED`to`true`
Note  
  
This parameter configuration overrides the OCI service's default configuration for dual-stack endpoints (when supported). For example, if dual-stack endpoints are disabled by default, and either of these parameters is set to`true`, then dual-stack endpoints are enabled for the service. As another example, if dual-stack endpoints are enabled by default, and either of these parameters is set to`false`, then dual-stack endpoints are disabled for the service. (If dual-stack endpoints aren't supported by the service, then the parameters have no effect.)

### Specifying a Dedicated Endpoint for the Object Storage Service

Securely access storage buckets in Object Storage with[dedicated endpoints](https://docs.oracle.com/iaas/Content/Object/Concepts/dedicatedendpoints.htm)using the OCI Terraform provider. When configuring the provider, use an environment variable, a parameter in the provider block, or both. If you use both, the provider block parameter takes precedence.

The environment variable is`OCI_REALM_SPECIFIC_SERVICE_ENDPOINT_TEMPLATE_ENABLED`. Default value is`false`. Set the value to`true`to use a dedicated endpoint.

The provider block parameter is`realm_specific_service_endpoint_template_enabled`. Default value is`false`. Set the value to`true`to use a dedicated endpoint.

#### Using a Dedicated Endpoint Only

- 

In the`provider`block, set`realm_specific_service_endpoint_template_enabled`to`true`.
```

```

#### Using Both Default and Dedicated Endpoints

Use the Terraform alias meta-argument to access both default service endpoints and realm-specific endpoints. Override default endpoints with realm-specific endpoints by specifying the provider parameter in resource creation.
- 

Define a`provider`block for each endpoint.
```

```

- 

Use[the Terraform`alias`meta-argument](https://developer.hashicorp.com/terraform/language/providers/configuration#alias-multiple-provider-configurations)in the`provider`block that's for a dedicated endpoint.

For example, add`alias = "custom_endpoint"`.
```

```

- 

In each`resource`block that you want to use a dedicated endpoint, reference the`provider`by the`alias`value.

For example, add`provider = "custom_endpoint"`.

The following example shows two provider blocks and two resource blocks. In this example,`bucket1`uses the default endpoint while`bucket2`uses the dedicated endpoint.
```

```

## Using the SDK and CLI Configuration File

Important  
  
Parameter names in the SDK and CLI configuration file are slightly different.

You can define the required provider values in the same`~/.oci/config`file that the SDKs and CLI use. For details on setting up this configuration, see[SDK and CLI Configuration File](https://docs.oracle.com/iaas/Content/API/Concepts/sdkconfig.htm).
Tip  
  
Terraform configuration file[provider blocks](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm#provider-definitions)can be removed if all[API Key Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#api-key-auth)required values are provided as environment variables or are set in the`~/.oci/config`file.

To set a nondefault OCI config profile as an environment value, use the following command:

```

```

You can also set the OCI config profile in a[provider block](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm#provider-definitions). For example:

```

```

## Order of Precedence

If the parameters are set in multiple locations, the order of precedence is as follows:
- The environment variable
- The non-default profile in the OCI config file, if provided
-
