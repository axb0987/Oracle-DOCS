# Add a Dimension
- Source: https://docs.oracle.com/iaas/analytics-for-applications/doc/add-dimension.html
- Fetched: 2026-09-05 19:00 CDT

### [Oracle Cloud Infrastructure Documentation](https://docs.oracle.com/iaas/Content/home.htm)

All Pages

[Skip to main content](https://docs.oracle.com/iaas/analytics-for-applications/doc/add-dimension.html#dcoc-content-body)

# Add a Dimension

You can create a custom dimension, join it to the prebuilt or custom facts, and add the custom dimension to any subject area to meet your business requirements.
- Sign in to your service.
- In Oracle Fusion Data Intelligence Console , click Semantic Model Extensions under Application Administration .
- On the Semantic Model Extensions page, click User Extensions .
You see the main and existing customization branches.
- In the User Extensions region, under Customization Branches, click a branch to open the Branch page.
- On the Branch page, click Add Step .
- In Add Step, select Add a Dimension .
You see the wizard sequence to add a dimension.
- In step 1 of the wizard, enter a name for your customization step, for example, Add Point of Sale Dimension and add a brief description.
- In step 2 of the wizard, select the schema, and then select the dimension table in Object . For example, COST_CENTER_VIEW1 .

Note  
  
If you don’t see the schema or table, then ensure that you have granted select permission to the OAX$OAC schema in the autonomous data warehouse. For example,`grant select on <schema>.<table> to OAX$OAC`. See[Load Customization Data to the Autonomous Data Warehouse](https://docs.oracle.com/iaas/analytics-for-applications/doc/load-customization-data-autonomous-data-warehouse.html#GUID-2A33AC14-5E48-488F-BB69-8D41C532398B).

You see the attributes available in the selected dimension table. You can use the Search and Filter fields to limit the attributes displayed for the dimension table.
- Select the attributes that you want to use from the dimension table and indicate an attribute to be used as the key for joining with a fact table in the target subject area.
- If any of the selected attributes have been removed or modified in the source table since the last refresh, then you see such columns highlighted and a message asking whether you want to update the table. Select OK in the message to reload the source columns. If you want to review the changes to the source columns, then click Cancel in the message, and later click Refresh to reload the source columns. If any of the attributes that you haven’t selected have been removed or modified in the source table, then you see the refreshed list of source columns. If any of the custom columns fail validation during the refresh, then you see a message asking you to resolve the cause of failure and revalidate.
- Optional: Click Create Column to add another column to your dimension table in the target subject area using these instructions:

- In Create Column, enter a display name.
- Under Data Elements , search for a data element from the physical table of the selected dimension table.
- From the search results, double-click the data element to place it in the text pane.
- Under Functions , search for a function to construct a column using expressions. For example, search for functions like "substring" or "concatenate" to construct new expression-based columns. From the search results, double-click the applicable result to add it to the central text pane.
- Click Validate , and then click Save .
- In step 3 of the wizard, select, drag, and drop available data elements into the Selected Data elements pane to design a hierarchy for the dimension and then click Next . In the Selected Data Elements pane, click a level to update its primary key and set its display attribute in the Properties pane.
You can add multiple levels in your hierarchy by right-clicking at a level and selecting Add Child or Add ‘n’ Child Levels. For example, your Region Hierarchy can have Region Total at Level 1, Region at Level 2, Country at Level 3, State at Level 4, and City at Level 5.
- In step 4 of the wizard, select Skip Joins if you don’t want to join the selected dimension table to any facts. To join the selected dimension table to a fact, select the fact table, fact key, and join type. Click Content Level to specify the content level for your fact.
You can join a single fact key column to multiple dimension keys.
Note  
  
Ensure that the data types of the join key pairs match. If your data types don't match but you want to proceed, then click Yes in the message. However, if the data types can't be absolutely matched, then the server-side validation rejects that join completely and you must change the data type of custom key column to match the factory data type.
- Optional: Click Add Fact Table to select another fact table to link your dimension to and define the join.
- Click Next .
- Optional: In step 5 of the wizard, select the subject areas to include the new dimension and click Finish .
You see a message that your step is being applied to the customization branch. After it's applied, you see the new customization step in the customization branch. You can now apply the customization branch to the main branch or edit it to add more steps.
Note  
  
If you’ve created Add a Dimension steps using the previous functionality, you can still edit and reapply through the Edit option.

- [About Oracle](https://www.oracle.com/corporate/index.html)
- [Contact Us](https://www.oracle.com/corporate/contact/index.html)
- [Legal Notices](https://docs.oracle.com/iaas/Content/legalnotices.htm)
- [Terms of Use &amp; Privacy](https://www.oracle.com/legal/privacy/)
- [Document Conventions](https://docs.oracle.com/iaas/Content/General/Reference/docconventions.htm)
-
