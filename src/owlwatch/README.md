# owlwatch

Tool for comparing panels and mappings. A data model is defined in [schema module](schema/model.py). This model is based
on a **Schema** abstraction, used as a common definition to compare ES Mappings and Kibana panels as they are exported by
[Kidash](https://github.com/grimoirelab/GrimoireELK/tree/master/kidash) tool.

## Supported Versions
Tested for:
 * ElasticSearch: 5.4.0
 * Lucene: 6.5.0
 * Kibana 5: 5.1.1-SNAPSHOT

**Currently it is not compatible with ElasticSeacrh versions older than 5 as ES mapping definition has changed.**

## Output
A summary of the comparison including:
 * Index name.
 * status: OK or KO.
 * Matches: number of properties in both schemas.
 * Not found in <schema_type>: number of properties not found in the target schema.  
 * Type mismatches: number of properties having different types.

Order matters, so comparisons have always a source schema and a target one.
In order to be considered 'compatible', target schema needs to contain, at least,
all properties in the source schema with same types. Thus, finding properties in
the target schema that doesn't exist in the source one is not considered an
error.

See [Examples](#examples) section below.

## Usage
There are two commands depending on what we wish to compare: compare-mapping and compare-panel

```
$> python3 owlwatch.py -h
usage: owlwatch.py [-h] [-g | -l] {compare-mapping,compare-panel} ...

     _____________________________
    ( Who watches the dashboards? )
    ( I do.                       )
     -----------------------------
          o   -._   _.-
           o   (0),(0)
                (   )
              __.._..__Bitergia

positional arguments:
  {compare-mapping,compare-panel}
    compare-mapping     Compares a mapping against panel JSON file or CSV
                                index definition
    compare-panel       Compares a panel JSON file against a ES mapping or a
                                CSV index definition

optional arguments:
  -h, --help            show this help message and exit
  -g, --debug
  -l, --info
```

### compare-mapping
```
$> python3 owlwatch.py compare-mapping -h
usage: owlwatch.py compare-mapping [-h] -e ES_HOST
                                   (-p PANEL_PATH | -c CSV_PATH)

optional arguments:
  -h, --help            show this help message and exit
  -e ES_HOST, --elastic-search ES_HOST
                        ES host
  -p PANEL_PATH, --panel-file PANEL_PATH
                        Panel JSON file path
  -c CSV_PATH, --csv-file CSV_PATH
                        Index CSV file path
```

### compare-panel
```
$> python3 owlwatch.py compare-panel -h  
usage: owlwatch.py compare-panel [-h] -p PANEL_PATH (-e ES_HOST | -c CSV_PATH)

optional arguments:
  -h, --help            show this help message and exit
  -p PANEL_PATH, --panel-file PANEL_PATH
                        Panel JSON file path
  -e ES_HOST, --elastic-search ES_HOST
                        ES host
  -c CSV_PATH, --csv-file CSV_PATH
                        Index CSV file path
```

### Examples

Mapping and panel are using same properties and types.
```
$> python3 owlwatch.py compare-mapping -e https://localhost:9200/data -p ../../json/irc.json  
-------
* irc *
-------
Comparison result: OK
Matches: 30
Not found in panel:  0
Type mismatches:  0
```

Mapping contains more properties than panel:
```
$> python3 owlwatch.py compare-mapping -e https://localhost:9200/data -p ../../json/slack.json
---------
* slack *
---------
Comparison result: KO
Matches: 64
Not found in panel:  2
Type mismatches:  0
Details:

Missing property: project
Missing property: project_1

```

Order matters, so the other way around the result could be different. In the
next example, mapping has some extra properties, as shown in the example above,
but at the same time covers all the properties needed by the panel to work:
```
$> python3 owlwatch.py compare-panel -e https://localhost:9200/data -p ../../json/slack.json
---------
* slack *
---------
Comparison result: OK
Matches: 64
Not found in mapping:  0
Type mismatches:  0
```

Some missing properties in mapping and also types are different for one property:
```
$> python3 owlwatch.py compare-panel -e https://localhost:9200/data -p ../../json/git.json
-------
* git *
-------
Comparison result: KO
Matches: 32
Not found in mapping:  2
Type mismatches:  1
Details:

* Type mismatch:
	message_analyzed: {'type': 'text', 'agg': True} != {'type': 'text'}
	- {'agg': True, 'type': 'text'}
	+ {'type': 'text'}
* Missing property: github_repo
* Missing property: url_id

```

To get more details, use `-l` for activating `INFO` log level:
```
$> python3 owlwatch.py -l compare-panel -e https://localhost:9200/data -p ../../json/git.json
[2017-10-11 14:13:54,887 - INFO] - ** The Owl is watching **
[2017-10-11 14:13:55,061 - INFO] -
* Missing property: url_id
* Missing property: github_repo
* Type mismatch:
	message_analyzed: {'type': 'text', 'agg': True} != {'type': 'text'}
	- {'agg': True, 'type': 'text'}
	+ {'type': 'text'}
Result: KO
-------
* git *
-------
Comparison result: KO
Matches: 32
Not found in mapping:  2
Type mismatches:  1
Details:

* Missing property: url_id
* Missing property: github_repo
* Type mismatch:
	message_analyzed: {'type': 'text', 'agg': True} != {'type': 'text'}
	- {'agg': True, 'type': 'text'}
	+ {'type': 'text'}

[2017-10-11 14:13:55,062 - INFO] - This is the end.
```
