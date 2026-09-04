from flask import Flask,request,render_template
from deep_translator import GoogleTranslator

app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    telugu_text=''
    tamil_text=''
    error=''
    if request.method=='POST':
        telugu_text=request.form.get('telugu_text','').split()
        if telugu_text:
            try:
                translator=GoogleTranslator(
                    source="te",
                    target="ta"
                )
                tamil_text=translator.translate(telugu_text)
            except Exception as e:
                error="Translator failed.Please try again"
        else:
            error="Please enter Telugu text"
    return render_template("index.html",telugu_text=telugu_text,tamil_text=tamil_text,error=error)

if __name__=='__main__':
    app.run(debug=True)