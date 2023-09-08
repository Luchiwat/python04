#หาพื้นที่สี่เหลี่ยมและสามเหลี่ยม
def inputLong( ) :
    wi = float( input('กว่าง '))
    lo = float(input('ยาว '))
    return wi,lo 

def inputhigh( ) :
    ba = float(input('ฐาน '))
    hi = float(input('สูง '))
    return ba,hi

def CalAndShowAreaSquare(wi,lo) :
    area = wi*lo
    print(f'สี่เหลี่ยมกว่าง {wi} ยาว {lo} มีพื้นที่ {area}')

def CalAndShowAreaTriamble(ba,hi) :
    area = ba*hi/2
    print(f'สามเหลี่ยมฐาน {ba} สูง {hi} มีพื้นที่ {area}')

wi,lo = inputLong( )
CalAndShowAreaSquare(wi,lo)
print('-------------------')
ba,hi = inputhigh( )
CalAndShowAreaTriamble(ba,hi)

