print("========== Data Analysis & Visualization Program ==========")
print("This program analyzes and visualizes data from a CSV or Excel file.")

from Packages import Matplotlib_2 as md

print("Importing necessary libraries... Done.")

data = None

while True:
    print("\n================ Main Menu ================")
    print("\nPlease choose an option:")
    print("=========================================== ")
    print("1. Load Dataset")
    print("2. Explore Dataset")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Values")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualizations")
    print("8. Exit")
    print("===========================================\n")
    choice = input("Enter your choice 1(1-8): ")
    print("============================================")
    print("You selected option :- ", choice)
    match choice:
        case '1':
            print("=========== Load Dataset ===========")
            print("1. Load Your Dataset :- ")
            print("2. Generate Random Dataset:- ")
            print("=====================================")
            choice = input("Enter your choice (1-2): ")
            print("You selected option", choice)
            match choice:
                case '1':
                    file_path = input("Enter the path to the file: ")
                    data = md.load_data(file_path)
                    print(f"Data Type Is :- {type(data)}")
                case '2':
                    data = md.Random_dataset()
                    print("Random dataset generated.")

        case '2':
            if data is None:
                print("No data loaded. Please load a dataset first.")
            else:
                md.display_statistics(data)

        case '3':
            if data is None:
                print("No data loaded. Please load a dataset first.")
            else:
                md.Dataframe(data)
                

        case '4':
            if data is None:
                print("No data loaded. Please load a dataset first.")
            else:
                data = md.handle_missing_values(data)

        case '5':
            if data is None:
                print("No data loaded. Please load a dataset first.")
            else:
                md.descriptive_statistics(data)

        case '6':
            if data is None:
                print("No data loaded. Please load a dataset first.")
            else:
                md.Data_visualization(data)

        case '7':
            if data is None:
                print("No data loaded. Please load a dataset first.")
            else:
                md.save_visualizations(data)

        case '8':
            print("Exiting the program. Goodbye!")
            break

        case _:
            print("~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!")
            print("Invalid choice. Please enter 1–8.")
            print("~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!")
