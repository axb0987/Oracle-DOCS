# Troubleshooting Object Storage Console Connections
- Source: https://docs.oracle.com/en-us/iaas/Content/Object/Troubleshooting/troubleshooting_console_connections.htm
- Fetched: 2026-09-05 02:52 CDT

# Troubleshooting Object Storage Console Connections

Learn troubleshooting solutions for issues you might encounter regarding connecting with the Console.

When the Console displays error messages that begin with "Error retrieving" followed by a resource name, it means that the Console can't connect to the Object Storage APIs to retrieve and display the requested resources. There are many reasons why this can happen. Walk through these steps to find why the Console can't connect to the APIs.

## Step 1: Try to connect to the Object Storage API endpoint in the region containing the buckets you're trying to access using the Console

- Open a browser and to the API endpoint:

```

```
See[Object Storage Service API](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/)for the list of API endpoints. If you can connect to the API endpoint, a JSON object is returned. For example:
```

```

- If you can connect to the API endpoint,[create a support ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
If you can't connect to the API endpoint, continue to[Step 2: Ensure your VPN isn't blocking Console access to the Object Storage APIs](https://docs.oracle.com/en-us/iaas/Content/Object/Troubleshooting/troubleshooting_console_connections.htm#vpn-blocking-console-access).

## Step 2: Ensure your VPN isn't blocking Console access to the Object Storage APIs

- Disconnect from any connected VPNs.
- Open a browser and go to the API endpoint that contains the buckets you are trying to access in the Console:
`https://objectstorage. <region_identifier> .oraclecloud.com`See[API Reference and Endpoints](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/)for the list of API endpoints. If you are able to connect to the API endpoint, a JSON object is returned. For example:
```

```

- If you can connect to the API endpoint, contact your security team about your VPN blocking URL access to the Object Storage APIs.
If you can't connect to the API endpoint, continue to[Step 3: Ensure your Web proxy servers aren't blocking Console access to the Object Storage APIs](https://docs.oracle.com/en-us/iaas/Content/Object/Troubleshooting/troubleshooting_console_connections.htm#web-proxy-console-access).

## Step 3: Ensure your Web proxy servers aren't blocking Console access to the Object Storage APIs

- Disable any configured proxies.
- Open a browser and go to the API endpoint that contains the buckets you are trying to access in the Console:
`https://objectstorage. <region_identifier> .oraclecloud.com`

See[https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/)for the list of API endpoints. If you can connect to the API endpoint, a JSON object is returned. For example:
```

```

- If you can connect to the API endpoint, contact your security team about your proxies blocking URL access to the Object Storage APIs.
If you can't connect to the API endpoint, continue to[Step 4: Ensure DNS filtering isn't blocking Console access to the Object Storage APIs](https://docs.oracle.com/en-us/iaas/Content/Object/Troubleshooting/troubleshooting_console_connections.htm#dns-filtering-console-access).

## Step 4: Ensure DNS filtering isn't blocking Console access to the Object Storage APIs

- Open a terminal window and run the following command to test DNS resolution to the API region:

```

```

- If the hostname resolves successfully,[create a support ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)
