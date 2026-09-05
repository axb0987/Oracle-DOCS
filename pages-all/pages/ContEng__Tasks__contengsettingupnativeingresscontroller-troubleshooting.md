# Troubleshooting the OCI Native Ingress Controller
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-troubleshooting.htm
- Fetched: 2026-09-05 01:56 CDT

# Troubleshooting the OCI Native Ingress Controller

Find out how to fix common problems with the OCI native ingress controller.

Having installed and configured the OCI native ingress controller (either as a standalone program or as a cluster add-on), use the information in this topic to identify and resolve common problems.

## Reviewing Validation Errors

The OCI native ingress controller identifies conflicting declarations in ingress resource manifests, and outputs validation errors in pod logs.
To review the log of the pod running the OCI native ingress controller:
- Obtain the name of the OCI native ingress controller pod by entering:

```

```

If multiple pod names are returned, identify the leader by reviewing the log for each pod and eliminating pods that are stuck in an acquiring lease state.
- Stream the OCI native ingress controller pod's log by entering:

```

```

For example:
```

```

- Review validation errors output by the OCI native ingress controller by searching the log for`validation failure`
