import unittest

from test import TestAccount

def run_tests(menu_option):
    suite = unittest.TestSuite()

    if menu_option == '1':
    #suite.addTest(TestAccount(''))

    elif menu_option == '2':

    # elif choice == '3':
    #
    # elif choice == '4':
    #
    # elif choice == '5':
    #
    # elif choice == '6':
    #
    # elif choice == '7':
    #
    # elif choice == '8':
    #
    # elif choice == '9':

    else:
        print("Invalid choice. Exiting.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    print("Enter a module from the menu to test ('1' for New Customer\n "
          "'2' for Edit Customer\n"
          "'3' for Delete Customer\n"
          "'4' for New Account\n"
          "'5' for Edit Account\n"
          "'6' for Delete Account\n"
          "'7' for Balance Enquiry\n"
          "'8' for Mini Statement\n"
          "'9' for Customized Statement")
    choice = input().strip().lower()
    run_tests(choice)