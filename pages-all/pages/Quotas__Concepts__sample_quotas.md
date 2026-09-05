# Sample Quotas
- Source: https://docs.oracle.com/en-us/iaas/Content/Quotas/Concepts/sample_quotas.htm
- Fetched: 2026-09-05 02:53 CDT

# Sample Quotas

Learn about sample quotas with specific examples of how to use quota policies.

Notable real-word examples using quota policies can be:
- Create a compartment for a developer. Block them from using everything except 1 DBaaS instance, 10 standard2 VM cores, and 50 GB of block storage.
- Create a compartment for the HR department, for permission matters only. Block all services.
- Create a compartment for the team that manages data for international customers in a country's data center. In this compartment, users can only create VMs in that country, but not in other data centers.

The following are specific examples of how to use quota policies:
- 

Disallow use of outbound email or notifications :
```

```

- 

Limit use of expensive resources such as`exadata`to 1 in the entire tenancy :
```

```

- 

Limit cores for VM.Standard2 and BM.Standard2 compute series to 10 in all compartments except the`productionApp`compartment :
```

```

- 

Set the quota for the VM.Standard.E4 and BM.Standard.E4 compute series to 240 OCPUs (cores) in each AD on compartment`MyCompartment`in the US West (Phoenix) region :
```

```

- 

Target a quota for an entire tenancy : Using keyword`in tenancy`at the end of a quota statement enforces the quota for entire tenancy. In this example, the total number of OCPUs for shapes in the VM.Standard2 and BM.Standard2 series are restricted to 240 across the entire tenancy (all regions/all ADs).
```

```

- 

Target a quota for a given compartment : Using the keyword`in compartment`, followed by the compartment name at the end of a quota statement, restricts quota enforcement just to that compartment of the tenancy. In this example, the total number of OCPUs for shapes in the VM.Standard2 and BM.Standard2 series are restricted to 20 for`ItCompartment`.
```

```

- 

Target a quota for specific region or AD : The scope of a quota can be further restricted to the specific region of a tenancy. In this example, the total number of OCPUs for shapes in the VM.Standard2 and BM.Standard2 series are restricted to 20 for only the US West (Phoenix) region.
```

```

- 

Target a specific AD within a region : In the example, the total number of OCPUs for shapes in the VM.Standard2 and BM.Standard2 series are restricted to 20 for only AD 1 within the Phoenix region.
```

```

- 

Target a quota for an entire resource family : You can set a quota for an entire resource family, such as all types of compute-core or all databases.
```

```

- 

Target nested compartments : Quotas can be set on any child compartment in the compartment hierarchy. To target a quota on nested compartments, use the following syntax:`parent:child:another_child`. If a tenancy admin wants to ensure that only the`grand_child`compartment is limited to 10 cores, where the`grand_child`compartment exists in compartment`child`, and which exists in the`parent`compartment, use the corresponding policy.
```

```

- 

Make an allowlist, setting every quota in a family to zero, and then explicitly allocating resources :
```

```

- 

Disallow all resources in a service family except specific resources : This example uses`zero`and`unset`statements to disallow any OCPU shapes, except the VM.Standard2 and BM.Standard2 series.
```

```

- 

Limit creating dense I/O compute resources to only one region :
```

```

You can clear quotas by using an`unset`statement, which removes the quota for a resource. Any limits on this resource will now be enforced by the service limits:
```

```
