from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


# App config.
DEBUG = True
app = Flask(__name__,static_url_path='/static')
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class ReusableForm(Form):
    name = TextField('Query:', validators=[validators.required()])
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print(form.errors)
    if request.method == 'POST':
        #query = request.form['name']
        final_output=""
        user_input=request.form['name']
        sents = sent_tokenize(user_input)
        word_sent = word_tokenize(user_input.lower())
        _stopwords = set(stopwords.words('english') + list(punctuation))
        user_input_words=[word for word in word_sent if word not in _stopwords]
        user_input_words=[stemmer.stem(i) for i in user_input_words]
        user_input_words=[i for i in user_input_words if (i in new_bag and i not in ('health','claim','want','know','cover','elig','insur','plan'))]
        
        
        key_section={}
        for i in user_input_words:
            temp=[]
            for key,val in d_stem.items(): 
                if i in val:
                    temp.append(key)
            key_section[i]=set(temp)
        
        
        if len(key_section.keys())!=0:    
            final_cmn_section= list(set.intersection(*map(set,key_section.values())))
#            print("Parents are-- \n",final_cmn_section)
            final_output+=find_parent_data(final_cmn_section,user_input_words)   
        
            
            soupTable= BeautifulSoup(html,'html.parser')
            
            trows = soupTable.find_all('tr')
            
            if len(final_cmn_section)==0:
                final_output+="our customer representative will contact you shortly"
                
            else:
                for i in final_cmn_section:
                    temp=i.split()
                    if len(temp)>=3:
                        temp=" ".join(temp[0:3])
                    else:
                        temp=i
                    
                    for tr in trows:
                        
                        if "See" in tr.text and temp.strip() in tr.text:
                            continue
                            
                        elif temp.strip() in tr.text and ("Coinsurance" in tr.text or "Copayment" in tr.text):
                            final_output+="<br><h4>"+"Coinsurance/Copayment details of : "+i.strip()+"</h4>"
                            section_tr=tr
#                            print(section_tr.text)
                            final_output+=section_tr.prettify()
                            
        else:
            final_output+="our customer representative will contact you shortly"
            
        #print(name)
		
        if form.validate():
            # Save the comment here.
            output = final_output
#            for i in range(0, len(final_output)):
#                output = output + final_output[i] + '\n'		
            flash(user_input)
            flash(output)			
        else:
            flash('All the form fields are required. ')
	
    return render_template('anthem_poc_template.html', form=form)
 
    




import mammoth
with open(r"C:\Users\user\Desktop\Anthem1.docx", "rb") as docx_file:
    result = mammoth.convert_to_html(docx_file)
    html = result.value # The generated HTML
    messages = result.messages # Any messages, such as warnings during conversion
f = open(r"C:\Users\user\Desktop\Anthem1.html","w")
f.write(html)

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html.parser')
#soup.prettify()

blacklist = ["img",'table']
for tag in soup.findAll():
        if tag.name.lower() in blacklist:
            # blacklisted tags are removed in their entirety
            tag.extract()




from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
from string import punctuation
#import pandas as pd
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")





def find_parent_data(lis,kwds):
#    print(kwds,lis)
    res=""
    res2=""
    for i in lis:
        res+="<h3>"+i+"</h3>"
        res2+="<h3>"+i+"</h3>"
        for key,val in d_h2.items():
            for key2,val2 in val.items():
                if i==key2:
#                    print("---------",key2)
#                    print("---",key2)
                    soup4= BeautifulSoup(val2,'html.parser')
                    ps=soup4.find_all('p')
                    for p1 in ps:
#                        print(p1)
                        checklist=str(p1).lower().split()
                        checklist=[stemmer.stem(y) for y in checklist]
#                        print(checklist)
#                        print(p1)
                        if all(x in checklist for x in kwds):
#                            print(p1,"\n")
                            res+=p1.prettify()
                            res2+=p1.prettify()
#                            print("iiffififif")
#                
                        else:
                            if any(x in checklist for x in kwds):
                                res+=p1.prettify()
       
        res+="<a id='more_info' onclick='show_full_info()'>Click here for more info</a><br>"
#        res+="<script>function show_full_info(){alert();}</script>"
                        
    return res  



all_h1=soup.find_all('h1')

d_h1={}

for h1 in all_h1:
    first=h1
    second=first.find_next('h1')
    temp=""
    
    while first.findNext()!=second:
        if str(first.findNext().text) != "":
            temp+= str(first.findNext())+" "
        first=first.findNext()
    #if temp!=" Please see “Therapy Services” later in this section. " and temp!=' See “Therapy Services” later in this section. ' and temp!="":
    temp=temp.replace('.'," . ")
    temp=temp.replace('('," ( ")
    temp=temp.replace(')'," ) ")
    temp=temp.replace('<'," <")
    temp=temp.replace('>',"> ")
    d_h1[str(h1.text)]=temp

d_h1.pop('Section 4. Table of Contents')

d_h2={}

for h1,h1_val in d_h1.items():
    d_unio={}
    soup2 = BeautifulSoup(h1_val,'html.parser')
    all_h2=soup2.find_all('h2')
    if len(all_h2)!=0 :
        for h2 in all_h2:
            first=h2
            second=first.find_next('h2')
            temp=""
        
            while first.findNext()!=second:
                if str(first.findNext().text) != "":
                    temp+= str(first.findNext())+" "
                first=first.findNext()
            #if temp!=" Please see “Therapy Services” later in this section. " and temp!=' See “Therapy Services” later in this section. ' and temp!="":
            temp=temp.replace('.'," . ")
            d_unio[h2.text]=temp
        d_h2[str(h1)]=d_unio
    else:
        d_h2[str(h1)]={str(h1):h1_val}
#        print("--------------------")


    
#
#for item,value in d_h2.items():
#    print(item,"\n",value,'-----------------','\n')    
#    



d_kwds={}
for key,val in d_h2.items():
#    print(val,"\n\n\n")
    for key2,val2 in val.items():
#        print("dsadad\n",key2)
        if val2 is not None:
            sents = sent_tokenize(val2)
            word_sent = word_tokenize(val2.lower())
            _stopwords = set(stopwords.words('english') + list(punctuation)+['·',
      '’',
      '“',
      '”'])
            section_words=[word for word in word_sent if word not in _stopwords]
            d_kwds[key2]=list(word for word in set(section_words) if (word.isalpha() and len(word)>2 and len(set(word))!=1))
        
        
        
    
d_stem={}
for key,val in d_kwds.items():
    singles = [stemmer.stem(i) for i in val]
    temp=set(singles)
    d_stem[key]=list(temp)
    


bag_of_words2=[]
for i,j in d_stem.items():
    bag_of_words2.append(j)
new_bag=[]
for list_word in bag_of_words2:
    for i in list_word:
        if i.isalpha():
            new_bag.append(i) 
new_bag=list(set(new_bag))
    




if __name__ == "__main__":
    app.run()
