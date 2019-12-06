using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Pratica6
{

    class Program
    {
        static Arvore arvore = new Arvore();
        static string Arquivo = "";

        [STAThread]
        static void Main(string[] args)
        {
            string line;
            OpenFileDialog theDialog = new OpenFileDialog();
            theDialog.Title = "Abrir arquivo de texto";
            theDialog.Filter = "TXT files|*.txt";
            theDialog.InitialDirectory = @"h:\";
            if (theDialog.ShowDialog() == DialogResult.OK)
            {
                System.IO.StreamReader file = new System.IO.StreamReader(theDialog.FileName);
                Arquivo = new System.IO.FileInfo(theDialog.FileName).Name;

                while ((line = file.ReadLine()) != null)
                {
                    string[] s = line.Split(';');

                    foreach (var materia in s.Select((x,i) => new {Value = x, Index = i }))
                    {
                        if(materia.Index > 1)
                        {
                            arvore.inserir(s[materia.Index], s);
                        }
                    }
                }

                Menu();

                file.Close();
            }

            Console.ReadLine();
        }



        static void OpcoesMenu()
        {
            Console.Clear();
            Console.WriteLine("F1  -  Informar arquivo");
            Console.WriteLine("F2  -  Imprimir disciplinas em ordem crescente");
            Console.WriteLine("F3  -  Imprimir disciplinas em pré-ordem");
            Console.WriteLine("F4  -  Imprimir disciplinas em pós - ordem");
            Console.WriteLine("F5  -  Listar Turma");
            Console.WriteLine("ESC -  Sair");
        }

        static void Menu()
        {
            OpcoesMenu();

            ConsoleKeyInfo opcao;
            opcao = Console.ReadKey();
            do
            {


                switch (opcao.Key)
                {
                    case ConsoleKey.F1:
                        {
                            Console.Clear();
                            Console.WriteLine(Arquivo);
                            Console.ReadKey();
                            OpcoesMenu();
                            Menu();
                        }
                        break;
                    case ConsoleKey.F2:
                        {
                            Console.Clear();
                            arvore.emOrdem(arvore.A);
                            Console.ReadKey();
                            OpcoesMenu();
                            Menu();
                        }
                        break;
                    case ConsoleKey.F3:
                        {
                            Console.Clear();
                            arvore.preOrdem(arvore.A);
                            Console.ReadKey();
                            OpcoesMenu();
                            Menu();
                        }
                        break;
                    case ConsoleKey.F4:
                        {
                            Console.Clear();
                            arvore.posOrdem(arvore.A);
                            Console.ReadKey();
                            OpcoesMenu();
                            Menu();
                        }
                        break;
                    case ConsoleKey.F5:
                        {
                            Console.Clear();

                            Console.Write("Informe o nome da disciplina: ");
                            string materia = Console.ReadLine();

                            Console.WriteLine();
                            Console.WriteLine("ALUNOS MATRICULADOS:");
                            NoArvore result = arvore.pesquisar(materia.ToUpper(), arvore.A);

                            foreach (var s in result.listaAluno)
                            {
                                Console.WriteLine($"{s[0]} - {s[1]}");
                            }
                            Console.ReadKey();
                            OpcoesMenu();
                            Menu();
                        }
                        break;
                    case ConsoleKey.Escape:
                        {
                            Environment.Exit(0);
                        }
                        break;
                }
            } while (opcao.Key != ConsoleKey.F1 && opcao.Key != ConsoleKey.F2 && opcao.Key != ConsoleKey.F3 && opcao.Key != ConsoleKey.F4 && opcao.Key != ConsoleKey.F5 && opcao.Key != ConsoleKey.Escape);
        }


    }
}
