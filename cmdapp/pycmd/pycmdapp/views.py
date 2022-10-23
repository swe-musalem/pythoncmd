from multiprocessing import context
from django.shortcuts import render
import time
# these libraryes is used to be able to catch the output out of exec
import sys
from io import StringIO


inputlst = []
def cmd(request):
    
    if request.method == 'POST':
        request.session['input'] =  request.POST.get('input')
        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        exec(request.POST.get('input'))
        sys.stdout = old_stdout
        inputlst.append(redirected_output.getvalue())
        
    context = {
            'inputlst': inputlst
        }
    return render(request,'cmd.html',context)