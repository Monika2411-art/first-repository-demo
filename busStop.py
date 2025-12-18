'''Bus Route Management 
Represent bus stops as a list.
 Add or remove stops dynamically. 
 Reverse the route.'''
bus_stops = []
while True:
    print('\n Bus Route management ')
    print("1.Add a bus stop")
    print("2.Remove a bus stop")
    print("3.Reverse the route")
    print("4.print the route")
    print("5.Exit")


    choice = input()
    if choice == '1':
        name = input("Enter the name of the stop\n")
        bus_stops.append(name)
        print(f"{name} added succesfully")



    elif choice == '2':
        name = input("Enter the name of the stop \n")
        if name in bus_stops:
            bus_stops.remove(name)
            print(f"{name} removed successfully from the route")    
        else:
            print(f"{name} not found in the list")



    elif choice == '3':
        bus_stops.reverse()
        print("route reverse succesfully.")
    


    elif choice == '4':
        for i , name in enumerate(bus_stops,start=1):
            print(f"{i}.{name}")
    


    elif choice == '5':
        exit()

