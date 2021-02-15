## Lambda setup

- run `create-layer.sh` on AWS CloudShell

```sh
aws lambda update-function-configuration \
    --function-name  biosample-upload-worker \
    --runtime python3.7
    --timeout 60 \
    --memory-size 10240
```

## SQL

```sql
ALTER TABLE biosample ADD PRIMARY KEY (biosample_id);
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
