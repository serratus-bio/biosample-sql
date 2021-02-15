## unzip to s3

```
wget -qO- https://ftp.ncbi.nlm.nih.gov/biosample/biosample_set.xml.gz | aws s3 cp - s3://serratus-public/notebook/210212_geo/victorlin/biosample_parse/biosample_set.xml.gz

aws s3 cp s3://serratus-public/notebook/210212_geo/victorlin/biosample_parse/biosample_set.xml.gz - | zcat | aws s3 cp - s3://serratus-public/notebook/210212_geo/victorlin/biosample_parse/biosample_set.xml
```

## head

```bsh
zcat < biosample_set.xml.gz | head -n 1000 > head.xml
```

## dir(element)

```
__bool__
__class__
__contains__
__copy__
__deepcopy__
__delattr__
__delitem__
__dir__
__doc__
__eq__
__format__
__ge__
__getattribute__
__getitem__
__gt__
__hash__
__init__
__init_subclass__
__iter__
__le__
__len__
__lt__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__reversed__
__setattr__
__setitem__
__sizeof__
__str__
__subclasshook__
_init
addnext
addprevious
append
attrib
base
clear
cssselect
extend
find
findall
findtext
get
getchildren
getiterator
getnext
getparent
getprevious
getroottree
index
insert
items
iter
iterancestors
iterchildren
iterdescendants
iterfind
itersiblings
itertext
keys
makeelement
nsmap
prefix
remove
replace
set
sourceline
tag
tail
text
values
xpath
```
