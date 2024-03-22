#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

int Login()
{
    cout << "Login" << endl;
}

int SignUp()
{
    cout << "SignUp" << endl;
}

int main()
{
    cout << "Do You Have An Account? ";
    string Data;
    cin >> Data;
    std::transform(Data.begin(), Data.end(), Data.begin(),
    [](unsigned char c){ return std::tolower(c); });
    if (Data == "y")
    {
        Login();
    }else
    {
        SignUp();
    }
    return 0;
}