# Proxy-Info-Checker
Takes a file of proxy IP addresses and port numbers in the format of <`10.10.10.10:80`> delimited by newline characters then runs them through `myip.com`'s api. Return information is pertaining to proxies:ports which successfully connected to the api and returned json information containing the attributes of pulic IP and country. Output is printed to the terminal.

### **Instructions**
- From CLI, run:
  ```console
  python proxy_info_checker.py
  ```
  and you will be instructed to enter a filepath to your list of proxies that you would like to check
  
  or
  
- From a python terminal, run:
  
  ```python
  #pass filepath as a parameter
  import proxy_info_checker check
  check.main('./path/to/file.txt')
  ```
  or
  
  ```python
  #let python prompt you for a file
  import proxy_info_checker as check
  check.main()
  ```

  ### **File Format**
  >127.0.0.1:1234
  >127.0.0.1:1234
  >127.0.0.1:1234
  >127.0.0.1:1234
  >127.0.0.1:1234
  >...
