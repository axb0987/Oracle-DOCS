# Known Issues for Cloud Shell
- Source: https://docs.oracle.com/en-us/iaas/Content/API/Concepts/devcloudshell_known_issues.htm
- Fetched: 2026-09-05 01:35 CDT

# Known Issues for Cloud Shell

Known issues have been identified in Cloud Shell.

## Functions created with 'Generic_X86_ARM' shape for Go and .NET runtimes cannot be deployed using ARM Cloud Shell

Functions created with 'Generic_X86_ARM' shape for Go and .NET runtimes cannot be deployed using ARM Cloud Shell. Details Due to cross compilation issues on OL7 ARM with docker buildx, deploying functions created with the 'Generic_X86_ARM' shape for the Go and .NET runtimes will produce an error similar to the following:
```

```
Workaround Users who have an option to switch their preferred Cloud Shell architecture can choose the`X86_64`architecture from the Cloud Shell`Actions`menu to resolve the error.

## Gradle is no longer preinstalled in Cloud Shell

Gradle is no longer pre-installed in Cloud Shell. Details Gradle is no longer pre-installed in Cloud Shell. Workaround Gradle can be downloaded from[https://services.gradle.org/distributions](https://services.gradle.org/distributions)and installed in the home directory. For example, to install 8.0.2 version of Gradle, execute the below commands in Cloud Shell:
```

```

To verify the installation is successful, run the following command:
```

```
This should display output similar to the following:
```

```

## Go SDK cannot automatically find some regions while running in Cloud Shell

Details: Due to some issues with one of its dependencies, the Go SDK feature which allows customers to automatically use new realms which might be unknown to the SDK is not functioning from within Cloud Shell.
Attempting to run code in Cloud Shell that uses this feature will result in the following error message:
```

```

Workaround: To resolve this issue, enable resolving regions using the instance metadata service for Go SDK. For more information, see:[Adding Regions](https://docs.oracle.com/iaas/Content/API/Concepts/sdk_adding_new_region_endpoints.htm)
