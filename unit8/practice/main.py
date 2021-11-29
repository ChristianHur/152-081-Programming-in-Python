"""
MIT License

Copyright (c) 2021 Christian Hur (Gateway Technical College)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

------------
Description:
------------
Write a program that fetch books data from an web API and print out the book information.

API:   http://apollo.gtc.edu/~hurc/152-081/unit8/api/

The api returns information of some books in JSON format.  Display the result in as follows:

Sample Run:
--------
Book 1
--------
isbn: 978-1119498919
title: Python for Everyone
author: Cay Hortsmann
year: 2019
price: $110.00
publisher: Wiley

------- 
Book 2
-------
isbn: 978-1076176035
title: C#: The Ultimate Intermediate Guide to Learn C# Programming Step by Step
author: Ryan Turner
year: 2019
price: $27.99
publisher: Independently published

etc...          
"""

import books
books.main()

