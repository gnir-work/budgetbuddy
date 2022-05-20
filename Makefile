CONTAINER_NAME=splunk_dashboard
HEC_NAME=splunk_hec_token
USERNAME=admin
PASSWORD=12345678
INDEX_NAME=bank

start:
	CONTAINER_NAME=${CONTAINER_NAME} PASSWORD=${PASSWORD} docker-compose up

stop:
	docker-compose down

splunk-bash:
	docker exec -it ${CONTAINER_NAME} bash

splunk-configure-index:
	# Added dash in order to skip failure in case the index doesnt exist
	- docker exec -it ${CONTAINER_NAME} sudo /opt/splunk/bin/splunk remove index ${INDEX_NAME}
	docker exec -it ${CONTAINER_NAME} sudo /opt/splunk/bin/splunk add index ${INDEX_NAME} 
	docker exec -it ${CONTAINER_NAME} sudo /opt/splunk/bin/splunk http-event-collector update splunk_hec_token -uri https://localhost:8089 -index ${INDEX_NAME} -auth ${USERNAME}:${PASSWORD}
