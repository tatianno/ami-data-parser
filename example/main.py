import sys
from time import sleep
from ami_data_parser import Controller
from asterisk.manager import (
   Manager, 
   ManagerAuthException, 
   ManagerException, 
   ManagerSocketException
)


AMI_HOST = '192.168.0.103'
AMI_USERNAME = 'DEV'
AMI_PASSWORD = 'gnew'


if __name__ == '__main__':

   manager = Manager()
   controller = Controller()

   try:
      # connect to the manager
      try:
         manager.connect(AMI_HOST)
         manager.login(AMI_USERNAME, AMI_PASSWORD)

         while True:
            queue_data = manager.command('queue show').response
            peer_data = manager.command('core show hints').response
            channel_data = manager.command('core show channels concise').response
            print('-----------queue data-----------------')
            print(controller.queue_update(queue_data))
            print('-----------peer data------------------')
            print(controller.peer_update(peer_data))
            print('-----------channel data---------------')
            print(controller.channel_update(channel_data))
            sleep(2)

      except ManagerSocketException:
         print("Error connecting to the manager")
         sys.exit(1)

      except ManagerAuthException:
         print("Error logging in to the manager")
         sys.exit(1)

      except ManagerException:
         print("Error")
         sys.exit(1)
      
      except KeyboardInterrupt:
         sys.exit(0)

   finally:
      manager.logoff()