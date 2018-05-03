*
* To change this license header, choose License Headers in Project Properties.
* To change this template file, choose Tools | Templates
* and open the template in the editor.
*/
package nfa;
/**
*
* @author jsaikishor
*/

class edgedef 
{
int from;
int to;
char symbol;
public edgedef()
{
from =0;
to=1;
symbol='e';
}
public edgedef(int f, int t , char s)
{
from =f;
to=t;
symbol=s;
}
}
class NFA
{
int finalstate;
int nv;
int ne;
edgedef edge[];
public NFA(char c)
{
nv =2;
ne =1;
edge=new edgedef[ne];
edge[0]=new edgedef(0,1,c);
finalstate=1;
}

public void display()
{
System.out.println("TRANSITION.NO FROM ON TO ");
for (int i=0; i<ne;i++)
System.out.println(" "+(i+1)+" q"+edge[i].from+" "+edge[i].symbol+" q"+edge[i].to);
System.out.println("Final State : q"+finalstate);
}
public NFA()
{
nv =2;
ne =1;
edge=new edgedef[ne];
edge[0]=new edgedef(0,1,'e');
finalstate=1;
}
@SuppressWarnings("empty-statement")
private static NFA concat(NFA nfa1, NFA nfa2) {

NFA newnfa = new NFA();
newnfa.nv = nfa1.nv + nfa2.nv ;
newnfa.ne = nfa1.ne + nfa2.ne +1;
newnfa.edge=new edgedef[newnfa.ne];
System.arraycopy(nfa1.edge, 0, newnfa.edge, 0, nfa1.ne);

newnfa.edge[nfa1.ne] = new edgedef(nfa1.finalstate, nfa1.finalstate+1, 'e');

for(int i=0;i<nfa2.ne;i++)
{
nfa2.edge[i].from+=nfa1.nv;
nfa2.edge[i].to+=nfa1.nv;

}

System.arraycopy(nfa2.edge, 0, newnfa.edge, nfa1.ne+1 , nfa2.ne);

newnfa.finalstate = newnfa.nv-1;
return newnfa;

}
private static NFA union(NFA nfa1, NFA nfa2) {

NFA newnfa = new NFA();
newnfa.nv = nfa1.nv + nfa2.nv +2;
newnfa.ne = nfa1.ne + nfa2.ne +4;
newnfa.edge=new edgedef[newnfa.ne];
newnfa.finalstate = newnfa.nv-1;

newnfa.edge[0] = new edgedef();

for(int i=0;i<nfa1.ne;i++)
{
nfa1.edge[i].from+=1;
nfa1.edge[i].to+=1;

}
System.arraycopy(nfa1.edge, 0, newnfa.edge, 1, nfa1.ne);

newnfa.edge[nfa1.ne+1] = new edgedef(0,nfa1.nv+1,'e');

for(int i=0;i<nfa2.ne;i++)
{
nfa2.edge[i].from+=nfa1.nv+1;
nfa2.edge[i].to+=nfa1.nv+1;

}

System.arraycopy(nfa2.edge, 0, newnfa.edge, nfa1.ne+2 , nfa2.ne);

newnfa.edge[newnfa.ne-2] = new edgedef(nfa1.nv,nfa1.nv + nfa2.nv +1,'e');

newnfa.edge[newnfa.ne-1] = new edgedef(nfa1.nv + nfa2.nv,nfa1.nv + nfa2.nv +1,'e');

return newnfa;

}
private static NFA star(NFA nfa) {
NFA newnfa = new NFA();
newnfa.nv = nfa.nv + 2 ;
newnfa.ne = nfa.ne + 4;
newnfa.finalstate = newnfa.nv-1;
newnfa.edge=new edgedef[newnfa.ne];
newnfa.edge[0] = new edgedef();
newnfa.edge[1] = new edgedef(0,newnfa.finalstate,'e');

for(int i=0;i<nfa.ne;i++)
{
nfa.edge[i].from +=1;
nfa.edge[i].to+=1;
}
System.arraycopy(nfa.edge, 0, newnfa.edge, 2, nfa.ne);

newnfa.edge[newnfa.ne-2] = new edgedef(nfa.edge[nfa.ne-1].to,1,'e');
newnfa.edge[newnfa.ne-1] = new edgedef(nfa.edge[nfa.ne-1].to,newnfa.finalstate,'e');

return newnfa;
}
public static NFA re2nfa(String re)
{
NFA newnfa = new NFA();
int rl = re.length();
if (rl == 0)
{
return new NFA();
}
else if (rl == 1)
{
return new NFA(re.charAt(0));
}
else if (!(re.contains("*")||re.contains("|")||re.contains("(")||re.contains(")")))
{
return concat(re2nfa(re.substring(0,1)),re2nfa(re.substring(1,rl)));
}
else 
{
int br=0; 
for (int i=0;i<rl;i++)
{
switch(re.charAt(i))
{
case '(': { br++;
if (i!=0 && br==1)
{
System.out.println(" concat of "+re.substring(0, i)+" and "+re.substring(i, rl));
return concat(re2nfa(re.substring(0, i)),re2nfa(re.substring(i, rl))); 
}

break; }
case ')': { br--; 
if (i==rl-1)
{
System.out.println(" removing () "+re+" became "+re.substring(1, i));
return re2nfa(re.substring(1, i)); 
}
break; }
case '|': 
{ 
if(i==0)
{ 
System.out.println("Wrong RE i = " + i + "br =" + br +" char at i is "+re.charAt(i)+" re is "+re);
}
else if (br==0)
{ 
System.out.println(" union of " + re.substring(0, i)+ " and " +re.substring(i+1, rl));
return union(re2nfa(re.substring(0, i)),re2nfa(re.substring(i+1, rl)));
}
break;
}
case '*': 
{ if(br ==0)
{
if (i==rl-1)
{
System.out.println(re+ " became star of "+re.substring(0, i));
return star(re2nfa(re.substring(0, i))); 
}
return concat(star(re2nfa(re.substring(0, i-1))),re2nfa(re.substring(i+1, rl)));
}
break;
}

}



}
}
return newnfa;
}


public static void main(String args[]) 
{
NFA nfa;
String re = "a(b|c)*";
nfa = re2nfa(re);
nfa.display();

}
 
}