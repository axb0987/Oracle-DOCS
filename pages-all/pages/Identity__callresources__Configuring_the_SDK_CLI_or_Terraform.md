# Configuring the SDK, CLI, or Terraform
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/Configuring_the_SDK_CLI_or_Terraform.htm
- Fetched: 2026-09-05 02:20 CDT

# Configuring the SDK, CLI, or Terraform

Learn about the Oracle Cloud Infrastructure Software Development Kits (SDKs) and Command Line Interface (CLI) which you can use to facilitate development of custom solutions.

For information about SDKs, see[Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)

## For the SDK for Java:

In your SDK for Java, create an`InstancePrincipalsAuthenticationDetailsProvider`object. For example:

```

```

## For the SDK for Python:

In your SDK for Python, create an`oci.auth.signers.InstancePrincipalsSecurityTokenSigner`object. For example:

```

```

To refresh the token without waiting, use the following command:

`signer.refresh_security_token()`

## Enabling Instance Principal Authorization for the CLI

To enable instance principal authorization from the CLI, you can set the authorization option (`--auth`) for a command. For example:

```

```

Alternatively, you can set the following environment variable:
```

```

Note that if both are set, the value set for`--auth`takes precedence over the environment variable.

For information about using the CLI, see[Working with the Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).

## Enabling Instance Principal Authorization for Terraform

To enable instance principal authorization in Terraform, you can set the`auth`attribute to "InstancePrincipal" in the provider definition as shown in the following sample:

```

```

Note that when you use instance principal authorization you do not need to include the`tenancy_ocid`,`user_ocid`,`fingerprint`, and`private_key_path`
