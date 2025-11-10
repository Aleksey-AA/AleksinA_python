name="Алексей"
age=31
height=184.5
print("Имя",name)
print("Возраст",age)
print("Рост",height)

x=10
print(type(x))
x=25.5
print(type(x))
x="Python"
print(x)
print(type(x))

a=7
b=a
print("a =",a)
print("b =",b)
a=10
print("b =","значение не изменилось потому, что b ссылается на a перед ее изменением")

x=y=z=100
print("x =",x)
print("y =",y)
print("z =",z)
print("x =",x,"y =",y,"z =",z)
print(id(x))
print(id(y))
print(id(z))
print("id одинаковый")
x,y,z=10,20,30
print("x =",x,"y =",y,"z =",z)
print(id(x))
print(id(y))
print(id(z))
print("id разные")

a=5
b=10
a,b=b,a
print("a =",a)
print("b =",b)

# True = 12
# print = 34
# if = 45
import keyword
print(keyword.kwlist)

var1 = 42
var2 = 3.14
var3 = "Hello"
print("var1 =", type(var1))
print("var2 =", type(var2))
print("var3 =", type(var3))
var1="любое строковое значение"
print("var1 =", type(var1))

q=143
w=24.543
e="строка"
r="23f"
t=2348875992.44958982929
print("q =",q,"тип -",type(q))
print("w =",w,"тип -",type(w))
print("e =",e,"тип -",type(e))
print("r =",r,"тип -",type(r))
print("t =",t,"тип -",type(t))
переменная = 45
print(переменная)
print("объявление переменной русским именем работает")