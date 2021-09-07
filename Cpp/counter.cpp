/* Monetary values in terms of dollars and cents */

#include <iostream>
using namespace std;

int main()
{
    int quarters;
    int dimes;
    int nickels;
    int pennies;
    int dollars, cents, total;

    cout<<"Please enter the number of coins:"<<endl;

    cout<<"# of quarters:";
    cin>>quarters;

    cout<<"# of dimes:";
    cin>>dimes;

    cout<<"# of nickels:";
    cin>>nickels;

    cout<<"# of pennies:";
    cin>>pennies;

    total = (quarters*25) + (dimes*10) + (nickels*5) + (pennies);
    dollars = total/100;
    cents = total % 100;

    cout<<"The total is "<<dollars<<"dollars and "<<cents<<"cents"<<endl;

    return 0;
    
}