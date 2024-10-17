package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
	"time"
)

const (
	VERSION_STR = "v1.0_17Oct2024"
)

func main() {
	fmt.Printf("Simple service starting. Version:%s", VERSION_STR)

	//https://stackoverflow.com/questions/11268943/is-it-possible-to-capture-a-ctrlc-signal-sigint-and-run-a-cleanup-function-i
	signalChan := make(chan os.Signal, 1)
	signal.Notify(signalChan, os.Interrupt)
	//https://stackoverflow.com/questions/42978358/how-does-the-systemd-stop-command-actually-work
	signal.Notify(signalChan, syscall.SIGTERM)

	var signalReceived os.Signal
signalWaitingLoop:
	for {
		select {
		case signalReceived = <-signalChan:
			fmt.Printf("signalReceived: %v\n", signalReceived)
			if signalReceived.String() == "interrupt" {
				fmt.Printf("Ctrl-C received - exiting\n")
			}
			if signalReceived.String() == "terminated" {
				fmt.Printf("'terminated' signal received. Will shutdown.\n")
			}
			break signalWaitingLoop
		case <-time.After(time.Second * 5):
			fmt.Printf("5 second keepalive.\n")
		} //select {
	} //signalWaitingLoop: for {
	fmt.Println("Simple service finished.")
}

//c46c48ddaccc53835237b551df240c1dc51ca78911fdec845481c04bb2bb438b71ed15431131850dd2654a136047dbe3129c728d4148f971d3bc0d7568124a86
