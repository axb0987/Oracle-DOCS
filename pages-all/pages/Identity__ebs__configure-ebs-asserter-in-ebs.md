# Configure the E-Business Suite Asserter in Oracle E-Business Suite
- Source: https://docs.oracle.com/en-us/iaas/Content/Identity/ebs/configure-ebs-asserter-in-ebs.htm
- Fetched: 2026-09-05 02:21 CDT

# Configure the E-Business Suite Asserter in Oracle E-Business Suite

Register the E-Business Suite Asserter application server with Oracle E-Business Suite.

## Registering the E-Business Suite Asserter with Oracle E-Business Suite

To establish communication with Oracle E-Business Suite, the E-Business Suite Asserter uses the application server ID in the database connection file. The database connection file is generated while registering the E-Business Suite Asserter application server with Oracle E-Business Suite.

- Sign in to the Oracle E-Business Suite application server machine. Don't use the root user. Use the user that installed and ran the WebLogic Server.
- Run the commands`echo $JAVA_HOME`and`echo $WL_HOME`, and then make note of the value that is set for each:
- `JAVA_HOME`:`/usr/java/jdk1.7.0_201`
- `WL_HOME`:`/u01/oracle/wlserver`

If the values of the commands`$JAVA_HOME`and`$WL_HOME`aren't set, request that the WebLogic administrator set them. The`$WL_HOME`value is only needed if you use a version of Oracle E-Business Suite greater than 12.2.

The values for the`$JAVA_HOME`and`$WL_HOME`might differ from your environment. Update the fields with the correct values for your environment.
- Run the following command to create a working folder:

```

```

- Extract the`fndext.jar`file, which is in the`WEB-INF/lib`folder inside the`ebs.war`file that you have downloaded from the IAM Console.
- Copy the`fndext.jar`file to the working folder you created in the previous step and also to the E-Business Suite Asserter WebLogic`$DOMAIN_HOME/lib`folder.
The name of the`fndext.jar`file might vary depending on the current version.
- Locate your Oracle E-Business Suite environment file (in this example,`/u01/install/VISION/EBSapps.env`) and run the following command:

```

```

The path to the`.env`file might vary depending on your environment.
- Locate the`.dbc`file that is associated with your Oracle E-Business Suite instance in the following folder:`$FND_SECURE/EBSDB.dbc`.
If your database instance name is`EBSDB`, the file has a name like`EBSDB.dbc`. Make a note of the full path of the`.dbc`file (including the file name itself):`/u01/install/VISION/fs1/inst/apps/EBSDB_ebs/appl/fnd/12.0.0/secure/EBSDB.dbc.`
- Run the following command to register the E-Business Suite Asserter application server with Oracle E-Business Suite:

```

```

Note  
  
The value of`CREATE NODE_NAME`is the asserter hostname. Use the value that is correct for your setup.
- Run the following command:

```

```

The resulting file name might be in all uppercase letters. Make a note of the`APPL_SERVER_ID`value.
- Copy the`EBSDB _ ebsasserter.example.com .dbc`file to the EBS Asserter's WebLogic Server machine under the`/opt/ebssdk`
