# Rotating Key References
- Source: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Tasks/ekms_rotating_key_references.htm
- Fetched: 2026-09-05 02:35 CDT

# Rotating Key References

Learn how to rotate key references in OCI External Key Management

## Pointing to the latest key version in a third-party key manager

Use this procedure when you want the OCI key reference to point to the latest key version in the third-party key manager. This is a two-step process. After rotating the key in the third-party key manager, you must also rotate the key reference in OCI so that OCI points to the latest key version.

- In the third-party key manager, rotate the key.
- In OCI, rotate the key reference without providing the external key version ID.

By default, when the external key version ID is not provided, the OCI key reference points to the latest key version available in the third-party key manager.

## Pointing to a specific key version in a third-party key manager

Use this procedure when you want the OCI key reference to explicitly bind to a specific key version in the third-party key manager.

- In the third-party key manager, copy the required key version ID.
-
