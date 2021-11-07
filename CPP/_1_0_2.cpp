#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
    int i = 0, o = 0, z = 0, t = 0;

    int arr[6] = {2, 1, 0, 2, 0, 1};
    for (i = 0; i < 6; i++)
    {

        if (arr[i] == 1)
        {
            o++;
        }
        else if (arr[i] == 0)
        {
            z++;
        }
        else
        {
            t++;
        }
    }

    int k = 0;

    for (i = 0; i < z; i++)
    {
        arr[k++] = 0;
    }
    for (i = 0; i < o; i++)
    {
        arr[k++] = 1;
    }
    for (i = 0; i < t; i++)
    {
        arr[k++] = 2;
    }
    for (i = 0; i < 6; i++)
    {
        cout << arr[i] << endl;
    }

    return 0;
}