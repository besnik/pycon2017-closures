using System;
using System.Collections.Generic;
using System.Linq;

namespace ConsoleApplication11
{
    public class Program
    {
        public static void _Main(string[] args)
        {
            // works
            Console.WriteLine("Version 1");
            var funcs = new List<Action>();

            for (var i=0; i<10; i++) {
                var j = i;
                funcs.Add(() => { Console.WriteLine(j); });
            }

            foreach (var f in funcs) f();

            // works
            Console.WriteLine("Version 2");
            funcs = new List<Action>();

            for (var i=0; i<10; i++) {
                Action<int> add = (x) => {
                    funcs.Add(() => { Console.WriteLine(x); });
                };
                add(i);
            }

            foreach (var f in funcs) f();

            // works
            Console.WriteLine("Version 3");
            funcs = new List<Action>();

            foreach(var i in Enumerable.Range(0,10)) {
                funcs.Add(() => { Console.WriteLine(i); });
            }

            foreach (var f in funcs) f();
        }
    }
}
