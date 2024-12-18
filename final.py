# Plant Growth Management System

plants = {}

def menu():
    """Display the main menu."""
    print("\nMenu:")
    print("1. Add Plant")
    print("2. View Plants")
    print("3. Apply Compost")
    print("4. Apply Biochar")
    print("5. Apply Inorganic Fertilizer")
    print("6. Edit Plant")
    print("7. Delete Plant")
    print("8. Exit")

def add_plant():
    """Add a new plant."""
    plant_id = input("Enter Plant ID: ")
    if plant_id in plants:
        print("Plant ID already exists. Try again.")
        return
    name = input("Enter Plant Name: ")
    soil_type = input("Enter Soil Type: ")
    ph = float(input("Enter Soil pH: "))
    organic_matter = float(input("Enter Organic Matter (%): "))
    plants[plant_id] = {
        "Name": name,
        "Soil Type": soil_type,
        "pH": ph,
        "Organic Matter": organic_matter,
        "Growth Rate": 0.0
    }
    print(f"Plant '{name}' added successfully!")

def view_plants():
    """View all plants."""
    if not plants:
        print("No plants available.")
        return
    for plant_id, details in plants.items():
        print(f"ID: {plant_id}, Name: {details['Name']}, Soil: {details['Soil Type']}, "
              f"pH: {details['pH']:.2f}, Organic Matter: {details['Organic Matter']:.2f}%, "
              f"Growth Rate: {details['Growth Rate']:.2f}")

def apply_compost():
    """Apply compost to a plant."""
    plant_id = input("Enter Plant ID: ")
    if plant_id not in plants:
        print("Plant ID not found.")
        return
    amount = float(input("Enter compost amount (kg): "))
    plants[plant_id]["Growth Rate"] += 0.4 * amount
    plants[plant_id]["Organic Matter"] += 0.2 * amount
    print(f"Compost applied to '{plants[plant_id]['Name']}'.")

def apply_biochar():
    """Apply biochar to a plant."""
    plant_id = input("Enter Plant ID: ")
    if plant_id not in plants:
        print("Plant ID not found.")
        return
    amount = float(input("Enter biochar amount (kg): "))
    plants[plant_id]["Growth Rate"] += 0.3 * amount
    plants[plant_id]["pH"] += 0.1 * amount
    plants[plant_id]["Organic Matter"] += 0.15 * amount
    print(f"Biochar applied to '{plants[plant_id]['Name']}'.")

def apply_inorganic_fertilizer():
    """Apply inorganic fertilizer to a plant."""
    plant_id = input("Enter Plant ID: ")
    if plant_id not in plants:
        print("Plant ID not found.")
        return
    nitrogen = float(input("Enter nitrogen amount (kg): "))
    phosphorus = float(input("Enter phosphorus amount (kg): "))
    potassium = float(input("Enter potassium amount (kg): "))
    plants[plant_id]["Growth Rate"] += 0.5 * (nitrogen + phosphorus + potassium)
    plants[plant_id]["pH"] -= 0.05 * (nitrogen + phosphorus + potassium)
    print(f"Inorganic fertilizer applied to '{plants[plant_id]['Name']}'.")

def edit_plant():
    """Edit plant details."""
    plant_id = input("Enter Plant ID: ")
    if plant_id not in plants:
        print("Plant ID not found.")
        return
    print("Leave fields blank to keep current values.")
    new_name = input(f"New name (current: {plants[plant_id]['Name']}): ")
    new_soil_type = input(f"New soil type (current: {plants[plant_id]['Soil Type']}): ")
    new_ph = input(f"New pH (current: {plants[plant_id]['pH']}): ")
    new_organic_matter = input(f"New organic matter (current: {plants[plant_id]['Organic Matter']}%): ")

    if new_name:
        plants[plant_id]["Name"] = new_name
    if new_soil_type:
        plants[plant_id]["Soil Type"] = new_soil_type
    if new_ph:
        plants[plant_id]["pH"] = float(new_ph)
    if new_organic_matter:
        plants[plant_id]["Organic Matter"] = float(new_organic_matter)
    
    print(f"Plant '{plant_id}' updated successfully.")

def delete_plant():
    """Delete a plant."""
    plant_id = input("Enter Plant ID to delete: ")
    if plant_id not in plants:
        print("Plant ID not found.")
        return
    del plants[plant_id]
    print(f"Plant '{plant_id}' deleted successfully.")

def main():
    """Main program loop."""
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == "1":
            add_plant()
        elif choice == "2":
            view_plants()
        elif choice == "3":
            apply_compost()
        elif choice == "4":
            apply_biochar()
        elif choice == "5":
            apply_inorganic_fertilizer()
        elif choice == "6":
            edit_plant()
        elif choice == "7":
            delete_plant()
        elif choice == "8":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()