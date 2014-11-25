#! /usr/bin/env python

import functions_list as f

x = f.customers()
assert x.addcustomer() == "hello world", "customer != 'hello world'"
