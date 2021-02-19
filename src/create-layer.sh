virtualenv ve
source ve/bin/activate
pip install -r ../requirements.txt
mkdir -p tmp/python
cp -rp ve/lib/python3.7/site-packages/* tmp/python
cp -rp ve/lib64/python3.7/site-packages/* tmp/python
pushd tmp
pushd python
rm -r *.dist-info *.virtualenv
popd
zip -r9 -q ../layer.zip python
popd
rm -r tmp ve

aws s3 cp layer.zip s3://serratus-aurora/lambda/layer.zip

aws lambda publish-layer-version \
    --layer-name biosample-upload \
    --content S3Bucket=serratus-aurora,S3Key=lambda/layer.zip \
    --compatible-runtimes python3.7

aws lambda update-function-configuration \
    --function-name  biosample-upload-worker \
    --layers "arn:aws:lambda:us-east-1:797308887321:layer:biosample-upload:8"
