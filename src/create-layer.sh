virtualenv ve
source ve/bin/activate
pip install lxml pytz
mkdir -p tmp/python
cp -rp ve/lib/python3.8/site-packages/* tmp/python
pushd tmp

pushd python
wget https://files.pythonhosted.org/packages/4c/33/87b15a5baeeb71bd677da3579f907e97476c5247c0e56a37079843af5424/pandas-1.2.2-cp37-cp37m-manylinux1_x86_64.whl
unzip -q pandas-1.2.2-cp37-cp37m-manylinux1_x86_64.whl
rm pandas-1.2.2-cp37-cp37m-manylinux1_x86_64.whl
rm -r *.dist-info
popd
zip -r9 -q ../layer.zip python
popd
rm -r tmp ve
