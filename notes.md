## Lambda setup

- run `create-layer.sh` on AWS CloudShell
    - [wrote a blog post about this](https://victorl.in/aws-lambda-layer-cloudshell/)

## SQL

```sql
ALTER TABLE biosample ADD PRIMARY KEY (biosample_id);
```

some interesting queries:

```sql
select count(*) from biosample
where lat_lon is not null or geo_loc_name is not null

select count(distinct geo_loc_name) from biosample

select geo_loc_name, count(*) from biosample
group by geo_loc_name
limit 100


-- json stuff

select *, jsonb_object_keys(geo_coord) from biosample2

select * from biosample2
where geo_coord->>'lat_lon' is not null

SELECT
  DISTINCT field
FROM (
  SELECT jsonb_object_keys(geo_coord) AS field
  FROM biosample2
) AS subquery
```

## unzip to s3

```sh
# copy biosample_set.xml.gz
wget -qO- https://ftp.ncbi.nlm.nih.gov/biosample/biosample_set.xml.gz | aws s3 cp - s3://serratus-public/notebook/210212_geo/victorlin/biosample_parse/biosample_set.xml.gz

# unzip to biosample_set.xml
aws s3 cp s3://serratus-public/notebook/210212_geo/victorlin/biosample_parse/biosample_set.xml.gz - | zcat | aws s3 cp - s3://serratus-public/notebook/210212_geo/victorlin/biosample_parse/biosample_set.xml
```

## head

```bsh
zcat < biosample_set.xml.gz | head -n 100000 > head.xml
```

## TODO

- fix XML mismatch error in last batch
    - `start,end = 42497641724,42509614403`
- geocoding
