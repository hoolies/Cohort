package main

import "fmt"

// Main Fuction
func main(){    
    fmt.Println("Please enter an IPv4 IP address:")
    // Declaring the variable name and type
    var ipv4 string
    // Taking input from use
    fmt.Scanln(&ipv4)
    // Dispaly the input back to the user
    fmt.Println("You told me the IOPv4 address is: " + ipv4)
}
