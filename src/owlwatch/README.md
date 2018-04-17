# owlwatch

Tool for comparing panels and mappings. A data model is defined in [schema module](schema/model.py). This model is basedon a **Schema** abstraction, used as a common definition to compare ES Mappings and Kibana panels as they are exported by [Kidash](https://github.com/grimoirelab/GrimoireELK/tree/master/kidash) tool.

## Supported Versions
Tested for:
 * ElasticSearch: 5.4.0
 * Lucene: 6.5.0
 * Kibana 5: 5.1.1-SNAPSHOT

**Currently not compatible with ElasticSeacrh versions older than 5 as ES mapping definition has changed.**

## Output
### Compare
A summary of the comparison including:
 * Index name.
 * status: OK or KO.
 * Matches: number of properties in both schemas.
 * Not found in < schema_type >: number of properties not found in the target schema.  
 * Type mismatches: number of properties having different types.

**Order matters**, so comparisons have always a source schema and a target one. In order to be considered 'compatible', target schema needs to contain, at least, all properties in the source schema with same types. Thus, finding properties in the target schema that don't exist in the source one is not considered an error.

### Check empty panels
This feature allows you to check whether a certain panel(s) is empty (or not) on a particular ES instance(s).
 * A project is a particular ES instance (e.g.: project1 could be https://project1.biterg.io). This field accepts:
  * Shortname: if the ES instance is hosted under the domain ".biterg.io" you can use the name of the project.
  * Url: if the ES instance is not hosted under the domain ".biterg.io", or it is hosted on localhost, you can use the complete url (e.g.: http://localhost:9200)
 * Storage_dir arg is mandatory if the option "--check_all" is used. The option "--check_all" will only work for all ES instances inside docker containers and
   the value of this argument (storage_dir) must be the path where all docker-compose.yml files are stored, otherwise the option "--check_all" won't work.
   e.g.: the right value of the argument "storage_dir" must be "/tmp/docker_compose_config_example/" for the path below:
   ```
   $> tree /tmp/docker_compose_config_example/
   /tmp/docker_compose_config_example/
   ├── project1
   │   └── docker-compose.yml
   ├── project2
   │   └── docker-compose.yml
   └── project3
       └── docker-compose.yml

   3 directories, 3 files
   ```
The output will show if the panel(s) is emtpy or is ok on the ES instance(s).
```
$> python3 owlwatch.py check-empty-panels --projects "project1, project2" --panels "Overview, About" -u myuser -p mypassword
Panel Overview is OK for project1
Panel Overview is OK for project2
Panel About is OK for project1
Panel About is OK for project2
```
See [Examples](#examples) section below.

## Usage
There are two commands depending on what we wish to compare: compare-mapping and compare-panel

```
$> python3 owlwatch.py -h
usage: owlwatch.py [-h] [-g | -l] [-v]
                   {compare-mapping,compare-panel,compare-csv,check-empty-panels}
                   ...

     _____________________________
    ( Who watches the dashboards? )
    ( I do.                       )
     -----------------------------
          o   -._   _.-
           o   (0),(0)
                (   )
              __.._..__Bitergia

positional arguments:
  {compare-mapping,compare-panel,compare-csv,check-empty-panels}
    compare-mapping     Compares a mapping against panel JSON file or CSV
                                index definition
    compare-panel       Compares a panel JSON file against a ES mapping or a
                                CSV index definition
    compare-csv         Compares a CSV index definition file against a ES mapping or a
                                JSON panel
    check-empty-panels  Check whether a certain panel is empty or not

optional arguments:
  -h, --help            show this help message and exit
  -g, --debug
  -l, --info
  -v, --version         show program's version number and exit
```

### Compare
#### compare-mapping
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

#### compare-panel
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

#### compare-csv
```
$> python3 owlwatch.py compare-csv -h  
usage: owlwatch.py compare-csv [-h] -c CSV_PATH_LIST
                               (-e ES_HOST | -p PANEL_PATH)

optional arguments:
  -h, --help            show this help message and exit
  -c CSV_PATH_LIST, --csv-file CSV_PATH_LIST
                        Index CSV file path. Add this argument as many times
                        as CSV files you need to check.
  -e ES_HOST, --elastic-search ES_HOST
                        ES host
  -p PANEL_PATH, --panel-file PANEL_PATH
                        Panel JSON file path
```

### Check empty panels
```
$> python3 /home/dpose/repositories/github/panels/src/owlwatch/owlwatch.py check-empty-panels -h
usage: owlwatch.py check-empty-panels [-h] (--projects PROJECTS | --check_all)
                                      [--port PORT] --panels PANELS [-u USER]
                                      [-p PASSWORD] [-s STORAGE_DIR]

optional arguments:
  -h, --help           show this help message and exit
  --projects PROJECTS  e.g.: "project1, project2"
  --check_all          Check the selected panels for all ES instances on the
                       current host
  --port PORT          e.g.: 9200
  --panels PANELS      e.g.: "panel1, panel2"
  -u USER              e.g.: myuser
  -p PASSWORD          e.g.: mypassword
  -s STORAGE_DIR       e.g.: /path_where_ES_can_be_found_on_the_host
```

### Examples
* [Mapping vs Panel](#mapping-vs-panel)
* [Panel vs Mapping](#panel-vs-mapping)
* [Panel vs CSV](#panel-vs-csv)
* [CSV vs Mapping](#csv-vs-mapping)
* [Check empty panels](#check-empty-panels)

#### Mapping vs Panel
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

#### Panel vs Mapping

Order matters, so the other way around the result could be different. In the next example, mapping has some extra properties, as shown in the example above, but at the same time covers all the properties needed by the panel to work:
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

#### Panel vs CSV

Same as above, but comparing panel against CSV to know what properties were defined in the schema but are not being used in any widget:
```
$> python3 owlwatch.py -l compare-panel -c ../../schema/slack.csv -p ../../json/slack.json
[2017-11-21 23:14:43,995 - INFO] - ** The Owl is watching **
[2017-11-21 23:14:43,995 - INFO] - Compare Panel from ../../json/slack.json
[2017-11-21 23:14:43,996 - INFO] - Against CSVs from ['../../schema/slack.csv']
[2017-11-21 23:14:43,997 - INFO] -
* Missing property: channel_purpose.last_set
* Missing property: channel_purpose.creator
* Missing property: channel_purpose.value
* Missing property: channel_topic.last_set
* Missing property: channel_topic.creator
* Missing property: channel_topic.value
Result: KO
---------
* slack *
---------
panel Vs. csv
Comparison result: KO
Matches: 58
Not found in csv:  6
Type mismatches:  0
Details:

* Missing property: channel_purpose.last_set
* Missing property: channel_purpose.creator
* Missing property: channel_purpose.value
* Missing property: channel_topic.last_set
* Missing property: channel_topic.creator
* Missing property: channel_topic.value

[2017-11-21 23:14:43,997 - INFO] - This is the end.
```

#### CSV vs Mapping

Another cool check can be done to compare CSV against the corresponding mapping. Result will tell us if the mapping is compatible with the index defined in CSV file. In fact we can compare several CSV files against a given ES host with a single command:
```
$> python3 owlwatch.py compare-csv -c ../../schema/slack.csv -c ../../schema/meetup.csv -e https://localhost:9200/data
----------
* meetup *
----------
csv Vs. mapping
Comparison result: KO
Matches: 71
Not found in mapping:  0
Type mismatches:  1
Details:

* Type mismatch:
	description_analyzed: {'type': 'text', 'agg': True} != {'type': 'text'}
	- {'agg': True, 'type': 'text'}
	+ {'type': 'text'}

---------
* slack *
---------
csv Vs. mapping
Comparison result: OK
Matches: 58
Not found in mapping:  0
Type mismatches:  0
```

#### Check empty panels
##### Check one panel on one ES instance
```
$> python3 owlwatch.py check-empty-panels --projects "project1" --panels "Overview" -u myuser -p mypassword
Panel Overview is OK for project1
```
##### Check one panel on more than one ES instance
```
$> python3 owlwatch.py check-empty-panels --projects "project1, project2" --panels "Overview" -u myuser -p mypassword
Panel Overview is OK for project1
Panel Overview is OK for project2
```
##### Check multiple panels on one ES instance
```
$> python3 owlwatch.py check-empty-panels --projects "project1" --panels "Overview, About" -u myuser -p mypassword
Panel Overview is OK for project1
Panel About is OK for project1
```
##### Check multiple panels on multiple ES instances
```
$> python3 owlwatch.py check-empty-panels --projects "project1, project2" --panels "Overview, About" -u myuser -p mypassword
Panel Overview is OK for project1
Panel Overview is OK for project2
Panel About is OK for project1
Panel About is OK for project2
```
##### Check multiple panels on all ES instances running on the current server
```
$> python3 owlwatch.py check-empty-panels --check_all --panels "Overview, About" -s "/tmp/docker_compose_config_example/"
Panel Overview is OK for project1
Panel Overview is OK for project2
Panel Overview is OK for project3
Panel Overview is OK for project4
Panel About is OK for project1
Panel About is OK for project2
Panel About is OK for project3
Panel About is OK for project4
```
