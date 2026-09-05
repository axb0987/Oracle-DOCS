# Known Issues for Logging
- Source: https://docs.oracle.com/en-us/iaas/Content/Logging/known-issues.htm
- Fetched: 2026-09-05 02:38 CDT

# Known Issues for Logging

These known issues have been identified in Logging.

## Some agent warnings or errors can be ignored
Details For Linux : When the Unified Monitoring Agent (UMA, or 'agent') restarts or the configuration downloader runs, you might see a warning such as the following in the`journalctl`logs:
```

```
This warning likely appears because some circuit breaker parameters are haven't been configured correctly. For Windows : After you upgrade the agent, you might notice an error event similar to the following:
```

```
Workaround You can safely ignore these warnings and errors. They have no effect on agent functionality

## Transient Error in UMA in systemd versions older than 251
Details If the Unified Monitoring Agent (UMA) runs on systemd versions older than 251, you might see an error similar to the following:
```

```
This happens because the older systemd version doesn't support the required features for namespace setup. Workaround To fix this[error](https://github.com/systemd/systemd/issues/21907), upgrade to systemmd[version 251](https://github.com/systemd/systemd/releases)or later.

## Unified Monitoring Agent upgrade failure
Details

Updates to the Unified Monitoring Agent running on the host might not be applied if the Custom Logs Monitoring plugin is disabled in the Oracle Cloud Agent's Management tab. This might result in missing important security patches, bug fixes, and new feature enhancements. Workaround
