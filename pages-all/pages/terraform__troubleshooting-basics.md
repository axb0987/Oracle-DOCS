# Troubleshooting Basics
- Source: https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting-basics.htm
- Fetched: 2026-09-05 19:21 CDT

# Troubleshooting Basics

When troubleshooting or getting support for the OCI Terraform provider, it's often useful to first check the status of the OCI services, the version of Terraform and the provider, and enable and collect verbose logging.
Tip  
  
Checking service status and verbose log output can help you determine whether an issue is related to the Terraform provider or the OCI service the provider is using.

See the[list of common issues](https://docs.oracle.com/iaas/Content/dev/terraform/troubleshooting.htm#common_issues)after you start with the basics.

## Checking OCI Service Status and Outages

To check on the latest status and whether there are any outages in OCI, see[OCI Status](https://ocistatus.oraclecloud.com/).

## Checking the Terraform and OCI Terraform Provider Versions

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

## Verbose Logging for OCI Terraform Provider

To get verbose console output when the provider is running, precede your Terraform command with the`TF_LOG`and`OCI_GO_SDK_DEBUG`flags. For example:

```

```

The[`TF_LOG`](https://www.terraform.io/docs/internals/debugging.html)level and`OCI_GO_SDK_DEBUG`
