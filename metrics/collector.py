from prometheus_client import start_http_server, Summary, Counter
import random
import time

# Create a Counter to track the number of code snippets generated
code_generated = Counter('code_snippets_generated_total', 'Total number of code snippets generated')

# Create a Summary to track the time taken to generate code
generation_time = Summary('code_generation_seconds', 'Time spent generating code')

# Simulate code generation activity
@generation_time.time()
def generate_code():
    # Simulate time taken to generate code
    time.sleep(random.uniform(0.5, 2.0))
    code_generated.inc()
    print('Code snippet generated')

if __name__ == '__main__':
    # Start up the server to expose the metrics
    start_http_server(8000)
    print('Metrics server started at http://localhost:8000')
    
    # Simulate periodic code generation
    while True:
        generate_code()
        time.sleep(random.randint(5, 10)) 