// works
funcs = []
for (let i=0; i<10; i++) { funcs.push(function() { console.log(i); }) }

for (index in funcs) { funcs[index](); }

// works
funcs = []
for (var i=0; i<10; i++) { let j = i; funcs.push(function() { console.log(j); }) }

for (index in funcs) { funcs[index](); }

// works
funcs = []
for (var i=0; i<10; i++) { 
    funcs.push((function(x) { return function() { console.log(x); }; })(i)) 
}

for (index in funcs) { funcs[index](); }