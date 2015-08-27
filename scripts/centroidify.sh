#!/bin/sh

# https://github.com/mbloch/mapshaper/wiki/Command-Reference
# https://github.com/mbloch/mapshaper/issues/63
# https://stedolan.github.io/jq/manual/

MAPSHAPER=`which mapshaper`
JQ=`which jq`

GEOJSON=$1

COORDS=`${MAPSHAPER} -i ${GEOJSON} -points inner -o - | ${JQ} '.features[] | .geometry.coordinates | @csv'`
COORDS=`echo ${COORDS} | sed 's/"//g'`
COORDS=`echo ${COORDS} | awk -F ',' '{ print $2","$1 }'`

echo $COORDS
exit 0
