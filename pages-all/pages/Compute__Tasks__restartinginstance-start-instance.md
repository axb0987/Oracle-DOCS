# Starting an Instance
- Source: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-start-instance.htm
- Fetched: 2026-09-05 01:52 CDT

# Starting an Instance

Start a Compute instance.

- [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-start-instance.htm#)
- [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-start-instance.htm#)
- [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/restartinginstance-start-instance.htm#)
- 

- Navigate to the Compute Instances list page. If you need help finding the list page, see[Listing Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/../Tasks/list-instances.htm).
- From the Actions menu (three dots) for the instance, select Start .
- 

Use the[instance action](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/action.html)command and required parameters to start an instance:

```

```

For a complete list of parameters and values for CLI commands, see the[CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/).
- 

For information about using the API and signing requests, see[REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)and[Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).

Use the[InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction)operation to start an instance, passing the value`START`
