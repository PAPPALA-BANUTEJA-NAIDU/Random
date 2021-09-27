#include<bits/stdc++.h>
using namespace std;

void selection(int arr[], int n) {
    for(int i = 0; i < n; i++) {
        int min_id = i;
        for(int j = i+1; j < n; j++){
            if(arr[min_id] > arr[j])
                min_id = j; 
        }
        swap(arr[i], arr[min_id]);
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
