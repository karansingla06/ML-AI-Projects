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
        user_input_words=[i for i in user_input_words if (i in new_bag and i not in ('claim','want','know','cover','elig'))]
        
        
        key_section={}
        for i in user_input_words:
            temp=[]
            for key,val in d_stem.items(): 
                if i in val:
                    temp.append(key)
            key_section[i]=set(temp)
        
        
        if len(key_section.keys())!=0:    
            final_cmn_section= list(set.intersection(*map(set,key_section.values())))
            print("Parents are-- \n",final_cmn_section)
            final_output+=find_parent_data(final_cmn_section,user_input_words)  
        
#            for i in final_cmn_section:
#            #print(i)
#                if len(d_ms[i].split())>250:
#                    sents = sent_tokenize(d_ms[i])
#                #print(sents)
#                    for sen in sents:
#                        checklist=sen.lower().split()
#                        checklist=[stemmer.stem(y) for y in checklist]
#                    #print(checklist,"\n")
#                        if all(x in checklist for x in user_input_words):
#                            print(sen,"\n")
#                            final_output+=sen+"\n\n"
#                else:    
#                    print(i,"\n",d_ms[i],"\n\n\n")
#                    final_output+="<br>"+i+"<br>"+d_ms[i]+"<br><br>"
            
        
        #            
        #print(final_cmn_section)
        
        
        
        
            trows = soup.find_all('tr')
            if len(final_cmn_section)==0:
                final_output+="our customer representative will contact you shortly"
                
            else:
                for i in final_cmn_section:
                    temp=i.split('and')
                    i=temp[0]
                    for tr in trows:    
                        if "See" in tr.text and i in tr.text:
                            continue
                            
                        elif i in tr.text:
                            section_tr=tr
                            print(section_tr.text)
                            final_output+="<br><table>"+section_tr.text+"</table><br>"
                            
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



#all_h2=soup.find_all('h2')
#    
#d_ms={}
#for item in all_h2:
#    first=item
#    second=first.find_next('h2')
#    temp=""
#    
#    while first.findNext()!=second:
#        if str(first.findNext().text) != "":
#            temp+= str(first.findNext())+" "
#        first=first.findNext()
#    #if temp!=" Please see “Therapy Services” later in this section. " and temp!=' See “Therapy Services” later in this section. ' and temp!="":
#    temp=temp.replace('.'," . ")
#    d_ms[str(item.text)]=temp
#
##for item,value in d_ms.items():
# #   print(item,"\n",value,'-----------------','\n')    
#    
#
#
#d_kwds={}
#for key,val in d_ms.items():
#    if val is not None:
#        sents = sent_tokenize(val)
#        word_sent = word_tokenize(val.lower())
#        _stopwords = set(stopwords.words('english') + list(punctuation)+['·',
#  '’',
#  '“',
#  '”'])
#        section_words=[word for word in word_sent if word not in _stopwords]
#        d_kwds[key]=list(word for word in set(section_words) if (word.isalpha() and len(word)>2 and len(set(word))!=1))
#        
#    
#d_stem={}
#for key,val in d_kwds.items():
#    singles = [stemmer.stem(i) for i in val]
#    temp=set(singles)
#    d_stem[key]=list(temp)
#    
#
#
#bag_of_words2=[]
#for i,j in d_stem.items():
#    bag_of_words2.append(j)
#new_bag=[]
#for list_word in bag_of_words2:
#    for i in list_word:
#        if i.isalpha():
#            new_bag.append(i) 
#new_bag=list(set(new_bag))

def find_parent_data(lis,kwds):
    res=""
    for i in lis:
        for key,val in d_h2.items():
            for key2,val2 in val.items():
                if i==key2:
                    res+="<h1><strong>"+key2+" :</strong></h1><br>\n"
                    res+=val2+"<br>"
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
    d_h1[str(h1.text)]=temp


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
        print("--------------------")


    

for item,value in d_h2.items():
    print(item,"\n",value,'-----------------','\n')    
    



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
