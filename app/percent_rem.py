def percentReplacerDict(md):
    keys = md.keys()
    for i in keys:
        if(i!='csrfmiddlewaretoken'):
            string = md[i]
            string=string.replace('%',r'\%')
            string  = string.replace('_',r'\_')
            string  = string.replace('#',r'\#')
            string  = string.replace('$',r'\$')
            string  = string.replace('~',r'\~')
            string  = string.replace('&',r'\&')
            string  = string.replace('^',r'\^')
            string  = string.replace('\\','\\\\')
            string  = string.replace('{',r'\{')
            string  = string.replace('}',r'\}')
            md[i] = string
    return(md)

def percentReplacerString(string):
    string=string.replace('%',r'\%')
    string  = string.replace('_',r'\_')
    string  = string.replace('#',r'\#')
    string  = string.replace('$',r'\$')
    string  = string.replace('~',r'\~')
    string  = string.replace('&',r'\&')
    string  = string.replace('^',r'\^')
    string  = string.replace('\\','\\\\')
    string  = string.replace('{',r'\{')
    string  = string.replace('}',r'\}')
    return(string)


    # PDFGEN_DIR = os.path.join(BASE_DIR,'app')

    # base_file_path = os.path.join(PDFGEN_DIR,"base.txt")
    # #read input file
    # fin = open(str(base_file_path),"rt")
    # #read file contents to string
    # data =fin.read()
    # #replace all occurrences of the required string here % to \%
    # data = data.replace('%', '\\%')
    # #close the input file
    # fin.close()
    
    
    # #open the input file in write mode
    # fin = open("data.txt", "wt")
    # #overrite the input file with the resulting data
    # fin.write(data)
    # #close the file
    # fin.close()
    

