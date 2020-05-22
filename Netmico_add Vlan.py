from netmiko import ConnectHandler
from datetime import datetime, date
import ast


device_list=[]
with open('source.txt', 'r') as inFile:
    device_list=ast.literal_eval(inFile.read())


def add_vlan(dev):
        vlan_num = input("Give me the vlan number you want to add: ")
        command_1 = 'vlan ' + vlan_num
        vlan_name = input("Give me a name for your vlan: ")
        command_2 = 'name ' + vlan_name
        config_set = [command_1, command_2]
        for device in dev:
            net_connect = ConnectHandler(**device)
            print("Connection to ",device['host']," stablished")
            #net_connect.send_config_from_file("source.txt")
            net_connect.send_config_set(config_set)
            print('Vlan ',vlan_num," added successfully ")
            choice_display = input('Do you want to see the result?(y/n)')
            output = net_connect.send_command('show vlan')
            if choice_display==("y" or 'Y' or  'yes' or 'Yes'):
                print(output)
            choice_save=input('Do you want to save the output?(y/n)')
            if choice_save == ("y" or 'Y' or 'yes' or 'Yes'):
                now = datetime.now()
                today = date.today()
                current_time = now.strftime("_%H-%M-%S")
                file=open(device['host']+'_'+str(today)+current_time+'.txt','w')
                file.write(output)
                file.close()
                net_connect.disconnect()
            print('=================================================')
        return print("done successfully")


add_vlan(device_list)