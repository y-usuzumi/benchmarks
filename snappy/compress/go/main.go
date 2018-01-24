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

func compress(data []byte, iterations int) {
	buf := make([]byte, len(data)*2)
	for i := 0; i < iterations; i++ {
		writer := snappy.NewWriter(bytes.NewBuffer(buf))
		_, e := writer.Write(data)
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
	concatRepetitions, _ := strconv.Atoi(args[2])
	iterations, _ := strconv.Atoi(args[3])
	fbytes, _ := ioutil.ReadFile(f)
	data := bytes.Repeat(fbytes, concatRepetitions)
	start := now()
	fmt.Printf("%.6f\n", start)
	compress(data, iterations)
	end := now()
	fmt.Printf("%.6f\n", end)
}
