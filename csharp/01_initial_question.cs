using System;
using System.Collections.Generic;

namespace ConsoleApplication01
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // this code has one problem...
            var funcs = new List<Action>();

            for (var i=0; i<10; i++) {
                funcs.Add(() => { Console.WriteLine(i); });
            }

            foreach (var f in funcs) f();
        }
    }
}
