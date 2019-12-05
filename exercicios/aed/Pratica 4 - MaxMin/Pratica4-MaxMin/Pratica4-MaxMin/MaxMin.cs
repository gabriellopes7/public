using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pratica4_MaxMin
{
    class MaxMin
    {

        // Operação relevante: TESTES (if)
        // T(n) = 2n - 2
        public void maxMin1(int[] vet)
        {
            int ma, me, cont = 0;
            int i;
            ma = me = vet[0];
            for (i = 1; i < vet.Length; i++)
            {

                if (vet[i] < me)
                {
                    
                    me = vet[i];                    
                }
                cont++;
                if (vet[i] > ma)
                {
                    
                    ma = vet[i];
                    
                }
                cont++;

            }
            Console.WriteLine("Maximo minimo 1: " + cont);
        }

        // Melhor caso: T(n) = n - 1
        // Pior caso: T(n) = 2n - 2
        // Caso médio: T(n) = 3n/2 - 3/2
        public void maxMin2(int[] vet)
        {
            int ma, me, cont = 0;
            int i;
            ma = me = vet[0];
            for (i = 1; i < vet.Length; i++)
            {
                if (vet[i] < me)
                {
                    me = vet[i];

                    
                }                   
                else
                {    
                    if (vet[i] > ma)
                    {
                        ma = vet[i];
                        
                    }
                    cont++;
                }
                cont++;


            }
            Console.WriteLine("Maximo minimo 2: " + cont);
        }

        // T(n) = 3n/2 - 2
        public void maxMin3(int[] vet)
        {
            int ma, me;
            int i;
            int cont = 0;
            if (vet[0] < vet[1])
            {
                me = vet[0];
                ma = vet[1];
                
            }
            else
            {
                me = vet[1];
                ma = vet[0];
                

            }
            cont++;

            for (i = 2; i < vet.Length; i += 2)
            {
                if (vet[i] < vet[i + 1])
                {
                    if (vet[i] < me)
                    {
                        me = vet[i];
                        
                    }
                    cont++;
                    if (vet[i + 1] > ma)
                    {
                        ma = vet[i + 1];
                        
                    }
                    cont++;

                }
                else
                {
                    if (vet[i + 1] < me)
                    {
                        me = vet[i + 1];
                        
                    }
                    cont++;

                    if (vet[i] > ma)
                    {
                        ma = vet[i];
                        

                    }

                    cont++;

                }

                cont++;
            }
            Console.WriteLine("Maximo minimo 3: " + cont);
        }
    }
}
