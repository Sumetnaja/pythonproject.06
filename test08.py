# เขียนโปรแกรม รับชื่อ อายุ ทางแป้นพิมพ์ แล้วแสดงผลออกมาว่า ชื่อ อายุนั้น เป็น เด็ก คนหนุ่ม หรือคนแก่
# อายุน้อยกว่า 18 คือ เด็ก /อายุ 19 - 45 คนหนุ่ม/46 ขึ้นคือคนแก่

# หาฟีเจอร์การทำงาน เพื่อจะเอาไปเขียนเป็นฟังก์ชั่น
# ฟีเจอร์ รับค่าข้อมูล , ตรวจสอบและแสดงผลว่าเป็น เด็ก คนหนุ่ม หรือคนแก่ , แสดงชื่อโปรแกรม

def showProgramName() :
    print('**--โปรแกรมตรวจสอบความเป็นเด็ก หนุ่ม แก่--**')

def inputData( ) :
    name = input('ป้อนชื่อ : ')
    age = int(input('ป้อนอายุ : '))
    return name, age

def checkShowStatus( name, age ) :
    if age <= 18 :
        print(f'คุณ{name} อายุ {age} ปี เป็นเด็ก')
    elif age >= 19 and age <= 45 :
        print(f'คุณ{name} อายุ {age} ปี เป็นคนหนุ่ม')
    else :
        print(f'คุณ{name} อายุ {age} ปี เป็นคนแก่')

print('----------------------------------')
showProgramName()
print('----------------------------------')
name, age = inputData()
print('----------------------------------')
checkShowStatus( name, age )
print('----------------------------------')


