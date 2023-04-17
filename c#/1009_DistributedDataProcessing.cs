using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TestConsole2
{
    class Program
    {
        static void Main(string[] args)
        {
            string sT = Console.ReadLine();
            int T = Convert.ToInt32(sT);

            for (int i = 0; i < T; i++) {
                string[] str_input = Console.ReadLine().Split('\x020');
                int[] input = Array.ConvertAll(str_input, s => int.Parse(s));
                
                int result = input[0];
                int[] n = new int[10];
                int length = 1;
                n[0] = input[0];
                for (int j = 1; j <= 9; j++) {
                    result *= input[0];
                    result %= 10;
                    length = j;
                    if (result == input[0])
                        break;
                    n[j] = result;
                }

                int index = input[1] % length;
                if (index == 0)
                    index = length;
                index--;
                Console.WriteLine(n[index]);
            }
        }
    }
}
