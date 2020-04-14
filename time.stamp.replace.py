# $language = "python"
# $interface = "1.0"
import re,sys,getopt
def main():
    opts,args = getopt.getopt(sys.argv[1:],'hi:o:')
    inputfile=''
    outputfile=''
    for opt,filename in opts:
        if opt=='-i':
            inputfile=filename
    #当未指定output filename时，默认使用原始文件名.edit.txt
    outputfile=inputfile+'.edit.txt'
    f1=open(inputfile,encoding='utf-8')
    f2=open(outputfile,'w+',encoding='utf-8')
    for s in f1.readlines():
        s = re.sub(r'#\d\d:\d\d:\d\d&#      ','',s)
        f2.write(s)
    f1.close()
    f2.close()
    f2=open(outputfile,'r',encoding='utf-8')
    f2.readlines()
main()