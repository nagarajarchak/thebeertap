from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template

app = Flask(__name__)

@app.route('/')
def index():
  #context = { 'prediction': pred, 'filename': filename }
  return render_template('index.html')

@app.route('/shotsmaxima')
def shots():
  return render_template('shots.html')

@app.route('/soberup')
def sober():
  return render_template('sober.html')

@app.route('/calculateshots', methods=["GET", "POST"])
def calculateshots():
  
  gender = request.form['Gender']
  weight = request.form['Weight']

  if gender in ["M","m", "Male","male"] and weight != "":
    weight = float(weight)
    shotsnum = round(3*0.68*weight/7,1)
 
  elif gender in ["F","f", "Female","female"] and weight != "":
    weight = float(weight)
    shotsnum = round(3*0.55*weight/7,1)
 
  else:
    weight = request.form['Weight']
    if gender == "" or weight == "":
      errormsg = "Please enter values for weight & gender."
      shots = "shots-maxima"
      shotsurl = "shots"
      context = { 'error': errormsg, 'shots': shots, 'shotsurl': shotsurl }
    else:
      errormsg = "Please enter a valid gender value. (Male / Female)."
      shots = "shots-maxima"
      shotsurl = "shots"
      context = { 'error': errormsg, 'shots': shots, 'shotsurl': shotsurl }

    return render_template('error.html',**context)

  shots = "shots-maxima"
  shotsurl = "shots"
  context = { 'shotsnum': shotsnum, 'shots': shots, 'shotsurl': shotsurl }
  return render_template('calcshots.html',**context)

@app.route('/calculatesober', methods=["GET", "POST"])
def calculatesober():
  
  gender = request.form['Gender']
  weight = request.form['Weight']
  beer = request.form['Beer']
  wine = request.form['Wine']
  shots = request.form['Shots']

  if beer == "":
    beer = 0
  
  if wine == "":
    wine = 0
  
  if shots == "":
    shots = 0
  

  if gender in ["M","m", "Male","male"] and weight != "":
    
    weight = float(weight)

    if beer == "" and wine == "" and shots == "":
      errormsg = "You're already sober!"
      sober = "sober-up"
      context = { 'error': errormsg, 'sober': sober }

      return render_template('errorsober.html',**context)
    
    elif beer == 0 and wine == 0 and shots == 0:
      errormsg = "You're already sober!"
      sober = "sober-up"
      context = { 'error': errormsg, 'sober': sober }

      return render_template('errorsober.html',**context)

    else:
      beer = float(beer)
      wine = float(wine)
      shots = float(shots)
      sobertime = round((280*(1.5*shots + 12*beer + 5*wine) / (3*0.68*weight) -2),1)
      sobertime = round(sobertime/60,1)
 
  elif gender in ["F","f", "Female","female"] and weight != "":
    
    weight = float(weight)

    if beer == "" and wine == "" and shots == "":
      errormsg = "You're already sober!"
      sober = "sober-up"
      context = { 'error': errormsg, 'sober': sober }

      return render_template('errorsober.html',**context)
    
    elif beer == 0 and wine == 0 and shots == 0:
      errormsg = "You're already sober!"
      sober = "sober-up"
      context = { 'error': errormsg, 'sober': sober }

      return render_template('errorsober.html',**context)

    else:
      beer = float(beer)
      wine = float(wine)
      shots = float(shots)
      sobertime = round((280*(1.5*shots + 12*beer + 5*wine) / (3*0.55*weight) -2),1)
      sobertime = round(sobertime/60,1)
 
  else:
    weight = request.form['Weight']
    beer = request.form['Beer']
    wine = request.form['Wine']
    shots = request.form['Shots']
    if gender == "" or weight == "" or beer == "" or wine == "" or shots == "":
      errormsg = "Please fill all blanks."
      sober = "sober-up"
      context = { 'error': errormsg, 'sober': sober }
    else:
      errormsg = "Please enter a valid gender value. (Male / Female)."
      sober = "sober-up"
      context = { 'error': errormsg, 'sober': sober }

    return render_template('errorsober.html',**context)
 
  sober = "sober-up"
  context = { 'sobertime': sobertime, 'sober': sober }
  return render_template('calcsober.html',**context)

app.run(debug=True, host='localhost', port=8080)