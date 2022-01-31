import os,sys,subprocess
program="""
#include<iostream>
using namespace std;
int main(){
  double height,weight;
  cout<<"Height?:";cin>>height;
  cout<<"Weight?:";cin>>weight;
  double bmi =weight/((height/100)*(height/100));
  cout<<"BMI is "<<bmi<<endl;
}
"""
with open('tmp.cpp',mode='w') as f:
  f.write(program)
!g++ tmp.cpp
!./a.out
