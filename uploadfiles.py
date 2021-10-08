import dropbox
import os

class TransferData:
 #   def__init__(self, token1):
 #       self.access_token=token1

    def upload_folder(folder_from,folder_to):
        #dbx=dropbox.Dropbox(self.access_token)
        dbx=dropbox.Dropbox('sl.A4-nUbUhgwcIL8nuPYgOXPwrwYYPNmA_tejGCGUQwwTlJQecU9LV-_sRzos8Bsod5JjkFTlSb8ggUjuJZGgCLJOBZR6YdYaPpcP0K2mjm44GbougrFV9hTjmlE6PvtvPRuYUQmM')
        for root, dirs, files in os.walk(folder_from):
            #for name in files
            #    print(os.path.join(root, name))
            relative_path = os.path.relpath(local_path, folder_from)
            dropbox_path = os.path.join(folder_to, relative_path)
            print(relative_path)
            print(dropbox_path)
            with open(local_path,'rb') as f:
                dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))
    

def main():
    access_token='sl.A4-nUbUhgwcIL8nuPYgOXPwrwYYPNmA_tejGCGUQwwTlJQecU9LV-_sRzos8Bsod5JjkFTlSb8ggUjuJZGgCLJOBZR6YdYaPpcP0K2mjm44GbougrFV9hTjmlE6PvtvPRuYUQmM'
    #TransferData=TransferData(access_token)
    #TransferData=TransferData()
    folder_from=input("Enter the Folder Path to Transfer.-")
    folder_to=input("Enter the Folder Path to Upload to Dropbox.-")

    TransferData.upload_folder(folder_from,folder_to)
    print("Folder Has Been Moved!")

if __name__=='__main__':
    main()