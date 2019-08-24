#!/usr/bin/env python
# coding=utf-8

import os, posixpath

format_string="{Title}.epub"
#format_string="{Author(s)} - {Title}.epub"

## Can be an arbitrary format string. E.g. 
## {Author(s)} -- {Title}.epub
## Would have both author and title. 
## Talipov S.N., 2019

for f in os.listdir("."):
    if posixpath.isdir(f):
        continue
    basename, extension = posixpath.splitext(f)
    if extension.lower()!='.epub':
        continue
    
    (i,o)=os.popen2(["ebook-meta", f])
    data=o.readlines()
    i.close()
    o.close()

    data=[d.split(":") for d in data]
    data=[(d[0], ":".join(d[1:])) for d in data]
    data=dict([(d[0].strip(), d[1].strip()) for d in data])
    new_name=format_string.format(**data).replace("/","-")
    print u'Renamed: ', f,  u' -> ' + new_name.decode('utf-8')
    os.rename(f, new_name)
