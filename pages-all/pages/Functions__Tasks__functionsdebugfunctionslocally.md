# Debugging Functions Locally Using Fn Server
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdebugfunctionslocally.htm
- Fetched: 2026-09-05 02:08 CDT

# Debugging Functions Locally Using Fn Server

Find out how to debug functions locally using Fn Server to test behavior, inspect runtime state, and troubleshoot issues before deploying to OCI.

OCI Functions is based on the open source Fn Project. The Fn Project provides the Fn Server, which you can run locally to develop and test functions before deploying them to Oracle Cloud Infrastructure. Running Fn Server locally provides an environment in which you can deploy, invoke, and manage functions on your local machine.

You can use Fn Server in local debug mode to deploy a function locally and attach a remote debugger to the running function. Local debug mode is supported for Java, Go, and Python functions, and is also available for functions that use a custom Dockerfile. The default local debug port is`5678`.

Before you begin, ensure that:
- You have created a function using the Fn CLI
- You are familiar with deploying and invoking functions

## Debugging Functions Locally

- Log in to your local environment.
- Install and start Docker by following the instructions in[1. Install and start Docker](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost_topic_install_docker)in the[Functions QuickStart on Local Host](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost).

A local container engine is required to build and run functions locally. If your environment uses a Docker-compatible alternative (such as Podman Desktop or Rancher Desktop), you can use that instead.
- Install the Fn Project CLI by following the instructions in[3. Install Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost_topic_install_fn_cli)in the[Functions QuickStart on Local Host](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost).
- 

In a terminal window, start Fn Server in local debug mode by entering:
```

```

The`--local-debug`option starts Fn Server in local debug mode. The`--local-debug-port`option specifies the port on the host machine that a remote debugger uses to attach to the function. If you do not specify`--local-debug-port`, Fn Server uses port`5678`by default.

For example, to use the default local debug port explicitly, enter:
```

```

- 

Open an existing function directory, or initialize a new function by entering:
```

```

```

```

- 

If necessary, create an application to contain the function by entering:
```

```

- 

Deploy the function locally in debug mode by entering:
```

```

For example, to deploy the function using the default debug port, enter:
```

```

When you deploy the function in debug mode, Fn Server builds the Docker image with debug capability, exposes the debug port, and maps the debug port to the local host.
- 

Invoke the function by entering:
```

```

When you invoke the function, the function pauses and waits for a remote debugger to attach.
- 

Attach a debugger to the function by using your preferred development environment.

Configure the debugger to connect to port`5678`, or to the custom port that you specified when you started Fn Server and deployed the function. Add breakpoints in your function code, then start the debug session from your development environment.
- 

Modify the function code and repeat the deploy, invoke, and debug steps as needed.

Redeploy the function locally in debug mode after making changes by entering:
```

```

Using this workflow, you can attach a debugger to locally running functions, inspect runtime state, and validate behavior before deploying to Oracle Cloud Infrastructure.

## Runtime-specific Debugging Examples

The following examples show how to attach debuggers for common runtimes after you have started Fn Server in local debug mode and deployed the function with`--local-debug`.

### Java example

Deploy the Java function locally in debug mode by entering:
```

```

Invoke the Java function by entering:
```

```

The function pauses and waits for a debugger to attach. Open the function directory in your Java IDE and create a remote debug configuration that connects to port`5678`, or to the custom port that you specified with`--local-debug-port`. Add a breakpoint in the Java function code, then start the debug session. The breakpoint is triggered when the function continues.

### Go example

Deploy the Go function locally in debug mode by entering:
```

```

Invoke the Go function by entering:
```

```

The function pauses and waits for a debugger to attach. Open the function directory in your Go IDE and configure the debugger to connect to port`5678`, or to the custom port that you specified with`--local-debug-port`. Add a breakpoint in the Go function code, then start the debug session. The breakpoint is triggered when the function continues.

### Python example

Deploy the Python function locally in debug mode by entering:
```

```

Invoke the Python function by entering:
```

```

The function pauses and waits for a debugger to attach. Open the function directory in your Python IDE and configure the debugger to connect to port`5678`, or to the custom port that you specified with`--local-debug-port`. Make sure that the local project path points to the function directory. Add a breakpoint in the Python function code, then start the debug session. The breakpoint is triggered when the function continues.

### Custom Dockerfile example

For functions that use a custom Dockerfile, configure the image so that Fn Server can attach a remote debugger when the function container starts.

To enable local debugging with a custom Dockerfile:
- Install the language-specific debugger in the function image. For example, use Delve for Go or`debugpy`for Python.
- Start the debugger in the container on port`5678`. The debugger inside the container must listen on port`5678`. Fn Server maps that port to the host port specified by`--local-debug-port`. If you do not specify`--local-debug-port`, Fn Server maps to port`5678`on the host by default.
- Add any language-specific Dockerfile settings required for debugging. For example, Go functions require build flags that enable debugging.

For example, a custom Dockerfile for a Go function can build the function with debugging enabled and start Delve on port`5678`:
```

```

After updating the Dockerfile, deploy and invoke the function in local debug mode, then attach your debugger to port`5678`, or to the custom host port that you specified with`--local-debug-port`.

## Troubleshooting Local Function Debugging using Fn Server

Debugger cannot attach to the function

Cause: Fn Server was not started in local debug mode, the function was not deployed with local debug options, the debugger is connecting to the wrong port, or the runtime is not configured for remote debugging.

Action: Verify that you started Fn Server with`fn start --local-debug --local-debug-port 5678`and deployed the function with`fn deploy --application <application-name> --local-debug --local-debug-port 5678`. Confirm that your debugger is connecting to port`5678`, or to the custom port that you specified.

Function does not pause and wait for a debugger

Cause: The function was not deployed in local debug mode, or the runtime/debugger configuration does not cause the function to wait for debugger attachment.

Action: Redeploy the function using`--local-debug --local-debug-port 5678`, invoke the function again, and confirm from the Fn Server output that the function is waiting for a debugger.

Port 5678 is already in use

Cause: Another process is already listening on the default local debug port.

Action: Stop the process that is using port`5678`, or specify a different host port with`--local-debug-port`. If you use a custom Dockerfile, keep the debugger inside the container listening on port`5678`, because Fn Server maps that container port to the host port that you specify.

Custom Dockerfile function cannot be debugged

Cause: The custom image does not include the required language-specific debugger, the debugger is not started when the container starts, or the debugger is not listening on port`5678`inside the container.

Action: Update the Dockerfile to install the debugger, start the debugger on port`5678`, and include any required language-specific debug settings. For Go, build the binary with debug flags such as`-gcflags="all=-N -l"`.

Function cannot access Oracle Cloud Infrastructure services

Cause: Resource principal authentication is not available when running functions locally.

Action: Use API key-based authentication or mock external dependencies while debugging locally. Validate full integration after deploying the function to Oracle Cloud Infrastructure.

Function behaves differently after deployment

Cause: Environment variables, IAM configuration, networking, or runtime settings can differ between the local environment and the deployed function environment.
