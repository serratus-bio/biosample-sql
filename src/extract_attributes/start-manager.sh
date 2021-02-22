aws rds-data execute-statement \
    --resource-arn "arn:aws:rds:us-east-1:797308887321:cluster:serratus-aurora" \
    --database "summary" \
    --secret-arn "arn:aws:secretsmanager:us-east-1:797308887321:secret:rds-db-credentials/cluster-KOFPN4Q2TKDBO5FHY6QO5M3S7Q/serratus-agdBn9" \
    --sql "truncate biosample6"

aws rds modify-current-db-cluster-capacity \
    --db-cluster-identifier serratus-aurora \
    --capacity 192 \
    --seconds-before-timeout 10

sleep 15

aws lambda invoke \
    --function-name biosample-upload-manager \
    --invocation-type Event \
    --cli-binary-format raw-in-base64-out \
    --payload '{}' \
    response.json
