# Document Generator MS Word Tags
- Source: https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/DocGen-Template-Tags.htm
- Fetched: 2026-09-05 02:09 CDT

# Document Generator MS Word Tags

A " tag " refers to an expression that the Document Generator can replace in a document template using JSON data.

# Data

The JSON data can be stored in Object Storage or specified inline in a request.

Example - Stored in Object Storage
```

```

Example - Specified inline in data.content
```

```

# Tags

Tags contain paths to some value in JSON data. For example, given this data:
```

```

You could use this template:
```

```

To generate this text:
```

```

Note that JSON keys are case-sensitive.`first_name`and`First_Name`are different JSON keys.

# Tag Delimiters

You can replace the default tag delimiters`{`and`}`with these values:
- `{{`and`}}`
- `{{{`and`}}}`

You can specify the tag delimiters in the custom properties of the MS Word template using both`document_generator_start_delimiter`and`document_generator_end_delimiter`as shown here:  
  

With the previous example, you can use this in your template:
```

```

To generate this text:
```

```

# Basic Tag

Syntax:`{dataRef}`

A Basic tag is used to inject text or numbers.

## Examples

Tag Data Result
`{basic}``{"basic":"Hello!"}`Hello!
`{number}``{"number": 7}`7

## Formatting

Basic tags can be formatted. See[Number Formatting](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/DocGen-Template-Tags.htm#number-formatting)and[Date Formatting](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/DocGen-Template-Tags.htm#date-formatting)for more details.

## Sample documents

MS Word Template JSON Data Output
[Word-Basic.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Basic.docx)[Word-Basic.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Basic.json)[Word-Basic-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Basic-output.docx)

# Vertical Loop Tag

Syntax:`{#dataRef}...{/dataRef}`

A Vertical Loop tag is used to produce copies of a section of text vertically.

Inside the loop, you can use loop metadata tags such as`{class_list_position}`and`{class_list_count}`. See[Loop Metadata Tags](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/DocGen-Template-Tags.htm#loop-metadata-tags).

## List Example

### Data

```

```

### Template

```

```

### Result

```

```

## Table Example

### Data

```

```

### Template

Id Name
`{#class_list}{student_id}``{name}{/class_list}`

### Result

Id Name
1 Sue
2 Bob
3 Jean

## Sample documents

MS Word Template JSON Data Output
[Word-VLoop.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-VLoop.docx)[Word-VLoop.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-VLoop.json)[Word-VLoop-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-VLoop-output.docx)

# Horizontal Loop Tag

Syntax:`{:dataRef}...{/dataRef}`

A Horizontal Loop tag is used to produce copies of a section of text horizontally.

Inside the loop, you can use loop metadata tags such as`{weekdays_position}`and`{weekdays_count}`. See[Loop Metadata Tags](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/DocGen-Template-Tags.htm#loop-metadata-tags).

Optional companion JSON property:
- To distribute the data evenly within the columns that contain the horizontal loop, add a boolean property named`{dataRef}_distribute`in the same JSON scope as the array. For example, for`{:weekdays2}...{/weekdays2}`, set`"weekdays2_distribute": true`.

## Table Example

### Data

```

```

### Template

Days`{:weekdays}{name}{/weekdays}`

### Result

Days Monday Tuesday Wednesday Thursday Friday

## Sample documents

MS Word Template JSON Data Output
[Word-HLoop.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-HLoop.docx)[Word-HLoop.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-HLoop.json)[Word-HLoop-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-HLoop-output.docx)

# Loop Metadata Tags

Loop metadata tags are available inside vertical and horizontal loops.

Tag Description
`{dataRef_position}`The one-based position of the current loop item:`1`,`2`,`3`, ...
`{dataRef_count}`The total number of rendered loop items.

The`dataRef`prefix comes from the final segment of the loop data reference. For example, a loop over`{#invoice.products}...{/invoice.products}`exposes`{products_position}`and`{products_count}`.

## Example

### Data

```

```

### Template

```

```

### Result

```

```

Loop metadata tags can also be used in conditional expressions inside the loop. For example:
```

```

If the JSON data already contains a property with the same name as a loop metadata tag, the JSON data value is used.

# Array Operations

These operations can be performed on vertical or horizontal arrays.

Loop metadata tags are supported in array operations. Use the original array name for metadata over the rendered operation result. For`break`and`group`, you can also use`{break_position}`/`{break_count}`or`{group_position}`/`{group_count}`for metadata within the current break bucket or group block. See[Loop Metadata Tags](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/DocGen-Template-Tags.htm#loop-metadata-tags).

Notes about Loop metadata tags:
- For`filter`,`sort`,`distinct`,`break`, or`group`, the position and count are based on the rendered items after the operation is applied.
- In`{#products|filter:price:>=:2}{#filtered}...{/filtered}{/products|filter:price:>=:2}`,`{products_position}`and`{products_count}`describe the filtered`products`result.
- The`filter`,`sort`, and`distinct`operations produce one rendered result, so they expose metadata under the original array name only.
- For`break`and`group`, the original array metadata is flattened across all rendered inner groups. For example,`{products_position}`can resolve to`1`,`2`,`3`across all products, while`{break_position}`/`{break_count}`or`{group_position}`/`{group_count}`restarts inside the current break bucket or group block.

## Filter

The`filter`operation takes three arguments:
- The property to filter on
- The comparison to perform
- The value to compare against

Currently, filtering is only supported on numeric types.

To use a filter, you must specify a new list, called`{#filtered}...{/filtered}`, inside the parent array being filtered.

### Example

#### Data

```

```

#### Template

`{#products|filter:price:>=:2}`

Category Name Price
`{#filtered}{category}``{name}``{price}{/filtered}`

`{/products|filter:price:>=:2}`

#### Result

Category Name Price
Clothing Shirt 3
Accessory Hat 2

## Sort

The`sort`operation takes two arguments:
- The name of the property to use for sorting
- `asc`or`desc`to sort the list in`ascending`or`descending`order.

To use a sort, you must specify a new list, called`{#sorted}...{/sorted}`, inside the parent array being sorted.

### Example

#### Data

```

```

#### Template

`{#products|sort:price:desc}`

Category Name Price
`{#sorted}{category}``{name}``{price}{/sorted}`

`{/products|sort:price:desc}`

#### Result

Category Name Price
Clothing Shirt 3
Accessory Hat 2
Accessory Belt 1

## Distinct

The`distinct`operation takes a single argument:
- The name of the property to select distinct values of.

### Example

#### Data

```

```

#### Template

```

```

#### Result

```

```

## Break

The`break`operator groups items together based on a shared property. It takes up to two arguments:
- The name of the property to group items on.
- `asc`or`desc`to sort the properties in`ascending`or`descending`order. This is optional, and defaults to the natural order.

To use a break, you must specify a new list, called`{#break}...{/break}`, inside the parent array being broken into groups.

### Example

In this example note that the "Belt" and "Hat" items shared a category ("Accessory"), but they are not grouped in the array ("Belt" is the first item in the array and "Hat" is the last item).

Once the`break`operator has been applied, the items are grouped together in the output.

#### Data

```

```

#### Template

```

```

#### Result

```

```

## Group

Splits an array into subarrays of the given size. A single argument is required:
- An integer specifying the group size.

To use a group, you must specify a new list, called`{#group}...{/group}`, inside the parent array being grouped.

If the array does not split perfectly into groups, the last group will be of smaller size. For example, if you have an array of 5 items, and you use`group:2`on it, then two groups of two items and one group of one item will be created.

### Example

#### Data

```

```

#### Template

```

```

#### Result

```

```

## Sample documents

MS Word Template JSON Data Output
[Word-VLoop-Arrays.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-VLoop-Arrays.docx)[Word-VLoop-Arrays.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-VLoop-Arrays.json)[Word-VLoop-Arrays-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-VLoop-Arrays-output.docx)

# Aggregators

## Sum

The Sum Aggregator is used to calculate the sum of an array.

### Example

#### Data

```

```

#### Template

```

```

#### Result

```

```

## Average

The Average Aggregator is used to calculate the average of an array.

### Example

#### Data

```

```

#### Template

```

```

#### Result

```

```

## Max

The Max Aggregator is used to find the maximum value of an array.

### Example

#### Data

```

```

#### Template

```

```

#### Result

```

```

## Min

The Min Aggregator is used to find the minimum value of an array.

### Example

#### Data

```

```

#### Template

```

```

#### Result

```

```

## Sample documents

MS Word Template JSON Data Output
[Word-Aggregators.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Aggregators.docx)[Word-Aggregators.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Aggregators.json)[Word-Aggregators-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Aggregators-output.docx)

# Conditional Tags

## # Tag

Syntax:`{#expression}...{/expression}`A Condition tag in a document displays a section only if the expression resolves to true. The`expression`can be either a reference to a non-array property in your JSON data or a boolean expression like`expr(age<18)`. See the section below on[conditional expressions](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/DocGen-Template-Tags.htm#conditional-expressions).

### Notes

- A condition evaluates to false when the referenced JSON property is`false`, an empty string (`""`), an empty array (`[]`),`null`, or missing. If the JSON property has any other value, the section is displayed.
- If the referenced JSON property has an array value, the tag behaves as a loop tag and duplicates the section for each iteration. See[Vertical Loop Tag](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/DocGen-Template-Tags.htm#vertical-loop-tag).

### Example

#### Data

```

```

#### Template

```

```

#### Result

```

```

## Sample documents

MS Word Template JSON Data Output
[Word-Conditionals.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Conditionals.docx)[Word-Conditionals.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Conditionals.json)[Word-Conditionals-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Conditionals-output.docx)

# Image Tag

Syntax:`{im:dataRef}`or`{image:dataRef}`or`{%dataRef}`

An Image tag is used to insert an image in a MS Word document. Example:`{im:my_image}`.

Images can be provided from an OCI Object Storage bucket or from a URL . Images must be provided as an object, for example:
```

```

Note: an image tag can be used in a watermark. In that case, the image will replace the entire watermark text, and any other tags in the watermark will be ignored.

## General

The specific schema for each source type is described below. You can also include the following optional properties in the image object to control image formatting:
- width: A`string`of digits, followed by unit of measure. E.G.`200px`. Sets the width of the image.
- height: A`string`of digits, followed by unit of measure. E.G.`200px`. Sets the height of the image.
- alt_text: A`string`. This will be set as the alternative text of the image.

### Supported units of measure:

Document Generator supports the following units of measure for images:
- px (pixels)
- in (inches)
- cm (centimeters)
- % (percentage)

### Default size of inserted images:

- Smaller images: If an image is smaller than the page size, the original size is preserved.
- Larger images: If an image is larger than the page size, it is resized to fit within the page width and height. The aspect ratio of the image is maintained.

### Image scaling:

If only one image dimension is provided, the Document Generator will calculate a scaled value for the missing dimension in order to preserve aspect ratio. For instance:
- If you provide a width , but no height , a scaled height will be calculated based on the image's native dimensions and the provided width .
- If you provide a height , but no width , a scaled width will be calculated based on the image's native dimensions and the provided height .

### Supported Formats

Document Generator supports the following image formats:
- PNG
- JPG
- GIF
- BMP

## Schemas

### OCI Object Storage

- `source`: must be set to`OBJECT_STORAGE`
- `objectName`: The path and name of the file
- `namespace`: The namespace of your object storage bucket
- `bucketName`: The name of the bucket that contains the file
- `mediaType`: The Media Type (MIME) of the image

#### Example

##### Data

```

```

##### Template

```

```

##### Result
  
  

### URL

- `source`: must be set to`URL`
- `url`: the image URL in`string`format

Note: to use images from the Internet, Document Generator needs outbound access to the Internet. For example, if Document Generator is running in a private subnet in OCI, you could set up a[NAT Gateway](https://docs.oracle.com/iaas/Content/Network/Tasks/NATgateway.htm)to allow Document Generator to connect to the Internet.

#### Example

##### Data

```

```

##### Template

```

```

##### Result
  
  

### Data URL

Document Generator also supports images provided as Data URLs. The image must be Base64-encoded.
- `source`: must be set to`URL`
- `url`: the image URL in`string`format

#### Example

##### Data

```

```

##### Template

```

```

##### Result
  
  

## Sample documents

MS Word Template JSON Data Output
[Word-Images.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Images.docx)[Word-Images.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Images.json)[Word-Images-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Images-output.docx)

# Barcode Tag

Syntax:`{bc:dataRef}`or`{barcode:dataRef}`

A Barcode tag is used to generate a barcode image in a MS Word document. Supported barcode types are:

Barcode barcodeType Example
[Code 128](https://en.wikipedia.org/wiki/Code_128)`CODE_128`  

[Code 39](https://en.wikipedia.org/wiki/Code_39)`CODE_39`  

[Data Matrix](https://en.wikipedia.org/wiki/Data_Matrix)`DATA_MATRIX`  

[International Article Number (EAN)](https://en.wikipedia.org/wiki/International_Article_Number)`EAN`  

[Quick-response code (QR code)](https://en.wikipedia.org/wiki/QR_code)`QR`  

[PDF417](https://en.wikipedia.org/wiki/PDF417)`PDF417`  

[Universal Product Code (UPC)](https://en.wikipedia.org/wiki/Universal_Product_Code)`UPC`  

## QuietZone

- `verticalSize`: number - Size of the vertical quiet zone (above and below the barcode)
- `horizontalSize`: number - Size of the horizontal quiet zone (right and left of the barcode)

### Example

```

```

## Properties common to all barcodes

- `barcodeType`(required):`CODE_128`,`CODE_39`,`DATA_MATRIX`,`EAN`,`QR`,`PDF417`,`UPC`
- `data`(required): String - Data to be encoded
- `moduleWidth`: number (default: 1) - The width of each bar in the barcode for 1D barcodes. The width and height of each dot for 2D barcodes
- `quietZone`: QuietZone - The empty space surrounding a barcode
- `scale`: number (default: 1.0) - Scale factor for the barcode image. All dimensions will be multiplied by this factor to generate a larger (scale &gt; 1) or smaller (scale &lt; 1) image
- `rotation`:`DEGREES_0`(default),`DEGREES_90`,`DEGREES_180`,`DEGREES_270`
- `altText`: String - Alternative text for the barcode image

## Code 128 - Specific properties

- `barHeight`: number (default: 40) - Height of each bar
- `fontSize`: number (default: 8) - Font size in points for human-readable text in the barcode image
- `allowedCodeSets`:`A`,`B`,`C`,`AB`,`ABC`(default)

### Example

```

```

## Code 39 - Specific properties

- `barHeight`: number (default: 40) - Height of each bar
- `fontSize`: number (default: 8) - Font size for human-readable text in the barcode image
- `moduleWidthRatio`: number (default: 2) - Ratio of wide bar width to narrow bar width. Allowed values are 2 or 3
- `isExtended`: boolean (default: false) - Whether to use Extended Code 39 to encode the full ASCII set
- `checkDigitType`:`NONE`(default),`MOD_43`

### Example

```

```

## Data Matrix - Specific properties

- `shape`:`SQUARE`,`RECTANGULAR`- If not specified, the smallest shape will be used. Note that if the`size`is specified, the shape will not be used
- `size`: number (from 1 to 30) - Size of the data matrix. If not specified, the optimal size is chosen based on the data to be encoded

### Example

```

```

## International Article Number (EAN) - Specific properties

- `barHeight`: number (default: 40) - Height of each bar
- `fontSize`: number (default: 8) - Font size for human-readable text in the barcode image
- `eanType`:`EAN_8`,`EAN_13`(default)

### Example

```

```

## Quick-response code (QR code) - Specific properties

- `version`: number (from 1 to 40) - QR code version. Determines the size of the symbol and how much data it can encode. Defaults to the minimum version necessary to encode the data
- `minEccLevel`:`LOW`,`MEDIUM`,`QUARTILE`,`HIGH`. Minimum error correction level. Defaults to the maximum level possible for the selected version and data
- `forceByteCompaction`: boolean (default: false) - Whether to force byte compaction mode. If false, the optimal compaction mode is chosen based on the data to be encoded

### Example

```

```

## PDF417 - Specific properties

- `forceByteCompaction`: boolean (default: false) - Whether to force byte compaction mode. If false, the optimal compaction mode is chosen based on the data to be encoded
- `rowHeight`: number (default: 3)
- `pdf417Type`:`NORMAL`(default),`TRUNCATED`,`MICRO`
- `eccLevel`: number (from 0 to 8) - The amount of the barcode to dedicate to error correction codewords. The number of error correction codewords is determined by 2^(eccLevel + 1). If not specified, a value is chosen based on the data to be encoded. Ignored for micro PDF417 barcodes

### Example

```

```

## Universal Product Code (UPC) - Specific properties

- `upcType`:`UPC_A`(default),`UPC_E`
- `barHeight`: number (default: 40) - Height of each bar
- `fontSize`: number (default: 8) - Font size for human-readable text in the barcode image
- `guardPatternExtraHeight`: number (default: 5) - Extra height for guard patterns
- `showCheckDigit`: boolean (default: true) - Whether to show the check digit in the human-readable text

### Example

```

```

## Example

### Data

```

```

### Template
  
  

### Output
  
  

## Sample documents

MS Word Template JSON Data Output
[Word-Barcodes.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Barcodes.docx)[Word-Barcodes.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Barcodes.json)[Word-Barcodes-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Barcodes-output.docx)

For more examples of variations for each barcode type, refer to the Excel tag examples.

# HTML Tag

Syntax:`{html:dataRef}`

An HTML tag is used to inject sanitized HTML into an MS Word document. The HTML is converted to an MS Word format.

## Supported HTML tags

`a`,`b`,`br`,`code`,`dd`,`del`,`div`,`dl`,`dt`,`em`,`figure`,`h1`,`h2`,`h3`,`h4`,`h5`,`h6`,`hr`,`i`,`img`,`ins`,`li`,`ol`,`p`,`s`,`small`,`span`,`strong`,`sub`,`sup`,`table`,`u`,`ul`,`var`

## Tables

HTML tables are supported. If an HTML table is inserted inside a Word table cell, only one level of HTML table nesting is supported. These are the supported table elements:
- `<table> ... </table>`
- `<col> </col>`
- `<colgroup> </colgroup>`
- `<tr> ... </tr>`
- `<th> ... </th>`
- `<td> ... </td>`
- `<thead> ... </thead>`
- `<tbody> ... </tbody>`
- `<tfoot> ... </tfoot>`

## Class-to-style mapping

- Use`class`in the HTML only to select Word styles. In particular, for using a specific font, specify a`class`that refers to a MS Word style that uses this font in the MS Word document.
- Heading tags`<h1>`...`<h6>`are always normalized to Word`Heading1`...`Heading6`.

### Basics

- HTML`class`is used for Word style mapping only .
- For non-heading elements,`class`is interpreted as a single Word style reference.

### Supported selector subset

Supported element selectors:
- `a`,`caption`,`col`,`colgroup`,`dd`,`div`,`dl`,`dt`,`figcaption`,`figure`
- `h1`,`h2`,`h3`,`h4`,`h5`,`h6`
- `hr`,`img`,`li`,`ol`,`p`,`pre`,`span`
- `table`,`tbody`,`td`,`tfoot`,`th`,`thead`,`tr`,`ul`

Supported descendant selectors:
- `thead th`,`thead td`,`tbody td`

`:root`is supported only for custom property collection (see variables section).

### Supported CSS property subset

Allowed properties:

Allowed text/formatting properties:
- `color`,`background-color`,`font-size`,`font-weight`,`font-style`,`text-decoration`,`vertical-align`,`text-align`,`line-height`

Allowed spacing properties:
- `margin`,`margin-top`,`margin-right`,`margin-bottom`,`margin-left`
- `padding`,`padding-top`,`padding-right`,`padding-bottom`,`padding-left`

Allowed table/box properties:
- `width`,`height`
- `border`,`border-top`,`border-right`,`border-bottom`,`border-left`
- `border-collapse`,`table-layout`

Not supported (dropped):
- `font-family`,`font`
- `background-image`
- CSS`url(...)`
- unsupported at-rules (`@import`,`@font-face`, etc.)
- inline custom properties (for example`style="--x: ..."`)

Allowed CSS function subset in values:
- `var(...)`
- `rgb(...)`,`rgba(...)`
- `hsl(...)`,`hsla(...)`

All other functions are dropped (for example`calc(...)`).

### CSS variables (`var(...)`) support

Limited, explicit support is provided:
- Variables are collected from`:root`declarations in`<style>`blocks.
- Supported forms:`var(--x)`and`var(--x, fallback)`
- If unresolved and no fallback is provided, the declaration is dropped.

## Example

### Data

```

```

### Template
  
  

### Output
  
  

## Sample documents

MS Word Template JSON Data Output
[Word-Html.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Html.docx)[Word-Html.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Html.json)[Word-Html-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Html-output.docx)

# Page Break and Column Break Tag

Syntax:`{?breakCondition}`or`{pb:breakCondition}`or`{pageBreak:breakCondition}`

The`breakCondition`controls whether Document Generator inserts a page break, a column break, or no break. It can be:

Template value Meaning
`{?true}`Always insert a page break
`{?my_break}`Resolve`my_break`from the JSON data
`{?expr(age >= 18)}`Evaluate a conditional expression and insert a page break when it is true

When`breakCondition`is a JSON data reference, the resolved JSON value determines the result:

JSON value Result
`true`Page break
`"true"`Page break
`"page"`or`"pagebreak"`Page break
`"column"`or`"columnbreak"`Column break
`false`,`null`, missing data, or any other value No break

When`breakCondition`is an`expr(...)`conditional expression, Document Generator inserts a page break if the expression evaluates to`true`. Expressions do not create column breaks. See the section below on[conditional expressions](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/DocGen-Template-Tags.htm#conditional-expressions).

## Example

### Data

```

```

### Template

```

```

## Sample documents

MS Word Template JSON Data Output
[Word-Breaks.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Breaks.docx)[Word-Breaks.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Breaks.json)[Word-Breaks-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Breaks-output.docx)

# Hyperlink Tag

Syntax:`{hy:dataRef}`or`{hyperlink:dataRef}`or`{*dataRef}`

A Hyperlink tag is used to insert a clickable hyperlink (including email addresses) into a document. A hyperlink must be provided as an object with the following properties:
- `url`: a URL in`string`format
- `url_text`(optional): a`string`to be displayed instead of the URL

## Example

### Data

```

```

### Template

```

```

### Result

Follow the link:[Click me!](https://www.oracle.com/)

## Sample documents

MS Word Template JSON Data Output
[Word-Hyperlinks.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Hyperlinks.docx)[Word-Hyperlinks.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Hyperlinks.json)[Word-Hyperlinks-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-Hyperlinks-output.docx)

# Number Formatting

If a value supplied to a basic tag is a number, Document Generator can format it.

A formatter is specified as follows:`{input_number|format:[format]:[separators]:[currency_symbol]}`where:
- `[format]`is a supported number format
- `[separators]`(optional) is a 2 character string. The first character indicates the decimal separator, the second character indicates the comma separator
- `[currency_symbol]`(optional) the currency symbol to apply if`L`is present in`[format]`

Number formats must be specified in one of the following[Oracle Number Formats](https://docs.oracle.com/en/database/oracle/oracle-database/23/sqlrf/Format-Models.html#GUID-24E16D8D-25E4-4BD3-A38D-CE1399F2897C):
- `FML999G999G999G999G990D00`
- `FML999G999G999G999G990`
- `999G999G999G999G990D00`
- `999G999G999G999G990D0000`
- `999G999G999G999G999G999G990`
- `999G999G999G999G990D00MI`
- `S999G999G999G999G990D00`
- `999G999G999G999G990D00S`
- `S999G999G999G999G990D00`
- `999G999G999G999G990D00PR`
- `FML999G999G999G999G990PR`
- `999G999G999G999G990D00PR`

## Examples

The following table shows examples of these formats, given a number:

Template unit_price: 1234.5 unit_price: -1234.5
`{unit_price|format:"FML999G999G999G999G990D00":"<>":"$"}`$1&gt;234&lt;50 -$1&gt;234&lt;50
`{unit_price|format:"999G999G999G999G990D00":",."}`1.234,50 -1.234,50
`{unit_price|format:"999G999G999G999G990D00":", "}`1 234,50 -1 234,50
`{unit_price|format:"999G999G999G999G999G999G990"}`1,234 -1,234
`{unit_price|format:"999G999G999G999G990D00MI"}`1,234.50 1,234.50-
`{unit_price|format:"S999G999G999G999G990D00"}`+1,234.50 -1,234.50
`{unit_price|format:"999G999G999G999G990D00PR"}`1,234.50 &lt;1,234.50&gt;
`{unit_price|format:"FML999G999G999G999G990PR"}`$1,234 &lt;$1,234&gt;

# Date Formatting

If a value supplied to a basic tag is an[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)date-time, Document Generator can format it.

Time Zone considerations:
- Input: When the time zone is not specified in the input date-time, UTC is used.
- Output: When the time zone is not specified in the output date, the input time zone is used.

A formatter is specified as follows:`{input_date|format_date:[format]:[time_zone]}`where:
- `[format]`is a supported date-time format
- `[time_zone]`(optional) is a character string representing a time zone, such as`America/Los_Angeles`,`UTC`or`+09:30`.

Date-time output formats must be specified as a[Java DateTime Formats](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/format/DateTimeFormatter.html).

## Examples

The following table shows examples of these formats, given a date with a time zone:

Template input_date: 2023-12-31T23:01:22-04:00
`{input_date|format_date:"dd-MM-yy HH:mm:ss"}`31-12-23 23:01:22
`{input_date|format_date:dd/MM/yyyy}`31/12/2023
`{input_date|format_date:"MMM dd, yyyy HH:mm:ss"}`Dec 31, 2023 23:01:22
`{input_date|format_date:"yyyy-MM-dd HH:mm:ss":"America/Los_Angeles"}`2023-12-31 19:01:22
`{input_date|format_date:"yyyy-MM-dd HH:mm:ss":"UTC"}`2024-01-01 03:01:22
`{input_date|format_date:"yyyy-MM-dd HH:mm:ss":"Z"}`2024-01-01 03:01:22
`{input_date|format_date:"yyyy-MM-dd HH:mm:ss":"+09:30"}`2024-01-01 12:31:22

The following table shows examples of these formats, given a date without a time zone:

Template input_date: 2023-12-31T23:01:22
`{input_date|format_date:"dd-MM-yy HH:mm:ss"}`31-12-23 23:01:22
`{input_date|format_date:dd/MM/yyyy}`31/12/2023
`{input_date|format_date:"MMM dd, yyyy HH:mm:ss"}`Dec 31, 2023 23:01:22
`{input_date|format_date:"yyyy-MM-dd HH:mm:ss":"America/Los_Angeles"}`2023-12-31 15:01:22
`{input_date|format_date:"yyyy-MM-dd HH:mm:ss":"UTC"}`2023-12-31 23:01:22
`{input_date|format_date:"yyyy-MM-dd HH:mm:ss":"Z"}`2023-12-31 23:01:22
`{input_date|format_date:"yyyy-MM-dd HH:mm:ss":"+09:30"}`2024-01-01 08:31:22

# Conditional expressions

For some Tags, Document Generator can use expressions that resolve to true or false.

These expressions combine JSON data references, operators (like`==`and`<`), built-in functions (like`StartsWith`) and literals (like`"John"`or`23`).

## Rules

- String comparisons are case-sensitive and use Unicode code-point comparison with NFC normalization.
- Operators are evaluated from left to right; precedence is: parentheses, comparisons,`&&`, then`||`. Short-circuiting applies to`&&`and`||`.
- Types are strict: numeric comparisons require numbers; equality only compares string-to-string, number-to-number, boolean-to-boolean. No cross-type coercion.
- JSON data references must be composed of letters (a-z, A-Z), underscores (_) or digits (0-9). The first character must be a letter or an underscore.
- Missing or null JSON data results in the expression resolving to false when evaluated.
- Invalid expression syntax in the template causes Document Generator to stop and return an error.

## List of supported Operators

Name Description Example
`==`True if the left operand is equal to the right operand`age == 18`
`!=`True if the left operand is not equal to the right operand`age != 18`
`>`True if the left operand is greater than the right operand`age > 18`
`>=`True if the left operand is greater than or equal to the right operand`age >= 18`
`<`True if the left operand is less than the right operand`age < 18`
`<=`True if the left operand is less than or equal to the right operand`age <= 18`
`&&`True if the left expression and the right expression are true`a == 0 && c == 42`
`||`True if the left expression or the right expression is true`a == 0 || c == 42`

## List of supported Functions

Name Description Example
`StartsWith`Data reference starts with given string`StartsWith(movieName, "The")`
`StartsWithIgnoreCase`Data reference starts with given string (case-insensitive)`StartsWithIgnoreCase(movieName, "the")`
`Contains`Data reference contains the given string`Contains(movieName, "Matrix")`
`ContainsIgnoreCase`Data reference contains the given string (case-insensitive)`ContainsIgnoreCase(movieName, "matrix")`

## Examples

Expression Comment
`age >= 18`
`a == b || c == d && e > 0``c == d && e > 0`is evaluated before`a == b`
`(title=="manager" || title == "director") && employeeCount > 2`Parentheses can be used
`StartsWith(movieName, "The") && year == 1999`Function`StartsWith`used
`Contains(movieName, "Matrix") || movies.0.actor != "Pitt"`Function`Contains`used. Referring to first actor in`movies`array
`(numberOfTomatoes > maxTomatoes) == false`Same as`numberOfTomatoes <= maxTomatoes`
`-1 >= -1.01 || UnknownName == "Smith"`Since first part is true,`UnknownName == "Smith"`is not evaluated
`Contains(drink, "Cafe\u0301")`Unicode characters are supported

# Tag - Advanced Examples

## Vertical Loop in a Vertical Loop

This example contains two nested loops: one for the movies and one for the actors.

MS Word Template JSON Data Output
[Word-LoopInLoop.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-LoopInLoop.docx)[Word-LoopInLoop.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-LoopInLoop.json)[Word-LoopInLoop-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-LoopInLoop-output.docx)

## Horizontal Loop in a Vertical Loop

This example contains two nested loops: one for the weeks and one for the days.

MS Word Template JSON Data Output
[Word-HLoopInVLoop.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-HLoopInVLoop.docx)[Word-HLoopInVLoop.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-HLoopInVLoop.json)[Word-HLoopInVLoop-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-HLoopInVLoop-output.docx)

## Aggregation and Formatting combination

In this example, the Total of the Invoice uses both Aggregation (sum) and Number Formatting.

MS Word Template JSON Data Output
[Word-AggregationAndFormat.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-AggregationAndFormat.docx)[Word-AggregationAndFormat.json](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-AggregationAndFormat.json)[Word-AggregationAndFormat-output.docx](https://docs.oracle.com/en-us/iaas/Content/Functions/non-dita/DocGenPBF-doc/markdown/examples/Word-AggregationAndFormat-output.docx)
