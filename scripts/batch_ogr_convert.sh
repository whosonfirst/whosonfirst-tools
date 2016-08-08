echo "Select format (geojson, csv)"
read format

if [ "$format" = 'geojson' ]
   then
       for FILE in ${1:-}*.shp; do
       FILENEW=`echo | basename $FILE | sed "s/.shp/.geojson/"`
       echo "converting file: $FILE into $FILENEW..."
       ogr2ogr -f 'GeoJSON' $FILENEW $FILE
       done
elif [ "$format" = 'csv' ]
   then
       for FILE in ${1:-}*.shp; do
       FILENEW=`echo | basename $FILE | sed "s/.shp/.csv/"`
       echo "converting file: $FILE into $FILENEW..."
       ogr2ogr -f 'csv' $FILENEW $FILE
       done
else
   echo "Not a valid format. Please select either geojson or csv (case-sensitive)"
   bash convert_v2.sh;

fi