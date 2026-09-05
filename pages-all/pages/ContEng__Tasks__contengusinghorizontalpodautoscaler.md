# Using the Kubernetes Horizontal Pod Autoscaler
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusinghorizontalpodautoscaler.htm
- Fetched: 2026-09-05 01:57 CDT

# Using the Kubernetes Horizontal Pod Autoscaler

Find out how to use the Kubernetes Horizontal Pod Autoscaler to automatically scale the number of pods on a cluster you've created using Kubernetes Engine (OKE).

You can use the Kubernetes Horizontal Pod Autoscaler to automatically scale the number of pods in a deployment, replication controller, replica set, or stateful set, based on that resource's CPU or memory utilization, or on other metrics. The Horizontal Pod Autoscaler can help applications scale out to meet increased demand, or scale in when resources are no longer needed. You can set a target metric percentage for the Horizontal Pod Autoscaler to meet when scaling applications. For more information, see[Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)in the Kubernetes documentation.

The Horizontal Pod Autoscaler is a standard API resource in Kubernetes that requires the installation of a metrics source, such as the Kubernetes Metrics Server, in the cluster. For more information, see[Deploying the Kubernetes Metrics Server on a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeployingmetricsserver.htm).

## Notes about the Horizontal Pod Autoscaler

Note the following:
- The Kubernetes Metrics Server only supports scaling based on CPU and memory utilization. Other implementations of the Kubernetes Metrics API support scaling based on custom metrics. Refer to the Kubernetes documentation for a list of alternative implementations (see[Implementations](https://github.com/kubernetes/metrics/blob/master/IMPLEMENTATIONS.md#custom-metrics-api)), and for more information about scaling based on custom metrics (see[Autoscaling on multiple metrics and custom metrics](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/#autoscaling-on-multiple-metrics-and-custom-metrics)).
- You can scale applications manually by updating manifest files, without using the Horizontal Pod Autoscaler.
- You can use the Kubernetes Horizontal Pod Autoscaler with both managed node pools and virtual node pools.

## Working with the Horizontal Pod Autoscaler

The instructions below are based on the[Horizontal Pod Autoscaler Walkthrough](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale-walkthrough/)topic in the Kubernetes documentation. They describe how to:
- Verify that the Kubernetes Metrics Server has been installed on a cluster.
- Deploy a sample php-apache web server.
- Create a Horizontal Pod Autoscaler resource that will scale based on CPU utilization.
- Start generation of a sample load.
- View the scaling operation in action.
- Stop the sample load generation.
- Clean up, by removing the php-apache web server and the Horizontal Pod Autoscaler.

### Step 1: Verify the Kubernetes Metrics Server Installation
- 
If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See[Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/../Tasks/contengdownloadkubeconfigfile.htm).
- 

Confirm that the Kubernetes Metrics Server has been deployed successfully on the cluster and is available by entering:

```

```

If the command returns a `Not Found` error, then you must deploy the Kubernetes Metrics Server on the cluster before proceeding. See[Deploying the Kubernetes Metrics Server on a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeployingmetricsserver.htm).

### Step 2: Deploy a Sample Application

Deploy a simple Apache web server application by entering:

```

```

The output from the above command confirms the deployment:
```

```

The Apache web server pod that is created from the manifest file:
- Has a 500m CPU limit, which ensures the container will never use more than 500 millicores, or 1/2 of a core.
- Has a 200m CPU request allowance, which allows the container to use 200 millicores of CPU resources, or 1/5 of a core.

### Step 3: Create a Horizontal Pod Autoscaler Resource
- 

Create a Horizontal Pod Autoscaler resource to maintain a minimum of 1 and a maximum of 10 replicas, and an average CPU utilization of 50%, by entering:

```

```

The output from the above command confirms the Horizontal Pod Autoscaler has been created.
```

```

The command creates a Horizontal Pod Autoscaler for the Apache web server deployment that:
- Maintains a minimum of 1 and a maximum of 10 replicas of the previously created pods controlled by the Apache web server deployment.
- Increases and decreases the number of replicas of the deployment to maintain an average CPU utilization of 50% across all pods.

If the average CPU utilization falls below 50%, the Horizontal Pod Autoscaler tries to reduce the number of pods in the deployment to the minimum (in this case, 1). If the average CPU utilization goes above 50 percent, the Horizontal Pod Autoscaler tries to increase the number of pods in the deployment to the maximum (in this case, 10). For more information, see[How does the Horizontal Pod Autoscaler work?](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#how-does-the-horizontal-pod-autoscaler-work)in the Kubernetes documentation.

For more information about the`kubectl autoscale`command, see[autoscale](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#autoscale)in the Kubernetes documentation.
- 

After a minute, confirm the current status of the Horizontal Pod Autoscaler by entering:

```

```

The output from the above command shows the current status:
```

```

The`TARGETS`column shows the average CPU utilization across all pods controlled by the Apache web server deployment. Since no requests are being sent to the server, the above example shows the current CPU utilization is 0%, compared to the target utilization of 50%. Note that you might see different numbers, depending on how long you wait before running the command.

### Step 4: Start Sample Load Generation
- 

Run a container with a busybox image to create a load for the Apache web server by entering:

```

```

- 

Generate a load for the Apache web server that will cause the Horizontal Pod Autoscaler to scale out the deployment by entering:

```

```

### Step 5: View the Scaling Operation
- 

After a minute, open a new terminal window and confirm the current status of the Horizontal Pod Autoscaler by entering:

```

```

The output from the above command shows the current status:
```

```

In the above example, you can see the current CPU utilization has increased to 250%, compared to the target utilization of 50%. Note that you might see different numbers, depending on how long you wait before running the command.

To achieve the utilization target of 50%, the Horizontal Pod Autoscaler will have to increase the number of replicas to scale out the deployment.
- 

After another few minutes, view the increased number of replicas by re-entering:

```

```

The output from the above command shows the current status:
```

```

In the above example, you can see that the Horizontal Pod Autoscaler has resized the deployment to 5 replicas, and the utilization target of 50% has been achieved. Note that you might see different numbers, depending on how long you wait before running the command.
- 

Verify the deployment has been scaled out by entering:

```

```

The output from the above command shows the current status:
```

```

Note that you might see different numbers, depending on how long you wait before running the command.

### Step 6: Stop Sample Load Generation
- In the terminal window where you created the container with the busybox image and generated the load for the Apache web server:
- Terminate the load generation by pressing`Ctrl+C`
- Close the command prompt by entering:

```

```

The output from the above command confirms the session has ended:
```

```

- After a minute, confirm the current status of the Horizontal Pod Autoscaler by entering:

```

```

The output from the above command shows the current status:
```

```

In the above example, you can see the current CPU utilization has reduced to 0%, compared to the target utilization of 50%. However, there are still 5 replicas in the deployment. Note that you might see different numbers, depending on how long you wait before running the command.
- 

After another few minutes, view the reduced number of replicas by re-entering:

```

```

The output from the above command shows the current status:
```

```

In the above example, you can see that the Horizontal Pod Autoscaler has resized the deployment to 1 replica.

Be aware that it will take time for the replica count to reduce to 1. Five minutes is the default timeframe for scaling in. Note that you might see different numbers, depending on how long you wait before running the command.
- 

Verify the deployment has been scaled in by entering:

```

```

The output from the above command shows the current status:
```

```

Note that you might see different numbers, depending on how long you wait before running the command.

### Step 7: Clean Up
- 

Delete the Horizontal Pod Autoscaler by entering:

```

```

Note that when you delete a Horizontal Pod Autoscaler, the number of replicas remains the same. A deployment does not automatically revert back to the state it had prior to the creation of the Horizontal Pod Autoscaler.
- 

Delete the Apache web server deployment by entering:

```

```
