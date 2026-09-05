# Estimating Monthly Costs
- Source: https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/signingup_topic-Estimating_Costs.htm
- Fetched: 2026-09-05 01:44 CDT

# Estimating Monthly Costs

Oracle provides you with a cost estimator to help you figure out your monthly usage and costs for Oracle's Infrastructure and Platform Cloud (Oracle IaaS/PaaS) services before you commit to an amount.

The cost estimate is automatically calculated based on your choice of the Oracle Cloud service category, its service configurations, and the usage of each resource in the configuration.

You can start using Oracle Cloud with no up-front cost. Oracle bills you for the services and resources you use. For planning, use the results from the Cost Estimator to estimate how much you are likely to be charged for usage each month.
Note  
  
The Cost Estimator is for evaluation purposes only, and does not provide an official quote.

The Cloud Cost Estimator Generation 2 allows you to determine what you would pay for certain Oracle Cloud services. It supports advanced features, such as favorites, and has the same support as the former first generation Cost Estimator. The Cloud Cost Estimator Generation 2 is always updated with the latest offerings and prices.

To use the Cloud Cost Estimator Generation 2:
- Go to the[Cost Estimator Generation 2](https://www.oracle.com/cloud/cost-estimator.html)page on the Oracle Cloud website. The Cost Estimator page opens.
- Under My Estimate , several items are available for selection, to get you started on an estimate:
- Compute shapes
- Services
- Reference architectures
- My favorites
- Search
- You can change the name of the estimate by hovering over the default My Estimate name. Click the edit icon to change the estimate name. This is how you refer to your cost estimate. As you create your estimate, it can consist of various configurations , and each configuration can have multiple services configured within it.
- You can start building your estimate by either adding Services , Compute shapes , Reference architectures , use previously stored favorites, or by searching for products or part numbers.
- Services : Services allow you to set some predefined initial quantities, in terms of a particular OCI category of cloud services, such as Core Infrastructure , Data Lakehouse , Application Integration , and so on.

Select the service category from the list. All Categories is selected by default. While on the Services tab, you can also click the Search bar to filter the list.

For example, if you choose Application Integration , several service options are displayed, with tiles for Oracle Integration Cloud , Oracle SOA Suite for Oracle Cloud Infrastructure , and Process Automation .

Click Load for the chosen service, which loads the preset into your configuration. A configuration panel is displayed corresponding to the service preset you chose. For example, if Oracle Integration Cloud is selected, you can set the utilization in terms of the number of Instances and Hrs/day x Day/month = &lt;utilization&gt; hrs/month. Choose a license edition, license type, real-time message count, and file processing amount.

When you are finished adding presets, click Add configuration to continue adding to your estimate.
- Compute shapes : Allows entering an estimate based on various compute shape types. Flexible is selected by default from Shape family , but you can also choose:
- Dense
- GPU
- HPC
- Optimized
- Standard

Select the desired shape. You can also filter the list by processor ( Any is selected by default). For the chosen shape, click Add .

A My Configuration panel for the compute shape VM is displayed. Under Utilization , click Edit to change the number of instances, hours per day, and days per month.

Under Shape , you can make adjustments, such as the processor, VM shape type, amount of OCPU, memory, and OS image. You can also choose pricing options, such as the capacity type and burstable option.

From the context (three dots) menu, you can delete an item by selecting Delete service . Product pages and documentation are also available in an adjacent menu.

Some shapes have a storage option, whereby you can set a storage capacity, performance level, or VPU. You can also apply the 200 GB Free Tier discount, by selecting the corresponding option. The block volume service Free Tier allowance is for the entire tenancy, 200 GB total per tenancy. If there are multiple quotes for the same tenancy, only total 200 GB can be applied.
Note  
  
Not all shape or storage options are available for a particular VM type.

When you are finished adding VM shapes, click Add configuration to continue adding to your estimate.
- Reference architectures : From this tab, you can add the following:
- Big Data and Analytics (Large)
- Big Data and Analytics (Medium)
- Big Data and Analytics (Small)
- Data Science (Large)
- Data Science (Medium)
- Data Science (Small)
- Oracle Analytics Cloud (Large)
- Oracle Analytics Cloud (Medium)
- Oracle Analytics Cloud (Small)
- Oracle Weblogic Server for OCI (Large)
- Oracle Weblogic Server for OCI (Medium)
- Oracle Weblogic Server for OCI (Small)

Click Load for the chosen reference architecture, which loads it into your configuration. A configuration panel is displayed corresponding to the reference architecture you chose. For example, if Data Science (Small) is selected, a new configuration panel is displayed that allows selecting utilization in terms of Hrs/day x Day/month = &lt;utilization&gt; hrs/month. A number of services are subsumed under the reference architecture, which you can further adjust pricing and usage for.

When you are finished adding reference architectures, click Add configuration to continue adding to your estimate.
- My favorites : Favorites are locally cached, per-session estimate configurations that you can load and reuse later. When you return to the Cost Estimator and load or import a favorite estimate, it reflects all of the latest list prices. See[Save and Share Your Cost Estimator Results](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/signingup_topic-Estimating_Costs.htm#save_and_share)for more information on storing favorites.
- Advanced Search : Click Advanced Search , and in the entry form start typing the name, service, or part number of the Oracle product you want to add to your estimate. You can also click the entry field without typing to display a list of Service Presets , Reference architectures , and SKUs you can choose from.

For example, if you enter Compute , a list of Compute-related Service Presets , SKUs , and Services are displayed. Each of these are separated by headings in the list.

You can also select multiple services from the Advanced Search tab, and you can mix your preferred combination of Service Presets , Reference architectures , and SKUs .

When you are finished adding items found through search, click Add to add them to your configuration. As with the other tabs, a panel with settings specific to the service preset, reference architecture, SKU, or service are displayed, where you can customize the products accordingly.

As you build your estimate, you can mix and match, or start with any of the tabbed configuration categories as preferred. Continue to add more services to your estimate by clicking the Add configuration button.
- As you add estimate items to your configuration, they are listed in the My Estimate page. The page lists all of your chosen products and services as collapsible and expandable sections that correspond to a service category, with per item cost estimates for each.

Each section displays the total estimated cost for the particular service. Each section has a context (three dots) menu with extra options or actions you can perform, such as adding additional SKUs. For any configuration, you can select Delete configuration to remove it, or Clone to make copies.

The total cost for each product or service is also displayed at the upper right of each section.

Meanwhile, the total Estimated Monthly Cost of the entire estimate configuration is displayed at the upper right, along with the ability to see your estimate in different currencies.

See[Example: Estimating Your Monthly Cost for Oracle Database Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/signingup_topic-Estimating_Costs.htm#estimate_cost_example_DBC), for an example. Also see[Save and Share Your Cost Estimator Results](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/signingup_topic-Estimating_Costs.htm#save_and_share)for instructions on adding an estimate to your favorites, and exporting and importing cost estimate configurations.

## Example: Estimating Your Monthly Cost for Oracle Database Cloud Service

In this example, see how you can estimate your monthly cost for Oracle Database Cloud Service based on your requirements.
- On the My Estimate page, click Add configuration and select the Services tab. Select Oracle Databases from the list.
- The Services tab is filled with the associated Oracle Databases categories (such as, Virtual Machine Exadata Database Cloud Service , and so on). Click Load for the chosen service, which loads the preset into your configuration. For example, if you chose Virtual Machine , a Database - Oracle Database Cloud Service - Virtual Machine section is added to your configuration.
- Next, select a virtual machine type from the list (for example, Oracle Database Cloud Service - Standard Edition ), and select the amount of OCPU per hour. The total cost is shown as you make changes to the service. You can also set the utilization in terms of the number of Instances and Hrs/day x Days/month = &lt;utilization&gt; hrs/month.
- Continue to add other services or customize your service as needed. You can also open the context (three dots) menu and click Clone , to create more copies you want to add to this service configuration. Or, click Add by SKU to add more products to the configuration.
- You can delete the service configuration by opening the context (three dots) menu and selecting Delete configuration . To delete a service, open the context (three dots) menu and select Delete service .

When you are finished with your estimate, you can either click Start for Free to start setting up services, or you can also[save to favorites, or export your estimate](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/signingup_topic-Estimating_Costs.htm#save_and_share)for further consideration and analysis.

## Save and Share Your Cost Estimator Results

When you are satisfied with your monthly usage estimates in the Cost Estimator Generation 2 , you can export and save your estimate as an Excel spreadsheet (XLS), comma-separated values (CSV), or JavaScript Object Notation (JSON) file.
Important  
  
In Cost Estimator Generation 2, only JSON files can be imported back into the application.

### Save Your Cost Estimates

You can save your estimates by either:
- Adding it to your favorites, or;
Note  
  
Favorites persist until you clear your cache, cookies, or browser history.
- Exporting it as an XLS, CSV, or JSON file.

To save your estimate as a favorite:
- From the main My Estimate page, you can use the Add to Favorites option from the context (three dots) menu. After you have built your cost estimate configuration, as described in[Estimating Monthly Costs](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/signingup_topic-Estimating_Costs.htm)or[Example: Estimating Your Monthly Cost for Oracle Database Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Billing/Tasks/signingup_topic-Estimating_Costs.htm#estimate_cost_example_DBC), open the context menu and select Add to Favorites . A notification is displayed that your configuration was successfully saved to the favorites. You can access your favorites by clicking Add configuration , and then select the My favorites tab. The favorite is labeled by default as My Estimate with the date and time.

To export your cost estimate:
- From the main My Estimate page, open the context (three dots) menu and select Export . The Export interface is displayed.
- From Export type , select one of the available export file formats:
- Excel Spreadsheet (XLS)
- Comma separated values (CSV)
- JavaScript Object Notation (JSON)
- In File name , a default file name is generated, with the current date and timestamp. You can edit the file name as preferred.
- Click Export . You are then prompted where you want to save the file to on your file system.

### Import or Load Your Saved Estimates

If you want to change your saved estimates, or if you're reviewing them, you can import them into the Cost Estimator. You can also load previously saved service configurations in your browser to continue with your estimate. To load an estimate from your current browser session, click the My favorites tab on the My Estimate page, and click the favorite's load icon. You can also remove a favorite by clicking the delete icon.

When importing, only JSON files (Cloud Estimator Generation 2), or OCE files from the legacy Cost Estimator, are supported. If you want to migrate from the legacy Cost Estimator to the newest one, you can export your estimate from the legacy Cost Estimator and import its OCE file into the latest Cloud Estimator Generation 2.

To import an estimate:
- From the main My Estimate page, open the context (three dots) menu and select Import . The Import window is displayed.
- Drag and drop the JSON file, or browse your file system for it.
- After you have selected your file, the file is listed in the window next to Selected files .
Note  
  
You can only import a single JSON file at a time. You can, however, import subsequent files, and the information is appended to the estimate, without removing existing selections.
- Click Import .
- Your imported cost estimate configuration is displayed on the My Estimate page. You can then make changes as required.

## Viewing a Cost Estimate in the Console

When you create certain resources in the Console, such as Compute instances, the Console shows an estimate of the monthly costs for the resource. Be aware of the following information:
- 

The estimated cost only includes the resources that are listed in the Console estimate. Other resources that are not listed in the estimate might incur additional costs.

For example, for Compute instances, the estimated cost includes only the shape, image, and boot volume. Other resources that are used by the instance, such as the network traffic consumed by the instance, are not included in the estimate.
- The estimate assumes that the resource is running for 24 hours a day, 31 days a month (744 hours).
- The estimate is based on your organization's rate card information, but does not include any tier unit pricing, if applicable.

## Accessing List Pricing for OCI Products

You can view the full list of prices for OCI products using the command line.

To access list pricing, use a curl command or a library with the preferred programming language, to programmatically access and process the data. Valid JSON is returned as a response.
```

```

Request headers :

Key Value
Accept "*/*"
Connection keep-alive
Accept-Encoding gzip, deflate, br

Query parameters : (sent to the API to filter objects)

Query Parameter Description
partNumber Part number (that is, Bxxxx)
currencyCode Specifies pricing values currencyCode.

The following is a sample response:
```

```

JSON pricing data is structured and defined in terms of the following:
- Result structure
- Product price - Object

Result Structure :

Attribute Type Description
partNumber string Part number (that is, B Part Number) (for example, B86078).
displayName string [L] Display name (for example, B86078 - Oracle Bare Metal Cloud Service - Dense I/O Compute Capacity - OCPU Per Hour).
metricName string [L] Quantifiable measure used for billing (for example, "Gigabyte Storage Capacity per Month").
serviceCategory string [L] Service Category (for example, "Compute Cloud Services").
prices array Product price.

Product price - Object (describes the array of prices, that is, the parameters the prices have):

Attribute Type Description
currencyCode string Specifies pricing values currencyCode.
model string Pricing Model (Enum: PAY_AS_YOU_GO).
rangeMin string Minimum quantity for tier pricing (exclusive). Only applicable for product supporting range-based pricing.
rangeMax string Maximum quantity for tier pricing (inclusive). Only applicable for product supporting range-based pricing.
rangeUnit string Unit of measurement of rangeMin and rangeMax (for example, "GB", "TB").
