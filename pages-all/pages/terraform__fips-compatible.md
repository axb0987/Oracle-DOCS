# Enabling FIPS Compatibility
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/fips-compatible.htm
- Fetched: 2026-09-05 19:20 CDT

# Enabling FIPS Compatibility

Maintain FIPS compliance while using the Oracle Cloud Infrastructure Terraform provider.

This page describes requirements and best practices for using Terraform with a FIPS-compatible version of the OCI Terraform provider.

## FIPS Encryption

To ensure the highest security standards, move traffic from Terraform to OCI endpoints over a TLS connection established with an HTTP client using FIPS certified encryption.

The standard[OCI Terraform Provider](https://docs.oracle.com/iaas/Content/dev/terraform/home.htm)is implemented in Go. Go's native cryptography implementations, while fully capable of establishing secure TLS connections with OCI endpoints, haven't been FIPS certified.

For Terraform traffic to transit to OCI endpoints over FIPS-compliant connections, you must use a special version of the Terraform provider that uses FIPS certified cryptography. This version of the OCI Terraform provider uses the[FIPS 140-2 certified](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4493)Oracle Cloud Infrastructure for BoringCrypto instead of Go's native cryptography implementation. Read more about the Oracle Cloud Infrastructure for BoringCrypto[here](https://csrc.nist.gov/CSRC/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp4493.pdf).

## Installing the FIPS-Compliant Terraform Provider

The FIPS-compliant OCI Terraform provider is only available for Oracle Linux. You can install the provider using yum.
Tip  
  

Before installing the OCI Terraform provider,[download and install Terraform from HashiCorp](https://docs.oracle.com/iaas/Content/dev/terraform/installing.htm#download-terraform).

If any existing OCI Terraform provider packages are already installed on the Oracle Linux machine, remove them first:

```

```

Install the FIPS-compatible OCI Terraform provider by running the following yum command from an Oracle Linux machine:

```

```

### Configuring the Terraform Provider

- 

Add an environment variable to set the target region for Terraform:

```

```

- 

Add an environment variable to disable interprocess traffic encryption between Terraform and the OCI Terraform provider:

```

```

- 

Add an environment variable to prevent Terraform from accessing the[HashiCorp Checkpoint service](https://checkpoint.hashicorp.com/):

```

```

- Configure the authentication method for the Terraform provider. See[Authentication](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#authentication)for more information.

## Operating Terraform in a Single Region

To ensure that traffic between Terraform and OCI services doesn't transit over public internet infrastructure, we recommend that you run Terraform and the OCI Terraform provider from a Compute instance that's hosted in the same region as the resources they create and manage.

### Creating a Compute Instance

After Terraform and the OCI Terraform provider are installed on an Oracle Linux machine, you can use Terraform and the following sample Terraform configuration file to:
- Create a designated compute instance you can use to provision more infrastructure within the same region.
- Install Terraform and the latest FIPS compliant OCI Terraform provider on the new instance.
- Restrict communication with the instance to OCI endpoints and HTTPS using a[service gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/servicegateway.htm).
- Enable[instance principal authentication](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#instance-principal-auth).

See[Authoring Configurations](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm)for more information.

To create the compute instance:
- Copy the[`main.tf`](https://docs.oracle.com/iaas/Content/dev/terraform/fips-compatible.htm#create-instance__main-tf-file)file to an Oracle Linux machine.
- Gather the information required to populate the Terraform configuration file's variables.
- 

Change the`oel-image`value in the Terraform configuration file to the Oracle Linux image OCID value for your region.

To find the Oracle Linux image OCID value for a region, see[Platform Images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm).
- 

Initialize Terraform in the directory that contains the Terraform configuration file:
```

```

- 

Apply the Terraform configuration:
```

```

```

```

Important  
  

The`instance-ip`output variable provides the IP address you need to use to sign in to the new compute instance.
`main.tf`

```

```

### Signing in to the Instance

Use the following SSH command to access the instance:

```

```

&lt;private_key_path&gt; is the full path and name of the file that contains the private key associated with the instance you want to access.

&lt;username&gt; is the default username for the instance. For Oracle Linux images, the default username is`opc`.

&lt;instance_ip_address&gt; is the instance IP address that was the output of the Terraform commands.

### Installing and Configuring Terraform on the Instance

- 

Use yum to install Terraform and the FIPS compatible OCI Terraform provider on the instance:

```

```

- 

Add an environment variable to enable[instance principal authentication](https://docs.oracle.com/iaas/Content/dev/terraform/configuring.htm#instance-principal-auth)to the bash profile:

```

```

- 

Add an environment variable to set the target region for Terraform:

```

```

- 

Add an environment variable to disable interprocess traffic encryption between Terraform and the OCI Terraform provider:

```

```

- 

Add an environment variable to prevent Terraform from accessing the[HashiCorp Checkpoint service](https://checkpoint.hashicorp.com/):

```

```

- 

Exit the instance:
```

```

### Implementing Security Rules

Before using the new instance to run Terraform, update the security rules to prevent egress traffic to any third-party endpoints other than OCI services. You can make this update by removing the following egress rule from the Terraform configuration file's`security-list1`resource and running`terraform apply`from the Oracle Linux machine:
```

```

Tip  
  

You can also use the OCI Console to[update your security rules](https://docs.oracle.com/iaas/Content/Network/Concepts/update-securitylist.htm)on the new instance.

### Running Terraform from the Instance

After creating the instance, installing and configuring Terraform on the instance, and updating the security rules, you can use Terraform to provision more OCI infrastructure within the same region. Copy any other Terraform configuration files to an instance, sign in to the instance, and run Terraform commands as with any other Terraform provider:
```

```
