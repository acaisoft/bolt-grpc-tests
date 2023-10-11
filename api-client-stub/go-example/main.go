package main

import (
	"context"
	"flag"
	"fmt"
	"log"
	"net"

  "sync/atomic"
	"google.golang.org/grpc"
	pb "example/service"
)

var (
	port = flag.Int("port", 50051, "The server port")
	counterResetMsg = string("Counter reset to 0.")
	ops atomic.Int64
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
	lis, err := net.Listen("tcp", fmt.Sprintf(":%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterApiServer(s, &server{})
	log.Printf("server listening at %v", lis.Addr())
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}