# OCI Functions Concepts
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/functionsconcepts.htm
- Fetched: 2026-09-05 02:07 CDT

# OCI Functions Concepts

Find out about the key concepts you need to understand before using OCI Functions.

## Functions Developers

Oracle Cloud Infrastructure users who use OCI Functions to create and deploy functions are referred to as 'functions developers'. To use OCI Functions, functions developers must have Oracle Cloud Infrastructure user accounts. Their user accounts must belong to groups to which appropriate policies grant access to function-related resources.

See[Creating Groups and Users to use with OCI Functions, if they don't exist already](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionscreatinggroupsusers.htm).

## Applications

In OCI Functions, an application is:
- a logical grouping of functions
- a way to allocate and configure resources for all functions in the application
- a common context to store configuration variables that are available to all functions in the application
- a way to ensure function runtime isolation

When you define an application in OCI Functions, you specify the subnets in which to run the functions in the application. You also specify whether to enable logging for the functions in the application.

When functions from different applications are invoked simultaneously, OCI Functions ensures these function executions are isolated from each other.

Best practice is to group multiple functions in a single application for better efficiency and performance.

OCI Functions shows applications and their functions in the Console.

See[Creating Applications](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionscreatingapps.htm).

## Functions

In OCI Functions, functions are:
- small but powerful blocks of code that generally do one simple thing
- grouped into applications
- stored as Docker images in a specified Docker registry
- invoked in response to a CLI command or signed HTTP request

When you deploy a function to OCI Functions using the Fn Project CLI, the function is built as a Docker image and pushed to a specified Docker registry.

A definition of the function is stored as metadata in the OCI Functions server. The definition describes how the function is to be executed and includes:
- the Docker image to pull when the function is invoked
- the maximum length of time the function is allowed to execute for
- the maximum amount of memory the function is allowed to consume

OCI Functions shows functions, and the applications into which they are grouped, in the Console.

See[Creating, Deploying, and Invoking a Helloworld Function](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionscreatingfirst.htm).

## Invocations

In OCI Functions, a function's code is run (or executed) when the function is called (or invoked). You can invoke a function that you've deployed to OCI Functions from:
- The Fn Project CLI.
- The Oracle Cloud Infrastructure SDKs.
- Signed HTTP requests to the function's invoke endpoint. Every function has an invoke endpoint.
- Other Oracle Cloud services (for example, triggered by an event in the Events service) or from external services.

When a function is invoked for the first time, OCI Functions pulls the function's Docker image from the specified Docker registry, runs it as a Docker container, and executes the function. If there are subsequent requests to the same function, OCI Functions directs those requests to the same container. After a period being idle, the Docker container is removed.

OCI Functions shows information about function invocations in metric charts.

See[Invoking Functions](https://docs.oracle.com/en-us/iaas/Content/Functions/Concepts/../Tasks/functionsinvokingfunctions.htm).

## Triggers

A trigger is the result of an action elsewhere in the system, that sends a request to invoke a function in OCI Functions. For example, an event in the Events service might cause a trigger to send a request to OCI Functions to invoke a function. Alternatively, a trigger might send regular requests to invoke a function on a defined, time-based schedule.
