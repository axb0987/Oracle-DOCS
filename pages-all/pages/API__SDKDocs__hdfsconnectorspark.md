# Using the HDFS Connector with Spark
- Source: https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/hdfsconnectorspark.htm
- Fetched: 2026-09-05 01:36 CDT

# Using the HDFS Connector with Spark

## Introduction

This article provides a walkthrough that illustrates using the Hadoop Distributed File System (HDFS) connector with the Spark application framework. For the walkthrough, we use the Oracle Linux 7.4 operating system, and we run Spark as a standalone on a single computer.

## Prerequisites

Following are prerequisites for completing the walkthrough:
- You must have permission to create a compute instance. For guidance, see[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
- You must be able to connect to the service instance that you've launched. For guidance, see[Connecting to an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm).
- You must have the appropriate OCID, fingerprint, and private key for the Identity and Access Management (IAM) user that you will use to interact with an Object Storage. For guidance, see[Setup and Prerequisites](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/../Concepts/devguidesetupprereq.htm).
- You must have an Object Storage bucket that you can connect to.
- The IAM user must be able to read and write to that bucket using the Console.

## Using Spark

### Install Spark and Dependencies
Note  
  
For the purpose of this example, install Spark into the current user's home directory. Note that for production scenarios, you would not do this.
Note  
  
Versions 2.7.7.0 and later no longer install all of the required third party dependencies. Required third party dependencies are bundled under the`third-party/lib`folder in the zip archive and should be installed manually.
- Create an instance of your Compute service. For guidance, see[Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
- Ensure that your service instance has a public IP address so that you can connect using a Secure Shell (SSH) connection. For guidance, see[Connecting to an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm).
- Connect to your service instance using an SSH connection.
- Install Spark and its dependencies, Java and Scala, by using the code examples that follow.
```

```

### Download the HDFS Connector and Create Configuration Files
Note  
  
For the purposes of this example, place the JAR and key files in the current user's home directory. For production scenarios you would instead put these files in a common place that enforces the appropriate permissions (that is, readable by the user under which Spark and Hive are running).

Download the HDFS Connector to the service instance and add the relevant configuration files by using the following code example. For additional information, see[HDFS Connector for Object Storage](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/hdfsconnector.htm).
```

```

In the`spark-defaults.conf`file, add the following at the bottom:

`spark.sql.hive.metastore.sharedPrefixes= shaded.oracle,com.oracle.bmc`

### Prepare Data

For testing data, we will use the MovieLens data set.
- Download the latest data set at[https://grouplens.org/datasets/movielens/latest/](https://grouplens.org/datasets/movielens/latest/). Be sure to download the "Small" data set.
- Unzip the download file.
- Upload the`movies.csv`file to your Object Storage bucket.

### Test Using the Spark Shell

With the data ready, we can now launch the Spark shell and test it using a sample command:
```

```

You receive an error at this point because the oci:// file system schema is not available. We need to reference the JAR file before starting the Spark shell. Here's an example for doing so:
```

```

The command is successful so we are able to connect to Object Storage. Note that if you do not wish to pass the`--jars`argument each time the command executes, you can instead copy the`oci-hdfs-full`JAR file into the`$SPARK_HOME/jars`directory.

### Start the Spark Thrift Server

Start the Spark Thrift Server on port 10015 and use the Beeline command line tool to establish a JDBC connection and then run a basic query, as shown here:
```

```

Once the Spark server is running, we can launch Beeline, as shown here:
```

```

Next, connect to the server, as shown here:
Note  
  
For the purposes of this example, we have not configured any security, so any user name and password will be accepted. For production scenarios you would not do this.
```

```

If we now check to see what tables exist, we see the following:
```

```

None exist presently; however, we can create a table and link it to the`movies.csv`file that we downloaded and placed in the Object Storage bucket, as shown here:
```

```

Note that the table stores its data externally in Object Storage and the data can be accessed using the HDFS Connector (the`oci://`file system scheme). Now that we have a table, we can query it:
```

```

## For more information

- [HDFS Connector for Object Storage](https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/hdfsconnector.htm)
- [Overview of Object Storage](https://docs.oracle.com/iaas/Content/Object/Concepts/objectstorageoverview.htm)
- [Apache Spark](https://spark.apache.org/)
