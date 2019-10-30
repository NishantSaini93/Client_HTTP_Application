from httpObject import HTTPObject
from httpConnection import HTTPConnection


def helpCommand(convertedArray):
    if convertedArray[0].lower() != "httpc":
        print("Please check your command(Use proper format)")
    elif len(convertedArray) == 2:
        print("httpc is a curl-like application but supports HTTP protocol only.")
        print("Usage\n    httpc command [arguments]\nThe commands are:")
        print("    get    executes a HTTP GET request and prints the response.")
        print("    post   executes a HTTP POST request and prints the response.")
        print("    prints this screen")
        print('\nUse httpc help "[command]" for more information about a command.')
    elif len(convertedArray) == 3:
        if convertedArray[1].lower() == "help":
            if convertedArray[2].lower() == "get":
                print(
                    "Usage:\n    httpc get [-v] [-h key:value] URL\nGets executes a HTTP GET request for a given URL.")
                print("    -v              Prints the detail of response such as protocol,status, and headers.")
                print("    -h key:values   Associates headers to HTTP Request with the format 'key:value'.")
            elif convertedArray[2].lower() == "post":
                print("Usage:\n    httpc post [-v] [-h key:value] [-d inline-data] [-f file] URL.")
                print("    -v              Prints the detail of response such as protocol,status, and headers.")
                print("    -h key:values   Associates headers to HTTP Request with the format 'key:value'.")
                print("    -d string       Associates an inline data to the body HTTP POST request.")
                print("    -f file         Associates the content of a file to the body HTTP POST request.")
                print("\nEither [-d] or [-f] can be used but not both.")
            else:
                print("Check your command")
    else:
        print("Check your command")


def main():
    flag = "good"
    while flag:
        flag = "good"
        inputCommand = input("Please enter the command:\n")
        convertedArray = inputCommand.split()
        for x in convertedArray:
            if x.lower() == "help":
                helpCommand(convertedArray)
                flag = "help"
            if x.lower() == "exit":
                flag = "exit"
        if flag == "good":
            try:
                my_http_obj = HTTPObject(inputCommand)
                HTTPConnection.send_request(my_http_obj)
            except Exception:
                pass
        elif flag == "exit":
            break


main()
