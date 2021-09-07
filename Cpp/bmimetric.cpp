/* Program gives BMI from height and Weight */

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int weight;
    float height;
    double BMI;

    cout<<"Please enter weight in kilograms: ";
    cin>>weight;

    cout<<"Please enter height in meters: ";
    cin>>height;

    BMI = weight / (height * height);

    cout<<"BMI is: "<<fixed<<setprecision(2)<<BMI<<endl;

    return 0;


}