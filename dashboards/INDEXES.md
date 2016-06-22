Current Supported Indexes
=========================


Git
---

```

{
   "git_enrich": {
      "mappings": {
         "items": {
            "dynamic": "true",
            "dynamic_templates": [
               {
                  "notanalyzed": {
                     "mapping": {
                        "type": "string",
                        "index": "not_analyzed"
                     },
                     "match": "*",
                     "match_mapping_type": "string"
                  }
               }
            ],
            "properties": {
               "Author": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "Committer": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_bot": {
                  "type": "boolean"
               },
               "author_date": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "author_domain": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_max_date": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "author_min_date": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "author_name": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_org_name": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_uuid": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "commit_date": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "committer_domain": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "committer_name": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "data": {
                  "type": "object",
                  "dynamic": "false"
               },
               "files": {
                  "type": "long"
               },
               "grimoire_creation_date": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "hash": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "hash_short": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "is_git_commit": {
                  "type": "long"
               },
               "lines_added": {
                  "type": "long"
               },
               "lines_changed": {
                  "type": "long"
               },
               "lines_removed": {
                  "type": "long"
               },
               "message": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "message_analyzed": {
                  "type": "string"
               },
               "metadata__timestamp": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "metadata__updated_on": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "ocean-unique-id": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "origin": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "project": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "repo_name": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "title": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "tz": {
                  "type": "long"
               },
               "utc_author": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "utc_commit": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               }
            }
         }
      }
   }
}

```

Gerrit
------

```

{
   "gerrit_enrich": {
      "mappings": {
         "items": {
            "dynamic": "true",
            "dynamic_templates": [
               {
                  "notanalyzed": {
                     "mapping": {
                        "type": "string",
                        "index": "not_analyzed"
                     },
                     "match": "*",
                     "match_mapping_type": "string"
                  }
               }
            ],
            "properties": {
               "author_bot": {
                  "type": "boolean"
               },
               "author_domain": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_name": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_org_name": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_uuid": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "branch": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "closed": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "data": {
                  "type": "object",
                  "dynamic": "false"
               },
               "domain": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "githash": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "grimoire_creation_date": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "is_gerrit_review": {
                  "type": "long"
               },
               "metadata__timestamp": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "metadata__updated_on": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "name": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "number": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "ocean-unique-id": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "opened": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "origin": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "patchsets": {
                  "type": "long"
               },
               "repository": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "status": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "summary": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "summary_analyzed": {
                  "type": "string"
               },
               "timeopen": {
                  "type": "double"
               },
               "url": {
                  "type": "string",
                  "index": "not_analyzed"
               }
            }
         }
      }
   }
}

```

Mboxes
------

```


{
   "mbox_enrich": {
      "mappings": {
         "items": {
            "dynamic": "true",
            "dynamic_templates": [
               {
                  "notanalyzed": {
                     "mapping": {
                        "type": "string",
                        "index": "not_analyzed"
                     },
                     "match": "*",
                     "match_mapping_type": "string"
                  }
               }
            ],
            "properties": {
               "Date": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "From": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "Message-ID": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "Subject": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "Subject_analyzed": {
                  "type": "string"
               },
               "author_bot": {
                  "type": "boolean"
               },
               "author_domain": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_name": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_org_name": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_uuid": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "data": {
                  "type": "object",
                  "dynamic": "false"
               },
               "email_date": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "grimoire_creation_date": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "is_mbox_message": {
                  "type": "long"
               },
               "is_pipermail_message": {
                  "type": "long"
               },
               "list": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "metadata__timestamp": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "metadata__updated_on": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "ocean-unique-id": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "origin": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "root": {
                  "type": "boolean"
               },
               "size": {
                  "type": "long"
               },
               "tz": {
                  "type": "long"
               }
            }
         }
      }
   }
}

```

Jenkins
-------

```

{
   "jenkins_enrich": {
      "mappings": {
         "items": {
            "dynamic": "true",
            "dynamic_templates": [
               {
                  "notanalyzed": {
                     "mapping": {
                        "type": "string",
                        "index": "not_analyzed"
                     },
                     "match": "*",
                     "match_mapping_type": "string"
                  }
               }
            ],
            "properties": {
               "build_date": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "builtOn": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "data": {
                  "type": "object",
                  "dynamic": "false"
               },
               "duration": {
                  "type": "long"
               },
               "duration_days": {
                  "type": "double"
               },
               "fullDisplayName": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "fullDisplayName_analyzed": {
                  "type": "string"
               },
               "grimoire_creation_date": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "is_jenkins_job": {
                  "type": "long"
               },
               "job_url": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "metadata__timestamp": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "metadata__updated_on": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "ocean-unique-id": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "origin": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "result": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "url": {
                  "type": "string",
                  "index": "not_analyzed"
               }
            }
         }
      }
   }
}

```

Github Issues/Pull Requests
---------------------------

```

{
   "github_issues": {
      "mappings": {
         "items": {
            "dynamic": "true",
            "dynamic_templates": [
               {
                  "notanalyzed": {
                     "mapping": {
                        "type": "string",
                        "index": "not_analyzed"
                     },
                     "match": "*",
                     "match_mapping_type": "string"
                  }
               }
            ],
            "properties": {
               "assignee_bot": {
                  "type": "boolean"
               },
               "assignee_domain": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "assignee_email": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "assignee_geolocation": {
                  "type": "geo_point"
               },
               "assignee_location": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "assignee_login": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "assignee_org": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "assignee_org_name": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "assignee_uuid": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_domain": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_org_name": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "author_uuid": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "closed_at": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "created_at": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "data": {
                  "type": "object",
                  "dynamic": "false"
               },
               "github_repo": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "grimoire_creation_date": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "id": {
                  "type": "long"
               },
               "id_in_repo": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "is_github_issue": {
                  "type": "long"
               },
               "labels": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "metadata__timestamp": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "metadata__updated_on": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "ocean-unique-id": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "origin": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "pull_request": {
                  "type": "boolean"
               },
               "repository": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "state": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "time_open_days": {
                  "type": "double"
               },
               "time_to_close_days": {
                  "type": "double"
               },
               "title": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "title_analyzed": {
                  "type": "string"
               },
               "updated_at": {
                  "type": "date",
                  "format": "strict_date_optional_time||epoch_millis"
               },
               "url": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "url_id": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "user_bot": {
                  "type": "boolean"
               },
               "user_domain": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "user_email": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "user_geolocation": {
                  "type": "geo_point"
               },
               "user_location": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "user_login": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "user_org": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "user_org_name": {
                  "type": "string",
                  "index": "not_analyzed"
               },
               "user_uuid": {
                  "type": "string",
                  "index": "not_analyzed"
               }
            }
         }
      }
   }
}

```
