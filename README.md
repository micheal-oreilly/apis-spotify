# apis-spotify

curl -X POST "https://api.twilio.com/2010-04-01/Accounts/AC6ef701d3c1f1b06e3136201ef111e458/Messages.json" --data-urlencode "From=+12765009157" --data-urlencode "Body=Ahoy, World!" --data-urlencode "To=+421949255079" -u AC6ef701d3c1f1b06e3136201ef111e458:1a52dd4ecddba3d671d342f2b4321016

curl -X POST "https://api.twilio.com/2010-04-01/Accounts/AC6ef701d3c1f1b06e3136201ef111e458/Messages.json" --data-urlencode "From=+12765009157" --data-urlencode "Body=Ahoy, World!" --data-urlencode "To=+12765009157" -u AC6ef701d3c1f1b06e3136201ef111e458:1a52dd4ecddba3d671d342f2b4321016

curl -X POST "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages.json" \
--data-urlencode "From=+12765009157" \
--data-urlencode "Body=Hi there" \
--data-urlencode "To=+15558675310" \
-u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN

curl -X GET "https://api.twilio.com/2010-04-01/Accounts/AC6ef701d3c1f1b06e3136201ef111e458/Messages.json" -u AC6ef701d3c1f1b06e3136201ef111e458:1a52dd4ecddba3d671d342f2b4321016


curl -X GET "https://api.twilio.com/2010-04-01/Accounts/$TWILIO_ACCOUNT_SID/Messages.json?To=%2B12765009157&PageSize=20" \
-u $TWILIO_ACCOUNT_SID:$TWILIO_AUTH_TOKEN