# Cloning a File System Fails
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/cloning_a_file_system_fails.htm
- Fetched: 2026-09-05 02:05 CDT

# Cloning a File System Fails

Cloning a file system can fail for various regions. Learn how to troubleshoot problems creating a clone.

Symptom 1: Cloning a file system fails with the following error:

"The cloning operation failed because the clone tree has reached the maximum number of clones (10) allowed to concurrently hydrate from a single specified parent. Wait until one or more clones of this parent finish hydrating, and then try again."

Cause 1: The clone tree has reached the maximum size of unhydrated clones descending from the parent you're cloning. See[Cloning Concepts](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/cloningFS.htm#Cloning_Concepts)for a diagram and examples. See[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/cloningFS.htm#Limitations_and_Considerations)for an example of how this value relates to hydrating clones.

Clone tree size can fluctuate while hydration is in progress, causing the cloning operation to fail. For example:

Let's say a root file system (File System A) has two child clones currently hydrating from it. (Clone 1 and Clone 2). Clone 1 has 10 children currently hydrating from it, which is the maximum allowed clone tree size for Clone 1.

If you delete Clone 1, File System A becomes the new parent of the 10 child clones currently hydrating, in addition to Clone 2. Deleting Clone 1 causes File System A to immediately reach the maximum clone tree size of 11.

If you then try to clone File System A, the operation fails because File System A has reached the maximum allowed clone tree size.

Solution 1: Wait until at least one of the parent's descendant clones has finished hydrating, and then try the operation again.

Symptom 2: Cloning a file system fails with the following error:

"The cloning operation failed because the clone tree branch has reached the maximum number of unhydrated clones (5) between the clone and a hydrated ancestor. Wait until a closer ancestor of the clone finishes hydrating, and then try again."

Cause 2: There are too many clones currently hydrating in the clone tree branch between the closest fully hydrated ancestor and the clone you're creating. This attribute is also called clone tree depth . See[Cloning Concepts](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/cloningFS.htm#Cloning_Concepts)for a diagram and examples. See[Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/cloningFS.htm#Limitations_and_Considerations)for an example of how this value relates to hydrating clones.

Solution 2: Wait until at least one closer ancestor of the clone has completed hydrating, and then try the operation again.

Symptom 3: Cloning a file system fails with no specific error.

Cause 3: The file system you're attempting to clone is currently in a DELETING state.

Solution 3: You can't create a clone from a parent file system that's currently being deleted. Clone a child or sibling of the file system instead.

For general information, see[Cloning File Systems](https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/../Tasks/cloningFS.htm)
