import Control
import DBHelper



while True:
    select = input("1.start game \n2.setting \n\n>>select menu : ")
    if select == '1':
        keylist = []
        stack = []
        row = 0;
        while True:
            print("\n\n",DBHelper.list())
            selectSet = input("\n>>select setting : ")
            row = DBHelper.load(selectSet)
            if row == None:
                print("\nDose not exist...")
            else:
                break

        for k in range(18):
            keylist.append(row[k+2])
            stack.append(0)
                
        Control.control(keylist, stack)
        

    if select == '2':
        print("Not yet developed")

