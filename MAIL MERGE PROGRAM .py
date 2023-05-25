with open("C:\\Users\\octoj\\OneDrive\\Desktop\\Python programming\\name.txt","r")as name:
    with open("C:\\Users\\octoj\\OneDrive\\Desktop\\Python programming\\body.txt","r")as body:
        b = body.read(5)
        b1 = body.read()
        for n in name:
            mail = b+" "+n.strip()+b1
            with open("C:\\Users\\octoj\\OneDrive\\Desktop\\Python programming\\"+n.strip()+".txt","w") as m_file:
                m_file.write(mail)