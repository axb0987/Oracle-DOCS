# OCI Functions Resiliency, Availability, Concurrency, and Scalability
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsavailability.htm
- Fetched: 2026-09-05 02:07 CDT

# OCI Functions Resiliency, Availability, Concurrency, and Scalability

Find out how OCI Functions enables you to meet requirements for resiliency, availability, concurrency, and scalabilty.

## Resiliency and Availability

Resiliency and availability refers to the ability of a system to continue operating, despite the failure or sub-optimal performance of some of its components.

In the case of OCI Functions:
- The control plane is a set of components that manages function definitions.
- The data plane is a set of components that executes functions in response to invocation requests.

For resiliency and high availability, both the control plane and data plane components are distributed across different availability domains and fault domains in a region. If one of the domains ceases to be available, the components in the remaining domains take over to ensure that function definition management and execution are not disrupted.

When functions are invoked, they run in the subnets specified for the application to which the functions belong. For resiliency and high availability, best practice is to specify a regional subnet for an application (or alternatively, multiple AD-specific subnets in different availability domains). If an availability domain specified for an application ceases to be available, OCI Functions runs functions in an alternative availability domain.

## Concurrency and Scalability

Concurrency refers to the ability of a system to run multiple operations in parallel using shared resources. Scalability refers to the ability of the system to scale capacity (both up and down) to meet demand.

In the case of Functions, when a function is invoked for the first time, the function's image is run as a container on an instance in a subnet associated with the application to which the function belongs. When the function is executing inside the container, the function can read from and write to other shared resources and services running in the same subnet (for example, Database as a Service). The function can also read from and write to other shared resources (for example, Object Storage), and other Oracle Cloud Services.

If OCI Functions receives multiple calls to a function that is currently executing inside a running container, OCI Functions automatically and seamlessly scales horizontally to serve all the incoming requests. OCI Functions starts multiple Docker containers, up to the limit specified for your tenancy. The default limit is 60 GB of RAM reserved for function execution per availability domain, although you can request an increase to this limit. Provided the limit is not exceeded, there is no difference in response time (latency) between functions executing on the different containers.
