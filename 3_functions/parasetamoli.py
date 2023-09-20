"""
COMP.CS.100: Parasetamoli
Tekijä: Erkka Lehtoranta
Opiskelijanumero: *SECRET*
A nonscientific dosing program for Paracetamol.
"""


def calculate_dose(weight, time_from_dose, total_24h):
    """Calculates the appropriate dose based on prerequisite information.

    :param weight: int, patient weight,
    :param time_from_dose: int, hours from previous dose,
    :param total_24h: int, milligrams dosed during past 24 hours.

    :return: int, dosage to be given to the patient (mg)."""
    DOSE_PER_KG = 15  # mg
    DAILY_MAX_DOSE = 4000  # mg

    if time_from_dose < 6:  # No serial drugging
        return 0
    max_per_dose = weight * DOSE_PER_KG
    if total_24h >= DAILY_MAX_DOSE:
        return 0
    else:
        return min(DAILY_MAX_DOSE - total_24h, max_per_dose)


def main():
    weight = int(input("Patient's weight (kg): "))
    time_from_dose = int(input(
        "How much time has passed from the previous dose (full hours): "))
    total_24h = int(input("The total dose for the last 24 hours (mg): "))
    print(f"The amount of Parasetamol to give to the patient: "
          f"{calculate_dose(weight, time_from_dose, total_24h)}")


if __name__ == "__main__":
    main()
