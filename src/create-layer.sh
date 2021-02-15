virtualenv ve
source ve/bin/activate
pip install -r requirements.txt
mkdir -p tmp/python
cp -rp ve/lib/python3.8/site-packages/* tmp/python
pushd tmp
pushd python
rm -r *.dist-info
popd
zip -r9 -q ../layer.zip python
popd
rm -r tmp ve
