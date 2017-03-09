// by default javascript / node.js makes scope of caller available to the function

var name = "gordon"
console.log("global var: " + name)

function test() {
    name = 5 // use let to define local var
    console.log("inside func: " + name)
}

test()
console.log("global var: " + name)