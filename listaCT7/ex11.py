from re import I


times = ["Alemanha", "Argentina", "Bélgica", "Brasil", "Colômbia", "Costa Rica", "França", "Holanda"]

def possiveisFinalistas(times):
    i=0
    while i < len(times):
        for vice in times:
            if times[i] != vice:
                print(times[i], vice)
        i = i+1
    

possiveisFinalistas(times)  