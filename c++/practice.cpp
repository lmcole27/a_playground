#include <iostream>
#include <ctime>
#include <cstdlib>

using namespace std;

int main() {
    /*
    cout << "Enter a temperature in Farenheit" << endl;
    double fahrenheit;
    cin >> fahrenheit;
    double celsius = (fahrenheit - 32) * 5/9;
    cout << "The temperature in Celsius is " << celsius << endl;
    
    cout << "Enter the circle’s radius" << endl;
    double radius;
    const double pi = 3.14;
    cin >> radius;
    double area = pi * pow(radius, 2);
    cout << "The circle with radius " << radius << " has an area of " << area << "." << endl;

    int x = 0xfe;
    int y = 0b11111110;
    cout << x << endl
         << y << endl;  

    */   
    int dice1;
    int dice2;
    int seed = time(0);
    srand(seed);
    dice1 = rand() % 7;
    dice2 = rand() % 7;
    cout << "The dice read " << dice1 << " and " << dice2 << endl;
    return 0;
}