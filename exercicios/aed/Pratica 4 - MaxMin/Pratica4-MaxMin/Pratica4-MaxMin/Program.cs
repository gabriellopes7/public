using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pratica4_MaxMin
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] crescente = new int[1000];
            int[] decrescente = new int[1000];
            int[] aleatorio = new int[1000];
            
 
            Random c = new Random();
            for(int i=0; i < crescente.Length; i++)
            {
                crescente[i] = i+1;
                decrescente[i] = crescente.Length - i;
                aleatorio[i] = c.Next(0, 500);
               
            }
            MaxMin cresce = new MaxMin();
            MaxMin decresce = new MaxMin();
            MaxMin aleato = new MaxMin();

            cresce.maxMin1(crescente);
            cresce.maxMin2(crescente);
            cresce.maxMin3(crescente);
            Console.WriteLine();
            decresce.maxMin1(decrescente);
            decresce.maxMin2(decrescente);
            decresce.maxMin3(decrescente);
            Console.WriteLine();
            aleato.maxMin1(aleatorio);
            aleato.maxMin2(aleatorio);
            aleato.maxMin3(aleatorio);



            Console.ReadKey();
            
        }
    }
}
