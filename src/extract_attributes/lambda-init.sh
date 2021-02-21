aws lambda update-function-configuration \
    --function-name  biosample-upload-worker \
    --runtime python3.7 \
    --timeout 60 \
    --memory-size 10240

aws lambda update-function-configuration \
    --function-name  biosample-upload-manager \
    --runtime python3.8 \
    --timeout 60 \
    --memory-size 10240
