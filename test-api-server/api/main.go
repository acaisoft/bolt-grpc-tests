package main

import (
	"context"
	"flag"
	"fmt"
	"github.com/prometheus/client_golang/prometheus"
	"github.com/prometheus/client_golang/prometheus/promhttp"
	"log"
	"net"
	"net/http"

	pb "api/service"
	grpcprom "github.com/grpc-ecosystem/go-grpc-middleware/providers/prometheus"
	"google.golang.org/grpc"
	"sync/atomic"
)

var (
	port            = flag.Int("port", 50051, "The server port")
	metricsPort     = flag.Int("metrics-port", 8081, "The metrics server port")
	counterResetMsg = string("Counter reset to 0.")
	ops             atomic.Int64
)

type server struct {
	pb.ApiServer
}

func (s *server) TriggerCounter(ctx context.Context, in *pb.ApiRequest) (*pb.CounterReply, error) {
	if in.GetValue() == 0 {
		ops.Add(1)
	} else {
		ops.Add(in.GetValue())
	}
	value := ops.Load()
	reply := pb.CounterReply{
		Value: &value,
	}
	return &reply, nil
}

func (s *server) GetCounter(ctx context.Context, in *pb.ApiRequest) (*pb.CounterReply, error) {
	value := ops.Load()
	reply := pb.CounterReply{
		Value: &value,
	}
	return &reply, nil
}

func (s *server) ResetCounter(ctx context.Context, in *pb.ApiRequest) (*pb.ApiReply, error) {
	ops.Store(0)
	reply := pb.ApiReply{
		Message: &counterResetMsg,
	}
	return &reply, nil
}

func main() {
	flag.Parse()

	srvMetrics := grpcprom.NewServerMetrics(
		grpcprom.WithServerHandlingTimeHistogram(
			grpcprom.WithHistogramBuckets([]float64{0.001, 0.01, 0.1, 0.3, 0.6, 1, 3, 6, 9, 20, 30, 60, 90, 120}),
		),
	)

	reg := prometheus.NewRegistry()
	reg.MustRegister(srvMetrics)
	reg.MustRegister()

	s := grpc.NewServer(
		grpc.ChainUnaryInterceptor(
			srvMetrics.UnaryServerInterceptor(),
		))

	pb.RegisterApiServer(s, &server{})
	srvMetrics.InitializeMetrics(s)

	httpPort := fmt.Sprintf(":%d", *metricsPort)
	http.Handle("/metrics", promhttp.HandlerFor(reg, promhttp.HandlerOpts{}))

	go func() {
		log.Printf("starting metrics server at %v", httpPort)
		if err := http.ListenAndServe(httpPort, nil); err != nil {
			log.Fatalf("failed to serve metrics: %v", err)
		}
	}()

	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
