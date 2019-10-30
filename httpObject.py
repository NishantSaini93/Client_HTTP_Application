import socket


class HTTPObject:
    """class to store http message"""
    _url = ''
    _host = ''
    _port = 80
    _urlParam = {}
    _req_type = ''
    _data = ''
    _is_inline = "false"
    _is_verbose = "false"
    _write_file = "false"
    _read_file = "false"
    _file1 = ''
    _file2 = ''
    _path = ''
    _headers = {}

    def get_url(self):
        return self._url

    def get_host(self):
        return self._host

    def get_port(self):
        return self._port

    def get_req_type(self):
        return self._req_type

    def get_path(self):
        return self._path

    def set_path(self, my_path):
        self._path = my_path

    def get_headers(self):
        return self._headers

    def get_inline(self):
        return self._is_inline

    def get_data(self):
        return self._data

    def get_read_file(self):
        return self._read_file

    def get_write_file(self):
        return self._write_file

    def get_file1(self):
        return self._file1

    def get_file2(self):
        return self._file2

    def get_is_verbose(self):
        return self._is_verbose

    def set_url(self, my_url):
        self._url = my_url

    def __init__(self, input_command):
        message = input_command.split()
        self._headers["User-Agent"] = socket.gethostname() + "-HTTP/1.0"
        for index in range(len(message)):
            if index == 0:
                if message[index].lower() != "httpc":
                    print("Check your command.\n")
                    raise Exception("Invalid Command")
            if index == 1:
                if message[index].lower() == "get":  # if command contains GET request
                    self._req_type = "GET"
                elif message[index].lower() == "post":  # if command contains POST request
                    self._req_type = "POST"
                else:
                    print("Check your command.\n")
                    raise Exception("Invalid Command")
            if message[index] == "-h":  # if headers option is enabled
                self._headers[message[index + 1].split(":")[0]] = message[index + 1].split(":")[1]  # store headers in \
                # a dictionary
            if message[index] == "-v":  # if verbose option is enabled
                self._is_verbose = "true"
            if message[index] == "-f":  # if file option is enabled
                self._read_file = "true"
                self._file1 = message[index + 1].replace("'", "")
            if message[index] == "-d":  # if inline data option is enabled
                self._is_inline = "true"
                start_of_data = input_command.find("-d")
                start = input_command.find("'", start_of_data)
                end = input_command.find("'", start + 1)
                self._data = input_command[start+1:end]
            if message[index] == "-o":  # if output option is enabled to write body of response to a file
                self._write_file = "true"
                self._file2 = message[index + 1]
            if message[index].startswith("'http://"):  # if string is a url
                self._url = message[index].replace("'", "")
                if self._url.split("/")[2].find(":") != -1:  # if any other port is used, default is 80
                    self._host = self._url.split("/")[2].split(":")[0]
                    self._port = int(self._url.split("/")[2].split(":")[1])
                else:
                    self._host = self._url.split("/")[2]
                if len(self._url.split("/")) > 3:
                    if len(self._url.split("/")[3].split("?")) > 1:  # if url parameters contained in url
                        for param in self._url.split("/")[3].split("?")[1].split("&"):
                            self._urlParam[param.split("=")[0]] = param.split("=")[1]
        self._path = "/"
        if len(self._url.split("/", 3)) > 3:
            self._path += self._url.split("/", 3)[3]

    def convert_to_string(self):
        count = 0;
        params = ''
        for key in self._urlParam:
            ++count
            if count != len(self._urlParam):
                params += "     \"" + key + "\": \"" + self._urlParam[key] + "\",\n"
            else:
                params += "     \"" + key + "\": \"" + self._urlParam[key] + "\"\n  },\n"
        print("{\n" +
              "  \"args\": {\n" +
              params +
              "  \"data\": \"", str(self._data) + "\",\n" +
              "  \"readfile\": {", str(self._file1) + "},\n" +
              "  \"writefile\": {", str(self._file2) + "},\n" +
              "  \"headers\": {\n     ", str(self._headers),
              "\n   },\n",
              "Host: ", str(self._host) + "\n" +
              "URL: ", str(self._url) + "\n" +
              "Port: ", str(self._port) + "\n"
                                          "Request Type: ", str(self._req_type) + "\n" +
              "Is Inline: ", str(self._is_inline) + "\n" +
              "Is Verbose: ", str(self._is_verbose) + "\n" +
              "Write File: ", str(self._write_file) + "\n" +
              "Read File: ", str(self._read_file) + "\n" +
              "Path: ", str(self._path) + "\n"
              )
