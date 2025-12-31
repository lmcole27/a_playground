#include <iostream>

using namespace std;

int main() {
    std::cout << "Hello World!" << std::endl;
    double sales = 95000;
    double state_tax_rate = 0.04;
    double county_tax_rate = 0.02;
    double total_tax = sales * (state_tax_rate + county_tax_rate);
    double income = sales - total_tax;
    cout << "Total tax = $" << total_tax << endl
         << "Income = $" << income << endl;   
    return 0;
}
    