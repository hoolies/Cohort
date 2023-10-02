package main

import (
    "fmt"
    "time"
)

func main() {
    fmt.Println("Enter your name")

    var uname string

    fmt.Scanln(&uname)

    weekday := time.Now().Weekday()

    fmt.Printf("Hello %v! Happy, %v", uname, weekday)
}
