using System;

namespace Pratica5 {
    class Preenchimento {
        public static void Aleatorio(int[] vet, int limite) {
            Random r = new Random();
            for (int i = 0; i < vet.Length; i++) {
                vet[i] = r.Next(0, limite);
            }
        }
        public static void Crescente(int[] vet, int limite) {
            // TO DO
            double aux;
            
            aux = 0;
            for(int i = 0; i < vet.Length; i++)
            {
                aux += 0.6;
                vet[i] = Convert.ToInt32(aux);
                 
            }
        }
        public static void Decrescente(int[] vet, int limite) {
            // TO DO
            double aux = 300.6;
            

            for(int i = 0; i<vet.Length;i++)
            {
                aux -= 0.6;
                vet[i] = Convert.ToInt32(aux);
            }
        }
    }
}
