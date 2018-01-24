package main

import (
	"fmt"
	"github.com/golang/snappy"
	"io/ioutil"
	"os"
	"strconv"
	"time"
)

func decompress(data []byte, iterations int) {
	for i := 0; i < iterations; i++ {
		snappy.Decode(nil, data)
	}
}

func now() float64 {
	now := time.Now()
	now_secs := now.Unix()
	now_nanos := now.UnixNano()
	return float64(now_secs) + float64(now_nanos)*1e-9
}

func main() {
	args := os.Args
	f := args[1]
	iterations, _ := strconv.Atoi(args[2])
	data, _ := ioutil.ReadFile(f)
	start := now()
	fmt.Printf("%.6f\n", start)
	decompress(data, iterations)
	end := now()
	fmt.Printf("%.6f\n", end)
}
