/* Monetary values in terms of dollars and cents */

#include <iostream>
using namespace std;

int main()
{
    int quarters;
    int dimes;
    int nickels;
    int pennies;
    int dollars, cents, total, offset;

    cout<<"Please enter the amount of money to convert:"<<endl;

    cout<<endl<<"# of dollars:";
    cin>>dollars;

    cout<<"# of cents:";
    cin>>cents;
    
    total = (dollars*100) + cents;

    quarters = total / 25;
    offset = total - (quarters * 25);

    dimes = offset / 10;
    offset = offset - (dimes * 10);

    nickels = offset / 5;
    offset = offset - (nickels*5);

    pennies = offset ;

    cout<<"The coins are "<<quarters<<"quarters, "<<dimes<<"dimes, "<<nickels<<"nickels and "<<pennies<<"pennies"<<endl;

    return 0;
    
}