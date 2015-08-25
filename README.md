# whosonfirst-tools

Various tools and helper scripts for working with Who's On First data. These are one-offs and things that don't necessarily need or deserve a dedicated package.

## scripts

## download-meta

Download all the files listed in one or more `meta` files (from [whosonfirst-data](https://github.com/whosonfirst/whosonfirst-data)) and store them locally. For example:

```
$> download-meta.py --source http://whosonfirst.mapzen.com/data --dest /usr/local/mapzen/test --verbose /usr/local/mapze\
n/whosonfirst-data/meta/wof-microhood-latest.csv 
DEBUG:root:read from /usr/local/mapzen/whosonfirst-data/meta/wof-microhood-latest.csv
DEBUG:root:fetch http://whosonfirst.mapzen.com/data/102/147/449/102147449.geojson
DEBUG:root:store as /usr/local/mapzen/test/102/147/449/102147449.geojson
DEBUG:urllib3.util.retry:Converted retries value: 0 -> Retry(total=0, connect=None, read=None, redirect=0)
INFO:urllib3.connectionpool:Starting new HTTP connection (1): whosonfirst.mapzen.com
DEBUG:urllib3.connectionpool:"GET /data/102/147/449/102147449.geojson HTTP/1.1" 200 1140
DEBUG:root:fetch http://whosonfirst.mapzen.com/data/102/147/461/102147461.geojson
DEBUG:root:store as /usr/local/mapzen/test/102/147/461/102147461.geojson

# and so on
```

## See also

* https://github.com/whosonfirst/whosonfirst-data
