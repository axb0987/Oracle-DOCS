# Getting Started
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblegetstarted.htm
- Fetched: 2026-09-05 01:36 CDT

# Getting Started

This topic discusses how to get started using the Oracle Cloud Infrastructure (OCI)[Ansible collection](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansible.htm). The OCI Ansible collection replaces our[legacy Ansible modules](https://github.com/oracle/oci-ansible-modules).
Note  
  
If you currently use our legacy Ansible modules and would like to start using collections, refer to our[migration guide](https://github.com/oracle/oci-ansible-collection/blob/master/MigrationGuide.md).

To start using Ansible with OCI, ensure that you meet the[prerequisites](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblegetstarted.htm#prerequisites), then install the Ansible collection[using yum](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblegetstarted.htm#installing_with_yum)or[manually](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblegetstarted.htm#manual_installation).
Tip  
  

You can use[Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm)to[preinstall the Oracle Cloud Development Kit on a Compute instance in your compartment](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/devtools.htm). The Oracle Cloud Development Kit includes Ansible, the OCI Ansible collection and its dependencies, and preconfigures the required authorization.

Both Ansible and our Ansible collection also come preinstalled and preauthenticated on[Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/devcloudshellgettingstarted.htm).

## Prerequisites for Using Ansible with Oracle Cloud Infrastructure

- You must have an Oracle Cloud Infrastructure account.
- You must have a user in that account in a security group with a policy that grants necessary permissions for working with resources in the account compartments. For guidance, see[How Policies Work](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm).
- You must have the necessary credentials and OCID information.

## Installing the Ansible Collection with Yum

If you're running Oracle Linux 7 or Oracle Linux 8, you can use yum to install the Oracle Cloud Infrastructure Ansible collection RPM.

The Ansible collection RPM installs the OCI Ansible collection and its required dependencies: the OCI SDK for Python and Ansible.
Note  
  
This installation uses Python version 3.6 and Ansible version 2.9 or later.

Use one of the following commands to enable the Oracle Linux developer repository and install the Ansible collection RPM, depending on your Oracle Linux version.

Oracle Linux 7:

```

```

Oracle Linux 8:

```

```

After installing the RPM, you must configure the[SDK and CLI configuration file](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm)as explained in[Configuring Authentication](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblegetstarted.htm#configureAuth).

### Test the Installation

To test the installation of the RPM and configuration of the SDK, you can run a sample Ansible playbook.

If you're using Oracle Linux 7, use the following command to test your installation:

```

```

If you're using Oracle Linux 8, use the following command to test your installation:

```

```

## Manual Installation

### Installing the Oracle Cloud Infrastructure SDK for Python

- Download and install the SDK for Python by following instructions in the topic,[SDK for Python](https://docs.oracle.com/iaas/Content/API/SDKDocs/pythonsdk.htm). For additional guidance, see[Downloading and Installing the SDK](https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/installation.html#downloading-and-installing-the-sdk).
- After installing the SDK for Python, you must configure it using instructions in the topic[Configuring the SDK](https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/installation.html#configuring-the-sdk).

### Installing and Configuring Ansible

- To install Ansible, follow the instructions provided in the[Ansible Installation Guide](http://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).
- For guidance configuring Ansible, see[Configuring Ansible](http://docs.ansible.com/ansible/latest/installation_guide/intro_configuration.html).
Note  
  
The OCI Ansible collection requires Ansible version 2.9 or later. If you are using an earlier version of Ansible, refer to the[documentation for our legacy modules](https://github.com/oracle/oci-ansible-modules).

### Installing the Oracle Cloud Infrastructure Ansible Collection

Install the OCI Ansible collection from Ansible Galaxy by using the following command:
```

```

If you've already installed the collection, you can update its modules to the latest version by adding the`--force`flag to the command. For example:
```

```

## Sample Playbooks

Sample playbooks are available in the Oracle Cloud Infrastructure Ansible collection GitHub project. The[samples library](https://github.com/oracle/oci-ansible-collection/tree/master/samples)is updated regularly with the addition of new samples. See[Example Ansible Playbooks](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblesamples.htm)for more information.

## Writing a Sample Playbook

After your installation is complete, or if you're using the Cloud Shell, you can write a sample playbook that uses Ansible modules. Following is an example playbook (named`list_buckets.yml`) that uses the`oci_object_storage_bucket_facts`module to fetch facts pertaining to the buckets in your compartment.
```

```

## Executing the Playbook

Execute the Ansible playbook using Python by invoking this command:

```

```

## How to Obtain Module Documentation

Detailed information about using our Ansible modules is available on[docs.oracle.com](https://docs.oracle.com/iaas/tools/oci-ansible-collection/latest/)and[readthedocs.io](https://oci-ansible-collection.readthedocs.io/en/latest/).

To obtain access to detailed information about using Ansible modules in the CLI, use the`ansible-doc`command on the module's name. For example, to get the documentation for the`oci_object_storage_bucket_facts`module, execute the following command:
```

```

## Configuring Authentication

When creating and configuring Oracle Cloud Infrastructure resources, Ansible modules use authentication information that is outlined in the[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm).
Caution  
  
[User Credentials](https://docs.oracle.com/iaas/Content/Identity/usercred/usercredentials.htm)that are referenced in Oracle Cloud Infrastructure SDK configuration files grant access to Oracle Cloud Infrastructure resources. Therefore, it is important to secure the credentials to prevent unauthorized access to these resources. To secure the credentials on the controller node where your Ansible playbooks run, follow guidelines outlined in the document[Securing IAM](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security.htm)(see section entitled "IAM Credentials").

Ansible modules permit you to override authentication information specified in the SDK configuration file by using module options and environment variables. Documentation for authentication overrides is provided internally, as described in[How to Obtain Module Documentation](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansiblegetstarted.htm#getModuleDocs). However, using environment variables and Ansible module options to override authentication information must be avoided in production scenarios.

We recommend using Oracle Cloud Infrastructure SDK configuration files to specify authentication information. To support multiple users, use the "profiles" feature in the SDK configuration file. When distributing roles that use Ansible modules, ensure that no IAM credentials are included with the roles.

## For More Information

- [Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html)
