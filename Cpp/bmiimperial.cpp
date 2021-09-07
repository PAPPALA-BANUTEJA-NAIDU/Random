/* Program gives BMI from height and Weight */

#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    float weight_in_Pounds, weight_in_Kilograms;
    float height_in_Inches, height_in_Meters;
    double BMI;

    cout<<"Please enter weight in pounds: ";
    cin>>weight_in_Pounds;

    weight_in_Kilograms = weight_in_Pounds * 0.453592;

    cout<<"Please enter height in inches: ";
    cin>>height_in_Inches;

    height_in_Meters = height_in_Inches * 0.0254;

    BMI = weight_in_Kilograms / (height_in_Meters * height_in_Meters);

    cout<<"BMI is: "<<fixed<<setprecision(2)<<BMI<<endl;

    return 0;


}