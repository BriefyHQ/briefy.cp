stop_containers: ## stop and remove docker containers
	# mysql
	docker ps|grep 'briefy-cp-test' |awk '{ print $$1}'|xargs docker stop
	docker ps -a|grep 'briefy-cp-test' |awk '{ print $$1}'|xargs docker rm

start_containers: stop_containers ## stop, remove and recreate docker containers
	# mysql
	docker run -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=cp --name briefy-cp-test mysql:5.7
	sleep 5
