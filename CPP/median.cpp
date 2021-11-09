#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int find_median(vector<int> v)
{
  int i, sum = 0;
  int s = v.size();
  sort(v.begin(), v.end());

  if (s % 2 == 0)
  {
    return ((v[s/2]+v[s/2-1])/2);
  }
  else
  {
    return v[s / 2];
  }
}

int main()
{

  vector<int> v;
  int y;

  for (int i = 0; i < 3; i++)
  {
    cin >> y;
    v.push_back(y);
  }

  cout << find_median(v);

  return 0;
}