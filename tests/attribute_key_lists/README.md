## Geospatial coordinate attributes

```sql
select distinct jsonb_object_keys(geo_coord_all)
from biosample
```

Manually sort into:

- TP: geo_coord_include.txt
- TN: geo_coord_exclude.txt
- FP: geo_coord_exclude_todo.txt
- [FN: unknown]

## Geospatial text attributes

```sql
select distinct jsonb_object_keys(geo_text_all)
from biosample
```

Manually sort into:

- TP: geo_text_include.txt
- TN: geo_text_exclude.txt
- FP: geo_text_exclude_todo.txt
- [FN: unknown]
