
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pratica6
{
    class Arvore
    {
        public NoArvore A = null;

        public void inserir(string chave, string[] aluno)
        {
            if (A == null)
            {
                A = new NoArvore(chave, aluno);
            }
            else
            {
                A.inserir(chave, aluno);
            }
        }

        public void emOrdem(NoArvore x)
        {
            if (x != null)
            {
                emOrdem(x.esq);
                Console.Write(x.chave + " ");
                Console.WriteLine();
                emOrdem(x.dir);
            }
        }

        public void preOrdem(NoArvore x)
        {
            if (x != null)
            {
                Console.Write(x.chave + " ");
                Console.WriteLine();
                preOrdem(x.esq);
                preOrdem(x.dir);
            }
        }

        public void posOrdem(NoArvore x)
        {
            if (x != null)
            {
                posOrdem(x.esq);
                posOrdem(x.dir);
                Console.Write(x.chave + " ");
                Console.WriteLine();
            }
        }

        public NoArvore pesquisar(string c, NoArvore d)
        {
            if (d == null || d.chave == c)
                return d;
            else if (string.Compare(c, d.chave) == -1)
                return pesquisar(c, d.esq);
            else
                return pesquisar(c, d.dir);
        }
    }

    public class NoArvore
    {
        public string chave;
        public List<string[]> listaAluno = new List<string[]>();
        public NoArvore esq, dir;

        public NoArvore(string c, string[] aluno)
        {
            chave = c;
            esq = dir = null;
            listaAluno.Add(aluno);
        }

        public void inserir(string c, string[] aluno)
        {
            if (string.Compare(c, chave) == -1)
            {
                if (esq == null)
                    esq = new NoArvore(c, aluno);
                else
                    esq.inserir(c, aluno);
            }
            else if (string.Compare(c, chave) == 1)
            {
                if (dir == null)
                    dir = new NoArvore(c, aluno);
                else
                    dir.inserir(c, aluno);
            }
            else
            {
                if(!listaAluno.Contains(aluno))
                    listaAluno.Add(aluno);
                //else
                //Console.Write("Chave duplicada. Impossível inserir!");
            }
        }
    }
}
