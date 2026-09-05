# Access to Kubernetes-mounted File System is Denied
- Source: https://docs.oracle.com/en-us/iaas/Content/File/Troubleshooting/access-denied-k8-mounted-fss.htm
- Fetched: 2026-09-05 02:05 CDT

# Access to Kubernetes-mounted File System is Denied

When a non-root user tries to write to File Storage directories, they receive a "permission denied" error.

Symptom :

A Kubernetes pod cannot write to the File Storage file system after it was mounted using`volumeMounts`. Updating pod security settings using`securityContext`,`runAsUser`, and`fsGroup`does not resolve the issue.

Cause :

The Kubernetes pod mounted the File Storage file system as the "root" user with root permissions. This restricts non-root users from writing to the file system and causes a permissions error.

Solution :

Use[`initContainers`](https://kubernetes.io/docs/concepts/workloads/pods/init-containers/)to mount the file system and run`chown`to change ownership so that pod members can write to the file system. For more information, see[Configure Pod Initialization](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-initialization/)
