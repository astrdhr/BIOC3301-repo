def main():
        filename=input("This program finds lines of letters in qual files (remember to put the filename in quotes):")
        infile=open(filename,'r')
        linelist=[]
        for x, line in enumerate(infile,1):
                        if line[0].isalpha()==True:
                                linelist.append(x)
        infile.close()
        print("List of lines in the file that start with a non-numerical character", linelist)
main()
