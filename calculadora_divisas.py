def exchange_money(budget, exchange_rate):
    if exchange_rate <= 0:
        raise ValueError("La tasa de cambio debe ser mayor que cero.")
    return round(budget / exchange_rate, 2)


def main():
    print("=== Calculadora de Divisas para Viajeros ===")
    print("Países disponibles:")
    print("1. Japón (JPY)")
    print("2. México (MXN)")
    print("3. Alemania (EUR)")
    print("4. Colombia (COP)")

    tasas = {
        "1": ("Japón", 0.0075),
        "2": ("México", 0.11),
        "3": ("Alemania", 1.09),
        "4": ("Colombia", 0.0003125)
    }

    opcion = input("Selecciona el país (1-4): ").strip()

    if opcion not in tasas:
        print("Opción inválida.")
        return

    pais, tasa = tasas[opcion]

    try:
        presupuesto = float(input("Ingresa tu presupuesto en USD: "))
        if presupuesto <= 0:
            print("El presupuesto debe ser positivo.")
            return
    except ValueError:
        print("Entrada inválida. Debes ingresar un número.")
        return

    resultado = exchange_money(presupuesto, tasa)
    print(f"\nEn {pais}, recibirás aproximadamente: {resultado} en moneda local.")

if __name__ == "__main__":
    main()