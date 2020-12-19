import os, sys, subprocess

file = sys.argv[1] if len(sys.argv) > 1 else input('Filename?')
problem = input('Problem?')
language = input('Language?').lower()

def get_args():
    if language in ['python', 'py', 'python3', 'py3']:
        return ['py', file]
    if language in ['java']:
        subprocess.run(['javac', file], capture_output=True, text=True, check=True)
    if language in ['java', 'class']:
        return ['java', '.'.join(file.split('.')[:-1])]

verdict = 'Something went wrong'
for i in os.listdir('.'):
    if i.startswith(str(problem).zfill(2)):
        if not os.path.isdir('!LOGS'):
            os.mkdir('!LOGS')
        for j in os.listdir('!LOGS'):
            os.remove(f'!LOGS/{j}')
        verdict = 'Verdict: '
        
        try:
            args = get_args()
        except subprocess.CalledProcessError as e:
            verdict = 'C'
            with open(f'!LOGS/err.err', 'w') as f:
                f.write(e.stderr)
            break
        if not args:
            verdict = 'Something went wrong'
            break
        for j in range(10):
            with open(f'{i}/{j}.txt') as f:
                process = subprocess.run(['python3', f'{i}/main.py'], capture_output=True, text=True, input=f.read())
                a = [k for k in process.stdout.splitlines() if k]
                with open(f'!LOGS/{j}.txt', 'w') as g:
                    g.write(process.stdout)
                f.seek(0)
                v = 'W'
                process = None
                try:
                    process = subprocess.run(args, capture_output=True, text=True, input=f.read(), timeout=10, check=True)
                except subprocess.TimeoutExpired as e:
                    v = 'T'
                    process = e
                except subprocess.CalledProcessError as e:
                    v = 'E'
                    process = e
                b = [k for k in (process.stdout or '').splitlines() if k]
                with open(f'!LOGS/{j}.out', 'w') as g:
                    g.write(process.stdout or '')
                with open(f'!LOGS/{j}.err', 'w') as g:
                    g.write(process.stderr or '')
                if a == b:
                    v = 'A'
                verdict += v
        break
print(verdict)
input()