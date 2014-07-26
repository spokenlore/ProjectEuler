#include <iostream>
#include <cmath>

using namespace std;

void problem1();
void problem2();
int problem3();

int main(){
    int problemnumber;
    cout << "What Project Euler problem would you like the answer to?"
        << endl;
    cin >> problemnumber;

    if (problemnumber == 1){
        problem1();
    }
    else if (problemnumber == 2){
        problem2();
    }
    else if (problemnumber == 3){
        problem3();
    }
    else
        cout << "Error. This number is either invalid or has not yet been completed";
    return 0;
}

void problem1(){
     int sum;
     cout << "The sum of all multiples of 3 and 5 up to 1000 is";
            for (int i = 0; i < 1000; i++) {
                if (i%5 == 0 or i%3 == 0){
                    sum += i;
                }
            }
            cout << sum;
    }

void problem2(){
     int i = 1;
     int x = 0, z = 0, sum = 0, y = 1;
        while (z < 4000000){
                z = x + y;
                x = y;
                y = z;
        if(z % 2 == 0){
            sum += z;
        }
        }
            cout << endl
            << "The sum of all even fibonacci numbers under 4,000,000 is " << sum;
    }

int problem3(){
    int number = 600851475143;
    //int number = 104261;
    int largestfactor = 1;
    bool isPrime = false;

    for (int x = number / 2; x > 1; x--){
        if (number % x == 0){
            if (number % 2 == 0){
                break;
            }
            bool isPrime = false;
            for (int i = 2; i < x; i++){
                if (x % i == 0){
                    isPrime = false;
                    break;
                }
                if (i == x-1)
                    isPrime = true;
                if (isPrime == true)
                {
                    cout << "The largest prime factor is " << x;
                    return 0;
                }
            }
        }
    }

    // cout << "The largest prime factor of 600851475143 is " << x;
    return 0;
    }
