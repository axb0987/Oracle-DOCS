# Configure Event Data Publisher in Oracle Access Governance
- Source: https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm
- Fetched: 2026-09-05 03:13 CDT

# Configure Event Data Publisher in Oracle Access Governance

You can publish the data events from Oracle Access Governance to your OCI tenancy using the Data Feed feature in the Oracle Access Governance Console. You first need to perform some preliminary configurations in your tenancy, and then add the connection details in the Oracle Access Governance Console. Once the connection details are validated, the first data event is published in your Object Storage Bucket, and all the subsequent updates are received continually and sequentially either in OCI Bucket or OCI Streams.

## Prerequisites

You can export Oracle Access Governance data into the OCI tenancy. Here are a few mandatory requirements to consider before you proceed with the set up.
- You must be assigned an Oracle Access Governance Administrator role`AG_Administrator`
- You must have an active Oracle Cloud Infrastructure (OCI) orchestrated system integrated with Oracle Access Governance to view the Data Feed menu under Service Administration .
- Oracle Access Governance service instance, service account, object storage, and other related resources must all reside in the same region and identity domain.
- The Oracle Access Governance service instance tenancy can be different to the tenancy where you want to receive the data as long as they're in the same region.
- If the region of your OCI resources is different than the Oracle Access Governance service instance region, then replicate the identity domain in the Oracle Access Governance service instance region. For more details, see[Replicating an Identity Domain to Multiple Regions](https://docs.oracle.com/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm).
- You may connect multiple Oracle Access Governance service instances available in different tenancies within a region to the same OCI resources. This means that data available in your multiple Oracle Access Governance service instances can be collected within the same bucket and stream. You may also choose to create separate OCI resources per Oracle Access Governance service instance.
- Ensure that your cloud account, including associated Object Storage buckets and Streaming services, has sufficient space and capacity before exporting object types. Review your account's[Object Storage Quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas_topic-Object_Storage_Quotas.htm)and[Limits on Streaming Resources](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview_topic-Limits_on_Streaming_Resources.htm)to avoid disruptions during the process.

## Set Up OCI Tenancy for Data Event Publisher

Before you can use the Data Feed feature in Oracle Access Governance to publish your data, you must create a few OCI resources to support this. You need to create a compartment, a service account, an IAM group, generate API Keys and Authentication Token for the service account, Create Buckets, OCI Streams, and assign appropriate policies to give the group and service accounts access to related resources.

### Step 1: Create a Compartment
Create a compartment dedicated for data feed so that you can assign restricted policies to access or modify resources in this compartment. You may skip the step if you already have a compartment. This compartment must contain all the required IAM resources (Domain, Groups, User), Object Storage (Buckets), and Streams for publishing event data.
- Sign in to the Oracle Cloud Infrastructure Console as a tenancy administrator.
- Open the navigation menu and select Identity &amp; Security .
- In the Identity section, select Compartments .
- Select Create Compartment and add compartment name and description.
- Confirm and select the Create Compartment button.
Compartment:`data-feed-compartment`.

For more details, see[To create a compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#To).

### Step 2: Create a New Domain
Create a new domain dedicated for data feed in the compartment created in[Step 1](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming).
- In your OCI cloud account, open the navigation menu and select Identity &amp; Security .
- In the Identity section, select Domains .
- Select the compartment
- Select Create domain and enter the basic details, such as name and description.
- On the left pane, in the Compartment list, select the compartment created in the[Step 1](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming).
- You may choose to select the default domain or create a new domain.

For more details, see[Create Identity Domain](https://docs.oracle.com/iaas/Content/Identity/domains/to-create-new-identity-domain.htm#create-identity-domain).
Domain:`domain-feed-domain`

### Step 3: Create IAM Group
- On the OCI Console, open the navigation menu and select Identity &amp; Security -&gt; Domains .
- Choose the domain created for data feed operations.
- On the left pane, select Groups . A list of the groups available in your domain is displayed.
- Enter the following details:
- Name : Enter group name.
- Description : Enter some descriptive information about the group.
- Select the user can request access check box.
- Select Create .
IAM Group:`writer_access_group`

### Step 4: Create a Service Account by adding an Identity User

Create a new identity user for service account purposes. This user is provided restricted access through policies and is only used for programmatic access to OCI resources by Oracle Access Governance . Assign this service user to the IAM Group created in Step 3.
- On the OCI Console, open the navigation menu and select Identity &amp; Security -&gt; Domains .
- Choose the domain created for data feed operations.
- On the left pane, select Users . A list of the users available in your domain is displayed.
- Enter the first name, last name, username or email address.
- Choose the IAM group to assign the user to the identity group.
- Select Create .

### Step 5: Create API Key

Create API keys to establish secure authentication between user cloud account and Oracle Access Governance service. Using this service account, it enables the service to perform appropriate operations on the OCI resources .
- In the service account user page, on the left pane, in the Resources section, select API keys .
- Select the Add API key button, and then select Generate API key pair .
- Download the public key and private key.
- Select Add . The configuration file is created displaying ocid , fingerprint , tenancy and region details.
- Open the private key file (.pem extension) with any text editor, and save the information available on the file. You'll need this to configure the data publisher feature in Oracle Access Governance.

### Step 6: Generate Authentication Token

Auth Tokens are Oracle-generated authentication tokens to authenticate and authorize the service account user to interact with OCI resources.
- In the service account user page, on the left pane, in the Resources section, select Auth Tokens .
- Click the Generate token button.
- In the Generate token window, enter a meaningful description and then click Generate token .

The token is generated. Copy the displayed token and save it to a secure location. You'll need this to configure the data publisher event feature in Oracle Access Governance.

### Step 7: Create a New Stream

Oracle Access Governance will publish the data sets smaller than`1 MB`to your OCI Streams. Generally, all the Day N events, having small-size updates, will be published to the streaming service set up in your tenancy.
- On the OCI Console, open the navigation menu and select Analytics &amp; AI .
- Under the Messaging section, choose Streaming .
- Enter a unique stream name.
- Choose the data publisher specific compartment.
- For stream pool, choose either to automatically create a default stream pool or to create your own stream pool.
- In the Define Stream Settings section:
- In the Retention (in hours) field, enter a number from 24 to 168 for retaining messages in this stream. You can choose to enter any number. However, we recommend to enter the maximum number, which is 168 hours.
- Enter the number of partitions you want to create in your stream. The maximum limit depends on your tenancy limits.
- Click Create . Your new messaging stream is created.

For more information, see[Creating a Stream](https://docs.oracle.com/iaas/Content/Streaming/Tasks/creatingstreamsandstreampools_create-stream.htm#create-streams).

Save Streaming Details
Once created, select the stream name link to view its details. To configure your stream in Oracle Access Governance, copy and save the following details related to your stream:
- Stream Name
- Message Endpoint
- Stream OCID
For Stream Pool, follow the steps to view and save the information:
- On the Stream details page, select the Stream Pool link.
- Copy and save the Stream Pool OCID.
- For viewing the Bootstrap Server link:
- On the left pane, in the Resources section, select Kafka Connection Settings .
- In the Kafka Connection Settings section, copy and save the Bootstrap Servers link.

### Step 8: Create a New Object Storage Bucket

Oracle Access Governance will publish the initial data event to the Object Storage Bucket. Regular updates with data larger than`1 MB`will be published to Buckets.
- On the OCI Console, open the navigation menu and select Storage .
- Under the Object Storage &amp; Archive Storage section, choose Buckets .
- Choose the data publisher specific compartment and then click Create Bucket .
- In the Create Bucket window, enter the bucket details.
- Select the Enable Object Versioning checkbox.
- Click Create . Your new bucket stream is created. For more information, see[Creating an Object Storage Bucket](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm#top). Save the bucket name and namespace. You'll need these to configure the data event publisher feature in Oracle Access Governance.
Bucket Name:`Data-event-publisher-bucket`

### Step 9: Set Up Policies for Data Event Publisher

You'll need to set up IAM policies to enable the Oracle Access Governance Data Event Publisher to access the OCI resources.
- On the OCI Console, open the navigation menu and select Identity &amp; Security , then Policies .
- Under Identity , select Policies .
- Enter name and meaningful description.
- In the Policy Editor section, use the toggle button to switch to manual editor.
- Enter the policy statements as follows:
```

```

```

```

For example
```

```

```

```

## Configure Settings for Data Publisher in Oracle Access Governance

You can configure settings in the Oracle Access Governance Console to start receiving the data events in your OCI tenancy. Use the Data Feed functionality to configure data publishing events.
You must complete the preliminary set up in your OCI tenancy before configuring the data feed functionality in Oracle Access Governance.

Navigate to the Data Feed Page
- On the Oracle Access Governance Console, select the navigation menu icon and then select Service Administration .
- Select Data Feed .

Enable the Data Feed Action
- On the Data Feed page, from the Actions menu, select Manage settings .
- Select Yes in the Do you want to enable the data feed? option. You'll see the configuration fields to enter details.
- Select the Enable data types check box to receive data events in your OCI Streams or OCI bucket storage.
- Select the Enable audit events check box to receive audit events in your OCI Stream. The same stream configuration would be used for sending audit events as data events.

Add OCI Object Storage Bucket Details
Enter your OCI bucket details. You'll get the required information from the bucket details created in your OCI tenancy. For more information, see[Step 5: Create API Keys](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming)and[Set Up OCI Tenancy for Data Event Publisher](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming).
- In the Which region is the bucket in? field, enter the region identifier where you have created the bucket. For example, for Ashburn region, enter`us-ashburn-1`. You can view the region name in the top navigation menu of your OCI Console and corresponding region identifier from[Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
- In the Which namespace is the bucket in? field, enter the bucket namespace. For more information, see[Getting an Object Storage Bucket's Details](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_view_bucket_details.htm).
- In the What is the bucket name? field, enter the bucket name.
- In the What is the tenancy OCID? field, enter the tenancy OCID. You can view the tenancy details in your cloud account profile or from the configuration file. For more information, see[Getting My Profile Details](https://docs.oracle.com/iaas/Content/Identity/usersettings/get-details-my-profile.htm#get-my-profile-details).
- In the Which region is the user in? field, enter the service account user region identifier. You'll get the details in the configuration file. For more information, see[Create API Keys](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming).
- In the What is the user's OCID? field, enter the OCID of the service account. You'll get the details in the configuration file. For more information, see[Create API Keys](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming).
- In the What is the user's fingerprint? field, enter fingerprint value. You'll get the details in the configuration file. For more information, see[Create API Keys](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming).
- In the What is the user's private SSH key? field, copy and paste the PEM file contents, starting from`-----BEGIN PRIVATE KEY-----`to`-----END PRIVATE KEY-----`. You should have this downloaded while creating the API keys for the service account. For more information, see[Create API Keys](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming).

Add OCI Stream and Stream Pool Details
- In the What is the auth token? field, enter the user authentication token value. For more information, see[Set Up OCI Tenancy for Data Event Publisher](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming).
- In the Which tenancy? field, enter the tenancy name. You can view the tenancy details in your cloud account profile. For more information, see[Getting My Profile Details](https://docs.oracle.com/iaas/Content/Identity/usersettings/get-details-my-profile.htm#get-my-profile-details).
- In the What is the username? field, enter the service account user name prefixed with domain name in the format`<domain-name/user name>`. For example, if the domain name is data-pub and service account user name as john.doe , then enter`data-pub/john.doe`.
- In the What is the message endpoint? field, enter message endpoint without`https`or bootstrap server value. For more information, see[Streaming Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming).
- In the What is the topic name? field, enter stream name. For more information, see[Streaming Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming).
- In the What is the stream pool OCID? field, enter the stream pool OCID. For more information, see[Streaming Details](https://docs.oracle.com/en-us/iaas/Content/access-governance/configure-event-data-publisher-in-oracle-access-governance.htm#set-up-oci-tenancy-for-data-publisher-and-streaming).
Tip  
  
Enter Stream Pool OCID and not Stream OCID.
- Click Save . The configuration details are saved. If there are any validation errors, you must resolve those before you could save the details.
- Under Actions , click Publish data now . A confirmation message displays and then click Publish .
Once you publish the data, the publishing status along with date and time is displayed on the Oracle Access Governance Console. Depending on the data size, it may take a couple of minutes to publish the entire data. Once completed, you will see the completion status on the Console with a message, "A data publish is completed successfully on &lt;Date&gt; &lt;Time&gt; by &lt;Administrator Email Address&gt;." In the OCI bucket, you should see multiple event files under the`json`folder.

You can consume OCI Stream messages using two different methods: the Kafka Java client and the OCI SDK . Each method follows a distinct decoding process for correct message interpretation.
- 

Using the OCI SDK : You must decode the stream message's key once and the value twice.
-
