# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 16:54:23 2022

@author: Hp
"""

import csv
from statistics import mean, stdev

# Membaca data dari file Negara.csv
with open('Negara.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)

# Menghitung mean dan standar deviasi dari kolom Luas dan Populasi
luas_mean = mean([int(row['Luas']) for row in data])
luas_stdev = stdev([int(row['Luas']) for row in data])
populasi_mean = mean([int(row['Populasi']) for row in data])
populasi_stdev = stdev([int(row['Populasi']) for row in data])

# Menulis data mean dan standar deviasi ke file NegaraStandarDeviasi.csv
with open('NegaraStandarDeviasi.csv', 'w') as csvfile:
    fieldnames = ['Negara', 'Luas Mean', 'Luas Std Dev', 'Populasi Mean', 'Populasi Std Dev']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', lineterminator='\n')

    # Menambahkan judul pada file output
    writer.writeheader()

    for row in data:
        writer.writerow({
            'Negara': row['Negara'],
            'Luas Mean': luas_mean,
            'Luas Std Dev': luas_stdev,
            'Populasi Mean': populasi_mean,
            'Populasi Std Dev': populasi_stdev
        })

# Menulis data mean dari kolom Luas dan Populasi ke file NegaraMean.csv
with open('NegaraMean.csv', 'w') as csvfile:
    fieldnames = ['Negara', 'Luas Mean', 'Populasi Mean']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=',', lineterminator='\n')

    # Menambahkan judul pada file output
    writer.writeheader()

    for row in data:
        writer.writerow({
            'Negara': row['Negara'],
            'Luas Mean': luas_mean,
            'Populasi Mean': populasi_mean
        })