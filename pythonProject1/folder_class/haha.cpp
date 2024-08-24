#include <stdio.h>

int main() {
  char nama[20];
  int stb;
  int sks1;
  char nilai1;
  int sks2;
  char nilai2;

  // Membaca input dari pengguna
  printf("Masukkan nama mahasiswa: ");
  scanf("%s", nama);
  printf("Masukkan STB: ");
  scanf("%d", &stb);
  printf("Masukkan SKS matakuliah 1: ");
  scanf("%d", &sks1);
  printf("Masukkan nilai matakuliah 1 [A-E]: ");
  scanf(" %c", &nilai1);
  printf("Masukkan SKS matakuliah 2: ");
  scanf("%d", &sks2);
  printf("Masukkan nilai matakuliah 2 [A-E]: ");
  scanf(" %c", &nilai2);

  // Menghitung IP semester
  int total_sks = sks1 + sks2;
  int total_nilai = (nilai1 - 'A') + (nilai2 - 'A');
  float ip = total_nilai / total_sks;

  // Mencetak output
  printf("STB: %d\n", stb);
  printf("Nama: %s\n", nama);
  printf("No. Matakuliah\t\tSKS\tNilai\t\tBobotXSKS\n");
  printf("1\t\t\t%d\t%d\t\t%d\n", sks1, nilai1, sks1 * (nilai1 - 'A'));
  printf("2\t\t\t%d\t%d\t\t%d\n", sks2, nilai2, sks2 * (nilai2 - 'A'));
  printf("Total\t\t\t%d\t%.2f\t\t%.2f\n", total_sks, ip, ip * total_sks);

  return 0;
}
