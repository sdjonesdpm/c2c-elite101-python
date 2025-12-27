#Ask which scale the user is converting from (C/F/K).
#Ask which scale to convert to (cannot match the from-scale).
#Prompt for the numeric temperature and apply the appropriate conversion formula.
#Output both the original and converted values with units.
def user_input_from(from_scale):
    from_scale = input("Enter the scale you are converting from (C/F/K): ").strip().upper()
    if from_scale not in ['C', 'F', 'K']:
        print("Invalid scale. Please enter C, F, or K.")
        return None
    return from_scale
def user_input_to(to_scale):
    to_scale = input("Enter the scale you are converting to (C/F/K): ").strip().upper()
    if to_scale not in ['C', 'F', 'K']:
        print("Invalid scale. Please enter C, F, or K.")
        return None
    return to_scale
def user_input_temperature():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        return temperature
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
        return None
def convert_temperature(from_scale, to_scale, temperature):
    if from_scale == to_scale:
        print("from_scale cannot be equal to to_scale.")
        return None
    if from_scale == 'C':
        if to_scale == 'F':
            return (temperature * 9/5) + 32
        elif to_scale == 'K':
            return temperature + 273.15
    elif from_scale == 'F':
        if to_scale == 'C':
            return (temperature - 32) * 5/9
        elif to_scale == 'K':
            return (temperature - 32) * 5/9 + 273.15
    elif from_scale == 'K':
        if to_scale == 'C':
            return temperature - 273.15
        elif to_scale == 'F':
            return (temperature - 273.15) * 9/5 + 32
def main():
    from_scale = None
    while from_scale is None:
        from_scale = user_input_from(from_scale)
    to_scale = None
    while to_scale is None or to_scale == from_scale:
        to_scale = user_input_to(to_scale)
        if to_scale == from_scale:
            print("to_scale cannot be equal to from_scale. Please choose a different scale.")
    temperature = None
    while temperature is None:
        temperature = user_input_temperature()
    converted_temperature = convert_temperature(from_scale, to_scale, temperature)
    if converted_temperature is not None:
        print(f"{temperature}°{from_scale} is equal to {converted_temperature:.2f}°{to_scale}.")
if __name__ == "__main__":
    main()
