package main

import "fmt"

func main(){
	n:=3
	result:=0
	for i:=0;i<4;i++{
		result=(result<<1)|(n&1)
		n>>=1
	}
	fmt.Println(result)
}
