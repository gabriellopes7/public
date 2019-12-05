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
        [STAThread]
        static void Main(string[] args)
        {
            string line;
            OpenFileDialog theDialog = new OpenFileDialog();
            theDialog.Title = "Open Text File";
            theDialog.Filter = "TXT files|*.txt";
            theDialog.InitialDirectory = @"h:\";
            if (theDialog.ShowDialog() == DialogResult.OK)
            {
                System.IO.StreamReader file = new System.IO.StreamReader(theDialog.FileName.ToString());
                while ((line = file.ReadLine()) != null)
                {
                    Console.WriteLine(line);
                }
                file.Close();
            }
            Console.ReadLine();
        }
    }
}
