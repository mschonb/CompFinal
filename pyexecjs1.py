import execjs
f1 = """
  f = function (ss) {
        f1 = function (ss) {// inicio accion semantica
	   ss[0].put("a",221);
       ss[1].put("sss", 555);
	   if(ss[0].contains("x")) ss[0]["contiene1"] = "si";
	   if(!ss[0].contains("zz")) ss[0]["contiene2"] = "no";
	   }
	//fin de accion semantica
	// tiene que agregar lo que viene enseguida
    	f2 = function (ss) {
           for(var i = 0; i < ss.length; i++) {
	   	   ss[i]["put"] = function(key,value) {this[key] = value};
		   ss[i]["contains"] = function(key) {return this[key] != null};
           ss[i]["get"] = function(key) {return this[key]}
           }
        }
        f2(ss);
	f1(ss)
	return ss;     
  }
"""

#copiado del txt de prods2.txt
accion_semantica = """function(ss) {ss[0].put("n", ss[2].get("n") + ss[3].get("n")); return ss;}"""

#siempre hay que usar esta funcion (aqui declaramos get, put y contains)
la_f2 = """
f2 = function (ss) {
        for(var i = 0; i < ss.length; i++) {
        ss[i]["put"] = function(key,value) {this[key] = value};
        ss[i]["contains"] = function(key) {return this[key] != null};
        ss[i]["get"] = function(key) {return this[key]}
     }
}
"""
# juntando todo en una sola funcion de js
funcion_acc = "f = function (ss) { f1 = " + accion_semantica + la_f2 + "f2(ss); f1(ss); return ss;}"
print(funcion_acc)
ctx2 = execjs.compile(funcion_acc)

#S0 -> +1 S2 S3 i.e. 4 elementos en la lista de dicts
s0 = {}
s1 = {}
s2 = {"n": 3}
s3 = {"n": 4}
arreglo_semantico = [s0, s1, s2, s3]
#imprimiendo el arreglo semantico antes
print(arreglo_semantico)
arreglo_semantico = ctx2.call("f", arreglo_semantico)
#...y despues
print(arreglo_semantico)

######## ejemplo del prof

# ctx = execjs.compile(f1)
# dico = dict() 
# dico2 = dict()
# dico["x"] = 10
# dico2["yes"] = 10000
# ss = [dico, dico2]
# ss = ctx.call("f",ss)
# print(ss)