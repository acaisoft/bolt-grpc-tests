
# Simple gRPC service in Go 
This is a simple gRPC API in Go, and it acts as a performance testing target for Bolt.
The service gathers some rudimentary statistics (like the total number of requests) to be scraped by Prometheus. On top of that, there are tons of other stats gathered by `node_exporter` that run in tandem with the service. 

## Deployment 
The service is deployed in GCP; below you can find the most important details about it:
 | | |
 |--|--|
 |IP|`34.118.123.171`|
 |gRPC service port| `50051` |
 |Zone|`europe-central2-a`|
 |Machine type|`e2-medium`| 

## Statistics 
We are gathering statistics regarding both the machine and the service itself. 
These metrics are available at the following addresses, respectively:
|address|source|
|--|--|
|`34.118.123.171:9100/metrics`|VM metrics|
|`34.118.123.171:8081/metrics`|gRPC API metrics| 

## Endpoints 
The API publishes three endpoints enabling simple interaction via gRPC:
|name|arguments|response|description|
|--|--|--|--|
|TriggerCounter|`value`(optional)|`value`|Increments internal counter by `value` if provided or by `1` if omitted.|
|GetCounter| - |`value`|Returns the current value of internal counter|
|ResetCounter| - |`<string>`:`"Counter reset to 0."`|Sets internal counter as `0`| 

## Tests 
Even simpler than the API itself, triggering all three endpoints with equal frequency. It's possible to observe efficiency and the total number of requests handled, as well as latency, service load, and many other statistics and metrics.
