package main

import "fmt"

import "rsc.io/quote"

// var c, python, java bool

var i, j int = 1, 2 // with initialisers

// func smth() {
// 	x, y := 1, -2
// 	if x > 0{
// 		return y
// 	}
// }

func main() {
	// var i, j int
	// var c, python, java = true, false, "no!"
	k := 3
	c, python, java := true, false, "no!" // Cannot do outside func can be used instead of var in functions
    fmt.Println(quote.Go())
	fmt.Println(i, j, c, k, python, java)
	// smth()
}