watch -n 10 'aws rds-data execute-statement \
    --resource-arn "arn:aws:rds:us-east-1:797308887321:cluster:serratus-aurora" \
    --database "summary" \
    --secret-arn "arn:aws:secretsmanager:us-east-1:797308887321:secret:rds-db-credentials/cluster-KOFPN4Q2TKDBO5FHY6QO5M3S7Q/serratus-agdBn9" \
    --sql "select count(*) from biosample6"'
