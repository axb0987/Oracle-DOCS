# File Storage CREATE API Operations Fail
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/createfilesystem_api_operation_fails.htm
- Fetched: 2026-09-05 02:05 CDT

# File Storage CREATE API Operations Fail

File Storage API resource`create`operations such as`createFileSystem`fail to create resources.

Cause: High volume can cause API calls to fail. If you haven't specified`retry`in your request, the operation isn't tried again, and the resource isn't created.
Solution: Retry the API operation. Use the`opc-retry-token`header in the create resource request. For example:
```

```

See[REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm)
