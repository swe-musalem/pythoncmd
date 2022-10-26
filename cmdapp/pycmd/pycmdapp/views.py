from re import I
from django.shortcuts import render
import time
# these libraryes is used to be able to catch the output out of exec function
import sys
from io import StringIO


inputlst = []
errorlst= []

def cmd(request):
    if request.method == 'POST':
        request.session['input'] =  request.POST.get('input')
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        try:
            exec(request.POST.get('input'))
        except NameError as err:
            
            request.session['err'] = str(err)
            errorlst.append(request.session['err'] )

        except SyntaxError as err:
        
            request.session['err'] = str(err)
            errorlst.append(request.session['err'] )
            
        inputlst.append(redirected_output.getvalue())
        
    context = {
            'inputlst': inputlst,
            'errorlst':errorlst,
        }
    return render(request,'cmd.html',context)