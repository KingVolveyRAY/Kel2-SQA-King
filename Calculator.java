package com.rayhan.junit;

public class Calculator {

    public int tambah(int a, int b) {
        return a + b;
    }

    public int kurang(int a, int b) {
        return a - b;
    }

    public int kali(int a, int b) {
        return a * b;
    }

    public double bagi(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("Pembagi tidak boleh bernilai nol (0)!");
        }
        return (double) a / b;
    }

    public boolean apakahGenap(int angka) {
        return angka % 2 == 0;
    }

    public String tentukanGrade(double nilai) {
        if (nilai < 0 || nilai > 100) {
            throw new IllegalArgumentException("Nilai harus berada di rentang 0 hingga 100!");
        }
        if (nilai >= 85) return "A";
        if (nilai >= 75) return "B";
        if (nilai >= 60) return "C";
        if (nilai >= 50) return "D";
        return "E";
    }
}
