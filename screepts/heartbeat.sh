START_DATE=`date`
COUNT=0
while [ true ]
do
	NOW_DATE=`date`
	echo "I live for $(( (`date -d "$START_DATE" +%s` - `date -d "$NOW_DATE" +%s`) / (1000) )) seconds\;`(date -d "$START_DATE" +%Y-%m-%d:%H.%M.%S)`\;I did it $(( $COUNT + 1 )) times"
	#echo "I live for $(( (`date -d "$START_DATE" +%s` - `date -d "$NOW_DATE" +%s`) / (1000) )) seconds\;`(date -d "$START_DATE" +%Y-%m-%d:%H.%M.%S)`\;I did it $(( $COUNT + 1 )) times"
	COUNT=$(( $COUNT + 1 ))
	sleep 10
done
