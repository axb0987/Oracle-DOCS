# Differences between OCI Functions and Fn Project
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsdiffswithfn.htm
- Fetched: 2026-09-05 02:07 CDT

# Differences between OCI Functions and Fn Project

Find out about the differences between OCI Functions and Fn Project.

In general, OCI Functions and Fn Project are very similar. However there are some differences, as detailed below.

## Differences in Authentication When Making API Calls

When you use the Oracle Cloud Infrastructure API with OCI Functions, in the request header you have to provide:
- the OCID of the compartment to which the function belongs
- Oracle Cloud Infrastructure authentication details

## Differences When Invoking Functions

To invoke a function deployed to OCI Functions, you have to explicitly specify an Oracle Cloud Infrastructure endpoint (unless you're using the Fn Project CLI).

For example,`https://fht7ns4mn2q.us-phoenix-1.functions.oci.oraclecloud.com/20181201/functions/ocid1.fnfunc.oc1.phx.aaaa____uxoa/actions/invoke`.

You can obtain the appropriate endpoint by making a call to the API, either directly or by using the Fn Project CLI command:

```

```

## Additional Context Configuration Parameters in OCI Functions

As well as supporting Fn Project context configuration parameters, OCI Functions also has some additional parameters, as shown in the following table.

Additional Parameter Set in Value Notes
`provider`A context configuration .yaml file in ~/.fn/contexts`oracle`

Enables OCI Functions rather than Fn Project functionality. When`provider`is set to`oracle`, the following parameters are valid:
- `oracle.compartment-id`
- `oracle.profile`

See[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionscreatefncontext.htm).
`oracle.compartment-id`A context configuration .yaml file in ~/.fn/contexts`<compartment -ocid>`

Specifies the OCID of the Oracle Cloud Infrastructure compartment that owns function-related resources.

See[Creating an Fn Project CLI Context to Connect to Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionscreatefncontext.htm).
`oracle.profile`A context configuration .yaml file in ~/.fn/contexts`<profile-name>`

Specifies which profile to use from the ~/.oci/config file. If not set, the profile named default is used.

See[Setting the Context for the Fn Project CLI Using the oracle.profile Parameter](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionssetoracleprofile.htm)

## Use of Annotations

When you're creating and viewing OCI Functions resources using the Fn Project CLI, you'll typically use parameters to specify values. For example, when using`fn create app <app-name>`to create a new application, you'll normally use the`--subnet-id <subnet-ocid>`parameter to specify the OCID of the subnet in which to run functions.

For advanced use and for backwards compatibility, some Fn Project CLI commands also support the use of annotations to identify and specify associated Oracle Cloud Infrastructure resources.

For example:
- When you're using the Fn Project CLI to create a new application, you can use the`--annotation`parameter to specify the OCID of the subnet in which to run the function, in the format:
```

```

- When you're using the Fn Project CLI to view the properties of a function, the`annotations`element shows the OCID of the compartment that owns the function.
