import os

a = open('baza.txt').read()

secim = input('''Bazani sil (1): 
Bazaya meluma daxil et (2): ''')



if secim == '1':
    if os.path.exists('baza.txt'):
        os.remove('baza.txt')
    else:
        print('Baza movcud deyil')

elif secim == '2':
    a = open('baza.txt').read()
    elave_edin = input('Yazdirin... ')
    if len(a) == 0:
        a = open('baza.txt', 'a')
        a.write(elave_edin)
    else:
        a = open('baza.txt').readlines()
        for x in a:
            if elave_edin not in x:
                a = open('baza.txt', 'a')
                a.write(', ' + elave_edin)
            else:
                print('Bu ad hal-hazirda movcuddur!')

a = open('baza.txt').read()
print('Bazada ' + str(len(a.split(','))) + ' melumat var')