from flask import Flask,render_template,redirect,request
import sqlite3
import random
app = Flask(__name__)

loc=['Bangalore','Mysore','Mangalore','Mumbai','Chennai','Hyderabad','Delhi','Pune']
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin',methods=["GET","POST"])
def admin():
    if request.method == "GET":
        return render_template('admin.html')
"""    elif request.method == "POST":
        name=request.form.get("name")
        #phone_no=request.form.get("phone_no")
        return render_template('adminapp.html', name=name)"""

@app.route('/adminapp',methods=["GET","POST"])
def adminapp():
    """if request.method == "GET":
        name=request.args.get("name")
    
        return render_template('adminapp.html',name=name)
    if request.method == "POST":"""
    name=request.form.get("name")
    
    seat = request.form.get("seat")
    city=request.form.get("city")
    
    
    
    return render_template('adminapp.html', name=name,seat=seat,city=city)
    
@app.route('/reg')
def reg():
    
        try:
            name=request.args.get("name")
            image = request.args.get("image")
            
            
           
            seat=request.args.get("seat")
            city=request.args.get("city")
            
            pid=random.randint(0, 100)
            p=[name,pid,int(seat),city,image]
            #print(p)
            with sqlite3.connect('data.db') as con:
                cur=con.cursor()
                cur.execute("INSERT INTO administrator (place_name,pid,seat,location,image_name) values (?,?,?,?,?)",(name,pid,int(seat),city,image))
               
                con.commit()
               
        except:
            con.rollback()
            
        finally:
            con.close()
            
            return render_template('reg.html')
   
@app.route('/user',methods=["GET","POST"])
def user():
    if request.method == "GET":
        return render_template('user.html')
    elif request.method == "POST":
            name=request.form.get("name")
            return render_template('userapp.html', name=name)
@app.route('/userapp',methods=["GET","POST"])
def userapp():
    if request.method == "GET":
        #loc=['Bangalore','Mysore','Mangalore','Mumbai','Chennai','Hyderabad','Delhi','Pune']
        name= request.args.get("name")
        
    #elif request.method == "POST":
        try:
            with sqlite3.connect('data.db') as con:
                cur=con.cursor()
                cur.execute("SELECT * FROM administrator")
                #a=cur.fetchone()
                b=cur.fetchall()
                #print(b[0][1])
                con.commit()
        except:
            con.rollback()
        finally:
            con.close()
            return render_template('/userapp.html',loc=loc,b=b,name=name)
    elif request.method =="POST":
        place=request.form.get("place")
        print(place)
        
        date= request.form.get("date")
        print(date)
        startTime = request.form.get("start-time")
        print(startTime)
        endTime = request.form.get("end-time")
        print(endTime)
        try:
            with sqlite3.connect('data.db') as con:
                cur=con.cursor()
                
                count= cur.execute("SELECT COUNT(*) FROM users")
                i=0
                temp=False
                error='REGISTERED'
                x=count.fetchone()
                a=x[0]
                print(a)
                #b=cur.fetchall()
                
                while(i<a):
                    b=cur.execute("SELECT * FROM users").fetchall()
                    print(b)
                    while True:
                        if (b[i][1]==place or b[i][2]==date):
                  
                                        
                            print(b[i][3])
                           # if((b[i][3]>=startTime and b[i][3]<=endTime) or (b[i][4]>=startTime and b[i][3]<=endTime) or (b[i][3]<=startTime and b[i][4]>=endTime)):   
                            if(b[i][4]>=startTime and b[i][3]<=endTime):
                                temp=False;
                                break
                            else:
                                temp=True
                                
                                break
                        else:
                            temp=True;
                            break
                    i=i+1
                if(temp==False):
                       error ='CANT REGISTER'
                       
                elif(temp==True):
                    con.execute("INSERT INTO users (place_name,date,start_time,end_time) values (?,?,?,?)",(place,date,startTime,endTime))
                    
                con.commit()
            
        except:
            con.rollback()
        finally:
            con.close()
            return render_template('/end.html', error=error)
if __name__ == '__main__':
    app.run(debug=True)
