# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 21:30:04 2025

@author: Thanh Thien Vu
"""

#Definere variable
F_El = 5000.0               # Forsikring for Elbil kr/år
F_Bensin = 7500.0           # Forsikring for bensinbil kr/år
Avgift = 8.38               # Trafikkforsikringsavgift kr/dag
El = 0.2                    # Drivstoffbruk kWh/km
Bensin = 1.0                # Drivstoffbruk kr/km
Strømpris = 2.0             # Strømpris kr/kWh
Bom_El = 0.1                # Bomavgift Elbil kr/km
Bom_Bensin = 0.3            # Bomavgift bensinbil kr/km

Antall_km = float (input ("Tast inn antall kjørt km: "))

# Årlig totalkostnad
Totalkostnad_El = F_El + (Avgift * 365) + (El * Antall_km * Strømpris) + (Bom_El * Antall_km)
Totalkostnad_Bensin = F_Bensin + (Avgift * 365) + (Bensin * Antall_km) + (Bom_Bensin * Antall_km)


print("Årlig totalkostnadene for Elbil: ", round(Totalkostnad_El, 2), "kr.")
print("Årlig totalkostnadene for bensinbil: ", round(Totalkostnad_Bensin, 2), "kr.")

# Tatt hensyn til negativ differanse
if Totalkostnad_El > Totalkostnad_Bensin:
    print("Årlig kostnadsdifferanse: ", round(Totalkostnad_El - Totalkostnad_Bensin, 2), "kr.")
else:
    print("Årlig kostnadsdifferanse: ", round(Totalkostnad_Bensin - Totalkostnad_El, 2), "kr.")