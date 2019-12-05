using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pratica2Restaurante
{
    
    class Program
    {
        Fila f = new Fila(100);
        Fila p = new Fila(100);
        Fila e = new Fila(100);

        static int count = 1;

        
        static void Main(string[] args)
        {
            //1 - Insercao de cliente na fila de pedidos
            //2 - Remocao de cliente na fila de pedidos
            //3 - Remocao de cliente na fila de pagametnos
            //4 - Remocao de cliente na fila de encomendas
            //5 - Sair
            Program m = new Program();
            m.Menu();


            Console.ReadKey();
        }

        public void Menu()
        {
            ConsoleKeyInfo opcao;
            do
            {
                Console.WriteLine("-------------------------------------------");
                Console.WriteLine("            R E S T A U R A N T E          ");
                Console.WriteLine("-------------------------------------------");
                Console.WriteLine("| F1  | Inserir cliente na fila de pedidos");
                Console.WriteLine("| F2  | Remover cliente da fila de pedidos");
                Console.WriteLine("| F3  | Remover cliente fila de pagamentos");
                Console.WriteLine("| F4  | Remover cliente fila de encomendas");
                Console.WriteLine("| ESC | SAIR");
                Console.Write("Digite uma opcao: ");
                opcao = Console.ReadKey();
                Console.WriteLine();
                switch (opcao.Key)
                {
                    case ConsoleKey.F1:
                        f.enfileirar(count);                         
                        Console.WriteLine("Cliente {0} inserido na fila de pedidos", count);
                        count++;
                        Console.ReadKey();
                        Console.Clear();
                        Menu();
                        break;
                    case ConsoleKey.F2:
                        if (f.vazia())
                        {
                            Console.WriteLine("Nao ha clientes na fila de pedidos");
                        }
                        else
                        {
                            int c = f.desenfileirar();
                            p.enfileirar(c);
                            Console.WriteLine("Cliente {0} inserido na fila de pagamentos", c);
                        }
                        Console.ReadKey();
                        Console.Clear();
                        Menu();
                        break;
                    case ConsoleKey.F3:
                        if (p.vazia())
                        {
                            Console.WriteLine("Nao ha clientes na fila de pagamentos");

                        }
                        else
                        {
                            int c = p.desenfileirar();
                            e.enfileirar(c);
                            Console.WriteLine("Cliente {0} foi inserido na fila de encomendas", c);
                        }
                        Console.ReadKey();
                        Console.Clear();
                        Menu();
                        break;
                    case ConsoleKey.F4:
                        if (e.vazia())
                        {
                            Console.WriteLine("Nao ha clientes na fila de encomendas");

                        }
                        else
                        {
                            int c = e.desenfileirar();
                            Console.WriteLine("O cliente {0} recebeu o seu pedido e foi embora", c);
                        }
                        Console.ReadKey();
                        Console.Clear();
                        Menu();
                        break;
                    case ConsoleKey.Escape:
                        Console.WriteLine("PROGRAMA FINALIZADO ! ");
                        Console.ReadKey();
                        break;
                    default:
                        Console.WriteLine("TECLA INVALIDA, TENTE NOVAMENTE ");
                        Console.ReadKey();                     

                        Console.Clear();
                        Menu();
                        break;
                }
            } while (opcao.Key != ConsoleKey.F1 && opcao.Key != ConsoleKey.F2 && opcao.Key != ConsoleKey.F3 &&
            opcao.Key != ConsoleKey.F4 && opcao.Key != ConsoleKey.Escape);
        }
       
    }
}
