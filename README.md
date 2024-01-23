# Proxy-Info-Checker
Retrieve information pertaining to proxy servers
#### *Type: Terminal Application*

### Description:
>Takes a file of proxy IP addresses and port numbers in the format of <`10.10.10.10:80`> delimited by newline characters then runs them through `myip.com`'s api. Return information is pertaining to proxies:ports which successfully connected to the api and returned json information containing the attributes of pulic IP and country. Output is printed to the terminal.


## **Instructions:**
#### Dowload
- Using CLI navigate to the directory in which you wish to install the application and run:
  ```console
  git clone https://github.com/Node0o1/Proxy-Info-Checker.git
  ```

#### Setup
- Using the CLI, navigate to the folder containing the requirements.txt file and install the file using Python's pip:
  ```console
  python -m pip install requirements.txt
  ``` 
  
#### Run
- From CLI, run:
  ```console
  python proxy_info_checker.py ./path/to/file.txt
  ```
  if the file is omitted, you will be instructed to enter a file.
  
  or
  
- From a python terminal, run:
  ```python
  #pass filepath as a parameter
  import proxy_info_checker as P
  P.check_list('./path/to/file.txt')
  ```
  
  or
  ```python
  #let python prompt you for a file
  import proxy_info_checker as P
  P.check_list()
  ```

- Alternatively, you can check a single proxy:port using a Python terminal and  running:
  ```python
  #replace 127.0.0.1 with the proxy and port you are testing
  import proxy_info_checker as P
  P.check(127.0.0.1:1234)
  ```

## **File Format:**
```
127.0.0.1:1234
127.0.0.1:1234
127.0.0.1:1234
127.0.0.1:1234
127.0.0.1:1234
...
```
