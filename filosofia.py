import urllib.request as urllib2
import urllib.error as error
import os
for i in range(291):
    if(i > 2) and (i != 213):
        try:
            url = "http://www.filosofia.com.br/figuras/livros_inteiros/" + str(i) + ".txt"
            response = urllib2.urlopen(url)
            data = response.read()
            filename = str(i) + ".txt"
            file_ = open(filename, 'wb')
            file_.write(data)
            file_.close()

            file_ = open(filename, 'r')
            filename_ = file_.readline().strip( ).rstrip("\n") + ".txt"
            file_.close()
            os.remove(filename)

            file_ = open(filename_, 'wb')
            file_.write(data)
            file_.close()

            print(str(i) + " - " + filename_)
        except error.HTTPError:
            pass