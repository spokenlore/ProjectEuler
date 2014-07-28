#include <iostream>
#include <cmath>

using namespace std;

void problem1();
void problem2();
int problem3();
int problem4();
int isPalindrome(long int num);

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
    else if (problemnumber == 4){
        problem4();
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
            << "The sum of all even fibonacci numbers under 4,000,000 is " << sum << endl;
    }

// Non-working solution to problem 3
int problem3(){
    const long long numm = 600851475143;
    long long int largestFact = 0;

    for (long long i = 2; i < numm; i++) {
        if (numm % i == 0) {
            bool isPrime = true;
            for (long long j = 2; j < i; j++) {
                if (i % j == 0) {
                    isPrime = false;
                    break;
                    cout << endl << "The greatest prime factor of " << numm << "is " << j << "." << endl;
                }
            }
            if (isPrime) {
                largestFact = i;
            }
        }
    }
}

int problem4(){
    //int n;
    //cout << "what is the number you want checked?" << endl;
    //cin >> n;
    long int a = 999;
    long int b = 999;
    bool checker = false;
    long int product = 0;
    int i = 0;
        while (checker = false){
           if (i % 2 == 0){
            a--;
           }
           else b--;
                product = a * b;
                if (isPalindrome(product) == 1){
                    checker = true;
                    cout << endl << product;
                }
                else checker = false;
                i++;
        }
                if (checker == true){
                    cout << endl << product << " is the largest possible palindrome.";
                return 0;}
                else return 0;
            }

int isPalindrome(long int num){
    //cout << num << endl;
        long int n = num;
        long int rev = 0;
        long int dig;
        while (num > 0){
            dig = num % 10;
            rev = rev * 10 + dig;
            num = num / 10;
        }
    if (n==rev){
        cout << "Your number"  << " is a palindrome!";
        return 1;
    }
    else return 0;
}
