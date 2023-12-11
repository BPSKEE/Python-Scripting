import subprocess

#MATLAB 1
print("Running MATLAB 1")
matlab_executable = ' ' #INSERT MATLAB EXECUTABLE PATH HERE
matlab_process = subprocess.run([matlab_executable, "-batch", "run('matlab1.m');pause(1);"], capture_output=True)
with open('input.txt', 'r') as file:
    input_array = [int(value) for line in file for value in line.split()]
#C
print("Running C")
subprocess.run(["gcc", "c.c", "-o", "c"])
c_process = subprocess.run(["./c"] + [str(x) for x in input_array], text=True, capture_output=True)
c_result = c_process.stdout.strip()
with open('c_output.txt', 'w') as file:
    file.write(c_result)

#Haskell
print("Running Haskell")
subprocess.run(['ghc', 'haskell.hs'])
haskell_process = subprocess.run(['./haskell'] + [str(x) for x in input_array], text=True, capture_output=True)
haskell_result = haskell_process.stdout.strip()
with open('haskell_output.txt', 'w') as file:
    file.write(haskell_result)

#Prolog
print("Running Prolog")
prolog_input = "[" + ",".join(map(str, input_array)) + "]."
p_result = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'prolog.pl'], input=prolog_input, capture_output=True, text=True)
prolog_result = p_result.stdout.strip()
prolog_result = prolog_result.strip('[]')
prolog_result = prolog_result.replace(',', ' ')
with open('prolog_output.txt', 'w') as file:
    file.write(prolog_result)

#MATLAB 2
print("Running MATLAB 2")
matlab_process = subprocess.run([matlab_executable, "-batch", "run('matlab2.m');pause(10);"], capture_output=True)
