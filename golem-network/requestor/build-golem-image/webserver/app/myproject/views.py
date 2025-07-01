from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import threading
import time
import json
from . import radiation_transport

DEFAULT_NUM_PHOTONS = 1_000_000
DEFAULT_SLAB_THICKNESS = 10.0
DEFAULT_ATTENUATION_COEFF = 0.1
DEFAULT_USE_SCATTER = False
DEFAULT_P_SCATTER = 0.7
DEFAULT_P_SCATTER_REVERSES_DIRECTION = 0.5
DEFAULT_SEED = 1
DEFAULT_SKIP_FULL_RESULT_FILE = False

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

        try:
            if request.body:
                params = json.loads(request.body)
                num_photons = params.get('num_photons', DEFAULT_NUM_PHOTONS)
                slab_thickness = params.get('slab_thickness', DEFAULT_SLAB_THICKNESS)
                attenuation_coeff = params.get('attenuation_coeff', DEFAULT_ATTENUATION_COEFF)
                use_scatter = params.get('use_scatter', DEFAULT_USE_SCATTER)
                p_scatter = params.get('p_scatter', DEFAULT_P_SCATTER)
                p_scatter_reverses_direction = params.get('p_scatter_reverses_direction', DEFAULT_P_SCATTER_REVERSES_DIRECTION)
                seed = params.get('seed', DEFAULT_SEED)
                skip_full_result_file = params.get('skip_full_result_file', DEFAULT_SKIP_FULL_RESULT_FILE)
            
            else:
                print("No simulation parameters received, using default values.")
                
                num_photons = DEFAULT_NUM_PHOTONS
                slab_thickness = DEFAULT_SLAB_THICKNESS
                attenuation_coeff = DEFAULT_ATTENUATION_COEFF
                use_scatter = DEFAULT_USE_SCATTER
                p_scatter = DEFAULT_P_SCATTER
                p_scatter_reverses_direction = DEFAULT_P_SCATTER_REVERSES_DIRECTION
                seed = DEFAULT_SEED
                skip_full_result_file = DEFAULT_SKIP_FULL_RESULT_FILE
        
        except json.JSONDecodeError as ex:
            print("Exception thrown when decoding JSON body, using default values.")
            print(ex)
            
            num_photons = DEFAULT_NUM_PHOTONS
            slab_thickness = DEFAULT_SLAB_THICKNESS
            attenuation_coeff = DEFAULT_ATTENUATION_COEFF
            use_scatter = DEFAULT_USE_SCATTER
            p_scatter = DEFAULT_P_SCATTER
            p_scatter_reverses_direction = DEFAULT_P_SCATTER_REVERSES_DIRECTION
            seed = DEFAULT_SEED
            skip_full_result_file = DEFAULT_SKIP_FULL_RESULT_FILE

        print("Simulation parameters:")
        print(f"num_photons={num_photons}")
        print(f"slab_thickness={slab_thickness}")
        print(f"attenuation_coeff={attenuation_coeff}")
        print(f"use_scatter={use_scatter}")
        print(f"p_scatter={p_scatter}")
        print(f"p_scatter_reverses_direction={p_scatter_reverses_direction}")
        print(f"seed={seed}")
        print(f"skip_full_result_file={skip_full_result_file}")

        def run_task():
            global task_output

            simulation = radiation_transport.Simulation(
                num_photons=num_photons,
                slab_thickness=slab_thickness,
                attenuation_coeff=attenuation_coeff,
                use_scatter=use_scatter,
                p_scatter=p_scatter,
                p_scatter_reverses_direction=p_scatter_reverses_direction,
                seed=seed
            )
            simulation.run_simulation()
            
            task_output = simulation.save_to_buffer(skip_full_result_file)
            
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