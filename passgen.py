def main():
 while True:
  keyword= input('Enter a keyword: ')
  print (str(keyword) + "\r")
  cn = 0
  namesm = ""
  names = ""
  namesm = namesm + str(keyword) + "\n"
  names = names + str(keyword) + "\n"
  while cn < 10001 :
   if cn < 3001 :
    namesm = namesm + str(keyword) + str(cn) + "\n"
    names = names + str(keyword) + str(cn) + "\n"
   cn += 1
  print ("---------- Done")
  text_file = open("passlist_small.txt","a")
  text_file.write(namesm)
  text_file.close()
  text_file = open("passlist_large.txt","a")
  text_file.write(names)
  text_file.close()
main()