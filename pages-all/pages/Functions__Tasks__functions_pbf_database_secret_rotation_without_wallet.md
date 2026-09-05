# Database Secret Rotation without Wallet Function
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_database_secret_rotation_without_wallet.htm
- Fetched: 2026-09-05 02:07 CDT

# Database Secret Rotation without Wallet Function

Find out how to use the Database Secret Rotation without Wallet pre-built function in OCI Functions to rotate secrets using TLS connection to the database.

## Common Usage Scenarios

Use the Database Secret Rotation without Wallet PBF to automatically rotate secrets of the database by making a JDBC TLS connection without a wallet.

Services related to the Database Secret Rotation without Wallet function include:
- [Key and Secret Management Concepts](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm#concepts)
- [Managing Vault Secrets](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets.htm)
- [Functions](https://docs.oracle.com/iaas/Content/Functions/home.htm)

## Scope

Scope considerations for this function include:
- The pre-built function can be used with any database supporting a JDBC URL.
- Secret Service uses the function created by the pre-built function to rotate the database secrets.

## Prerequisites and Recommendations

The following are best practices when using this pre-built function:
- Set the pre-built function timeout to 300 seconds.
- Make sure that the VCN linked to the application facilitates access to other OCI services by using a service gateway, internet gateway, or NAT gateway.
- Make sure that the subnet that is attached to the VCN has a route table and a security list.
- Make sure that the subnet's route table includes a rule that is using a service gateway created inside the VCN. Make sure that the service gateway has access to OCI services within the region for which you are configuring secret rotations.
- Make sure that the subnet's security list includes an egress rule that has a destination set to the service gateway created inside the VCN.
- 

Make sure that you have configured network access for the autonomous database to allow incoming requests from the application in which the pre-built function is going to be created, as follows:
- When using the OCI Console to create or update the autonomous database, display the Choose network access area or the Update network access area of the page. For more information, see the[Autonomous AI Database Serverless](https://docs.oracle.com/iaas/autonomous-database-serverless/index.html#GUID-0B230036-0A05-4CA3-AF9D-97A255AE0C08)documentation.
- Select one of the following types of network access:
- Allow secure access from everywhere: Select this option if you want the autonomous database to be accessed from the internet.
- Secure access from allowed IPs and VCNs only: Select this option if you only want the autonomous database to be accessed from VCNs and IPs in an access control list (ACL). Add one or more access control rules, according to the network from which you want the autonomous database accessed.
- Private endpoint access only: Select this option if you want the autonomous database to be accessed from a private endpoint within an OCI VCN. Select the VCN and subnet from which you want the autonomous database accessed.

## Configuring the Database Secret Rotation without Wallet Function

To configure a Database Secret Rotation without Wallet function, perform the following steps:

- On the Pre-Built Functions page, select Database Secret Rotation without Wallet , and then select Create function .
- Configure the Name , Compartment , and Application as follows:

- Name: A name of your choice for the new function. The name must start with a letter or underscore, followed by letters, numbers, hyphens, or underscores. Length can be 1–255 characters. Avoid entering confidential information.

To create the function in a different compartment, select Change Compartment .
- Application: Select the application in which you want to create the function.

If a suitable application doesn't already exist in the current compartment, select Create new application and specify the following details:
- Name: A name for the new application. Avoid entering confidential information.
- VCN: The VCN (virtual cloud network) in which to run functions in the application. Optionally, select VCN compartment: to select a VCN from a different compartment.
- Subnets: The subnet (or subnets, up to a maximum of three) in which to run functions. Optionally, select Subnets compartment: to select a subnet from a different compartment.
- Shape: The processor architecture of the compute instances on which to deploy and run functions in the application. All the functions in the application are deployed and run on compute instances with the same architecture. The function's image must contain the necessary dependencies for the architecture you select.
- Tags: If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Security attributes: If you have permissions to create a resource, then you might also have permissions to add security attributes to that resource. To add a security attribute, you must have permissions to use the security attribute namespace. For more information about security attributes and security attribute namespaces, see[Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). If you're not sure whether to add security attributes, skip this option or ask an administrator. You can add security attributes later.
- Configure the IAM policy for pre-built functions.

By default, OCI Functions creates a dynamic group and an IAM policy with the policy statements required to run the pre-built function. Proceed as follows:
- If you want OCI Functions to automatically create the dynamic group and policy, make no changes to accept the default behavior.
- If you don't want OCI Functions to automatically create the dynamic group and policy, select Do not create a dynamic group and IAM policy .
Important  
  
If you select the Do not create a dynamic group and IAM policy option, you must define the dynamic group and the IAM policy yourself. For more information, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_database_secret_rotation_without_wallet.htm#pbf-catalog_database_secret_rotation_without_wallet__permissions-database_secret_rotation_without_wallet).

You also have to configure an IAM policy to allow the Secret Rotation Service to invoke the function. For more information, see[Permissions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_database_secret_rotation_without_wallet.htm#pbf-catalog_database_secret_rotation_without_wallet__permissions-database_secret_rotation_without_wallet).
- Configure function memory and timeout values as follows:

- Memory (in MBs): The maximum amount of memory that the function can use while running, in megabytes. This is the memory available to the function image. (Default: 512 MB)
- Timeout (in seconds): The maximum amount of time that the function can run for, in seconds. If the function doesn’t complete in the specified time, the system cancels the function. (Default: 300)
- (Optional) Configure Provisioned concurrency to minimize any initial delays when invoking the function by specifying a minimum number of concurrent function invocations for which you want to have execution infrastructure constantly available. (Default: Not selected)

If selected, specify the number of provisioned concurrency units assigned to this function. Default: 20.

For more information about provisioned concurrency, see[Reducing Initial Latency Using Provisioned Concurrency](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingprovisionedconcurrency.htm).
- Optionally enter any tags in the Tags section. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace . For more information about tagging, see[Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
- Select Create .

The deploy dialog displays the tasks to deploy the function (see[Finishing Pre-Built Function Deployment](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functions_pbf_finishing_prebuilt_deploy.htm)).

## Configuration Options

### Permissions

Running a function requires certain IAM policies.

For the Database Secret Rotation without Wallet function, you have to create a dynamic group and configure an IAM policy to allow the Secret Rotation Service to invoke the function. To set the proper policies, perform the following steps:
- Create a dynamic group with the rule:

```

```

This rule includes all vault secrets in the dynamic group. You can limit which vault secret is included in the dynamic group by using a more restrictive rule. For example:
```

```

- Configure an IAM policy that enables the resources included in the dynamic group to invoke functions. For example:

```

```

Note  
  
Replace`<vs-dynamic-group-name>`with the name of the dynamic group that you created for the vault secret.

In addition, if you selected the Do not create a dynamic group and IAM policy option when creating the function, you must define the dynamic group and the IAM policy yourself to enable the function to manage secrets. To set the proper policies, perform the following steps:
- Create a dynamic group with the rule:
```

```

This rule includes all functions in the dynamic group. You can limit which function is included in the dynamic group by using a more restrictive rule. For example:
```

```

- Configure an IAM policy using the dynamic group:

```

```

You can limit which vault secrets the function can manage by using a more restrictive policy. For example:
```

```

Note  
  
Replace`<function-ocid>`with the OCID of the function that you created in preceding steps.
Note  
  
Replace`<dynamic-group-name>`with the name of the dynamic group that you created using the function's OCID.
Note  
  
Replace`<compartment_ocid>`with the OCID of the compartment that contains the function.

### Invoking This Function

The function created using this PBF would be invoked by the Secret Service to rotate the secret.
- Create a function using this PBF and copy the function ID.
- 
- Open the navigation menu, select Identity &amp; Security , and then select Vault .
- Under List scope , select a compartment that contains the secrets that you have created in a vault.
- 
From the list of secrets, select a secret name that you require to rotate using this PBF, or create a new secret.
- To create a new secret, see[Create a secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingsecrets_topic-To_create_a_new_secret.htm).
- To update an existing secret, see[Update a secret](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/tasks_managingsecrets_topic_to_update_a_secret_dita.htm).
- Select Target system type as Function for rotations.
- Add the function ID copied from step 1 as the Target system ID .
- Ensure that the secret follows these requirements:
- The first version of the secret must be manually created. Select Manual Secret Generation with the secret content in the following JSON format:
```

```

- The password has to be the same password that is set for the database to be rotated.
- After successful creation of the secret, Automatic Secret Generation has to be enabled so that subsequent secret versions can be auto-generated by the Secret Service.
- Edit the newly created secret, enable Automatic Secret Generation , and provide the secret content in the following JSON format:
```

```

- In Automatic Secret Generation , password is given as`%GENERATED_PASSPHRASE%`so that the Secret Service can auto-generate the password in this field.
- Username and password must establish a connection with the database using the format:`jdbc:oracle:thin:@ <connectionString> ?user= <username> &password= <example-password>`
- Ensure to use TLS connection.
Note  
  
This function isn't compatible with MTLS connection.

### Troubleshooting

OCI Functions common status codes

The following table summarizes common OCI Functions errors that you might encounter when working with pre-built functions:

Error Code Error Message Action
200 Success None
404 NotAuthorizedOrNotFound Verify that the required policies are configured (see[Running Fn Project CLI commands returns a 404 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionstroubleshooting_topic-Issues-setting-up-and-running-Oracle-Functions.htm#Running_Fn_Project_CLI_commands_returns_a_404_error)).
444 Timeout

The connection between the client and OCI Functions was interrupted during function execution (see[Invoking a function causes the client to report a timeout, and a 444 error is shown in the function's logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#functionstroubleshooting_topic_Function_timeout_client_message_and_a_444_error)). A retry might solve the issue.

Note that most clients have an inner timeout of 60 seconds. Even when the pre-built function timeout is set to 300 seconds, the following might be required:
- When using the OCI CLI : Use --read-timeout 300
- When using the OCI SDK : Set the read timeout to 300 when creating the client
- When using DBMS_CLOUD.SEND_REQUEST : Use UTL_HTTP.set_transfer_timeout(300);

For more information, see[Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsinvokingfunctions.htm).
502, 504 (various) Most issues return a 502 status code (see[Invoking a function returns a Function failed message and a 502 error](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionstroubleshooting_topic-Issues-invoking-functions.htm#Invoking_a_function_returns_a_Functionfailed_message_and_a_502_error)). A 502 error with the message "error receiving function response" might be resolved by increasing the memory allocation. A 502 might occur occasionally when the function is in some transient state. A retry might solve the issue.

To further identify the cause, enable logging features for the pre-built function (see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsexportingfunctionlogfiles.htm)). For detailed information on troubleshooting a function, see[Troubleshooting OCI Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionstroubleshooting.htm).

Database Secret Rotation without Wallet pre-built function error messages

The following table summarizes the errors that you might encounter when working with this pre-built function:

Step Status Code Response Message Description
VERIFY_CONNECTION 200 Connection using the pending secret version was successful! A pending version of the secret exists, and the database connection was successfully established using that version.
Connection using the current secret version was successful! The database connection was successful with the current secret version.
400 Connection using the current secret version was unsuccessful. Invalid credentials in the current secret version or any pending version (if exists), or network configuration for connection between the function and database is incorrect.
404 Current version of the secret not found No current version of the secret exists with the given secretId .
500 &lt;EXCEPTION MESSAGE&gt; Thrown when any exception occurs while verifying connection.
CREATE_PENDING_VERSION 200 Pending version already exists! A pending version of the secret already exists. Doesn't create a new pending version.
Pending version created successfully! A pending version doesn't exist, a new pending version of the secret is created.
&lt;EXCEPTION CODE&gt; Pending version creation failed. Exception from DP client while trying to create a new pending version of the secret.
500 &lt;EXCEPTION MESSAGE&gt; Thrown when any exception occurs while creating a new version.
UPDATE_TARGET_SYSTEM 200 Target system already updated. The database can be connected using the pending secret version, indicating that this version was previously used to update the database credentials.
Target system updated successfully! Database credentials were updated with the pending version of the secret.
404 No pending version exists. No pending version of the secret exists which can be used to update the target system.
500 Target system update failed. Attempted to update the target system with the new pending version credentials, but the database connection verification using those credentials failed.
&lt;EXCEPTION MESSAGE&gt; Thrown when any exception occurs while updating the target system.
PROMOTE_PENDING_VERSION 200 Pending version promoted! Pending version successfully got promoted to current.
500 &lt;EXCEPTION MESSAGE&gt; Thrown when any exception occurs while promoting the pending version.

To further identify the cause, enable logging features for the pre-built function (see[Storing and Viewing Function Logs](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/../Tasks/functionsexportingfunctionlogfiles.htm)).

Log Analysis Tips

All the pre-built functions provide an option to specify the logging level as a configuration parameter. You can set the logging level to`DEBUG`to get more information.

Since an application has multiple functions, the pre-built function log entries are identified by the prefix "PBF | &lt;PBF NAME&gt; ".

For example, a log entry for the Database Secret Rotation without Wallet pre-built function looks similar to the following:
```

```
