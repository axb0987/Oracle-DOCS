# Using Object Storage for State Files
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/object-storage-state.htm
- Fetched: 2026-09-05 19:20 CDT

# Using Object Storage for State Files

Store Terraform state files in OCI Object Storage.
Note  
  
Of the backend types covered on this page, we recommend using an[Using the OCI native backend](https://docs.oracle.com/iaas/Content/dev/terraform/object-storage-state.htm#s3).

## Using the OCI native backend

Note  
  
[Upgrade to Terraform](https://developer.hashicorp.com/terraform/language/upgrade-guides)version v1.12.0 or greater to use the OCI native backend.

See[Data Source Configuration (OCI Backend)](https://developer.hashicorp.com/terraform/language/backend/oci#data-source-configuration).

## Using an S3-Compatible Backend (Deprecated)

Note  
  
The S3-compatible backend method is deprecated. Only use this method if you're not able to[upgrade to Terraform](https://developer.hashicorp.com/terraform/language/upgrade-guides)version v1.12.0 or greater.

To configure the S3-compatible backend, complete the steps in the following sections.

### Task 1: Set Up Access to OCI

For more information about S3 compatibility, see[Amazon S3 Compatibility API Prerequisites](https://docs.oracle.com/iaas/Content/Object/Tasks/s3compatibleapi.htm#usingAPI). For information about permissions for Object Lifecycle Management, see[Required IAM Policies](https://docs.oracle.com/iaas/Content/Object/Tasks/usinglifecyclepolicies.htm#permissions).

- [Sign Up for Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingup.htm)and obtain a unique namespace.
- Any user of the Amazon S3 Compatibility API with Object Storage needs permission to work with the service. If you're not sure if you have permission, contact your administrator. For basic information about policies, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm). For policies that enable use of Object Storage, see[Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm)and the[Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm).
- Use an existing or create a Customer Secret Key. A Customer Secret Key consists of an Access Key/Secret Key pair. See[Working with Customer Secret Keys](https://docs.oracle.com/iaas/Content/Identity/access/managing-user-credentials.htm#Working2)for details. To use or create the key pair:

- To use an existing Customer Secret Key, you must already know the Secret Key. For security reasons, you can't retrieve a Secret Key after generation. To show or copy the Access Key: In the navigation menu , select the Profile menu and then select User settings . On the left side of the page, select Customer secret keys . Hover over the Access Key associated with the Name of a particular Customer Secret key, then select Copy .
- To create a Customer Secret Key using the Console, see[To create a Customer Secret key](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcredentials.htm#create-secret-key).
- To create a Customer Secret Key using the CLI, see[oci iam customer-secret-key create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/iam/customer-secret-key/create.html).

### Task 2: Configure Authentication

- Set the location for the credentials file.

Caution  
  
Never set the`access_key`and the`secret_key`attributes in the same Terraform backend configuration. Storing these attributes in the same configuration creates a security risk.

The default location is`~/.aws/credentials`. You can set an alternate location by using the S3 backend`shared_credentials_file`option.
- Configure the`[default]`entry in the credentials file with the appropriate Object Storage credentials.

The file can contain any number of credential profiles. If you provide a different profile name, you must also update the backend`profile`option in the Terraform configuration file.

Following is an example of Object Storage credentials:

```

```

Note  
  
The key values provided in the example aren't valid. Valid`aws_access_key_id`and`aws_secret_access_key`are user-specific values generated using the previous steps.

### Task 3: Configure the S3 Backend in Terraform

- Set the Object Storage`endpoint`value in the following format:
`https:// <namespace> .compat.objectstorage. <region> .oraclecloud.com`
- Update the`terraform`block within the[Terraform configuration](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm)to define the[backend type](https://developer.hashicorp.com/terraform/language/backend).

Note  
  
Because variables and locals aren't accepted in the`terraform`block, you must hard-code backend configuration values.

Following are blocks organized by Terraform version. Select the block that maches the version of the Terraform configuration.

Terraform version 1.6.4 or later

```

```

Terraform versions before 1.64

```

```

Caution  
  
If the same bucket is used across many Terraform configurations, the key must be unique to avoid overwriting the state file. This example uses a single bucket (`terraform-states`) to store all Terraform state files, but uses a unique prefix for the object name based on the resource (`networking`).
- Run[`terraform init`](https://developer.hashicorp.com/terraform/cli/commands/init).

If you already have an existing`terraform.tfstate`file, then Terraform prompts you to confirm that the current state file is the one to upload to the remote state.
- Run[`terraform apply`](https://developer.hashicorp.com/terraform/cli/commands/apply).
The generated[state file](https://developer.hashicorp.com/terraform/language/state)is uploaded to Object Storage.
To share state across Terraform projects, use the backend configuration in`terraform_remote_state`. For more information, see[Accessing Remote States](https://docs.oracle.com/iaas/Content/dev/terraform/object-storage-state.htm#access-remote-states).

## Using an HTTP Backend

Note  
  
Because the HTTP backend requires a pre-authenticated request (PAR) for each state file, the preferred method for storing state files in Object Storage is[Using the OCI native backend](https://docs.oracle.com/iaas/Content/dev/terraform/object-storage-state.htm#s3).

Use the[HTTP backend type](https://developer.hashicorp.com/terraform/language/backend/http)to store state using a REST client, and to fetch, update, and purge state using the`HTTP``GET`,`POST`, and`DELETE`methods.

To configure the HTTP backend, complete the steps in the following sections.

### Task 1: Upload Existing State

A state file must exist in the bucket before you create the pre-authenticated request (PAR). This file can be an existing state file, or an empty file for the initial state.

To upload an existing state file it using Curl, make an`HTTP``PUT`request to the object store URL:

```

```

For instructions to upload a file to a bucket using the Console, CLI, or API, see[Uploading an Object Storage Object to a Bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingobjects_topic-To_upload_objects_to_a_bucket.htm).

### Task 2: Create a Read/Write Pre-Authenticated Request

With a pre-authenticated request (PAR) in Object Storage that specifies read/write permissions, you can access the Terraform state file without providing credentials.

For instructions to create a PAR using the Console, CLI, or API, see[Creating a Pre-Authenticated Request in Object Storage](https://docs.oracle.com/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_create_a_preauthenticated_request_for_all_objects_in_a_bucket.htm).

### Task 3: Configure the HTTP Backend in Terraform

- Set the address value in the following format, where the region and access URI are specific to you:

```

```

Example:

```

```

- Update the`terraform`block within the[Terraform configuration](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm)to define the[backend type](https://developer.hashicorp.com/terraform/language/backend).

Note  
  
Because variables and locals aren't accepted in the`terraform`block, you must hard-code backend configuration values.

Following is an example Terraform configuration using the region`us-phoenix-1`.

```

```

For more example configuration and state files that reference code, and a summary of configuration variables, see[HTTP](https://developer.hashicorp.com/terraform/language/backend/http).
- Run[`terraform init`](https://developer.hashicorp.com/terraform/cli/commands/init).
- Run[`terraform apply`](https://developer.hashicorp.com/terraform/cli/commands/apply).
The generated[state file](https://developer.hashicorp.com/terraform/language/state)is uploaded to Object Storage.
To share state across Terraform projects, use the backend configuration in`terraform_remote_state`. For more information, see[Accessing Remote States](https://docs.oracle.com/iaas/Content/dev/terraform/object-storage-state.htm#access-remote-states).

## Accessing Remote States

Use[terraform_remote_state](https://developer.hashicorp.com/terraform/language/state/remote-state-data)to access properties of objects in one Terraform configuration from another configuration.

For example, you might use one configuration to define compartments and another to define VCNs. If resources are in the same Terraform configuration folder, you can refer to a compartment OCID from the VCN configuration by using something such as this:`module.iam_compartment_SANDBOX.compartment_id`.

But assume that our definitions don't share a state file and we have a file structure similar to the following:

```

```

In this example:
- Both`governance`and`networking`configurations[store their respective state files on an OCI Object Storage bucket](https://docs.oracle.com/iaas/Content/dev/terraform/object-storage-state.htm#s3-3)using the`remote-backend.tf`and`terraform-states_bucket_credentials`files.
- The`compartments.tf`file creates a compartment at the root level using the[`iam-compartment`module](https://registry.terraform.io/modules/oracle-terraform-modules/iam/oci/latest/submodules/iam-compartment)from the Terraform Registry as follows:

```

```

### Defining Outputs

The`terraform_remote_state`data source can access output values from another Terraform configuration using the latest state file with a remote backend. For the`networking`configuration to access the`governance`configuration and dynamically retrieve Terraform resources properties, you must define outputs for the`governance`Terraform configuration. Without a defined output, the values can't be used from outside of its configuration.

The`governance/outputs.tf`file would look similar to the following:

```

```

### Referring to a Remote State

In this example, we're using the[`vcn`module](https://registry.terraform.io/modules/oracle-terraform-modules/vcn/oci/latest)from Terraform Registry to define a new VCN. The`networking`configuration refers to the`governance`configuration to define the VCN's compartment OCID:

```

```

But, for the`compartment_id = data.terraform_remote_state.governance.outputs.iam_compartment_SANDBOX["id"]`line to be correctly interpreted, you must define a`data.terraform_remote_state`object.

### Defining the Remote State Data Source

After the following`terraform_remote_state`data source is added to the`networking`configuration, you can access the`governance`Terraform outputs from configurations within the`networking`folder:

```

```

If you define the remote state data source in a separate file, such as`remote-state-data_governance.tf`, you can copy and paste the file as needed. Each new configuration can then refer to the compartment in the same way.

## For More Information

- [State](https://developer.hashicorp.com/terraform/language/state)
- [Backend types](https://developer.hashicorp.com/terraform/language/backend#backend-types)
- [The terraform_remote_state Data Source](https://developer.hashicorp.com/terraform/language/state/remote-state-data)
