build_base:
	cd docker/base
	docker build --no-cache -f docker/base/Dockerfile -t chemical-extraction-backend-base .