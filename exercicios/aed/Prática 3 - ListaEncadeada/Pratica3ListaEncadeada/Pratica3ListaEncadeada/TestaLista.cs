using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace TiposAbstratosDeDados
{    
    class TestaLista
    {
        static void Main(string[] args)
        {
            Menu();



            Console.ReadKey();
        }
        static ConsoleKeyInfo opcao;
        static Lista l = new Lista();
        static int c;
        static string nome;
        static void Menu()
        {
            do
            {
                Console.WriteLine("TESTA LISTA:");
                Console.WriteLine("------------------------------");
                Console.WriteLine(" |  F 1  | Inserir");
                Console.WriteLine(" |  F 2  | Pesquisar");
                Console.WriteLine(" |  F 3  | Imprimir");
                Console.WriteLine(" |  ESC  | Sair");
                Console.WriteLine("------------------------------");
                Console.Write("Digite uma opcao: ");                
                opcao = Console.ReadKey();
                Console.WriteLine();
                switch (opcao.Key)
                {
                    case (ConsoleKey.F1):
                        Console.Clear();
                        Inserir();
                        break;
                    case (ConsoleKey.F2):
                        Console.Clear();
                        Pesquisar();
                        break;
                    case (ConsoleKey.F3):
                        Console.Clear();
                        Imprimir();
                        break;
                    case (ConsoleKey.Escape):
                        Console.WriteLine("PROGRAMA ENCERRADO COM SUCESSO");
                        
                        break;
                    default:
                        Console.WriteLine("OPCAO INVALIDA, TENTE NOVAMENTE");
                        Console.ReadKey();
                        Console.Clear();
                        Menu();
                        break;
                }

      


            } while (opcao.Key != ConsoleKey.F1 && opcao.Key != ConsoleKey.F2 && opcao.Key != ConsoleKey.F3 && opcao.Key != ConsoleKey.Escape);
            
        }
        static void Inserir()
        {
            Console.Clear();
            Console.Write("Digite um nº (-1 para sair): ");            
            c = Convert.ToInt32(Console.ReadLine());
                       
            while (c != -1)
            {            
                if (l.pesquisar(c)== null)
                {
                    Console.Write("Digite um nome: ");
                    nome = Console.ReadLine();
                    l.inserir(new NoLista(c,nome));
                    Inserir();
                    
                }
                else
                {
                    Console.WriteLine("O Número digitado já existe na lista, tente novamente");
                    Console.ReadKey();
                    Inserir();

                }
                
            }
            Console.WriteLine("Retornando ao Menu");
            Thread.Sleep(2000);
            Console.Clear();
            Menu();
        }
        static void Pesquisar()
        {
            Console.Write("Digite um nº a ser pesquisado: ");
            c = Convert.ToInt32(Console.ReadLine());

            NoLista n = l.pesquisar(c);
            if (n == null)
                Console.WriteLine("Valor não encontrado!");
            else
            {
                Console.WriteLine("Achou: " + n.chave);
                Console.WriteLine("Nome: " + n.nome);
                Console.WriteLine("Deseja remover o nó ? ");
                Console.WriteLine("F1 - SIM");
                Console.WriteLine("F2 - NAO");
                ConsoleKeyInfo opcao = Console.ReadKey();
                if(opcao.Key == ConsoleKey.F1)
                {
                    l.remover(c);
                    n.nome = null;
                }

            }
                
            Console.WriteLine("Retornando ao Menu");
            Thread.Sleep(2000);
            Console.Clear();
            Menu();
        }
        static void Imprimir()
        {
            Console.WriteLine("Lista impressa: ");
            l.imprimir();
            Console.WriteLine("Presssione qualquer tecla para retornar");
            Console.ReadKey();
            Console.Clear();
            Menu();
        }
       
    }
}