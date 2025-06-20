from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import threading
import time
from . import radiation_transport

# Global state variable (in production, use database or cache)
task_state = {"state": "waiting"}
task_output = None

def index(request):
    return render(request, 'index.html', {'state': task_state['state']})

def get_state(request):
    return JsonResponse(task_state)

@csrf_exempt
def start_task(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid method'}, status=405)

    if task_state['state'] == 'waiting':
        task_state['state'] = 'running'

        def run_task():
            global task_output

            simulation = radiation_transport.Simulation()
            simulation.run_simulation()
            
            task_output = simulation.save_to_buffer()
            
            task_state['state'] = 'done'
        
        thread = threading.Thread(target=run_task)
        thread.daemon = True
        thread.start()
    
    return JsonResponse(task_state)

@csrf_exempt
def reset_task(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid method'}, status=405)
        
    task_state['state'] = 'waiting'
    
    global task_output
    task_output = None

    return JsonResponse(task_state)

def download_output(request):
    if task_output is None:
        return JsonResponse({'error': 'No output available'}, status=404)
    
    response = HttpResponse(task_output, content_type='application/x-hdf')
    response['Content-Disposition'] = f'attachment; filename="task_output_{int(time.time())}.h5"'

    return response