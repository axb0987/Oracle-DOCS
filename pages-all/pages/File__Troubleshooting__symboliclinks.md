# Symbolic Links (Symlinks) Produce Errors
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/symboliclinks.htm
- Fetched: 2026-09-05 02:06 CDT

# Symbolic Links (Symlinks) Produce Errors

The File Storage service fully supports the use of symbolic links. However, symbolic links are interpreted by the client and symlinks that point outside of the mounted File Storage system may be interpreted differently by each client and lead to unexpected results, such as broken links or pointing to the wrong file. Symbolic link targets that work on one client might be broken on another due to differences in file system layout or because clients mounted the file system using different mount targets.

Snapshots can also break symbolic links that point to a target outside the file system's root directory. This is because when you create a snapshot of a file system, it becomes available as a subdirectory of the .snapshot directory.

To minimize these potential issues, use a relative path as the target path when creating a symbolic link to a file in the network file system. Also, ensure that relative paths do not point to a target path outside the File Storage service root directory except when the target is on the local machine. If you must use a symbolic link that points to a target path outside the file system, use an absolute path starting with the client's root directory.

For example:
- Pointing to "/user/bin/example" works .
- Pointing to "/yourmountpoint/..." does not work.
-
