// this code has one problem...

funcs = []
for (var i=0; i<10; i++) { 
    funcs.push(function() { console.log(i); }) 
}

for (index in funcs) { funcs[index](); }