# Managing Outbound Connectors
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Tasks/managing-outbound-connectors.htm
- Fetched: 2026-09-05 02:04 CDT

# Managing Outbound Connectors

File Storage uses outbound connectors to communicate with an external server, such as an LDAP server.

An outbound connector contains all the information needed to connect, authenticate, and gain authorization to perform the account's required functions. Currently, outbound connectors are only used for communicating with LDAP servers. You specify configuration options for the connector when you[add LDAP authentication to a mount target](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/ldap-setup.htm#updating-mts-for-ldap).

When connecting to an LDAP server, a mount target uses the first outbound connector specified in its configuration. If the mount target fails to log in to the LDAP server using the first outbound connector, it uses the second outbound connector.

Multiple mount targets can use the same outbound connector. You can associate an outbound connector with a mount target only when they exist in the same availability domain. You can have up to 32 outbound connectors per availability domain.

See the following topics for detailed instructions related to outbound connector management:
- [Creating an Outbound Connector](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/create-outbound-connector.htm)
- [Listing Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/list-outbound-connectors.htm)
- [Getting an Outbound Connector's Details](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/get-outbound-connector-details.htm)
- [Editing an Outbound Connector](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/edit-outbound-connector.htm)
- [Moving an Outbound Connector Between Compartments](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/move-outbound-connector.htm)
- [Rotating Outbound Connectors](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/rotate-outbound-connector.htm)
- [Locking an Outbound Connector](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/lock-outbound-connector.htm)
- [Deleting an Outbound Connector](https://docs.oracle.com/en-us/iaas/Content/File/Tasks/delete-outbound-connector.htm)

## Required IAM policy

To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a policy by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which compartment your access works in.

For administrators: The policy in[Let users create, manage, and delete file systems](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#general-file-system-management)allows users to manage outbound connectors.
Because outbound connectors also require access to secrets to connect to an external server, such as an LDAP server, additional IAM policies for both the user configuring the mount target and the mount target itself are required.
Important  
  
These policies must be created before you can configure mount targets to use LDAP for authorization.

### Policy to Enable Mount Target Configuration

Grant the user or group configuring LDAP on a mount target permissions using a policy such as the following. This allows the user to read the Vault secrets needed during configuration.

```

```

This allows the user to issue File Storage commands that will read the Vault secrets and display parts of the secret for validation during configuration.

### Policy to Allow a Mount Target to Retrieve Secrets

The File Storage service requires the ability to read the secrets. File Storage uses resource principals to grant a specific set of mount targets access to the Vault secret. This is a two step process, first the mount targets which need access must be put into a dynamic group, and then the dynamic group is granted access to read the secrets.

- 

Create a dynamic group for the mount targets with a policy such as the following:

```

```

Note  
  
If you have more than one rule in a dynamic group, ensure that you use`Match any rules defined below`option.
- 

Create an IAM policy that gives the dynamic group of mount targets read access to Vault secrets:

```

```

If you're new to policies, see[Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm)and[Details for the File Storage Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/filestoragepolicyreference.htm).

## Details About An Outbound Connector

The details page provides the following information about an outbound connector: OCID Every Oracle Cloud Infrastructure resource has an Oracle-assigned unique ID called an Oracle Cloud Identifier (OCID). You need an outbound connector's OCID to use the Command Line Interface (CLI) or the API. You also need the OCID when contacting support. See[Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). CREATED The date and time that the outbound connector was created. COMPARTMENT When you create an outbound connector, you specify the compartment that it resides in. A compartment is a collection of related resources (such as cloud networks, compute instances, or file systems) that are only accessible to those groups that have been given permission by an administrator in your organization. You need your outbound connector's compartment to use the Command Line Interface (CLI) or the API. For more information, see[Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm). AVAILABILITY DOMAIN When you create an outbound connector, you specify the availability domain that it resides in. An availability domain is one or more data centers within a region. You need an outbound connector's availability domain to use the Command Line Interface (CLI) or the API. For more information, see[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm). CONNECTOR TYPE The type of outbound connector. The only supported type is LDAPBIND. SERVER DNS NAME The fully qualified domain name of instance where the LDAP service is running. PORT The LDAPS port of the LDAP service. BIND DISTINGUISHED NAME The LDAP Distinguished Name used to log into the LDAP server. SECRET OCID The OCID of the secret in Vault which contains the password associated with the Bind Distinguished Name. SECRET VERSION The version number of the LDAP password secret. ENABLE TRUSTED CERTIFICATE Indicates whether the outbound connector is configured to use a trusted certificate for LDAPS connections. TRUSTED CERTIFICATE SECRET The OCID of the secret in Vault that contains the trusted certificate. TRUSTED CERTIFICATE SECRET VERSION The version number of the trusted certificate secret.

## Troubleshooting Bad Request (HTTP 400) Errors When Configuring a Trusted Certificate

If you create an outbound connector and you provided a Trusted Certificate secret OCID and secret version, the request can fail with Bad Request (HTTP 400) . This usually means the service couldn't validate the secret, the version, or the certificate content.

Here are some common causes and fixes:

### Cause: Invalid Vault secret OCID

The Trusted Certificate OCID you entered isn't a Vault`Secret`OCID (or the secret name is invalid).

### Remedy: Use a valid Vault secret OCID

- Confirm the OCID points to a Vault Secret (not a vault, key, or another resource type).
- Update the outbound connector to use the correct trusted certificate secret OCID.

### Cause: Invalid secret version

The trusted certificate secret version must be greater than 0. If you use 0 (or a negative number), validation fails.

### Remedy: Set the version to a number greater than 0

- In Vault, check the secret versions available for your trusted certificate secret.
- Update the outbound connector to use a secret version greater than 0.

### Cause: Missing self-signed root certificate

The service reads the certificate (or bundle) from the secret and expects to find a self-signed (root) certificate. If it can't find one, validation fails.

### Remedy: Ensure the secret includes a self-signed root certificate

- Check the secret content and confirm it includes a self-signed root CA certificate (either as a single cert or within a bundle).
- Update the Vault secret content if needed, then re-create the outbound connector.

### Cause: Expired root certificate

The self-signed (root) certificate found in the secret is expired. You might see the message`Root Certificate is expired`.

### Remedy: Replace the expired certificate

- Upload a valid (non-expired) root certificate into the Vault secret.
- If the update creates a new secret version, update the outbound connector to use that version, then retry.

### Cause: Vault secret access failure

The service can't read the secret (for example, because of missing permissions, the secret being unavailable, or connectivity issues).

### Remedy: Confirm permissions and access to the secret

- Verify IAM policies allow the user making the change and the mount target (resource principal) to read`secret-family`in the secret's compartment.
- Confirm the secret exists and is available, and that Vault access is working from your environment.

### Cause: Invalid X.509 certificate format

The secret content isn't a valid X.509 certificate (or certificate bundle), so the service can't parse it.

### Remedy: Store a valid X.509 certificate (or bundle)

- Confirm the certificate data you stored is a properly formatted X.509 certificate (or bundle) and isn't truncated or corrupted.
-
