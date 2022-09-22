from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
import MySQLdb

db=MySQLdb.connect("localhost","root","","dbassembleurpc")
c=db.cursor()

######################################################################
#                           LOAD INDEX PAGE
######################################################################
def index(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"index.html")
######################################################################
#                           LOGIN
######################################################################
def login(request):
    """ 
        The function to load index page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        email=request.POST.get("txtEmail")
        pwd=request.POST.get("txtPassword")
        s="select count(*) from tbllogin where username='"+email+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            s="select * from tbllogin where username='"+email+"'"
            c.execute(s)
            i=c.fetchone()
            if(i[1]==pwd):
                request.session['email'] = email
                if(i[3]=="1"):
                    if(i[2]=="admin"):
                        return HttpResponseRedirect("/adminhome")
                    elif(i[2]=="customer"):
                        return HttpResponseRedirect("/customerhome")
                    elif(i[2]=="courier"):
                        return HttpResponseRedirect("/courierhome")
                else:
                    msg="You are not authenticated to login"
            else:
                msg="Incorrect password"
        else:
            msg="User doesnt exist"
    return render(request,"commonlogin.html",{"msg":msg})
######################################################################
#                      REGISTRATION
######################################################################
def register(request):
    """ 
        The function to load customer registration page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        pwd=request.POST["txtPassword"]
        s="insert into tblregistration (uName,uAddress,uContact,uEmail) values('"+name+"','"+address+"','"+contact+"','"+email+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry registration error"
        else:
            s="insert into tbllogin (username,password,utype,status) values('"+email+"','"+pwd+"','customer','1')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry login error"
            else:
                msg="Registration successfull"
    return render(request,"commonregister.html",{"msg":msg})
######################################################################
#                      COURIER REGISTRATION
######################################################################
def courier(request):
    """ 
        The function to load courier registration page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        pwd=request.POST["txtPassword"]
        s="insert into tblcourier (crName,crAddress,crContact,crEmail) values('"+name+"','"+address+"','"+contact+"','"+email+"')"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry registration error"
        else:
            s="insert into tbllogin (username,password,utype,status) values('"+email+"','"+pwd+"','courier','0')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry login error"
            else:
                msg="Registration successfull"
    return render(request,"courier.html",{"msg":msg})
######################################################################
#                                                                    #
#                                                                    #
#                           ADMIN                                    #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                           LOAD ADMIN PAGE
######################################################################
def adminhome(request):
    """ 
        The function to load admin home page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    return render(request,"adminhome.html")
######################################################################
#                           CATEGORY
######################################################################
def admincategory(request):
    """ 
        The function to load category page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        cat=request.POST["txtCategory"]
        s="select count(*) from tblcategory where catName='"+cat+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Data already exist"
        else:
            s="insert into tblcategory (catName,catStatus) values('"+cat+"','1')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Data added successfully"
    data=loadcategory
    return render(request,"admincategory.html",{"msg":msg,"data":data})
def loadcategory():
    """ 
        The function to load category
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tblcategory where catStatus='1'"
    c.execute(s)
    data=c.fetchall()
    return data
######################################################################
#                           BRAND
######################################################################
def adminbrand(request):
    """ 
        The function to load brand page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        cat=request.POST["txtCategory"]
        s="select count(*) from tblbrand where brandName='"+cat+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Data already exist"
        else:
            s="insert into tblbrand (brandName,brandStatus) values('"+cat+"','1')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Data added successfully"
    data=loadbrand
    return render(request,"adminbrand.html",{"msg":msg,"data":data})
def loadbrand():
    """ 
        The function to load brand 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tblbrand where brandStatus='1'"
    c.execute(s)
    data=c.fetchall()
    return data
######################################################################
#                           DELETE BRAND
######################################################################
def adminbranddelete(request):
    """ 
        The function to delete brand
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    bid=request.GET.get("id")
    s="update tblbrand set brandStatus='0' where brandId='"+bid+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/adminbrand")
######################################################################
#                           ADMIN COURIER
######################################################################
def admincourier(request):
    """ 
        The function to load courier details
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select tblcourier.*,tbllogin.status from tblcourier,tbllogin where tblcourier.crEmail=tbllogin.username and tbllogin.status<>'-1'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"admincourier.html",{"data":data})
######################################################################
#                           ADMIN UPDATE USER
######################################################################
def adminupdateuser(request):
    """ 
        The function to update user
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.GET.get("id")
    status=request.GET.get("status")
    s="update tbllogin set status='"+status+"' where username='"+email+"'"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/admincourier")
######################################################################
#                           RAM
######################################################################
def adminram(request):
    """ 
        The function to load ram page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        ram=request.POST["txtRam"]
        size=request.POST["txtSize"]
        speed=request.POST["txtSpeed"]
        speciality=request.POST["txtSpeciality"]
        bid=request.POST["brand"]
        rate=request.POST["txtRate"]
        s="select count(*) from tblRam where name='"+ram+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Data already exist"
        else:
            s="insert into tblram (name,size,speed,speciality,bid,rate) values('"+ram+"','"+size+"','"+speed+"','"+speciality+"','"+bid+"','"+rate+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Data added successfully"
    data=loadram()
    s="select * from tblbrand where brandStatus='1'"
    c.execute(s)
    brand=c.fetchall()
    return render(request,"adminram.html",{"msg":msg,"data":data,"brand":brand})
def loadram():
    """ 
    The function to load ram 
    -----------------------------------------------
    Parameters: 
        HTTP request 
          
    Returns: 
            tml page
    """
    s="select tblram.*,tblbrand.brandName from tblram,tblbrand where tblbrand.brandId=tblram.bid"
    c.execute(s)
    data=c.fetchall()
    return data
######################################################################
#                           DISPLAY
######################################################################
def admindisplay(request):
    """ 
        The function to load display page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        ram=request.POST["txtRam"]
        size=request.POST["txtSize"]
        speed=request.POST["txtSpeed"]
        panel=request.POST["txtPanel"]
        speciality=request.POST["txtSpeciality"]
        bid=request.POST["brand"]
        rate=request.POST["txtRate"]
        s="select count(*) from tblRam where name='"+ram+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Data already exist"
        else:
            s="insert into tbldisplay (name,size,resolution,panel,speciality,bid,rate) values('"+ram+"','"+size+"','"+speed+"','"+panel+"','"+speciality+"','"+bid+"','"+rate+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Data added successfully"
    data=loaddisplay()
    s="select * from tblbrand where brandStatus='1'"
    c.execute(s)
    brand=c.fetchall()
    return render(request,"admindisplay.html",{"msg":msg,"data":data,"brand":brand})

def loaddisplay():
    """ 
    The function to load display 
    -----------------------------------------------
    Parameters: 
        HTTP request 
          
    Returns: 
            tml page
    """
    s="select tbldisplay.*,tblbrand.brandName from tbldisplay,tblbrand where tblbrand.brandId=tbldisplay.bid"
    c.execute(s)
    data=c.fetchall()
    return data
######################################################################
#                           HDD
######################################################################
def adminhdd(request):
    """ 
        The function to load hdd page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        ram=request.POST["txtRam"]
        size=request.POST["txtSize"]
        speed=request.POST["txtSpeed"]
        speciality=request.POST["txtSpeciality"]
        bid=request.POST["brand"]
        rate=request.POST["txtRate"]
        s="select count(*) from tblRam where name='"+ram+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Data already exist"
        else:
            s="insert into tblhdd (name,capacity,speed,speciality,bid,rate) values('"+ram+"','"+size+"','"+speed+"','"+speciality+"','"+bid+"','"+rate+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Data added successfully"
    data=loadhdd()
    s="select * from tblbrand where brandStatus='1'"
    c.execute(s)
    brand=c.fetchall()
    return render(request,"adminhdd.html",{"msg":msg,"data":data,"brand":brand})
def loadhdd():
    """ 
    The function to load hdd 
    -----------------------------------------------
    Parameters: 
        HTTP request 
          
    Returns: 
            tml page
    """
    s="select tblhdd.*,tblbrand.brandName from tblhdd,tblbrand where tblbrand.brandId=tblhdd.bid"
    c.execute(s)
    data=c.fetchall()
    return data
######################################################################
#                           PROCESSOR
######################################################################
def adminprocessor(request):
    """ 
        The function to load processor page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        ram=request.POST["txtRam"]
        size=request.POST["txtSize"]
        speed=request.POST["txtSpeed"]
        speciality=request.POST["txtSpeciality"]
        bid=request.POST["brand"]
        rate=request.POST["txtRate"]
        s="select count(*) from tblRam where name='"+ram+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Data already exist"
        else:
            s="insert into tblprocessor (name,cache,speed,speciality,bid,rate) values('"+ram+"','"+size+"','"+speed+"','"+speciality+"','"+bid+"','"+rate+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Data added successfully"
    data=loadprocessor()
    s="select * from tblbrand where brandStatus='1'"
    c.execute(s)
    brand=c.fetchall()
    return render(request,"adminprocessor.html",{"msg":msg,"data":data,"brand":brand})
def loadprocessor():
    """ 
    The function to load processor 
    -----------------------------------------------
    Parameters: 
        HTTP request 
          
    Returns: 
            tml page
    """
    s="select tblprocessor.*,tblbrand.brandName from tblprocessor,tblbrand where tblbrand.brandId=tblprocessor.bid"
    c.execute(s)
    data=c.fetchall()
    return data


######################################################################
#                           PRODUCT
######################################################################
def adminproduct(request):
    """ 
        The function to load phone page of the project. 
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    if(request.POST):
        name=request.POST["txtName"]
        desc=request.POST["txtDesc"]
        catid=request.POST["category"]
        speciality=request.POST["txtSpeciality"]
        
        img=request.FILES["txtFile"]
        fs=FileSystemStorage()
        filename=fs.save(img.name,img)
        uploaded_file_url=fs.url(filename)

        rate=request.POST["txtRate"]
        s="select count(*) from tblproducts where name='"+name+"'"
        c.execute(s)
        i=c.fetchone()
        if(i[0]>0):
            msg="Data already exist"
        else:
            s="insert into tblproducts (name,description,catId,speciality,img,rate) values('"+name+"','"+desc+"','"+catid+"','"+speciality+"','"+uploaded_file_url+"','"+rate+"')"
            try:
                c.execute(s)
                db.commit()
            except:
                msg="Sorry some error occured"
            else:
                msg="Data added successfully"
    data=loadproduct()
    s="select * from tblcategory where catStatus='1'"
    c.execute(s)
    brand=c.fetchall()
    return render(request,"adminproduct.html",{"msg":msg,"data":data,"category":brand})
def loadproduct():
    """ 
    The function to load product 
    -----------------------------------------------
    Parameters: 
        HTTP request 
          
    Returns: 
            tml page
    """
    s="select * from tblproducts"
    c.execute(s)
    data=c.fetchall()
    return data

######################################################################
#                      ORDER
######################################################################
def adminorder(request):
    """ 
        The function to load order
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """

    s="select tblassemble.asId,tbldisplay.name,tblprocessor.name,tblhdd.name,tblram.name,tblassemble.total,tblregistration.uName,tblassemble.odate,tblassemble.status from tblassemble,tbldisplay,tblprocessor,tblram,tblhdd,tblregistration where tblassemble.disId=tbldisplay.dsId and tblassemble.hddId=tblhdd.hId and tblassemble.ramId=tblram.rId and tblassemble.proId=tblprocessor.proId  and tblregistration.uEmail=tblassemble.cEmail "
    c.execute(s)
    data=c.fetchall()
    s="select tblcart.*,tblproducts.*,tblregistration.uName from tblcart,tblproducts,tblregistration where tblcart.pid=tblproducts.pId and tblcart.email=tblregistration.uEmail "
    c.execute(s)
    data1=c.fetchall()
    return render(request,"adminorder.html",{"data":data,"order":data1})
######################################################################
#                      SELECT COURIER
######################################################################
def adminselectcourier(request):
    """ 
        The function to select courier
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    id=request.GET.get("id")
    request.session["oid"]=id
    s="select * from tblcourier where crEmail in(select username from tbllogin where status='1')"
    c.execute(s)
    data=c.fetchall()
    return render(request,"adminselectcourier.html",{"data":data})
######################################################################
#                      UPDATE ORDER
######################################################################
def adminupdateorder(request):
    """ 
        The function to load order
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    if(request.GET):
        id=request.GET.get("id")
        order=request.GET.get("order")
        if order=="assemble":
            s="update tblassemble set status='delivered' where asId='"+id+"'"
        elif order=="order":
            s="update tblcart set status='delivered' where cartId='"+id+"'"
        c.execute(s)
        db.commit()
        return HttpResponseRedirect("/adminorder")
######################################################################
#                                                                    #
#                                                                    #
#                           COURIER                                #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                      COURIER HOME
######################################################################
def courierhome(request):
    """ 
        The function to load courier home page
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        s="update tblcourier set crName='"+name+"',crAddress='"+address+"',crContact='"+contact+"' where crEmail='"+email+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry registration error"
        else:
            msg="Updation successfull"
    s="select * from tblcourier where crEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"courierhome.html",{"msg":msg,"data":data})
######################################################################
#                      ORDER
######################################################################
def courierorder(request):
    """ 
        The function to load order
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblassemble.asId,tbldisplay.name,tblprocessor.name,tblhdd.name,tblram.name,tblassemble.total,tblregistration.uName,tblassemble.odate,tblassemble.status from tblassemble,tbldisplay,tblprocessor,tblram,tblhdd,tblregistration,tblassign where tblassign.asId=tblassemble.asId and tblassign.crEmail='"+email+"' and tblassemble.disId=tbldisplay.dsId and tblassemble.hddId=tblhdd.hId and tblassemble.ramId=tblram.rId and tblassemble.proId=tblprocessor.proId  and tblregistration.uEmail=tblassemble.cEmail "
    c.execute(s)
    data=c.fetchall()
    # s="select tblassemble.asId,tbldisplay.name,tblprocessor.name,tblhdd.name,tblram.name,tblassemble.total,tblregistration.uName,tblassemble.odate,tblassemble.status from tblassemble,tbldisplay,tblprocessor,tblram,tblhdd,tblregistration where tblassemble.disId=tbldisplay.dsId and tblassemble.hddId=tblhdd.hId and tblassemble.ramId=tblram.rId and tblassemble.proId=tblprocessor.proId  and tblregistration.uEmail=tblassemble.cEmail and tblassemble.status='delivered'"
    # c.execute(s)
    # data1=c.fetchall()
    return render(request,"courierorder.html",{"data":data})
######################################################################
#                      ORDER
######################################################################
def courierupdate(request):
    """ 
        The function to load order
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    id=request.session["oid"]
    if(request.POST):
        status=request.POST["status"]
        s="update tblassemble set status='"+status+"' where asId='"+id+"'"
        c.execute(s)
        db.commit()
        return HttpResponseRedirect("/courierorder")
    return render(request,"courierupdate.html")
######################################################################
#                                                                    #
#                                                                    #
#                           CCUSTOMER                                #
#                                                                    #
#                                                                    #
######################################################################
######################################################################
#                      CUSTOMER HOME
######################################################################
def customerhome(request):
    """ 
        The function to load vustomer home page
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    msg=""
    email=request.session["email"]
    if(request.POST):
        name=request.POST["txtName"]
        address=request.POST["txtAddress"]
        contact=request.POST["txtContact"]
        email=request.POST["txtEmail"]
        s="update tblregistration set uName='"+name+"',uAddress='"+address+"',uContact='"+contact+"' where uEmail='"+email+"'"
        try:
            c.execute(s)
            db.commit()
        except:
            msg="Sorry registration error"
        else:
            msg="Updation successfull"
    s="select * from tblregistration where uEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    return render(request,"customerhome.html",{"msg":msg,"data":data})
######################################################################
#                      CUSTOMER REQUIREMENT
######################################################################
def customerreq(request):
    """ 
        The function to load customer requirement
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    s="select * from tblcategory"
    c.execute(s)
    data=c.fetchall()
    if(request.POST):
        cat=request.POST["category"]
        req=request.POST["txtSpeciality"]
        request.session["req"]=req
        if cat=="1":
            return HttpResponseRedirect("/customerdisplay")
        else:
            return HttpResponseRedirect("/customerproduct")
    return render(request,"customerreq.html",{"category":data})
######################################################################
#                      CUSTOMER PRODUCT
######################################################################
def customerproduct(request):
        """ 
        The function to load customer product
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
        """
    
        req=request.session["req"]
        s="select * from tblproducts where speciality='"+req+"'"
        c.execute(s)
        data=c.fetchall()
        # display=request.GET.get("id")
        # request.session["display"]=display
        # return HttpResponseRedirect("/customerhdd")
        return render(request,"customerproduct.html",{"data":data})
######################################################################
#                      CUSTOMER CART
######################################################################
def addtocart(request):
    email=request.session['email']
    pid=request.GET.get('id')
    s="insert into tblcart(email,pid,odate,status) values('"+email+"','"+pid+"',(select sysdate()),'ordered')"
    c.execute(s)
    db.commit()
    return HttpResponseRedirect("/customercat1")
def customercart1(request):
    email=request.session['email']
    s="select tblproducts.*,tblcart.* from tblproducts,tblcart where tblproducts.pId=tblcart.pid and tblcart.email='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    if request.POST:
        return HttpResponseRedirect("/payment")
    return render (request,"customercart1.html",{"data":data})
######################################################################
#                      CUSTOMER DISPLAY
######################################################################
def customerdisplay(request):
        """ 
        The function to load customer display
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
        """
    
        req=request.session["req"]
        s="select * from tbldisplay where speciality='"+req+"'"
        c.execute(s)
        data=c.fetchall()
        # display=request.GET.get("id")
        # request.session["display"]=display
        # return HttpResponseRedirect("/customerhdd")
        return render(request,"customerdisplay.html",{"data":data})
######################################################################
#                      CUSTOMER HDD
######################################################################
def customerhdd(request):
        """ 
        The function to load customer hdd
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
        """

        display=request.GET.get("id")
        request.session["display"]=display
        req=request.session["req"]
        s="select * from tblhdd where speciality='"+req+"'"
        c.execute(s)
        data=c.fetchall()
        # hdd=request.GET.get("id")
        # request.session["hdd"]=hdd
        # return HttpResponseRedirect("/customerram")
        return render(request,"customerhdd.html",{"data":data})
######################################################################
#                      CUSTOMER RAM
######################################################################
def customerram(request):
        """ 
        The function to load customer ram
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
        """

        hdd=request.GET.get("id")
        request.session["hdd"]=hdd
        req=request.session["req"]
        s="select * from tblram where speciality='"+req+"'"
        c.execute(s)
        data=c.fetchall()
        # ram=request.GET.get("id")
        # request.session["ram"]=ram
        # return HttpResponseRedirect("/customerprocessor")
        return render(request,"customerram.html",{"data":data})
######################################################################
#                      CUSTOMER PROCESSOR
######################################################################
def customerprocessor(request):
        """ 
        The function to load customer processor
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
        """

        ram=request.GET.get("id")
        request.session["ram"]=ram
        req=request.session["req"]
        s="select * from tblprocessor where speciality='"+req+"'"
        c.execute(s)
        data=c.fetchall()       
        return render(request,"customerprocessor.html",{"data":data})
######################################################################
#                      CUSTOMER SELECT PROCESSOR
######################################################################
def customerslctpro(request):
    """ 
        The function to load selected items
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
    """
    if(request.GET):
        req=request.session["req"]
        email=request.session["email"]


        processor=request.GET.get("id")
        s="select rate from tblprocessor where proId='"+processor+"'"
        c.execute(s)
        i=c.fetchone()
        prorate=i[0]

        display=request.session["display"]
        s="select rate from tbldisplay where dsId='"+display+"'"
        c.execute(s)
        i=c.fetchone()
        disrate=i[0]

        hdd=request.session["hdd"]
        s="select rate from tblhdd where hId='"+hdd+"'"
        c.execute(s)
        i=c.fetchone()
        hddrate=i[0]

        ram=request.session["ram"]
        s="select rate from tblram where rId='"+ram+"'"
        c.execute(s)
        i=c.fetchone()
        ramrate=i[0]

        total=prorate+disrate+hddrate+ramrate

        s="insert into tblassemble(cEmail,req,disId,hddId,proId,ramId,total,status,odate) values('"+email+"','"+str(req)+"','"+str(display)+"','"+str(hdd)+"','"+str(processor)+"','"+str(ram)+"','"+str(total)+"','ordered',(select sysdate()))"
        c.execute(s)
        db.commit()
        return HttpResponseRedirect("/customerassemble")
######################################################################
#                      CUSTOMER ASSEMBLE
######################################################################
def customerassemble(request):
    """ 
        The function to load selected items
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
         
    s="select max(asId) from tblassemble"
    c.execute(s)
    i=c.fetchone()
    asId=i[0]

    s="select tblassemble.asId,tbldisplay.name,tbldisplay.rate,tblprocessor.name,tblprocessor.rate,tblhdd.name,tblhdd.rate,tblram.name,tblram.rate,tblassemble.total,tblassemble.odate from tblassemble,tbldisplay,tblprocessor,tblram,tblhdd where tblassemble.disId=tbldisplay.dsId and tblassemble.hddId=tblhdd.hId and tblassemble.ramId=tblram.rId and tblassemble.proId=tblprocessor.proId and tblassemble.asId='"+str(asId)+"'"
    c.execute(s)
    data=c.fetchall()
    if 'pay' in request.POST:
        return HttpResponseRedirect("/payment")
    if 'cart' in request.POST:
        c.execute("update tblassemble set status='in cart' where asId='"+str(asId)+"'")
        db.commit()
        return HttpResponseRedirect("/customercart")
    return render(request,"customerassemble.html",{"data":data})

######################################################################
#                      CUSTOMER CART
######################################################################
def customercart(request):
    """ 
        The function to load cart
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblassemble.asId,tbldisplay.name,tblprocessor.name,tblhdd.name,tblram.name,tblassemble.total,tblassemble.odate from tblassemble,tbldisplay,tblprocessor,tblram,tblhdd where tblassemble.disId=tbldisplay.dsId and tblassemble.hddId=tblhdd.hId and tblassemble.ramId=tblram.rId and tblassemble.proId=tblprocessor.proId and tblassemble.status='in cart' and tblassemble.cEmail='"+email+"'"
    c.execute(s)
    data=c.fetchall()
    s="select sum(total) from tblassemble where cEmail='"+email+"' and status='in cart'"
    c.execute(s)
    i=c.fetchone()
    amt=i[0]
    if 'pay' in request.POST:
        for d in data:
            s="update tblassemble set status='ordered' where asId='"+str(d[0])+"'"
            c.execute(s)
        db.commit()
        return HttpResponseRedirect("/payment")
    return render(request,"customercart.html",{"data":data,"amt":amt})

######################################################################
#                      PAYMENT
######################################################################    
import webbrowser
def sendsms(ph,msg):
    sendToPhoneNumber= "+91"+ph
    url = "http://sms.mdsmedia.in/http-api.php?username=7000183&password=LCCCOK123&senderid=LCCCOK&route=23&number="+sendToPhoneNumber+"&message="+msg
    # contents = urllib.request.urlopen(url)
    webbrowser.open(url)
######################################################################
#                      PAYMENT
######################################################################
def payment(request):
    """ 
        The function to load payment
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    if(request.POST):
        num=request.POST["txtPhone"]
        card=request.POST["txtcardno"]
        import random
        pin=random.randint(1000,9999)
        request.session['ppin']=pin
        msg="Thank you for making online transaction with your card xxxx xxxx xxxx "+str(card[-4:])+". Your pin is "+str(pin)+". Please don't share your pin."
        sendsms(num,msg)
        return HttpResponseRedirect("/pin?i="+str(pin))
    return render(request,"payment.html") 
######################################################################
#                      PIN
######################################################################
def pin(request):
    """ 
        The function to load payment
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    ppin=request.session['ppin']
    ppin=request.GET.get("i")
    if(request.POST):
        pin=request.POST["pin"]
        
        if(pin==ppin):
            return HttpResponseRedirect("/customerassembleorder")
    return render(request,"pin.html") 
######################################################################
#                      ASSEMBLED ORDER
######################################################################
def customerassembleorder(request):
    """ 
        The function to load payment
        -----------------------------------------------
        Parameters: 
            HTTP request 
          
        Returns: 
            html page
    """
    email=request.session["email"]
    s="select tblassemble.asId,tbldisplay.name,tblprocessor.name,tblhdd.name,tblram.name,tblassemble.total,tblassemble.status from tblassemble,tbldisplay,tblprocessor,tblram,tblhdd where tblassemble.disId=tbldisplay.dsId and tblassemble.hddId=tblhdd.hId and tblassemble.ramId=tblram.rId and tblassemble.proId=tblprocessor.proId and tblassemble.cEmail='"+email+"' and tblassemble.status<>'in cart'"
    c.execute(s)
    data=c.fetchall()
    s="select tblcart.*,tblproducts.* from tblcart,tblproducts where tblcart.pid=tblproducts.pId and tblcart.email='"+email+"'"
    c.execute(s)
    order=c.fetchall()
    return render(request,"customerassembleorder.html",{"data":data,"order":order}) 