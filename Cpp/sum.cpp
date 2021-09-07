/* This code requires two inputs to give the sum of both the inputs */

#include <iostream>
using namespace std;

int main()
{
    int num1;
    int num2;
    int sum;

    cout<<"Please enter two numbers:"<<endl;
    cin>>num1>>num2;

    sum = num1 + num2;

    cout<<num1<<" + "<<num2<<" = "<<sum<<endl;

    return 0;
}