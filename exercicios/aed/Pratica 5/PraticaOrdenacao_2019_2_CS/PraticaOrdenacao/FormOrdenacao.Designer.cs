namespace Pratica5
{
    partial class FormOrdenacao
    {
        /// <summary>
        /// Variável de designer necessária.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpar os recursos que estão sendo usados.
        /// </summary>
        /// <param name="disposing">verdade se for necessário descartar os recursos gerenciados; caso contrário, falso.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region código gerado pelo Windows Form Designer

        /// <summary>
        /// Método necessário para suporte do Designer - não modifique
        /// o conteúdo deste método com o editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.panel = new System.Windows.Forms.Panel();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.algoritmoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.bolhaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.mergeToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.quickSortToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.heapSortToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.shellSortToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.insercaoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.selecaoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.estatísticasToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.bolhaToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.seleçãoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.inserçãoToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.shellsortToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.heapsortToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.quicksortToolStripMenuItem1 = new System.Windows.Forms.ToolStripMenuItem();
            this.mergesortToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.ajudaToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.sobreToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.bgw = new System.ComponentModel.BackgroundWorker();
            this.radioButton1 = new System.Windows.Forms.RadioButton();
            this.radioButton2 = new System.Windows.Forms.RadioButton();
            this.radioButton3 = new System.Windows.Forms.RadioButton();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // panel
            // 
            this.panel.Location = new System.Drawing.Point(12, 56);
            this.panel.Name = "panel";
            this.panel.Size = new System.Drawing.Size(500, 300);
            this.panel.TabIndex = 0;
            this.panel.Paint += new System.Windows.Forms.PaintEventHandler(this.panel_Paint);
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.algoritmoToolStripMenuItem,
            this.estatísticasToolStripMenuItem,
            this.ajudaToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(524, 24);
            this.menuStrip1.TabIndex = 1;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // algoritmoToolStripMenuItem
            // 
            this.algoritmoToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.bolhaToolStripMenuItem,
            this.mergeToolStripMenuItem,
            this.quickSortToolStripMenuItem,
            this.heapSortToolStripMenuItem,
            this.shellSortToolStripMenuItem,
            this.insercaoToolStripMenuItem,
            this.selecaoToolStripMenuItem});
            this.algoritmoToolStripMenuItem.Name = "algoritmoToolStripMenuItem";
            this.algoritmoToolStripMenuItem.Size = new System.Drawing.Size(73, 20);
            this.algoritmoToolStripMenuItem.Text = "Algoritmo";
            // 
            // bolhaToolStripMenuItem
            // 
            this.bolhaToolStripMenuItem.Name = "bolhaToolStripMenuItem";
            this.bolhaToolStripMenuItem.Size = new System.Drawing.Size(126, 22);
            this.bolhaToolStripMenuItem.Text = "Bolha";
            this.bolhaToolStripMenuItem.Click += new System.EventHandler(this.bolhaToolStripMenuItem_Click);
            // 
            // mergeToolStripMenuItem
            // 
            this.mergeToolStripMenuItem.Name = "mergeToolStripMenuItem";
            this.mergeToolStripMenuItem.Size = new System.Drawing.Size(126, 22);
            this.mergeToolStripMenuItem.Text = "Merge";
            this.mergeToolStripMenuItem.Click += new System.EventHandler(this.mergeToolStripMenuItem_Click);
            // 
            // quickSortToolStripMenuItem
            // 
            this.quickSortToolStripMenuItem.Name = "quickSortToolStripMenuItem";
            this.quickSortToolStripMenuItem.Size = new System.Drawing.Size(126, 22);
            this.quickSortToolStripMenuItem.Text = "QuickSort";
            this.quickSortToolStripMenuItem.Click += new System.EventHandler(this.quickSortToolStripMenuItem_Click);
            // 
            // heapSortToolStripMenuItem
            // 
            this.heapSortToolStripMenuItem.Name = "heapSortToolStripMenuItem";
            this.heapSortToolStripMenuItem.Size = new System.Drawing.Size(126, 22);
            this.heapSortToolStripMenuItem.Text = "HeapSort";
            this.heapSortToolStripMenuItem.Click += new System.EventHandler(this.heapSortToolStripMenuItem_Click);
            // 
            // shellSortToolStripMenuItem
            // 
            this.shellSortToolStripMenuItem.Name = "shellSortToolStripMenuItem";
            this.shellSortToolStripMenuItem.Size = new System.Drawing.Size(126, 22);
            this.shellSortToolStripMenuItem.Text = "ShellSort";
            this.shellSortToolStripMenuItem.Click += new System.EventHandler(this.shellSortToolStripMenuItem_Click);
            // 
            // insercaoToolStripMenuItem
            // 
            this.insercaoToolStripMenuItem.Name = "insercaoToolStripMenuItem";
            this.insercaoToolStripMenuItem.Size = new System.Drawing.Size(126, 22);
            this.insercaoToolStripMenuItem.Text = "Insercao";
            this.insercaoToolStripMenuItem.Click += new System.EventHandler(this.insercaoToolStripMenuItem_Click);
            // 
            // selecaoToolStripMenuItem
            // 
            this.selecaoToolStripMenuItem.Name = "selecaoToolStripMenuItem";
            this.selecaoToolStripMenuItem.Size = new System.Drawing.Size(126, 22);
            this.selecaoToolStripMenuItem.Text = "Selecao";
            this.selecaoToolStripMenuItem.Click += new System.EventHandler(this.selecaoToolStripMenuItem_Click);
            // 
            // estatísticasToolStripMenuItem
            // 
            this.estatísticasToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.bolhaToolStripMenuItem1,
            this.seleçãoToolStripMenuItem,
            this.inserçãoToolStripMenuItem,
            this.shellsortToolStripMenuItem1,
            this.heapsortToolStripMenuItem1,
            this.quicksortToolStripMenuItem1,
            this.mergesortToolStripMenuItem});
            this.estatísticasToolStripMenuItem.Name = "estatísticasToolStripMenuItem";
            this.estatísticasToolStripMenuItem.Size = new System.Drawing.Size(76, 20);
            this.estatísticasToolStripMenuItem.Text = "Estatísticas";
            // 
            // bolhaToolStripMenuItem1
            // 
            this.bolhaToolStripMenuItem1.Name = "bolhaToolStripMenuItem1";
            this.bolhaToolStripMenuItem1.Size = new System.Drawing.Size(128, 22);
            this.bolhaToolStripMenuItem1.Text = "Bolha";
            this.bolhaToolStripMenuItem1.Click += new System.EventHandler(this.bolhaToolStripMenuItem1_Click_1);
            // 
            // seleçãoToolStripMenuItem
            // 
            this.seleçãoToolStripMenuItem.Name = "seleçãoToolStripMenuItem";
            this.seleçãoToolStripMenuItem.Size = new System.Drawing.Size(128, 22);
            this.seleçãoToolStripMenuItem.Text = "Seleção";
            this.seleçãoToolStripMenuItem.Click += new System.EventHandler(this.seleçãoToolStripMenuItem_Click);
            // 
            // inserçãoToolStripMenuItem
            // 
            this.inserçãoToolStripMenuItem.Name = "inserçãoToolStripMenuItem";
            this.inserçãoToolStripMenuItem.Size = new System.Drawing.Size(128, 22);
            this.inserçãoToolStripMenuItem.Text = "Inserção";
            this.inserçãoToolStripMenuItem.Click += new System.EventHandler(this.inserçãoToolStripMenuItem_Click);
            // 
            // shellsortToolStripMenuItem1
            // 
            this.shellsortToolStripMenuItem1.Name = "shellsortToolStripMenuItem1";
            this.shellsortToolStripMenuItem1.Size = new System.Drawing.Size(128, 22);
            this.shellsortToolStripMenuItem1.Text = "Shellsort";
            this.shellsortToolStripMenuItem1.Click += new System.EventHandler(this.shellsortToolStripMenuItem1_Click);
            // 
            // heapsortToolStripMenuItem1
            // 
            this.heapsortToolStripMenuItem1.Name = "heapsortToolStripMenuItem1";
            this.heapsortToolStripMenuItem1.Size = new System.Drawing.Size(128, 22);
            this.heapsortToolStripMenuItem1.Text = "Heapsort";
            this.heapsortToolStripMenuItem1.Click += new System.EventHandler(this.heapsortToolStripMenuItem1_Click);
            // 
            // quicksortToolStripMenuItem1
            // 
            this.quicksortToolStripMenuItem1.Name = "quicksortToolStripMenuItem1";
            this.quicksortToolStripMenuItem1.Size = new System.Drawing.Size(128, 22);
            this.quicksortToolStripMenuItem1.Text = "Quicksort";
            this.quicksortToolStripMenuItem1.Click += new System.EventHandler(this.quicksortToolStripMenuItem1_Click);
            // 
            // mergesortToolStripMenuItem
            // 
            this.mergesortToolStripMenuItem.Name = "mergesortToolStripMenuItem";
            this.mergesortToolStripMenuItem.Size = new System.Drawing.Size(128, 22);
            this.mergesortToolStripMenuItem.Text = "Mergesort";
            this.mergesortToolStripMenuItem.Click += new System.EventHandler(this.mergesortToolStripMenuItem_Click);
            // 
            // ajudaToolStripMenuItem
            // 
            this.ajudaToolStripMenuItem.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.sobreToolStripMenuItem});
            this.ajudaToolStripMenuItem.Name = "ajudaToolStripMenuItem";
            this.ajudaToolStripMenuItem.Size = new System.Drawing.Size(50, 20);
            this.ajudaToolStripMenuItem.Text = "Ajuda";
            // 
            // sobreToolStripMenuItem
            // 
            this.sobreToolStripMenuItem.Name = "sobreToolStripMenuItem";
            this.sobreToolStripMenuItem.Size = new System.Drawing.Size(113, 22);
            this.sobreToolStripMenuItem.Text = "Sobre...";
            this.sobreToolStripMenuItem.Click += new System.EventHandler(this.sobreToolStripMenuItem_Click);
            // 
            // bgw
            // 
            this.bgw.WorkerSupportsCancellation = true;
            this.bgw.DoWork += new System.ComponentModel.DoWorkEventHandler(this.bgw_DoWork);
            this.bgw.RunWorkerCompleted += new System.ComponentModel.RunWorkerCompletedEventHandler(this.bgw_RunWorkerCompleted);
            // 
            // radioButton1
            // 
            this.radioButton1.AutoSize = true;
            this.radioButton1.Checked = true;
            this.radioButton1.Location = new System.Drawing.Point(2, 32);
            this.radioButton1.Name = "radioButton1";
            this.radioButton1.Size = new System.Drawing.Size(73, 17);
            this.radioButton1.TabIndex = 2;
            this.radioButton1.TabStop = true;
            this.radioButton1.Text = "Crescente";
            this.radioButton1.UseVisualStyleBackColor = true;
            this.radioButton1.CheckedChanged += new System.EventHandler(this.radioButton1_CheckedChanged);
            // 
            // radioButton2
            // 
            this.radioButton2.AutoSize = true;
            this.radioButton2.Location = new System.Drawing.Point(81, 32);
            this.radioButton2.Name = "radioButton2";
            this.radioButton2.Size = new System.Drawing.Size(86, 17);
            this.radioButton2.TabIndex = 3;
            this.radioButton2.Text = "Decrescente";
            this.radioButton2.UseVisualStyleBackColor = true;
            this.radioButton2.CheckedChanged += new System.EventHandler(this.radioButton2_CheckedChanged);
            // 
            // radioButton3
            // 
            this.radioButton3.AutoSize = true;
            this.radioButton3.Location = new System.Drawing.Point(173, 32);
            this.radioButton3.Name = "radioButton3";
            this.radioButton3.Size = new System.Drawing.Size(66, 17);
            this.radioButton3.TabIndex = 4;
            this.radioButton3.TabStop = true;
            this.radioButton3.Text = "Aleatório";
            this.radioButton3.UseVisualStyleBackColor = true;
            this.radioButton3.CheckedChanged += new System.EventHandler(this.radioButton3_CheckedChanged);
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Items.AddRange(new object[] {
            "1000",
            "10000",
            "50000",
            "100000",
            "500000"});
            this.comboBox1.Location = new System.Drawing.Point(255, 32);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(140, 21);
            this.comboBox1.TabIndex = 5;
            this.comboBox1.SelectedIndexChanged += new System.EventHandler(this.comboBox1_SelectedIndexChanged_1);
            // 
            // FormOrdenacao
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(524, 361);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.radioButton3);
            this.Controls.Add(this.radioButton2);
            this.Controls.Add(this.radioButton1);
            this.Controls.Add(this.panel);
            this.Controls.Add(this.menuStrip1);
            this.DoubleBuffered = true;
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MainMenuStrip = this.menuStrip1;
            this.MaximizeBox = false;
            this.Name = "FormOrdenacao";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Prática 5 - Métodos de Ordenação 2019/2";
            this.Load += new System.EventHandler(this.FormOrdenacao_Load);
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Panel panel;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem algoritmoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem bolhaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem ajudaToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem sobreToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem estatísticasToolStripMenuItem;
        private System.ComponentModel.BackgroundWorker bgw;
        private System.Windows.Forms.ToolStripMenuItem bolhaToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem mergeToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem quickSortToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem heapSortToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem shellSortToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem insercaoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem selecaoToolStripMenuItem;
        private System.Windows.Forms.RadioButton radioButton1;
        private System.Windows.Forms.RadioButton radioButton2;
        private System.Windows.Forms.RadioButton radioButton3;
        private System.Windows.Forms.ToolStripMenuItem seleçãoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem inserçãoToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem shellsortToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem heapsortToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem quicksortToolStripMenuItem1;
        private System.Windows.Forms.ToolStripMenuItem mergesortToolStripMenuItem;
        private System.Windows.Forms.ComboBox comboBox1;
    }
}

