#include <iostream>
using namespace std;

int main()
{
    int hour12, hour24, minutes;
    char temp;

    cout<<"Enter the time in 24 hour format:";
    cin>>hour24>>temp>>minutes;

    hour12 = hour24 - 12;

    if(hour24 <= 12 and minutes <= 60)
        cout<<"Time is "<<hour24<<":"<<minutes<<" am"<<endl;
    else if(hour24 < 24 and minutes <=60)
        cout<<"Time is "<<hour12<<":"<<minutes<<" pm"<<endl;

    else 
        cout<<"invalid time"<<endl;

    return 0;
}