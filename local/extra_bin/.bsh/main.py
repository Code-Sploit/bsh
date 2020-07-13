from cmd import Cmd
import os
from getpass import getpass
username = input(str("Logon as: "))
if (os.path.isfile(".data/au/" + str(username))):
    print("Sorry that username is already in use!")
elif (os.path.isfile(".data/aa/" + str(username))):
    print("Sorry that username is already in use!")
else:
    pass

class AdminPrompt(Cmd):
    global username
    prompt = str(username) + "@admin-id" + " omega-sh> "
    intro = "Welcome to the admin omega shell!"
        
    def do_exit(self, inp):
        '''\nExits the program.\n\nUsage: exit'''
        print("Bye")
        os.remove("/usr/local/extra_bin/.osh/.data/aa/" + str(username))
        os.system("touch /usr/local/extra_bin/.osh/.data/au/" + str(username))
        return True
    
    def do_diradd(self, inp):
        '''\nCreate Directory.\n\nUsage: diradd "name"'''
        try:
            os.system("mkdir " + str(inp))
        except Exception as e:
            print(e)
    def do_setowner(self, inp):
        '''\nSets owner of directory/file.\n\nUsage: setowner "name" "file"'''
        name = inp.split(" ")[0]
        filename = inp.split(" ")[1]
        try:
            os.system("chown " + str(name) + " " + str(filename))
        except Exception as e:
            print(e)
    def do_setpremissions(self, inp):
        '''\nSet premissions of directory/file.\n\nUsage: setpremissions "premissions" "file"'''
        premisssions = inp.split(" ")[0]
        filename = inp.split(" ")[1]
        try:
            os.system("chmod " + str(premissions) + " " + str(filename))
        except Exception as e:
            print(e)
    
    def do_edit(self, inp):
        '''\nEdit a file.\n\nUsage: edit "filename"'''
        try:
            os.system("vim " + str(inp))
        except Exception as e:
            print(e)
    
    def do_echo(self, inp):
        '''\nEcho text.\n\nUsage: echo "text"'''
        print(inp)

    def do_remove(self, inp):
        '''\nRemove file.\n\nUsage: remove "filename"'''
        try:
            os.system("rm -rf " + str(inp))
        except Exception as e:
            print(e)
    
    def do_add(self, inp):
        '''\nAdd file.\n\nUsage: add "filename"'''
        try:
            os.system("touch " + str(inp))
        except Exception as e:
            print(e)

    def do_list(self, inp):
        '''\nList files in specified directory.\n\nUsage: list or list "directory"'''
        if (inp == ""):
            try:
                os.system("ls")
            except Exception as e:
                print(e)
        else:
            try:
                os.system("ls " + inp)
            except Exception as e:
                print(e)

    def do_listall(self, inp):
        '''\nList all files in specified directory.\n\nUsage: listall or listall "directory"'''
        if (inp == ""):
            try:
                os.system("ls -lah")
            except Exception as e:
                print(e)
        else:
            try:
                os.system("ls -lah " + inp)
            except Exception as e:
                print(e)
    
    def do_clear(self, inp):
        '''\nClear the screen.\n\nUsage: clear'''
        os.system("clear")

    def do_read(self, inp):
        '''\nRead a file.\n\nUsage: read "filename"'''
        try:
            os.system("cat " + inp)
        except Exception as e:
            print(e)

    def do_whereami(self, inp):
        '''\nPrints current working directory path.\n\nUsage: whereami'''
        os.system("pwd")

    def do_gotodir(self, inp):
        '''\nChange current working directory path to specified path.\n\nUsage: gotodir "path"'''
        try:
            os.chdir(inp)
        except Exception as e:
            print(e)

    def do_copy(self, inp):
        '''\nCopy files.\n\nUsage: copy "file" "file2" or copy "file" "/path/to/file2" or copy "/path/to/file" "/path/to/file2" or copy "/path/to/file" "file2"'''
        file1 = inp.split(" ")[0]
        file2 = inp.split(" ")[1]
        try:
            os.system("cp " + file1 + " " + file2)
        except Exception as e:
            print(e)

    def do_move(self, inp):
        '''\nMove files.\n\nUsage: move "file" "file2" or move "file" "/path/to/file2" or move "/path/to/file" "/path/to/file2" or move "/path/to/file" "file2"'''
        file1 = inp.split(" ")[0]
        file2 = inp.split(" ")[1]
        try:
            os.system("mv " + file1 + " " + file2)
        except Exception as e:
            print(e)
    
    def do_kick(self, inp):
         '''\nKicks a user.\n\nUsage: kick "user"'''
         with open("/usr/local/extra_bin/.osh/.tmp/p/" + str(inp) + ".pid","r") as f:
             string = f.read()
             os.system("kill " + str(string))
    
    def do_listusers(self, inp):
        '''\nList all users.\n\nUsage: listusers'''
        print("Users are: " + str(os.popen("ls /usr/local/extra_bin/.osh/.data/au/").read()))
    
    def do_listadmins(self, inp):
        '''\nList all admins.\n\nUsage: listadmins'''
        print("Admins are: " + str(os.popen("ls /usr/local/extra_bin/.osh/.data/aa/").read()))

class MyPrompt(Cmd):
    global username
    prompt = str(username) + "@user-id" + " omega-sh> "
    intro = "Welcome to the user omega shell!"
    
    with open("/usr/local/extra_bin/.osh/.tmp/p/" + str(username) + ".pid","w") as f:
        f.write(str(os.getpid()))
    
    os.system("touch /usr/local/extra_bin/.osh/.data/au/" + str(username))
    
    def do_exit(self, inp):
        '''\nExits the program.\n\nUsage: exit'''
        print("Bye")
        os.remove("/usr/local/extra_bin/.osh/.data/au/" + str(username))
        os.remove("/usr/local/extra_bin/.osh/.tmp/p/" + str(username) + ".pid")
        return True

    def do_echo(self, inp):
        '''\nEcho text.\n\nUsage: echo "text"'''
        print(inp)
        def do_diradd(self, inp):
        '''\nCreate Directory.\n\nUsage: diradd "name"'''
        try:
            os.system("mkdir " + str(inp))
        except Exception as e:
            print(e)
            
    def do_diradd(self, inp):
        '''\nCreate Directory.\n\nUsage: diradd "name"'''
        try:
            os.system("mkdir " + str(inp))
        except Exception as e:
            print(e)
    
    def do_setowner(self, inp):
        '''\nSets owner of directory/file.\n\nUsage: setowner "name" "file"'''
        name = inp.split(" ")[0]
        filename = inp.split(" ")[1]
        try:
            os.system("chown " + str(name) + " " + str(filename))
        except Exception as e:
            print(e)
    def do_setpremissions(self, inp):
        '''\nSet premissions of directory/file.\n\nUsage: setpremissions "premissions" "file"'''
        premisssions = inp.split(" ")[0]
        filename = inp.split(" ")[1]
        try:
            os.system("chmod " + str(premissions) + " " + str(filename))
        except Exception as e:
            print(e)
    
    def do_edit(self, inp):
        '''\nEdit a file.\n\nUsage: edit "filename"'''
        try:
            os.system("vim " + str(inp))
        except Exception as e:
            print(e)
    def do_remove(self, inp):
        '''\nRemove file.\n\nUsage: remove "filename"'''
        try:
            os.system("rm -rf " + str(inp))
        except Exception as e:
            print(e)
    
    def do_add(self, inp):
        '''\nAdd file.\n\nUsage: add "filename"'''
        try:
            os.system("touch " + str(inp))
        except Exception as e:
            print(e)

    def do_list(self, inp):
        '''\nList files in specified directory.\n\nUsage: list or list "directory"'''
        if (inp == ""):
            try:
                os.system("ls")
            except Exception as e:
                print(e)
        else:
            try:
                os.system("ls " + inp)
            except Exception as e:
                print(e)

    def do_listall(self, inp):
        '''\nList all files in specified directory.\n\nUsage: listall or listall "directory"'''
        if (inp == ""):
            try:
                os.system("ls -lah")
            except Exception as e:
                print(e)
        else:
            try:
                os.system("ls -lah " + inp)
            except Exception as e:
                print(e)
    
    def do_clear(self, inp):
        '''\nClear the screen.\n\nUsage: clear'''
        os.system("clear")

    def do_read(self, inp):
        '''\nRead a file.\n\nUsage: read "filename"'''
        try:
            os.system("cat " + inp)
        except Exception as e:
            print(e)

    def do_whereami(self, inp):
        '''\nPrints current working directory path.\n\nUsage: whereami'''
        os.system("pwd")

    def do_gotodir(self, inp):
        '''\nChange current working directory path to specified path.\n\nUsage: gotodir "path"'''
        try:
            os.chdir(inp)
        except Exception as e:
            print(e)

    def do_copy(self, inp):
        '''\nCopy files.\n\nUsage: copy "file" "file2" or copy "file" "/path/to/file2" or copy "/path/to/file" "/path/to/file2" or copy "/path/to/file" "file2"'''
        file1 = inp.split(" ")[0]
        file2 = inp.split(" ")[1]
        try:
            os.system("cp " + file1 + " " + file2)
        except Exception as e:
            print(e)

    def do_move(self, inp):
        '''\nMove files.\n\nUsage: move "file" "file2" or move "file" "/path/to/file2" or move "/path/to/file" "/path/to/file2" or move "/path/to/file" "file2"'''
        file1 = inp.split(" ")[0]
        file2 = inp.split(" ")[1]
        try:
            os.system("mv " + file1 + " " + file2)
        except Exception as e:
            print(e)

    def do_lgnadmin(self, inp):
        '''\nMake admin.\n\nUsage: mkadmin - or mkadmin "user"'''
        with open("/usr/local/extra_bin/.osh/.scrty/adminpass.txt","r") as f:
            adminpass = f.read()

        passg = getpass(str("Password: "))
        passg = passg + "\n"

        if (adminpass == passg):
            print("You are now admin!")
            print(str(username))
            os.remove("/usr/local/extra_bin/.osh/.data/au/" + str(username))
            os.system("touch /usr/local/extra_bin/.osh/.data/aa/" + str(username))
            AdminPrompt().cmdloop()
        else:
            print("Invalid password!")

MyPrompt().cmdloop()
