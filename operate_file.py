#operate_file.py
#对文件的操作
#需要注意的方法有open、join、split、index、readline、readlines、writelines
def main():
    infile1=open("C:/Users/马克/Desktop/姓名-电话.txt","rb")
    infile2=open("C:/Users/马克/Desktop/姓名-邮箱.txt","rb")
    infile1.readline()
    infile2.readline()
    content1=infile1.readlines()
    content2=infile2.readlines()

    name1=[]
    name2=[]
    tele=[]
    email=[]

    for content in content1:
        element=content.split()
        name1.append(str(element[0].decode("gbk")))
        tele.append(str(element[1].decode("gbk")))
    for content in content2:
        element=content.split()
        name2.append(str(element[0].decode("gbk")))
        email.append(str(element[1].decode("gbk")))

    content=[]
    content.append("姓名\t电话\t邮箱\n")

    for i in range(len(name1)):
        s=""
        if name1[i] in name2:
            j=name2.index(name1[i])
            s="\t".join([name1[i],tele[i],email[j]])
            s+="\n"
        else:
            s="\t".join([name1[i],tele[i],str("----")])
            s+="\n"
        content.append(s)

    for i in range(len(name2)):
        s=""
        if name2[i] not in name1:
            s="\t".join([name2[i],str("---"),email[i]])
            s+="\n"
        content.append(s)
        
    outfile=open("C:/Users/马克/Desktop/姓名-电话-邮箱.txt","w")
    outfile.writelines(content)
    infile1.close()
    infile2.close()
    outfile.close()
main()
