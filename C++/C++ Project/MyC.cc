#include <iostream>
#include <string>
#include <algorithm>
#include <cctype>

using namespace std;

int Login()
{
    
}

int SignUp()
{
}

int main()
{
    cout << "Do You Have An Account? ";
    string Data << cin << endl;
    std::transform(Data.begin(), Data.end(), Data.begin(),
    [](unsigned char c){ return std::tolower(c); });
    if (Data == "Y")
    {
        SignUp();
    }else
    {
        Login();
    }
    return 0;
}