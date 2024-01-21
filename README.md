# Proxy-Info-Checker
Takes a file of proxy IP addresses and port numbers in the format of <`10.10.10.10:80`> delimited by newline characters then runs them through `myip.com`'s api. Return information is pertaining to proxies:ports which successfully connected to the api and returned json information containing their attributes such as pulic IP and country. Output is printed to the terminal.
