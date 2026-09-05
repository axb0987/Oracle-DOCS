# Start and Stop App Gateway
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/start-and-stop-app-gateway.htm
- Fetched: 2026-09-05 02:18 CDT

# Start and Stop App Gateway

You can start and stop App Gateway server and App Gateway agent using scripts, or using the services installed in the server where your App Gateway runs.

## Using a Script to Start and Stop App Gateway

start and stop the App Gateway server and agent using scripts provided in the server. Sign in to the App Gateway server and then run the following command:

- To start App Gateway server.

```

```

- To start App Gateway agent.

```

```

- To stop App Gateway server.

```

```

- To stop App Gateway agent.

```

```

When you start the App Gateway server, App Gateway contacts IAM to retrieve the port number you configured during the App Gateway registration in the IAM Console. The App Gateway server starts using this port number.

The App Gateway agent is responsible for synchronizing the App Gateway configuration (hosts and applications) from IAM to the App Gateway server.

To check the running status of the App Gateway server, run the following command:`/scratch/oracle/cloudgate/home/bin/cg-status`

## Using the Service to Start and Stop App Gateway

You can start and stop the App Gateway server and agent as services running on the server. Sign in to the App Gateway server and then run the following command:

- To start App Gateway server.

```

```

- To start App Gateway agent.

```

```

- To stop App Gateway server.

```

```

- To stop App Gateway agent.

```

```

To check the running status of the App Gateway server, run the following command:`/scratch/oracle/cloudgate/home/bin/cg-status`
