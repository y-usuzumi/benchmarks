package main

import (
	"bytes"
	"fmt"
	"github.com/golang/snappy"
	"io/ioutil"
	"os"
	"strconv"
	"time"
)

func decompress(data []byte, iterations int) {
	buf := make([]byte, len(data)*10)
	for i := 0; i < iterations; i++ {
		reader := snappy.NewReader(bytes.NewReader(data))

		_, e := reader.Read(buf)
		if e != nil {
			fmt.Println(e)
			os.Exit(1)
		}
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
