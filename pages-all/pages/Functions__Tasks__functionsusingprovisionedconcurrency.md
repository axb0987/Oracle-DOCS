# Reducing Initial Latency Using Provisioned Concurrency
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsusingprovisionedconcurrency.htm
- Fetched: 2026-09-05 02:09 CDT

# Reducing Initial Latency Using Provisioned Concurrency

Find out how to use provisioned concurrency to minimize initial delays when invoking functions in OCI Functions.

When a function is invoked for the first time (referred to as a 'cold start'), OCI Functions provisions the function invocation with the execution infrastructure it requires. The execution infrastructure includes the compute and network resources necessary to successfully invoke the function. The initial provisioning, and hence the response to the first invocation, might take some variable amount of time (potentially several seconds, or longer). The initial function invocation's execution infrastructure is retained for a period of time (referred to as the 'idle time'), for use by subsequent invocations of the same function. When a subsequent function invocation is able to make use of existing infrastructure (referred to as a 'hot start'), there is usually a sub-second response time to the function invocation.

It's common that you'll want consistent, sub-second, responses to function invocations. To minimize any latency associated with initial provisioning and to ensure hot starts, you can enable provisioned concurrency for a function. Provisioned concurrency is the ability of OCI Functions to always have available the execution infrastructure for at least a certain minimum number of concurrent function invocations. Provisioned concurrency is measured in 'provisioned concurrency units' (PCUs). The total number of PCUs available depends on the size of the function, the tenancy limit, and whether provisioned concurrency has been enabled for other functions in the tenancy.

To use provisioned concurrency, you specify the number of PCUs required for the function. Typically, you'll want to specify a similar number of PCUs to the number of concurrent function invocations you expect. The available memory you specify for a function determines both the smallest number of PCUs you can specify for that function, and the increments by which you can increase the number of PCUs, as follows:

Memory Minimum number of PCUs: Increase PCUs in increments of: Example
128 MB 40 40 80
256 MB 20 20 60
512 MB 10 10 50
1024 MB 10 10 40
2048 MB 10 10 30
3072 MB 10 10 30

As you can see, the PCUs value must always be a multiple of 10. If available memory is 256 MB, the PCUs value must be a multiple of 20. If available memory is 128 MB, the PCUs value must be a multiple of 40.

You can specify PCUs for a function in different ways:
- Using the Console when creating a new function based on an existing Docker image that has already been pushed to the Docker registry (see[Creating Functions from Existing Docker Images](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionscreatingfunctions.htm)).
- Using the Fn Project CLI to create or update a function, and specifying the optional`--provisioned-concurrency`option, in the format:
```

```

where:
- `none`indicates that provisioned concurrency is not to be used
- `constant:<value>`indicates that provisioned currency is to be used. In this case,`<value>`is the minimum number of concurrent function invocations.

For example:
```

```

```

```

```

```

- Using the Oracle Cloud Infrastructure CLI to create or update a function, and specifying the optional`--provisioned-concurrency`option, in the format:
```

```

where:
- `\"strategy\": \"<CONSTANT|NONE>\"`indicates whether to use provisioned concurrency (in which case, specify`CONSTANT`), or not to use provisioned concurrency (in which case, specify`NONE`).
- `\"count\": <value>`indicates the minimum number of concurrent function invocations, when`\"strategy\": \"CONSTANT\"`

For example:

```

```

```

```

Note that the`--provisioned-concurrency`parameters must be in valid JSON format, which depends on the platform you are using (see[Managing CLI Input and Output](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output)). You can provide the parameters as a string at the command line, as a file, or as a command line string and as a file.
- Using the API (see[CreateFunction](https://docs.oracle.com/iaas/api/#/en/functions/latest/Function/CreateFunction)and[UpdateFunction](https://docs.oracle.com/iaas/api/#/en/functions/latest/Function/UpdateFunction)
