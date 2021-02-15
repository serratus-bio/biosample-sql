pushd worker
zip -rq package .
aws lambda update-function-code \
    --function-name biosample-upload-worker \
    --zip-file fileb://./package.zip
rm package.zip
popd

pushd manager
zip -rq package .
aws lambda update-function-code \
    --function-name biosample-upload-manager \
    --zip-file fileb://./package.zip
rm package.zip
popd
