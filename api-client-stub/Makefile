goprotoc:
	PATH=${PATH}:$(shell go env GOPATH)/bin && \
	cd go-example && \
	protoc --go_out=. --go_opt=paths=source_relative --go-grpc_out=. --go-grpc_opt=paths=source_relative  service/api.proto

pyprotoc:
	. venv/bin/activate && \
	python -m grpc_tools.protoc -Igo-example/service --python_out=pb --pyi_out=pb --grpc_python_out=pb go-example/service/api.proto
