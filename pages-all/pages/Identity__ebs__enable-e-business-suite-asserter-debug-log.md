# Enabling the E-Business Suite Asserter Debug Log
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/enable-e-business-suite-asserter-debug-log.htm
- Fetched: 2026-09-05 02:21 CDT

# Enabling the E-Business Suite Asserter Debug Log

To send logs to a file, add`FileHandler`to the`handlers`property in the`logger.properties`file. This enables file logging globally.

- Create a`logger.properties`file with entries as follows:

```

```

- Add the option`-Djava.util.logging.config.file=<logger.properties file created above>`in Oracle WebLogic Server:
- Using a browser, access the Oracle WebLogic Server Administration Console.
- In the Oracle WebLogic Server Administration Console, select servers under Environment in the Domain Structure .
- In the Servers table, select the name of the server instance where the E-Business Suite Asserter is deployed.
- From the WebLogic Server menu, select Administration , then select Server Start .
- From the Server Start page, you can add the option`-Djava.util.logging.config.file=<logger.properties file created above>`in the Arguments field.
- Select Save .
- Restart the Oracle WebLogic Server where the E-Business Suite Asserter is deployed.
The E-Business Suite Asserter debug log file is in`<HOME DIR>/ebsasserter.log`
