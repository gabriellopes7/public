using System;
using System.ComponentModel;
using System.Diagnostics;
using System.Drawing;
using System.Reflection;
using System.Windows.Forms;

namespace Pratica5 {
    public partial class FormOrdenacao : Form {
        int[] vet = new int[500]; // vetor interno para a animação
        int esq, dir;

        public FormOrdenacao() {
            InitializeComponent();
            panel.Paint += new PaintEventHandler(panel_Paint);
            typeof(Panel).InvokeMember("DoubleBuffered", BindingFlags.SetProperty | BindingFlags.Instance | BindingFlags.NonPublic, null, panel, new object[] { true });
        }

        private void panel_Paint(object sender, PaintEventArgs e) {
            for (int i = 0; i < vet.Length; i++) {
                e.Graphics.DrawLine(Pens.BlueViolet, i, 299, i, 299 - vet[i]);
            }
        }

        private void bolhaToolStripMenuItem_Click(object sender, EventArgs e) {
            iniciaAnimacao(() => OrdenacaoGrafica.Bolha(vet, panel));
            

        }

        // TODO: animação e estatísticas dos demais métodos de ordenação

        private void sobreToolStripMenuItem_Click(object sender, EventArgs e) {
            MessageBox.Show(this, 
                "Métodos de Ordenação - 2019/2\n\nDesenvolvido por:\n71900365 - NOME DO ALUNO\nGabriel Lopes da Silva Ladeira\n\nAlgoritmos e Estruturas de Dados\nFaculdade COTEMIG\nSomente para fins didáticos.", 
                "Sobre o trabalho...", 
                MessageBoxButtons.OK, 
                MessageBoxIcon.Information);
        }

        private void iniciaAnimacao(Action a) {
            if (bgw.IsBusy != true) {
                if (radioButton1.Checked)
                {
                    Preenchimento.Crescente(vet, 299);
                    bgw.RunWorkerAsync(a);

                }
                else if (radioButton2.Checked)
                {
                    Preenchimento.Decrescente(vet, 299);
                    bgw.RunWorkerAsync(a);

                }
                else
                {
                    Preenchimento.Aleatorio(vet, 299);
                    bgw.RunWorkerAsync(a);
                }
                
            }
            else {
                MessageBox.Show(this,
                   "Aguarde o fim da execução atual...",
                   "Métodos de Ordenação - 2019/2",
                   MessageBoxButtons.OK,
                   MessageBoxIcon.Exclamation);
            }
        }

        private void bgw_DoWork(object sender, DoWorkEventArgs e)
        {
            Action a = (Action)e.Argument;
            a();
        }

        private void bgw_RunWorkerCompleted(object sender, RunWorkerCompletedEventArgs e) {
            MessageBox.Show(this,
               "Animação concluída!",
               "Métodos de Ordenação - 2019/2",
               MessageBoxButtons.OK,
               MessageBoxIcon.Information);
        }

        

        private void mergeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            int i, j;
            i = 0;
            j = vet.Length-1;
            iniciaAnimacao(() => OrdenacaoGrafica.mergeSort(vet,i,j,panel));

        }

        private void quickSortToolStripMenuItem_Click(object sender, EventArgs e)
        {
            esq = 0;
            dir = vet.Length-1;
            iniciaAnimacao(() => OrdenacaoGrafica.quickSort(vet, esq, dir,panel));

        }

        private void heapSortToolStripMenuItem_Click(object sender, EventArgs e)
        {
            iniciaAnimacao(() => OrdenacaoGrafica.heapSort(vet, panel));

        }

        private void shellSortToolStripMenuItem_Click(object sender, EventArgs e)
        {
            iniciaAnimacao(() => OrdenacaoGrafica.shellSort(vet, panel));

        }

        private void insercaoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            iniciaAnimacao(() => OrdenacaoGrafica.insercao(vet, panel));
        }

        private void selecaoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            iniciaAnimacao(() => OrdenacaoGrafica.selecao(vet, panel));

        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {

        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {

        }

        //METODOS ESTATISTICOS
        #region Bolha
        private void bolhaToolStripMenuItem1_Click_1(object sender, EventArgs e)
        {
            string preenchimento = "";
            int tamanho = Convert.ToInt32(comboBox1.SelectedItem);
            vet = new int[tamanho];
            if (radioButton1.Checked)
            {
                Preenchimento.Crescente(vet, tamanho);
                preenchimento = "Crescente";


            }
            else if (radioButton2.Checked)
            {
                Preenchimento.Decrescente(vet, tamanho);
                preenchimento = "Decrescente";
            }
            else if (radioButton3.Checked)
            {
                Preenchimento.Aleatorio(vet, tamanho);
                preenchimento = "Aleatório";
            }


            var stopwatch = new Stopwatch();
            stopwatch.Start(); // inicia cronômetro
            OrdenacaoEstatistica.Bolha(vet);
            stopwatch.Stop(); // interrompe cronômetro
            long elapsed_time = stopwatch.ElapsedMilliseconds; // calcula o tempo decorrido
            MessageBox.Show(this,
                  "Tamanho do vetor: " + tamanho +
                  "\nOrdenação inicial: " + preenchimento +
                  "\n\nTempo de execução: " + String.Format("{0:F4} seg", elapsed_time / 1000.0) +
                  "\nNº de comparações: " + OrdenacaoEstatistica.cont_c +
                  "\nNº de trocas: " + OrdenacaoEstatistica.cont_t,
                  "Estatísticas do Método Bolha",
                  MessageBoxButtons.OK,
                  MessageBoxIcon.Information);
            OrdenacaoEstatistica.cont_c = 0; //ao final do método eu zero os contadores
            OrdenacaoEstatistica.cont_t = 0;
        }
        #endregion

        #region Seleção
        private void seleçãoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            string preenchimento = "";
            int tamanho = Convert.ToInt32(comboBox1.SelectedItem);
            vet = new int[tamanho];
            if (comboBox1.SelectedIndex == 0)
            {
                vet = new int[1000];
                Preenchimento.Aleatorio(vet, 1000);
            }
            else if (comboBox1.SelectedIndex == 1)
            {
                vet = new int[10000];
                Preenchimento.Aleatorio(vet, 10000);
            }
            else if (comboBox1.SelectedIndex == 2)
            {
                vet = new int[50000];
                Preenchimento.Aleatorio(vet, 50000);
            }
            else if (comboBox1.SelectedIndex == 3)
            {
                vet = new int[100000];
                Preenchimento.Aleatorio(vet, 100000);
            }
            else if (comboBox1.SelectedIndex == 4)
            {
                vet = new int[500000];
                Preenchimento.Aleatorio(vet, 500000);
            }
            var stopwatch = new Stopwatch();
            stopwatch.Start(); // inicia cronômetro
            iniciaAnimacao(() => OrdenacaoEstatistica.selecao(vet));
            stopwatch.Stop(); // interrompe cronômetro
            long elapsed_time = stopwatch.ElapsedMilliseconds; // calcula o tempo decorrido
            MessageBox.Show(this,
                  "Tamanho do vetor: " + tamanho +
                  "\nOrdenação inicial: " + preenchimento + 
                  "\n\nTempo de execução: " + String.Format("{0:F4} seg", elapsed_time / 1000.0) +
                  "\nNº de comparações: " + OrdenacaoEstatistica.cont_c +
                  "\nNº de trocas: " + OrdenacaoEstatistica.cont_t,
                  "Estatísticas do Método Seleção",
                  MessageBoxButtons.OK,
                  MessageBoxIcon.Information);
            OrdenacaoEstatistica.cont_c = 0;
            OrdenacaoEstatistica.cont_t = 0;
        }
        #endregion

        #region Inserção
        private void inserçãoToolStripMenuItem_Click(object sender, EventArgs e)
        {
            string preenchimento = "";
            int tamanho = Convert.ToInt32(comboBox1.SelectedItem);
            vet = new int[tamanho];
            if (comboBox1.SelectedIndex == 0)
            {
                vet = new int[1000];
                Preenchimento.Aleatorio(vet, 1000);
            }
            else if (comboBox1.SelectedIndex == 1)
            {
                vet = new int[10000];
                Preenchimento.Aleatorio(vet, 10000);
            }
            else if (comboBox1.SelectedIndex == 2)
            {
                vet = new int[50000];
                Preenchimento.Aleatorio(vet, 50000);
            }
            else if (comboBox1.SelectedIndex == 3)
            {
                vet = new int[100000];
                Preenchimento.Aleatorio(vet, 100000);
            }
            else if (comboBox1.SelectedIndex == 4)
            {
                vet = new int[500000];
                Preenchimento.Aleatorio(vet, 500000);
            }
            var stopwatch = new Stopwatch();
            stopwatch.Start(); // inicia cronômetro
            iniciaAnimacao(() => OrdenacaoEstatistica.insercao(vet));
            stopwatch.Stop(); // interrompe cronômetro
            long elapsed_time = stopwatch.ElapsedMilliseconds; // calcula o tempo decorrido
            MessageBox.Show(this,
                  "Tamanho do vetor: " + tamanho +
                  "\nOrdenação inicial: " + preenchimento +
                  "\n\nTempo de execução: " + String.Format("{0:F4} seg", elapsed_time / 1000.0) +
                  "\nNº de comparações: " + OrdenacaoEstatistica.cont_c +
                  "\nNº de trocas: " + OrdenacaoEstatistica.cont_t,
                  "Estatísticas do Método Inserção",
                  MessageBoxButtons.OK,
                  MessageBoxIcon.Information);
            OrdenacaoEstatistica.cont_c = 0;
            OrdenacaoEstatistica.cont_t = 0;
        }
        #endregion

        #region ShellSort

        private void shellsortToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            string preenchimento = "";
            int tamanho = Convert.ToInt32(comboBox1.SelectedItem);
            vet = new int[tamanho];
            if (comboBox1.SelectedIndex == 0)
            {
                vet = new int[1000];
                Preenchimento.Aleatorio(vet, 1000);
            }
            else if (comboBox1.SelectedIndex == 1)
            {
                vet = new int[10000];
                Preenchimento.Aleatorio(vet, 10000);
            }
            else if (comboBox1.SelectedIndex == 2)
            {
                vet = new int[50000];
                Preenchimento.Aleatorio(vet, 50000);
            }
            else if (comboBox1.SelectedIndex == 3)
            {
                vet = new int[100000];
                Preenchimento.Aleatorio(vet, 100000);
            }
            else if (comboBox1.SelectedIndex == 4)
            {
                vet = new int[500000];
                Preenchimento.Aleatorio(vet, 500000);
            }
            var stopwatch = new Stopwatch();
            stopwatch.Start(); // inicia cronômetro
            iniciaAnimacao(() => OrdenacaoEstatistica.shellSort(vet));
            stopwatch.Stop(); // interrompe cronômetro
            long elapsed_time = stopwatch.ElapsedMilliseconds; // calcula o tempo decorrido
            MessageBox.Show(this,
                  "Tamanho do vetor: " + tamanho +
                  "\nOrdenação inicial: " + preenchimento +
                  "\n\nTempo de execução: " + String.Format("{0:F4} seg", elapsed_time / 1000.0) +
                  "\nNº de comparações: " + OrdenacaoEstatistica.cont_c +
                  "\nNº de trocas: " + OrdenacaoEstatistica.cont_t,
                  "Estatísticas do Método ShellSort",
                  MessageBoxButtons.OK,
                  MessageBoxIcon.Information);
            OrdenacaoEstatistica.cont_c = 0;
            OrdenacaoEstatistica.cont_t = 0;
        }
        #endregion

        #region HeapSort
        private void heapsortToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            string preenchimento = "";
            int tamanho = Convert.ToInt32(comboBox1.SelectedItem);
            vet = new int[tamanho];
            if (comboBox1.SelectedIndex == 0)
            {
                vet = new int[1000];
                Preenchimento.Aleatorio(vet, 1000);
            }
            else if (comboBox1.SelectedIndex == 1)
            {
                vet = new int[10000];
                Preenchimento.Aleatorio(vet, 10000);
            }
            else if (comboBox1.SelectedIndex == 2)
            {
                vet = new int[50000];
                Preenchimento.Aleatorio(vet, 50000);
            }
            else if (comboBox1.SelectedIndex == 3)
            {
                vet = new int[100000];
                Preenchimento.Aleatorio(vet, 100000);
            }
            else if (comboBox1.SelectedIndex == 4)
            {
                vet = new int[500000];
                Preenchimento.Aleatorio(vet, 500000);
            }
            var stopwatch = new Stopwatch();
            stopwatch.Start(); // inicia cronômetro
            iniciaAnimacao(() => OrdenacaoEstatistica.heapSort(vet));
            stopwatch.Stop(); // interrompe cronômetro
            long elapsed_time = stopwatch.ElapsedMilliseconds; // calcula o tempo decorrido
            MessageBox.Show(this,
                  "Tamanho do vetor: " + tamanho +
                  "\nOrdenação inicial: " + preenchimento +
                  "\n\nTempo de execução: " + String.Format("{0:F4} seg", elapsed_time / 1000.0) +
                  "\nNº de comparações: " + OrdenacaoEstatistica.cont_c +
                  "\nNº de trocas: " + OrdenacaoEstatistica.cont_t,
                  "Estatísticas do Método HeapSort",
                  MessageBoxButtons.OK,
                  MessageBoxIcon.Information);
            OrdenacaoEstatistica.cont_c = 0;
            OrdenacaoEstatistica.cont_t = 0;
        }
        #endregion

        #region QuickSort
        private void quicksortToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            string preenchimento = "";
            int tamanho = Convert.ToInt32(comboBox1.SelectedItem);
            vet = new int[tamanho];
            if (comboBox1.SelectedIndex == 0)
            {
                vet = new int[1000];
                Preenchimento.Aleatorio(vet, 1000);
            }
            else if (comboBox1.SelectedIndex == 1)
            {
                vet = new int[10000];
                Preenchimento.Aleatorio(vet, 10000);
            }
            else if (comboBox1.SelectedIndex == 2)
            {
                vet = new int[50000];
                Preenchimento.Aleatorio(vet, 50000);
            }
            else if (comboBox1.SelectedIndex == 3)
            {
                vet = new int[100000];
                Preenchimento.Aleatorio(vet, 100000);
            }
            else if (comboBox1.SelectedIndex == 4)
            {
                vet = new int[500000];
                Preenchimento.Aleatorio(vet, 500000);
            }
            var stopwatch = new Stopwatch();
            stopwatch.Start(); // inicia cronômetro

            esq = 0;
            dir = vet.Length - 1;
            iniciaAnimacao(() => OrdenacaoEstatistica.quickSort(vet, esq, dir));

            stopwatch.Stop(); // interrompe cronômetro
            long elapsed_time = stopwatch.ElapsedMilliseconds; // calcula o tempo decorrido
            MessageBox.Show(this,
                  "Tamanho do vetor: " + tamanho +
                  "\nOrdenação inicial: " + preenchimento +
                  "\n\nTempo de execução: " + String.Format("{0:F4} seg", elapsed_time / 1000.0) +
                  "\nNº de comparações: " + OrdenacaoEstatistica.cont_c +
                  "\nNº de trocas: " + OrdenacaoEstatistica.cont_t,
                  "Estatísticas do Método QuickSort",
                  MessageBoxButtons.OK,
                  MessageBoxIcon.Information);
            OrdenacaoEstatistica.cont_c = 0;
            OrdenacaoEstatistica.cont_t = 0;

        }
        #endregion

        #region MergeSort
        private void mergesortToolStripMenuItem_Click(object sender, EventArgs e)
        {
            string preenchimento = "";
            int tamanho = Convert.ToInt32(comboBox1.SelectedItem);
            vet = new int[tamanho];
            if (comboBox1.SelectedIndex == 0)
            {
                vet = new int[1000];
                Preenchimento.Aleatorio(vet, 1000);
            }
            else if (comboBox1.SelectedIndex == 1)
            {
                vet = new int[10000];
                Preenchimento.Aleatorio(vet, 10000);
            }
            else if (comboBox1.SelectedIndex == 2)
            {
                vet = new int[50000];
                Preenchimento.Aleatorio(vet, 50000);
            }
            else if (comboBox1.SelectedIndex == 3)
            {
                vet = new int[100000];
                Preenchimento.Aleatorio(vet, 100000);
            }
            else if (comboBox1.SelectedIndex == 4)
            {
                vet = new int[500000];
                Preenchimento.Aleatorio(vet, 500000);
            }
            var stopwatch = new Stopwatch();
            stopwatch.Start(); // inicia cronômetro

            int i, j;
            i = 0;
            j = vet.Length - 1;
            iniciaAnimacao(() => OrdenacaoEstatistica.mergeSort(vet, i, j));

            stopwatch.Stop(); // interrompe cronômetro
            long elapsed_time = stopwatch.ElapsedMilliseconds; // calcula o tempo decorrido
            MessageBox.Show(this,
                  "Tamanho do vetor: " + tamanho +
                  "\nOrdenação inicial: " + preenchimento +
                  "\n\nTempo de execução: " + String.Format("{0:F4} seg", elapsed_time / 1000.0) +
                  "\nNº de comparações: " + OrdenacaoEstatistica.cont_c +
                  "\nNº de trocas: " + OrdenacaoEstatistica.cont_t,
                  "Estatísticas do Método MergeSort",
                  MessageBoxButtons.OK,
                  MessageBoxIcon.Information);
            OrdenacaoEstatistica.cont_c = 0;
            OrdenacaoEstatistica.cont_t = 0;

        }
        #endregion
        private void comboBox1_SelectedIndexChanged_1(object sender, EventArgs e)
        {

        }

        private void FormOrdenacao_Load(object sender, EventArgs e)
        {

        }
    }
       

        
    
}
