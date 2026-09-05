# Examples
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/typescriptsdkexamples.htm
- Fetched: 2026-09-05 01:37 CDT

# Examples

This topic describes how to download and run OCI SDK for TypeScript and JavaScript usage examples.

GitHub

Examples of SDK usage can be found on[GitHub](https://github.com/oracle/oci-typescript-sdk/), including:
- [Example: Create an instance](https://github.com/oracle/oci-typescript-sdk/tree/master/examples/typescript/launch_instance.ts)
- [Example: Invoke Oracle Function](https://github.com/oracle/oci-typescript-sdk/tree/master/examples/typescript/invoke-function.ts)
- [Example: Move Compartment](https://github.com/oracle/oci-typescript-sdk/tree/master/examples/typescript/move-compartment.ts)

The examples are also in the downloadable .zip file for the SDK. Examples for older versions of the SDK are in the downloadable .zip for the specific version, available on[GitHub](https://github.com/oracle/oci-typescript-sdk/releases).

If you'd like to see another example not already covered, file a[GitHub issue](https://github.com/oracle/oci-typescript-sdk/issues).

SDK Reference

In addition to the examples found on GitHub, the[SDK for TypeScript and JavaScript API reference](https://docs.oracle.com/iaas/tools/typescript/latest/globals.html)contains code examples that you can copy and modify to run in your own environment.

## Running Examples

Note  
  
If you're using Windows, you'll need to install[Git Bash for Windows](https://git-scm.com/download/win)before running the following commands.
- Git clone the SDK for TypeScript and JavaScript`git clone https://github.com/oracle/oci-typescript-sdk.git`
- Change to the directory where you installed the`oci-typescript-sdk`repository.
- Run`npm install`
- Run`npm run build`
- If you do not have typescript globally installed, run:
```

```

Note  
  
We've tested and support TypeScript version 4.1.3 with the OCI SDK for TypeScript and JavaScript. We cannot guarantee full support for other versions of TypeScript.
- You can optionally install ts-node globally to make it easier to run examples:
```

```

- Create your configuration file in your home directory. See[SDK and CLI Configuration File](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/sdkconfig.htm)for more information.
- Change directory into the TypeScript example folder to run TypeScript examples. For example:
```

```

- Run any of the examples.
For example, if you're running ts-node:
```

```

If you're not running ts-node:
```

```

- Some examples are available in JavaScript. They are located in the`oci-typescript-sdk/examples/javascript`folder. To run the JavaScript equivalent of the above example:
```

```
