# Protecting Kubernetes Clusters from Resource Leaks
- Source: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprotectingclustersfromresourceleaks.htm
- Fetched: 2026-09-05 01:55 CDT

# Protecting Kubernetes Clusters from Resource Leaks

Find out how to prevent system instability by protecting the Kubernetes clusters you've created using Kubernetes Engine (OKE) from leaking resources.

The control plane of a Kubernetes cluster can become unstable when an application deployed on the cluster triggers unintended or uncontrolled resource creation. As compute and memory resources become exhausted, the cluster's performance and availability are severely impacted.

To maintain the availability of control planes, Kubernetes Engine can protect clusters you've created from such resource 'leakage' using a validating admission webhook named`oke-resource-leak-protection.cluster.com`. A validating admission webhook is an HTTP callback that receives an admission request from kube-apiserver and sends a response of whether or not kube-apiserver should accept that request.

The`oke-resource-leak-protection.cluster.com`webhook maintains a count of certain types of Kubernetes objects in the cluster. When the webhook receives an admission request for the creation of a new object of a given type, the webhook determines if creating the object would breach an internal limit for objects of that type.

By default, Kubernetes Engine creates the`oke-resource-leak-protection.cluster.com`webhook in clusters that have ten or fewer worker nodes. The webhook:
- rejects requests to create additional pods, if the total number of pods in the cluster would exceed 10,000
- rejects requests to create additional secrets, if the total number of secrets in the cluster would exceed 2,000

When the`oke-resource-leak-protection.cluster.com`webhook rejects requests to create objects, it issues an error message explaining why the creation request has been rejected, similar to the following:
```

```

The error message informs you of a potential resource leak. If you see this message, we recommend you take appropriate action before availability of the cluster's control plane is impacted. For example:
- If the additional object creation requests are not what you intended, examine application code to identify and address the cause of resource leakage.
- If the additional object creation requests are what you intended, disable the default resource leak detection and the validating admission webhook (see[Disabling default resource leak detection](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengprotectingclustersfromresourceleaks.htm#contengprotectingclustersfromresourceleaks__section_disable-leak-detection)).

As alternatives to (or in addition to) using the`oke-resource-leak-protection.cluster.com`webhook to control object creation, you can also protect clusters from resource leaks by:
- creating your own validating admission webhooks (see[ValidatingAdmissionWebhook](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#validatingadmissionwebhook)in the Kubernetes documentation)
- applying Kubernetes resource quotas (see[Resource Quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/)in the Kubernetes documentation)
- applying Kubernetes validating admission policies (see[Validating Admission Policy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)in the Kubernetes documentation)

## Disabling default resource leak detection

To disable resource leak detection and the Kubernetes Engine default validating admission webhook:
- 

Change the value of the`Managed`annotation in the`oke-resource-leak-protection`ConfigMap to specify that you don't want the default validating admission webhook to limit the number of objects in the cluster, by entering:

```

```

- 

Remove the default validating admission webhook by entering:
```

```

## Re-enabling resource leak detection

To re-enable resource leak detection and the validating admission webhook, having previously disabled them:
- 

Change the value of the`Managed`annotation in the`oke-resource-leak-protection`ConfigMap to specify that you want the default validating admission webhook to resume limiting the number of objects in the cluster, by entering:

```

```

If the`oke-resource-leak-protection.oke.com`
