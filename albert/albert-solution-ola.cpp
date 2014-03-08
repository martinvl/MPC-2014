#include<iostream>
#include<set>


using namespace std;


struct petr{
  int pos, pri;
};


bool operator<(const petr &a, const petr &b){
  if (a.pri==b.pri)
    return a.pos<b.pos;
  return a.pri<b.pri;
}


int main(){
  int L, N; cin>>L>>N;
  petr p;
  set<petr> s;
  set<int> q;
  for (int i=0; i<N; ++i){
    cin>>p.pos>>p.pri;
    s.insert(p);
  }
  q.insert(-L);
  q.insert(p.pos);
  int ans=0;
  for (set<petr>::iterator it=s.begin(); it!=s.end(); ++it){
    p=*it;
    if (q.find(p.pos)!=q.end())
      continue;
    q.insert(p.pos);
    set<int>::iterator i=q.find(p.pos);
    int a=p.pos, b=p.pos+L;
    i--;
    if ((*i)+L>a) a=(*i)+L;
    ++i; ++i;
    if (b>(*i)) b=(*i);
    if (b>a)
      ans+=(b-a)*p.pri;
  }
  int a=-L;
  for (set<int>::iterator it=q.begin(); it!=q.end();++it){
    if ((*it)-a>L)
      ans=-1;
    a=*it;
  }
  if (ans==-1)
    cout<<"Stay home"<<endl;
  else
    cout<<ans<<endl;
  return 0;
}
