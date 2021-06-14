# RegularExpression
import re

string = 'search this inside of this text please'


def searchInString():
    a = re.search('this', string)
    print(a.span())
    print(a.start())
    print(a.end())


def searchUsingPattern():
    pattern = re.compile("this")
    a = pattern.search(string)
    print(a.group())
    b = pattern.findall(string)
    print(b)


def matching():
    anotherString = 'search this inside now'
    pattern = re.compile("search this")
    c = pattern.fullmatch(anotherString)
    print(c)
    d = pattern.match(anotherString)
    print(d)


if __name__ == '__main__':
    searchInString()
    searchUsingPattern()
    matching()
