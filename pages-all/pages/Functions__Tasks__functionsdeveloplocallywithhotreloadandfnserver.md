# Developing Functions Locally with Rapid Iteration Using Fn Server
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsdeveloplocallywithhotreloadandfnserver.htm
- Fetched: 2026-09-05 02:08 CDT

# Developing Functions Locally with Rapid Iteration Using Fn Server

Find out how to use Fn Server and`fn watch`to automatically redeploy functions locally when project files change.

OCI Functions is based on the open source Fn Project. The Fn Project provides the Fn Server, which you can run locally to develop and test functions before deploying them to Oracle Cloud Infrastructure. Running Fn Server locally provides an environment in which you can build, deploy, invoke, and manage functions on your local machine.

When developing functions locally with Fn Server, you often repeat the same cycle: edit code, redeploy the function locally, and invoke the function to verify the change. You can use the`fn watch`command to automate part of this cycle. The command watches your function project files and redeploys the function locally whenever changes are detected.

The`fn watch`command is intended for local development only. It redeploys functions to the local Fn Server by running`fn deploy --app <app> --local`, and does not push images to remote registries. Additional file changes that happen while a deployment is in progress are ignored until the deployment finishes. To stop watching for changes, press Ctrl+C.

Before you begin, ensure that:
- The Fn Project CLI is installed and includes support for the`fn watch`command
- You have created a local application for the function
- You have a function directory that contains a`func.yaml`file

## Developing Functions Locally with Automatic Redeployment

- Log in to your local environment.
- Install and start Docker by following the instructions in[1. Install and start Docker](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost_topic_install_docker)in the[Functions QuickStart on Local Host](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost).

A local container engine is required to build and run functions locally. If your environment uses a Docker-compatible alternative (such as Podman Desktop or Rancher Desktop), you can use that instead.
- Install the Fn Project CLI by following the instructions in[3. Install Fn Project CLI](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost_topic_install_fn_cli)in the[Functions QuickStart on Local Host](https://docs.oracle.com/en-us/iaas/Content/Functions/Tasks/functionsquickstartlocalhost.htm#functionsquickstartlocalhost).
- 

In a terminal window, start Fn Server to run functions locally by entering:
```

```

- 

Open an existing function directory, or initialize a new function. For example, by entering:
```

```

```

```

The function directory must contain a`func.yaml`file.
- 

If necessary, create an application to contain the function. For example, by entering:
```

```

- 

Deploy the function locally once. For example, by entering:
```

```

The command builds the function image and deploys it to the local Fn Server.
- 

Start watch mode from the function project directory. For example, by entering:
```

```

The`fn watch`command recursively watches files under the current directory.
- 

Edit the function code and save your changes.

When`fn watch`detects the saved changes, it automatically redeploys the function locally by running:
```

```

The updated function is then available for local invocation.
- 

Invoke the function and verify the change. For example, by entering:
```

```

- When you have finished testing, stop watch mode by pressing Ctrl+C.

Using this workflow, you can reduce the time spent manually redeploying functions during local development and quickly verify changes by invoking the updated function.

## Ignoring Files and Directories with Automatic Redeployment

By default,`fn watch`ignores changes in the following directories:
- `.git`
- `.fn`
- `node_modules`
- `target`
- `dist`
- `vendor`

To ignore additional files or directories, create a`.fnignore`file in the watched directory. Add one pattern per line.

For example:
```

```

You can also specify ignore rules when starting watch mode by entering:
```

```

## Controlling Redeploy Timing

To avoid repeated redeploys while files are changing quickly,`fn watch`uses a debounce timer. The default debounce time is`500ms`.

To specify a different debounce time, use the`--debounce`option by entering:
```

```

## Troubleshooting Automatic Redeployment

Changes are not redeployed automatically

Cause:`fn watch`is not running from the function project directory, the directory does not contain`func.yaml`, or the changed file is ignored by default or by an ignore rule.

Action: Start`fn watch --app <application-name>`from the function project directory. Confirm that the directory contains`func.yaml`. Check whether the changed file is under an ignored directory such as`.git`,`.fn`,`node_modules`,`target`,`dist`, or`vendor`, or whether it matches a pattern in`.fnignore`or an`--ignore`option.

The function is redeployed repeatedly while files are being updated

Cause: Multiple file changes are occurring in quick succession, such as changes caused by an IDE, formatter, build tool, or dependency manager.

Action: Increase the debounce interval by using the`--debounce`option. For example, enter`fn watch --app myapp --debounce 2s`.

File changes are ignored during a deployment

Cause: Additional file changes that happen during an ongoing deployment are ignored until that deployment finishes.

Action: Wait for the current deployment to finish, then save the file again or make another change to trigger a new redeploy.

The function cannot be invoked after automatic redeployment

Cause: Fn Server is not running locally, the local application was not created, or the redeployment failed.

Action: Confirm that Fn Server is running by starting it with`fn start`. Confirm that the application exists, for example by creating it with`fn create app <application-name>`if necessary. Review the`fn watch`output for deployment errors, then invoke the function again.

Local watch mode pushes images to a remote registry

Cause: The function was deployed separately without local deployment, or a different workflow is being used outside`fn watch`.

Action: Use`fn watch --app <application-name>`for local watch mode. The command redeploys using`fn deploy --app <application-name> --local`
