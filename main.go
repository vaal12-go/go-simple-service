package main

import (
	"fmt"
	"os"
	"os/signal"
	"syscall"
	"time"
)

func main() {
	fmt.Println("Simple service starting.")

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
