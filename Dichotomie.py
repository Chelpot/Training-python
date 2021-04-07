def main():
    tab = [0,5,8,13,16,32,35,36,86,140,3004,3456,4566,45554]
    print(recherche_dichotomique(140, tab))
    
def recherche_dichotomique(target, liste, start = 0, end = -1):
    if start == end:
        return start
    if end == -1:
        end = len(liste)-1
    m = (start+end)//2
    if liste[m] == target:
        return m
    elif liste[m] > target:
        return recherche_dichotomique(target, liste, start, m-1)
    else :
        return recherche_dichotomique(target, liste, m+1, end)
    
main()
