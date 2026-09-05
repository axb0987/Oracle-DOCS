# Input/output Error When Listing Snapshots
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/input-output-error-listing-snapshots.htm
- Fetched: 2026-09-05 02:06 CDT

# Input/output Error When Listing Snapshots

When listing the contents of the`.snapshots`folder on Linux, the system returns an "Input/output error."

Cause: Snapshots of the file system are listed in the`.snapshots`folder as directory names. If the snapshot name contains characters that result in an invalid file name (for example, "/" ), Linux cannot list them and returns "Input/output error" instead.
