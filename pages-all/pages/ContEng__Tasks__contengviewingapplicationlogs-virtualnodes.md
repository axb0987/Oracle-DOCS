# Viewing Application Logs on Virtual Nodes
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingapplicationlogs-virtualnodes.htm
- Fetched: 2026-09-05 01:57 CDT

# Viewing Application Logs on Virtual Nodes

Find out how to view the logs of applications running on virtual nodes in a Kubernetes cluster you've created using Kubernetes Engine (OKE).

Having created a cluster with virtual nodes using Kubernetes Engine, you have two options to access the logs of applications running on the virtual nodes:
- View the stdout and stderr logs from application containers using the`kubectl logs`command.
- Send application logs to a persistent log server for viewing.

## Viewing stdout and stderr logs using the kubectl logs command
To view the stdout and stderr logs from an application's containers using the`kubectl logs`command:
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- In a terminal window, run the`kubectl logs`command by entering:
```

```

For example:
```

```

When the pod contains more than one container, specify the container for which you want to view the logs. For example, if the`myapp`pod has two containers called`nginx`and`logging`and you want to display the logs of the`logging`container, enter:
```

```

## Sending logs to a persistent log server

You can send the logs of applications running on virtual nodes to a remote log server such as OpenSearch, and view the logs on that server. Since virtual nodes do not support the Kubernetes daemonset, you cannot run a logging agent at the node level. Instead, you can run a lightweight logging agent as a sidecar for each of the application's pods. You can use any logging agent that can run as a sidecar on a Kubernetes pod, such as[Fluent Bit](https://github.com/fluent/fluent-bit).

For example, to run Fluent Bit as a sidecar on a pod to send application logs to a remote OpenSearch log server:
- Create a Kubernetes ConfigMap per cluster or per namespace, specifying the Fluent Bit configuration settings to use. In particular, note that you must specify the remote log server's IP address, port number, and authentication parameters.

For example:
```

```

where:
- `host <ip-address>`specifies the IP address of the Opensearch server.
- `port <port-number>`specifies the port of the Opensearch server (9200 by default).
- `HTTP_User <username>`specifies the username for the Opensearch server.
- `HTTP_Passwd <example-password>`specifies the password for the Opensearch server.
- Add a Fluent Bit sidecar to each pod. Note that you must configure all pods with a Fluent Bit sidecar to ensure that application logs are sent to the persistent log destination.
- 

In the`volumes`section of each pod spec, specify:
- An emptyDir where application logs are written, as follows:
```

```

- A reference to the ConfigMap you created previously, as follows:
```

```

- 

In the`containers`section of each pod spec, you must specify that the logging container:
- Uses the`fluent/fluent-bit`image.
- Mounts the`logs`emptyDir and the`fluentbit-config`ConfigMap.

For example:
```

```

Here's an example of a complete pod specification:
```

```
