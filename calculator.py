```python
def calculate_load():
    print("--- Electrical & Solar Load Calculator ---")
    appliances = []
    total_watts = 0

    while True:
        name = input("\nAppliance ka naam likho (ya band karne ke liye 'done' likho): ")
        if name.lower() == 'done':
            break
        try:
            watts = float(input(f"{name} kitne Watt ka hai?: "))
            hours = float(input(f"Din mein kitne ghante chalta hai?: "))
            qty = int(input(f"Kitne {name} hain? (Quantity): "))

            daily_wh = watts * hours * qty
            total_watts += (watts * qty)
            appliances.append((name, qty, watts, daily_wh))
        except ValueError:
            print("Galti: Sirf numbers enter karein!")

    print("\n--- Summary Report ---")
    total_daily_units = 0
    for item in appliances:
        units = item[3] / 1000
        total_daily_units += units
        print(f"- {item[0]} (x{item[1]}): {item[2]}W | Daily Consumption: {units:.2f} Units (kWh)")

    print(f"\nTotal Connected Load: {total_watts} Watts ({total_watts/1000:.2f} kW)")
    print(f"Total Daily Consumption: {total_daily_units:.2f} Units")
    print(f"Estimated Monthly Bill (at ₹8/unit): ₹{total_daily_units * 30 * 8:.2f}")

if __name__ == "__main__":
    calculate_load()
