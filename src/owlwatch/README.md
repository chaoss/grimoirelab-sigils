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
A list of properties and their differences, if any, followed by a status line and a summary of differences if it is the case. 
See [Examples](#examples) section below.

## Usage
There are two commands depending on what we wish to compare: compare-mapping and compare-panel

```
$> python3 owlwatch.py -h
usage: owlwatch.py [-h] [-g] {compare-mapping,compare-panel} ...

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
$> python3 owlwatch.py compare-mapping -e https://localhost:3600/data -p ../../json/irc.json  
[2017-10-03 13:54:46,495 - INFO] - ** The Owl is watching **
   'author_bot': {'agg': True, 'type': 'boolean'}
   'author_id': {'agg': True, 'type': 'keyword'}
   'author_name': {'agg': True, 'type': 'keyword'}
   'author_org_name': {'agg': True, 'type': 'keyword'}
   'author_user_name': {'agg': True, 'type': 'keyword'}
   'author_uuid': {'agg': True, 'type': 'keyword'}
   'body': {'agg': True, 'type': 'keyword'}
   'body_analyzed': {'agg': True, 'type': 'text'}
   'channel': {'agg': True, 'type': 'keyword'}
   'grimoire_creation_date': {'agg': True, 'type': 'date'}
   'is_supybot_message': {'agg': True, 'type': 'number'}
   'metadata__enriched_on': {'agg': True, 'type': 'date'}
   'metadata__gelk_backend_name': {'agg': True, 'type': 'keyword'}
   'metadata__gelk_version': {'agg': True, 'type': 'keyword'}
   'metadata__timestamp': {'agg': True, 'type': 'date'}
   'metadata__updated_on': {'agg': True, 'type': 'date'}
   'nick': {'agg': True, 'type': 'keyword'}
   'nick_bot': {'agg': True, 'type': 'boolean'}
   'nick_id': {'agg': True, 'type': 'keyword'}
   'nick_name': {'agg': True, 'type': 'keyword'}
   'nick_org_name': {'agg': True, 'type': 'keyword'}
   'nick_user_name': {'agg': True, 'type': 'keyword'}
   'nick_uuid': {'agg': True, 'type': 'keyword'}
   'ocean-unique-id': {'agg': True, 'type': 'keyword'}
   'origin': {'agg': True, 'type': 'keyword'}
   'sent_date': {'agg': True, 'type': 'date'}
   'tag': {'agg': True, 'type': 'keyword'}
   'type': {'agg': True, 'type': 'keyword'}
   'update_date': {'agg': True, 'type': 'date'}
   'uuid': {'agg': True, 'type': 'keyword'}
Result: OK
[2017-10-03 13:54:46,718 - INFO] - This is the end.
```

Mapping and panel are using different properties or types.
```
$> python3 owlwatch.py compare-mapping -e https://localhost:3600/data -p ../../json/slack.json
[2017-10-03 14:00:56,830 - INFO] - ** The Owl is watching **
[2017-10-03 14:00:57,088 - ERROR] - {'subscribed': {'agg': True, 'type': 'numbe[3187 chars]er'}} != {'file_is_public': {'agg': True, 'type': 'n[3200 chars]er'}}
  {'author_bot': {'agg': True, 'type': 'number'},
   'author_domain': {'agg': True, 'type': 'keyword'},
   'author_id': {'agg': True, 'type': 'keyword'},
   'author_name': {'agg': True, 'type': 'keyword'},
   'author_org_name': {'agg': True, 'type': 'keyword'},
   'author_user_name': {'agg': True, 'type': 'keyword'},
   'author_uuid': {'agg': True, 'type': 'keyword'},
   'avatar': {'agg': True, 'type': 'keyword'},
   'channel_created': {'agg': True, 'type': 'number'},
   'channel_id': {'agg': True, 'type': 'keyword'},
   'channel_is_archived': {'agg': True, 'type': 'number'},
   'channel_is_general': {'agg': True, 'type': 'number'},
   'channel_is_starred': {'agg': True, 'type': 'number'},
   'channel_member_count': {'agg': True, 'type': 'number'},
   'channel_name': {'agg': True, 'type': 'keyword'},
   'channel_purpose.creator': {'agg': True, 'type': 'keyword'},
   'channel_purpose.last_set': {'agg': True, 'type': 'number'},
   'channel_purpose.value': {'agg': True, 'type': 'keyword'},
   'channel_topic.creator': {'agg': True, 'type': 'keyword'},
   'channel_topic.last_set': {'agg': True, 'type': 'number'},
   'channel_topic.value': {'agg': True, 'type': 'keyword'},
   'file_id': {'agg': True, 'type': 'keyword'},
   'file_is_editable': {'agg': True, 'type': 'number'},
   'file_is_external': {'agg': True, 'type': 'number'},
   'file_is_public': {'agg': True, 'type': 'number'},
   'file_mode': {'agg': True, 'type': 'keyword'},
   'file_name': {'agg': True, 'type': 'keyword'},
   'file_size': {'agg': True, 'type': 'number'},
   'file_title': {'agg': True, 'type': 'keyword'},
   'file_type': {'agg': True, 'type': 'keyword'},
   'grimoire_creation_date': {'agg': True, 'type': 'date'},
   'is_admin': {'agg': True, 'type': 'number'},
   'is_owner': {'agg': True, 'type': 'number'},
   'is_primary_owner': {'agg': True, 'type': 'number'},
   'is_slack_message': {'agg': True, 'type': 'number'},
   'metadata__enriched_on': {'agg': True, 'type': 'date'},
   'metadata__gelk_backend_name': {'agg': True, 'type': 'keyword'},
   'metadata__gelk_version': {'agg': True, 'type': 'keyword'},
   'metadata__timestamp': {'agg': True, 'type': 'date'},
   'metadata__updated_on': {'agg': True, 'type': 'date'},
   'number_attachs': {'agg': True, 'type': 'number'},
   'origin': {'agg': True, 'type': 'keyword'},
   'profile_title': {'agg': True, 'type': 'keyword'},
   'reaction_count': {'agg': True, 'type': 'number'},
   'reactions': {'agg': True, 'type': 'keyword'},
   'reply_count': {'agg': True, 'type': 'number'},
   'subscribed': {'agg': True, 'type': 'number'},
   'subtype': {'agg': True, 'type': 'keyword'},
   'tag': {'agg': True, 'type': 'keyword'},
   'team_id': {'agg': True, 'type': 'keyword'},
   'text': {'agg': True, 'type': 'keyword'},
-  'text_analyzed': {'type': 'text'},
+  'text_analyzed': {'agg': True, 'type': 'text'},
?                    +++++++++++++

   'type': {'agg': True, 'type': 'keyword'},
   'tz': {'agg': True, 'type': 'number'},
   'unread_count': {'agg': True, 'type': 'number'},
   'user': {'agg': True, 'type': 'keyword'},
   'user_data_bot': {'agg': True, 'type': 'number'},
   'user_data_domain': {'agg': True, 'type': 'keyword'},
   'user_data_id': {'agg': True, 'type': 'keyword'},
   'user_data_name': {'agg': True, 'type': 'keyword'},
   'user_data_org_name': {'agg': True, 'type': 'keyword'},
   'user_data_user_name': {'agg': True, 'type': 'keyword'},
   'user_data_uuid': {'agg': True, 'type': 'keyword'},
   'uuid': {'agg': True, 'type': 'keyword'}}
Result: ERROR [+]: 1 [-]: 1
[2017-10-03 14:00:57,089 - INFO] - This is the end.

```
