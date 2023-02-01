#include <bits/stdc++.h>
using namespace std;


int main() {
  vector <int> v;

  for (int i = 0; i < 5 ;i++){
    v.push_back(i);
  }

  for (int i = 0; i < 5 ;i++){
    cout<< v[i] << "\n";
    cout << "Capacicy" << " "<<v.capacity() << "\n";
    cout << "Size" << " " <<v.size() << "\n";
  }
}