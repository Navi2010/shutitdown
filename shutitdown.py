def shutdown():
    print ('make answer below all lowercase')
    user_input = input("do you want to shut down the system? (yes/no): ")
    
    if user_input == 'yes':
        print("shutting down...")
    elif user_input == 'no':
        print("abort shutdown.")
    else:
        print("sorry, there has been an error.")
shutdown()
