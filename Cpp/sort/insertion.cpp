#include<bits/stdc++.h>
using namespace std;

void selection(int arr[], int n) {

    for (int i = 0; i < n; i++) {
        int j = i;
        while (j >= 1 && arr[j] < arr[j-1]) {
            swap(arr[j], arr[j-1]);
            j--;
        }
    }
    //array print
    for(int i = 0; i< n; i++)
        cout << arr[i] << " ";
    cout << "\n";
}

int main() {
    int n;
    cin >> n;
    int arr[n];
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    selection(arr, n);
    return 0;
}
