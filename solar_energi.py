def get_input(prompt, default, cast_func=float):
    user_input = input(f"{prompt} (default={default}): ")
    return cast_func(user_input) if user_input else default

def format_energy(value_wh):
    if value_wh >= 1000:
        return f"{value_wh / 1000:.2f} kWh"
    else:
        return f"{value_wh:.0f} Wh"

# -------- Input Data (dengan nilai default) --------
print("Masukkan data sistem (tekan ENTER untuk pakai nilai default dari tabel)")

# Panel surya
solar_wp = get_input("Solar Panel Watt Peak (WP)", 100)
solar_voltage = get_input("Tegangan Panel (V)", 17.8)
solar_current = get_input("Arus Panel (A)", 5.62)
sun_hours = get_input("Durasi Penyinaran Efektif (jam)", 5)

# Beban
load_voltage = get_input("Tegangan Beban (V)", 12)
load_current = get_input("Arus Beban (A)", 0.5)
load_hours = get_input("Durasi Penggunaan Beban (jam)", 8)

# Baterai
battery_voltage = get_input("Tegangan Baterai (V)", 12)
battery_capacity_ah = get_input("Kapasitas Baterai (Ah)", 25)

# Efisiensi sistem dan charging
system_efficiency = 0.75
battery_efficiency = 0.85

# -------- Perhitungan Energi --------
solar_energy_wh = solar_wp * sun_hours * system_efficiency
load_power_w = load_voltage * load_current
load_energy_wh = load_power_w * load_hours
battery_capacity_wh = battery_voltage * battery_capacity_ah
battery_charge_time = battery_capacity_wh / (solar_wp * system_efficiency * battery_efficiency)

# -------- Output --------
print("\n--- HASIL PERHITUNGAN ---")
print(f"Energi Panel Surya (setelah efisiensi): {format_energy(solar_energy_wh)}")
print(f"Energi Beban: {format_energy(load_energy_wh)}")
print(f"Kapasitas Baterai: {format_energy(battery_capacity_wh)}")
print(f"Waktu Pengisian Baterai: {battery_charge_time:.2f} jam")

total_kebutuhan = load_energy_wh + (battery_capacity_wh / battery_efficiency)
if solar_energy_wh >= total_kebutuhan:
    print("Energi CUKUP untuk beban dan isi baterai.")
else:
    print("Energi TIDAK cukup, perlu tambah panel atau kurangi beban.")
